import pathlib
import sysconfig

import click


pth_name = "shimtax_register.pth"


@click.group(name="shimtax")
def main() -> None:
    pass


@main.command(
    name="register",
    help="Enable automatic registration via shimtax_register.pth.",
)
def register():
    purelib = pathlib.Path(sysconfig.get_path("purelib"), pth_name)

    content = """import os,sys;exec("import shimtax; shimtax.register()")\n"""

    purelib.write_text(data=content, encoding="utf-8")


@main.command(
    name="unregister",
    help="Disable automatic registration via shimtax_register.pth.",
)
def unregister():
    purelib = pathlib.Path(sysconfig.get_path("purelib"), pth_name)

    purelib.unlink(missing_ok=True)
