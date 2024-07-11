import os

import autobahn.asyncio.component
from sferriol.python.dictionary import adict, as_adict
from sferriol.python.env import load as _load_env
import tomli_w


BASE_DIR = ".sf-wamp"
BROKER_DIR = "broker"
BROKER_EXE = "crossbar"
CFG_FILENAME = "config.toml"
_OS_ENV_PREFIX = "SF_WAMP"
VENV_DIR = "venvs"

default = adict(
    heartbeat_period=5,  # in seconds
    log_level="info",
    private_key="",
    realm="realm1",
    service_dir="services",
    url="ws://127.0.0.1:8080/ws",
)


def init_dir(app_dir: str) -> None:
    app_dir = os.path.abspath(app_dir)
    base_dir = os.path.expanduser(os.path.join(app_dir, BASE_DIR))
    # create base directory
    os.makedirs(base_dir, exist_ok=True)


def init_config(app_dir: str) -> None:
    base_dir = os.path.expanduser(os.path.join(app_dir, BASE_DIR))
    cfg_dict = dict(default)
    # create cfg file
    cfg_file = os.path.join(base_dir, CFG_FILENAME)
    with open(cfg_file, "wb") as f:
        tomli_w.dump(cfg_dict, f)


def init_service(app_dir: str) -> None:
    base_dir = os.path.expanduser(os.path.join(app_dir, BASE_DIR))
    # create services dir
    os.mkdir(os.path.join(base_dir, default.service_dir))


def load_config(app_dir: str) -> dict:
    base_dir = os.path.expanduser(os.path.join(app_dir, BASE_DIR))
    cfg_file = os.path.join(base_dir, CFG_FILENAME)
    if not os.path.exists(cfg_file):
        di = default
    else:
        di = _load_env(default, cfg_file, _OS_ENV_PREFIX)
    return di


run = autobahn.asyncio.component.run
