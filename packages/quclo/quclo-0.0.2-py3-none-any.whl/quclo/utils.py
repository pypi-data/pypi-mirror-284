"""Utility functions for QuClo."""

import os
import configparser
from datetime import datetime, timedelta

CONFIG_FILE = os.path.expanduser("~/.quclo_config")
QUCLO_API_URL = "https://quclo.com/api/"


def save_api_key(api_key):
    """Save the API key to the config file."""
    config = configparser.ConfigParser()
    config.read(CONFIG_FILE)
    if "auth" not in config:
        config["auth"] = {}
    config["auth"]["api_key"] = api_key
    with open(CONFIG_FILE, "w") as configfile:
        config.write(configfile)


def load_api_key():
    """Load the API key from the config file."""
    config = configparser.ConfigParser()
    config.read(CONFIG_FILE)
    return config.get("auth", "api_key", fallback=None)


def duration_to_expires_at(duration: int | None) -> str | None:
    """Convert a duration to an expiration date."""
    if duration is None:
        return None
    return (datetime.now() + timedelta(days=duration)).isoformat()
