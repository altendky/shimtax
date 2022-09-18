import pathlib
import sysconfig

pth_name = "shimtax_register.pth"


def write_pth() -> None:
    purelib = pathlib.Path(sysconfig.get_path("purelib"), pth_name)

    content = """import os,sys;exec("import shimtax; shimtax.register()")\n"""

    purelib.write_text(data=content, encoding="utf-8")


def delete_pth() -> None:
    purelib = pathlib.Path(sysconfig.get_path("purelib"), pth_name)

    purelib.unlink(missing_ok=True)
