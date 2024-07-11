import asyncio
import click
import logging
import os
import pprint
import signal
import sys
import time

from sferriol.python.dictionary import adict, as_adict
import txaio

txaio.use_asyncio()


from sferriol.wamp import BASE_DIR, BROKER_EXE, load_config
from sferriol.wamp import broker

_cfg = as_adict(load_config("."))


@click.group()
@click.option("--log", help="log level to print", default="info")
@click.option("--app_dir", help="Application directory", default=".", show_default=True)
def general(log, app_dir):

    txaio.start_logging(level=log)


@general.group()
def app():
    """Application management"""
    pass


@app.command()
@click.pass_context
def start(ctx):
    from sferriol.wamp import app

    app_dir = ctx.parent.parent.params["app_dir"]
    app.start(app_dir)


@general.group()
def broker():
    pass


@broker.command()
@click.pass_context
def init(ctx):
    from sferriol.wamp import broker

    app_dir = ctx.parent.parent.params["app_dir"]
    broker.init(app_dir)


@broker.command()
@click.pass_context
def start(ctx):
    from sferriol.wamp import broker

    app_dir = ctx.parent.parent.params["app_dir"]
    broker.start(app_dir)


@broker.command()
@click.pass_context
def stop(ctx):
    from sferriol.wamp import broker

    app_dir = ctx.parent.parent.params["app_dir"]
    broker.stop(app_dir)


@general.command()
@click.argument("uri")
@click.pass_context
def call(ctx, uri):
    """Do a WAMP call"""
    from sferriol.wamp import load_config
    from sferriol.wamp.component import _create_component, run

    app_dir = ctx.parent.params["app_dir"]
    cfg = load_config(app_dir)
    comp = _create_component(cfg)

    @comp.on_join
    async def _(session, details):
        ret = await session.call(uri)
        pprint.pprint(ret)
        os.kill(os.getpid(), signal.SIGTERM)

    run([comp])


@general.group()
def config():
    """Configure application"""
    print("TODO")


@config.command()
@click.pass_context
def show(ctx):
    from sferriol.wamp import load_config

    app_dir = ctx.parent.parent.params["app_dir"]
    di = load_config(app_dir)
    pprint.pprint(di)


@general.command()
@click.argument("app_dir")
def init(app_dir):
    """Create environment dir (.sf-wamp) in application dir (APP_DIR)"""
    from sferriol.wamp import init_dir, init_config, init_service

    init_dir(app_dir)
    init_config(app_dir)
    init_service(app_dir)


@general.group()
def mon():
    """Monitoring tools"""


@mon.command()
@click.pass_context
def broadcast(ctx):
    from sferriol.wamp import mon

    app_dir = ctx.parent.parent.params["app_dir"]
    mon.broadcast(app_dir)


@general.group()
def service():
    """Service tools"""


@service.command()
@click.pass_context
def list(ctx):
    print("TODO")


@service.command()
@click.argument(
    "name",
)
@click.argument(
    "services_dir",
)
@click.pass_context
def run(ctx, name, services_dir):
    from sferriol.wamp import service as _service

    app_dir = ctx.parent.parent.params["app_dir"]
    _service.run(app_dir, name, services_dir)


def main():
    sys.exit(general())
