"""Proxy utilities for QuClo."""

import requests
from functools import wraps
from quclo.utils import QUCLO_API_URL


def set_global_proxy(proxy_url=QUCLO_API_URL, api_key: str | None = None):
    """Set a global proxy for all requests."""
    requests.post = lambda url, *args, **kwargs: requests.post(
        proxy_url, *args, **kwargs
    )


def proxy(proxy_url=QUCLO_API_URL, api_key: str | None = None):
    """Decorator to temporarily override requests.post with a proxy."""

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            original_post = requests.post
            requests.post = lambda url, *args, **kwargs: original_post(
                proxy_url, *args, **kwargs
            )
            try:
                return func(*args, **kwargs)
            finally:
                requests.post = original_post

        return wrapper

    return decorator
