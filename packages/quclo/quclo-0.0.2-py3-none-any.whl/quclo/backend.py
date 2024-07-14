"""Backend module for QuClo."""

from quclo.models import Backend as BackendModel


class Backend:
    def __init__(self):
        """A QuClo-integrated backend."""
        assert BackendModel()
