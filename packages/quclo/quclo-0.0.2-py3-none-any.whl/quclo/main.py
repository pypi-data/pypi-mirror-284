"""QuClo CLI Tool."""

import click
from quclo.user import User
from quclo.circuit import Circuit
from quclo.backend import Backend
from quclo.utils import save_api_key, load_api_key


@click.group()
def main():
    """QuClo CLI Tool"""
    pass


@main.group()
def user():
    """Manage QuClo users."""
    pass


@user.command()
@click.option("--email", help="Email for the user.", prompt="Email")
@click.option(
    "--password",
    help="Password for the user.",
    prompt="Password",
    hide_input=True,
)
def create(email: str | None, password: str | None):
    """Sign up for QuClo."""
    if not email:
        email = click.prompt("Email")
    if not password:
        password = click.prompt("Password", hide_input=True)
    user = User(email=email, password=password)
    user.create()
    click.echo(f"User {email} created.")


@user.command()
@click.option("--email", help="Email of the user.", prompt="Email")
@click.option(
    "--password",
    help="Password of the user.",
    prompt="Password",
    hide_input=True,
)
@click.option("--duration", help="Duration of the API key.", type=int)
def login(email: str | None, password: str | None, duration: int | None):
    """Sign in to QuClo."""
    if not email:
        email = click.prompt("Email")
    if not password:
        password = click.prompt("Password", hide_input=True)
    user = User(email, password)
    api_key = user.get_api_key(duration=duration)
    save_api_key(api_key)
    click.echo(f"Logged in. API Key saved.")


@main.group()
def backend():
    """Query QuClo backends."""
    pass


@backend.command()
def list():
    """List the available backends."""
    pass


@backend.command()
@click.option("--backend", help="Backend to show details for.")
def show(backend: str):
    """Show details of a backend."""
    pass


@main.group()
def circuit():
    """Manage circuits on QuClo."""
    pass


@circuit.command()
@click.option("--circuit", help="Circuit to run.")
@click.option("--priority", help="Priority of the circuit run.")
@click.option("--backend", help="Backend to use for the circuit run.")
def run(circuit: str, backend: str | None, priority: str | None):
    """Run a circuit with QuClo."""

    priority = (
        "best" if (priority is None and backend is None) else priority
    )  # Default to best priority
    circuit_obj = Circuit(circuit=circuit, priority=priority, backend=backend)
    api_key = load_api_key()
    id = circuit_obj.run(api_key=api_key)
    click.echo(f"Circuit {id} submitted.")


@circuit.command()
@click.argument("id")
def status(id: str):
    """Get the status of a circuit from QuClo."""
    pass


@circuit.command()
@click.argument("id")
def result(id: str):
    """Get the result of a circuit from QuClo."""
    pass


if __name__ == "__main__":
    main()
