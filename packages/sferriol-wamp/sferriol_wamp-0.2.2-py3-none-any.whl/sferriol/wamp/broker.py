import json
import os
import shutil
import venv

from sferriol.python.dictionary import adict, as_adict
import tomli_w
import tomllib

from sferriol.wamp import (
    BASE_DIR,
    BROKER_DIR,
    BROKER_EXE,
    VENV_DIR,
    load_config,
)

requirements = {
    "crossbar": "crossbar@git+https://github.com/ninousf/crossbar.git@pinned",
    "pip": "pip==24.0",
    "setuptools": "setuptools==70.0.0",
}

CROSSBAR_VERSION = "20.12.3"

_module_path = os.path.dirname(__file__)
_requirements_path = os.path.join(_module_path, "requirements-crossbar.txt")


def init(app_dir: str) -> None:
    init_dir(app_dir)
    init_venv(app_dir)
    init_crossbar(app_dir)


def init_crossbar(app_dir: str) -> None:
    base_dir = os.path.expanduser(os.path.join(app_dir, BASE_DIR))
    broker_dir = os.path.join(base_dir, BROKER_DIR)
    crossbar_cfg_file = os.path.join(broker_dir, ".crossbar/config.json")
    venv_dir = os.path.join(base_dir, VENV_DIR, BROKER_DIR)
    broker_exe = f"{venv_dir}/bin/crossbar"

    # check broker exe ok
    if not os.path.exists(broker_exe):
        raise FileNotFoundError("Broker application (crossbar) does not exist")

    # init broker
    os.system(f"{broker_exe} init --appdir {broker_dir}")

    # put the application realm in broker config
    cfg = as_adict(load_config(app_dir))
    with open(crossbar_cfg_file, "r") as f:
        broker_cfg = as_adict(json.load(f))
    for w in broker_cfg.workers:
        if w.type == "router":
            w.realms[0].name = cfg.realm


def init_dir(app_dir: str) -> None:
    base_dir = os.path.expanduser(os.path.join(app_dir, BASE_DIR))
    broker_dir = os.path.join(base_dir, BROKER_DIR)
    # create broker directory
    os.makedirs(broker_dir, exist_ok=True)


def init_venv(app_dir: str) -> None:
    app_dir = os.path.abspath(app_dir)
    base_dir = os.path.expanduser(os.path.join(app_dir, BASE_DIR))
    venv_dir = os.path.join(base_dir, VENV_DIR, BROKER_DIR)
    # create broker env directory
    os.makedirs(venv_dir, exist_ok=True)
    # create venv for crossbar
    builder = venv.EnvBuilder(with_pip=True)
    builder.create(venv_dir)

    req = requirements
    # update venv
    os.system(f"{venv_dir}/bin/pip install {req['pip']} {req['setuptools']}")

    # install crossbar in venv
    os.system(f"{venv_dir}/bin/pip install {req['crossbar']}")


def start(app_dir: str) -> None:
    app_dir = os.path.abspath(app_dir)
    base_dir = os.path.expanduser(os.path.join(app_dir, BASE_DIR))
    broker_dir = os.path.join(base_dir, BROKER_DIR)
    venv_dir = os.path.join(base_dir, VENV_DIR, BROKER_DIR)

    crossbar_dir = os.path.join(broker_dir, ".crossbar")
    broker_exe = f"{venv_dir}/bin/crossbar"
    os.system(
        f"{broker_exe} start --cbdir {crossbar_dir} --color false --logtofile >/dev/null 2>&1 &"
    )


def stop(app_dir: str) -> None:
    app_dir = os.path.abspath(app_dir)
    base_dir = os.path.expanduser(os.path.join(app_dir, BASE_DIR))
    broker_dir = os.path.join(base_dir, BROKER_DIR)
    venv_dir = os.path.join(base_dir, VENV_DIR, BROKER_DIR)

    crossbar_dir = os.path.join(broker_dir, ".crossbar")
    broker_exe = f"{venv_dir}/bin/crossbar"
    os.system(f"{broker_exe} stop --cbdir {crossbar_dir}")
