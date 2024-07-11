import asyncio
import os
import socket
import time

from sferriol.wamp import BASE_DIR, component, load_config


def _create_comp(app_dir):
    base_dir = os.path.expanduser(os.path.join(app_dir, BASE_DIR))
    cfg = load_config(app_dir)
    name = f"mon-{socket.gethostname()}-{os.getpid()}"
    comp = component.create(name, cfg)
    return comp


def broadcast(app_dir, timeout=3):
    comp = _create_comp(app_dir)
    comp.sub_id = time.time()

    @comp.subscribe("pong")
    def _(sub_id, name):
        if sub_id == comp.sub_id:
            print(name)

    @comp.on_join
    async def _(session, details):
        session.publish("ping", sub_id=comp.sub_id)
        await asyncio.sleep(timeout)
        comp.stop()

    component.run([comp])


def comp(comp):

    @comp.subscribe("ping")
    def ping(sub_id):
        comp.publish("pong", sub_id=sub_id, name=comp.name)


def start(app_dir, name=None):
    if name is None:
        name = socket.gethostname()
    base_dir = os.path.expanduser(os.path.join(app_dir, BASE_DIR))
    cfg = load_config(app_dir)
    comp = component.create(name, cfg)
    component.run([comp])
