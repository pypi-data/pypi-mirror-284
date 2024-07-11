import asyncio
import os

import autobahn
from sferriol.python.dictionary import adict, as_adict

from sferriol.wamp import load_config
from .main import create


def register(uri, *args, **kwargs):
    """
    Marking the function as a service that will need to be threaded then added
    as a method to wamp's component.

    This way, user defined functions can still call between
    themselves in an unthreaded manner
    """

    def wrapper(f):

        assert callable(f)
        """ the uris collected from decorator will be passed to wamp.register()"""
        f._wamp_register = (uri, args, kwargs)

        return f

    return wrapper


def run(app_dir, name, services_dir):

    cfg = load_config(app_dir)

    options = adict(name=name)
    options.update(cfg)
    options.services_dir = services_dir

    comp = create(options)
    autobahn.asyncio.component.run([comp])
