"""QuClo CLI Tool."""

import click
from quclo.user import User
from quclo.circuit import Circuit
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
def create():
    """Create a new QuClo user."""
    email = click.prompt("Email")
    password = click.prompt("Password", hide_input=True)
    user = User()
    user.create(email, password)
    click.echo(f"User {email} created.")


@user.command()
def login():
    """Login to QuClo."""
    email = click.prompt("Email")
    password = click.prompt("Password", hide_input=True)
    user = User(email, password)
    api_key = user.get_api_key()
    save_api_key(api_key)
    click.echo(f"Logged in. API Key saved.")


@main.group()
def circuit():
    """Manage QuClo circuits."""
    pass


@circuit.command()
@click.argument("circuit")
@click.option("--priority", help="Priority of the circuit run.")
@click.option("--backend", help="Backend to use for the circuit run.")
def run(circuit: str, backend: str | None = None, priority: str | None = None):
    """Run a QuClo circuit."""

    api_key = load_api_key()
    if not api_key:
        click.echo("Please login first.")
        return
    if priority and backend:
        click.echo("Please provide only one of priority or backend.")
        return
    circuit = Circuit(circuit)
    if priority:
        circuit.run(priority=priority)
    elif backend:
        circuit.run(backend=backend)
    click.echo("Circuit run.")


if __name__ == "__main__":
    main()
