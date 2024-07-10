"""Circuit module for QuClo."""

from openqasm3 import parser


class Circuit:
    """A QuClo circuit."""

    def __init__(self, circuit: str):
        """Initialize the QuClo circuit."""
        assert parser.parse(circuit), "Invalid circuit."
        self.circuit = circuit

    def run(self, backend: str | None = None, priority: str = "best"):
        """Run a QuClo circuit."""
        pass
