#!/usr/bin/env python3
import argparse
import datetime
import os
import sqlite3
import sys
from dataclasses import dataclass
from enum import Enum
from pathlib import Path
import tomllib

from jinja2 import Environment, PackageLoader

from stampy.commands import act, add, check
from stampy.config import Config
from stampy.contextvars import db_conn, jinja_env
from stampy.email import handle_email
from stampy.jmap import JmapClient
from stampy.sql import SELECT_USER_INFO, initialize_db
from stampy.types import Action, BirthdayContext, SenderContext

parser = argparse.ArgumentParser(
    prog="stampy",
    description="Whether to forgive is your choice, but with stampy, you will *never* forget.",
)
parser.add_argument("--config-file")

subparsers = parser.add_subparsers(required=True)

check_parser = subparsers.add_parser("check")
check_parser.set_defaults(func=check)
act_parser = subparsers.add_parser("act")
act_parser.set_defaults(func=act)
act_parser = subparsers.add_parser("add")
act_parser.set_defaults(func=add)


def set_if_none(obj, name, value):
    if getattr(obj, name) is None:
        setattr(obj, name, value)


def _resolve_config(args) -> Config:
    """Assemble the appropriate config from the given CLI args."""
    if args.config_file:
        config_path = Path(args.config_file)
    else:
        config_fallback_path = Path(os.getenv("HOME")) / ".config"
        config_dir = os.getenv("XDG_CONFIG_HOME", config_fallback_path)
        config_path = Path(config_dir) / "stampy" / "config.toml"

    if not config_path.exists():
        print(f"No config file found (attempted to read '{config_path}').")
        sys.exit(1)

    with open(config_path, "rb") as config_file:
        config = Config(**tomllib.load(config_file))

    set_if_none(config, "editor", os.getenv("EDITOR", "vim"))
    return config


def main():
    args = parser.parse_args()
    config = _resolve_config(args)
    # Set up the database connection
    db_conn.set(initialize_db(Path(config.db_path)))
    # Set up the Jinja environment
    # TODO: defer this until needed
    # TODO: support user-provided templates
    loader = PackageLoader("stampy")
    jinja_env.set(Environment(loader=loader, autoescape=False))
    args.func(config)


if __name__ == "__main__":
    main()
