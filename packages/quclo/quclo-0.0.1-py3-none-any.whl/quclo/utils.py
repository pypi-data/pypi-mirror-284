"""Utility functions for the QuClo."""

import os
import configparser

CONFIG_FILE = os.path.expanduser("~/.quclo_config")


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
