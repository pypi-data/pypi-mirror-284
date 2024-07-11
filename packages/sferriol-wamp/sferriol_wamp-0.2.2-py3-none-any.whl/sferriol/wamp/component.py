#!/usr/bin/env python
# -*- coding: utf-8 -*-
import asyncio
import functools
import inspect
import logging
import time
import traceback

import autobahn.asyncio.component
from autobahn.wamp.types import PublishOptions, RegisterOptions, SubscribeOptions

from sferriol import python
from sferriol.python.dictionary import adict, as_adict

logger = logging.getLogger(__name__)


class Remote_Component:
    def __init__(self, name, session):
        self.name = name
        self._session = session

    def __getattr__(self, meth_name):
        return functools.partial(self._session.call, f"{self.name}:{meth_name}")


class Wrapped_Component:
    def __init__(self, name, wamp_comp):
        self.name = name
        self._wamp = wamp_comp

        self._wamp.on("join", self._register_methods)

    def _list_public_methods(self):
        l = list()
        for m in dir(self):
            attr = getattr(self, m)
            if not m.startswith("_") and inspect.ismethod(attr):
                l.append(attr)
        return l

    def _register_methods(self, session, details):
        self._session = session
        for meth in self._list_public_methods():
            session.register(
                meth,
                procedure=f"{self.name}:{meth.__name__}",
                #                options = RegisterOptions(force_reregister=True),
            )

    def _(self, name):
        return Remote_Component(name, self._session)


def _create_component(options):
    """
    Configure and return a Component instance according to the given
    `options`
    """
    options = as_adict(options)
    if options.url.startswith("ws://"):
        kind = "websocket"
    elif options.url.startswith("rs://"):
        kind = "rawsocket"
    else:
        raise ValueError("URL should start with ws:// or rs://")

    authentication = dict()
    if options.private_key:
        if not options.authid:
            raise ValueError(
                "Require --authid and --authrole if --private-key (or WAMP_PRIVATE_KEY) is provided"
            )
        authentication["cryptosign"] = {
            "authid": options.authid,
            "authrole": options.authrole,
            "privkey": options.private_key,
        }

    return autobahn.asyncio.component.Component(
        transports=[
            {
                "type": kind,
                "url": options.url,
            }
        ],
        authentication=authentication if authentication else None,
        realm=options.realm,
    )


def _methods(comp):
    @python.method(comp)
    async def call(self, uri, *args, **kwargs):
        logger.debug(f"call.begin: {uri}")
        ret = await self.session.call(uri, *args, **kwargs)
        logger.debug(f"call.end: {uri}")
        return ret

    @python.method(comp)
    def publish_function_events(self, fn):
        """
        Publish when function (fn) starts (start evt), finished (done event) and when it raises an error
        """
        fn_name = getattr(fn, "__name__", str(fn))
        fn_uri = f"{comp.name}:{fn_name}"

        @functools.wraps(fn)
        async def async_wrapper(*args, **kwargs):
            self.publish(f"{fn_uri}|start", stamp=time.time())
            try:
                ret = await fn(*args, **kwargs)
            except Exception as e:
                self.publish(
                    f"{fn_uri}|error",
                    stamp=time.time(),
                    traceback=traceback.format_exception(e),
                )
                raise e
            else:
                self.publish(f"{fn_uri}|done", stamp=time.time())
                return ret

        @functools.wraps(fn)
        def wrapper(*args, **kwargs):
            self.publish(f"{fn_uri}|start", stamp=time.time())
            try:
                ret = fn(*args, **kwargs)
            except Exception as e:
                self.publish(
                    f"{fn_uri}|error",
                    stamp=time.time(),
                    traceback=traceback.format_exception(e),
                )
                raise e
            else:
                self.publish(f"{fn_uri}|done", stamp=time.time())
                return ret

        if asyncio.iscoroutinefunction(fn):
            return async_wrapper
        else:
            return wrapper

    @python.method(comp)
    def is_started(self):
        return self._done_f is not None

    @python.method(comp)
    def is_stopped(self):
        return self._done_f is None

    @python.method(comp)
    def publish(self, uri, *args, **kwargs):
        logger.debug(f"publish.begin: {uri}")
        ret = self.session.publish(uri, *args, **kwargs)
        logger.debug(f"publish.end: {uri}")
        return ret

    comp.registers = list()

    @python.method(comp)
    def register(self, uri=None, options=None, check_types=False):
        """
        A decorator as a shortcut for registering during on-join

        For example::

            @component.register(
                "com.example.add",
                options=RegisterOptions(invoke='roundrobin'),
            )
            def add(*args, **kw):
                print("add({}, {}): event received".format(args, kw))
        """
        assert options is None or isinstance(options, RegisterOptions)

        # by default, force reregister
        if options is None:
            options = RegisterOptions(force_reregister=True)

        def decorator(fn):
            _uri = uri
            if _uri is None:
                _uri = f"{self.name}:{fn.__name__}"

            def do_registration(session, details):
                return session.register(
                    fn, procedure=_uri, options=options, check_types=check_types
                )

            self.on("join", do_registration)
            if hasattr(self, "session"):
                # already joined
                self.session.register(
                    fn, procedure=_uri, options=options, check_types=check_types
                )

            comp.registers.append(_uri)
            return fn

        return decorator

    @python.method(comp)
    def subscribe(self, topic, options=None, check_types=False):
        """
        A decorator as a shortcut for subscribing during on-join

        For example::

            @component.subscribe(
                "some.topic",
                options=SubscribeOptions(match='prefix'),
            )
            def topic(*args, **kw):
                print("some.topic({}, {}): event received".format(args, kw))
        """
        assert options is None or isinstance(options, SubscribeOptions)

        def decorator(fn):
            def do_subscription(session, details):
                return session.subscribe(
                    fn, topic=topic, options=options, check_types=check_types
                )

            self.on("join", do_subscription)

            if hasattr(self, "session"):
                # already joined
                self.session.subscribe(
                    fn, topic=topic, options=options, check_types=check_types
                )
            return fn

        return decorator


def create(name, options):
    options = as_adict(options)
    comp = _create_component(options)
    initialize(comp, name, options)
    return comp


def initialize(comp, name, options):
    comp.name = name
    comp.cmd = "idle"
    comp.heartbeat_period = options.get("heartbeat_period", None)
    comp.options = options
    comp.joined = asyncio.Event()

    _methods(comp)

    # heartbeat
    async def heartbeat():
        while True:
            await asyncio.sleep(comp.heartbeat_period)
            comp.session.publish(
                "component.heartbeat",
                stamp=time.time(),
                name=comp.name,
                command=comp.cmd,
                options=PublishOptions(exclude_me=False),
            )

    @comp.on_join
    async def on__join(session, details):
        comp.session = session
        if comp.heartbeat_period:
            comp.heartbeat_task = asyncio.create_task(heartbeat())
        if hasattr(comp, "do_join"):
            await comp.do_join()
        comp.joined.set()

    @comp.on_leave
    async def on__leave(session, details):
        if hasattr(comp, "heartbeat_task"):
            comp.heartbeat_task.cancel()
        if hasattr(comp, "do_leave"):
            await comp.do_leave()
        comp.joined.clear()

    @comp.register()
    def list_registers():
        return comp.registers

    @comp.register(f"{comp.name}:ping", options=RegisterOptions(force_reregister=True))
    def register__ping():
        return "pong"

    return comp


create_wamp_component = _create_component
run = autobahn.asyncio.component.run
