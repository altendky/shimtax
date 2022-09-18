import click

import shimtax._pth


@click.group(name="shimtax")
def main() -> None:
    pass


@main.command(
    name="register",
    help="Enable automatic registration via shimtax_register.pth.",
)
def register() -> None:
    shimtax._pth.write_pth()


@main.command(
    name="unregister",
    help="Disable automatic registration via shimtax_register.pth.",
)
def unregister() -> None:
    shimtax._pth.delete_pth()
