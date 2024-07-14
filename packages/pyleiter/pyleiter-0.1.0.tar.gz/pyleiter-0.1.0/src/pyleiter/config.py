import os
import toml

from pyleiter.errors import PyProjectTomlNotFoundError, PyleiterKeyNotFoundError

import logging

logger = logging.getLogger(__name__)


def _find_pyproject_toml():
    cwd = os.getcwd()
    cwd_files = os.listdir("./")
    for f in cwd_files:
        if "pyproject.toml" in f:
            return f
    return PyProjectTomlNotFoundError(f"File 'pyproject.toml' not found in path {cwd}")


def _parse_config_file(filepath):
    with open(filepath, "r") as fd:
        return toml.load(fd)


def _get_pyleiter_config(config: dict):
    try:
        return config["pyleiter"]
    except KeyError as excp:
        raise PyleiterKeyNotFoundError(
            "'pyleiter' key not found in 'pyproject.toml'. Please double check your configuration."
        ) from excp


def read_pyleiter_config() -> dict:
    filepath = _find_pyproject_toml()
    logger.info("Using project file: '%s'", filepath)
    config_dict = _parse_config_file(filepath)
    return _get_pyleiter_config(config_dict)
