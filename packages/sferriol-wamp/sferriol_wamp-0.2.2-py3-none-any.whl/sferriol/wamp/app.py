import os
import socket

from sferriol.wamp import BASE_DIR, component, load_config


def create(name, cfg):
    return component.create(name, cfg)


def init(comp):

    comps = dict()

    @comp.register()
    def add_component(name, source, cfg):
        _cfg = dict(comp.cfg)
        _cfg.update(cfg)
        mod = _load_source(source)
        comps[name] = mod.create(name, _cfg)

    @comp.subscribe("ping")
    def ping(sub_id):
        comp.publish("pong", sub_id=sub_id, name=comp.name)


def start(app_dir, name=None):
    if name is None:
        name = socket.gethostname()
    base_dir = os.path.expanduser(os.path.join(app_dir, BASE_DIR))
    cfg = load_config(app_dir)
    comp = create(name, cfg)
    init(comp)
    component.run([comp])
