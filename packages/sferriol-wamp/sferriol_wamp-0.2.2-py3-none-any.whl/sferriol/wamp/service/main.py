#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import asyncio
import concurrent.futures
import functools
import importlib.util
import logging
import os
import random
import sys

import click
from sferriol.python import load_module_from_file, method, module_name_from_file
from sferriol.python.dictionary import adict, as_adict

from sferriol.wamp import component

logger = logging.getLogger(__name__)


def _load_module(fpath):
    name = module_name_from_file(fpath)
    module_di = adict(
        fpath=fpath, registers=dict(), error=None, name=name, functions=list()
    )
    try:
        module = load_module_from_file(fpath)
        logger.debug(f"module {name} loaded")
        module_di.doc = module.__doc__
        functions = module_di.functions
        for name in dir(module):
            obj = getattr(module, name)
            # detect functions to register as service
            if hasattr(obj, "_wamp_register"):
                functions.append(obj)
    except Exception as e:
        module_di.error = e
        logger.warning(f"Unable to load module {name}: {e}")
    return module_di


def _py_files(dir):
    # return python files in the dir directory
    files = os.listdir(dir)
    files = [os.path.join(dir, file) for file in files if file.endswith(".py")]
    return files


async def _register_module_functions(module_di, session):
    name = module_di.name
    #    for f in module_di.functions:
    for f in module_di.threaded_functions:
        uri, register_args, register_kwargs = f._wamp_register
        reg_di = module_di.registers[uri] = adict(error=None)
        try:
            reg = await session.register(f, uri, *register_args, **register_kwargs)
            reg_di.register = reg
            logger.info(f"{name}: {uri} registered")
            reg_di.error = None
            reg_di.doc = f.__doc__
        except KeyError as e:
            reg_di.error = e
            logger.warning(f"module {name}: Unable to register {uri}: {e}")


async def _unregister_module_functions(module_di):
    name = module_di.name
    for uri in module_di.registers.keys():
        reg_di = module_di.registers[uri]
        await reg_di.register.unregister()
        logger.info(f"{name}: {uri} unregistered")


def create(options):
    comp = component.create(options.name, options)

    init(comp)

    return comp


def init(comp):

    @method(comp)
    def _threaded_function(self, func):
        """wraps into a threaded func"""

        @functools.wraps(func)
        async def _wrapper(*args, **kwargs):
            loop = asyncio.get_running_loop()
            result = await loop.run_in_executor(
                self.service_pool, functools.partial(func, *args, **kwargs)
            )
            return result

        _wrapper._wamp_register = func._wamp_register
        return _wrapper

    @method(comp)
    def _threaded_module_functions(self, module_di):
        module_di.threaded_functions = [
            self._threaded_function(func) for func in module_di.functions
        ]

    @comp.register()
    @method(comp)
    def module_count(self):
        """
        Returns the number of modules currently managed.
        """
        return len(self.modules)

    @comp.register()
    @method(comp)
    def module_info(self, name):
        """
        Returns the data about a specific module
        """
        assert name in self.modules
        mod = self.modules[name]
        infos = adict(name=name, fpath=mod.fpath, error=mod.error, doc=mod.doc)
        infos.services = [
            {"doc": reg.doc, "error": reg.error, "name": k}
            for k, reg in mod.registers.items()
        ]
        return infos

    @comp.register()
    @method(comp)
    def module_list(self):
        """
        Returns the list of the modules currently managed
        """
        return list(self.modules.keys())

    @comp.register()
    @method(comp)
    async def upgrade_module(self, name):
        """
        Upgrade a specific module
        """
        assert name in self.modules

        # unregisters all current registers
        module_di = self.modules[name]
        await _unregister_module_functions(module_di)

        # load new module
        module_di = _load_module(module_di.fpath)

        # force all services functions to run in a thread in order not to block services manager
        self._threaded_module_functions(module_di)

        # store new module
        self.modules[module_di.name] = module_di

        # registers all new registers
        await _register_module_functions(module_di, self.session)

    @method(comp)
    def service_files(self):
        options = self.options
        services_dir = os.path.normpath(options.services_dir)

        # list module python files from service dir.
        return _py_files(services_dir)

    @comp.on_join
    @method(comp)
    async def on_join(self, session, details):
        """
        register all methods on this object decorated with "@wamp.register"
        """
        logger.info("joined")
        self.session = session

        # create the thread pool for services
        # each service call is executed in a seperated thread
        self.service_pool = concurrent.futures.ThreadPoolExecutor()

        # lis(t module python files from service dir.
        files = self.service_files()

        # load modules
        modules = self.modules = dict()
        for fpath in files:
            module_di = _load_module(fpath)
            # force all services functions to run in a thread in order not to block services manager
            self._threaded_module_functions(module_di)
            modules[module_di.name] = module_di
            await _register_module_functions(module_di, session)
