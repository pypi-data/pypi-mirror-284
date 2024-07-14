from pyleiter.config import read_pyleiter_config
from pyleiter.runner import run_process
import argparse


def _build_arg_parser(config: dict) -> argparse.ArgumentParser:
    arg_parser = argparse.ArgumentParser(
        prog="pyleiter",
        description="Simple task management for a Python project",
        epilog="Enjoy!",
    )
    command_help = {}
    for key, item in config.items():
        command_help[key] = item.get("help", "Help not provided")

    arg_parser.add_argument(
        "command", choices=list(config.keys()), help=str(command_help)
    )
    return arg_parser


def _run_command(config: dict, command: str):
    cmd = config[command]["command"]
    return run_process(cmd)


def main():
    config = read_pyleiter_config()
    arg_parser = _build_arg_parser(config)
    args = arg_parser.parse_args()
    _run_command(config, args.command)
