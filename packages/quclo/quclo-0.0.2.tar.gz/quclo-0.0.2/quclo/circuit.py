"""Circuit module for QuClo."""

from quclo.models import Circuit as CircuitModel


class Circuit:
    """A QuClo circuit."""

    def __init__(
        self,
        circuit: str,
        priority: str | None = None,
        backend: str | None = None,
    ):
        """Initialize the circuit."""
        assert CircuitModel(qasm=circuit, priority=priority, backend=backend)
        self.circuit = circuit
        self.priority = priority
        self.backend = backend

    def run(self, api_key: str) -> str:
        """Run the circuit."""
        pass
