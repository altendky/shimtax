import pathlib
import textwrap

import attrs
import pytest


@attrs.define
class Conftest:
    path: pathlib.Path

    def append(self, text: str) -> None:
        with self.path.open("a") as file:
            file.write(
                textwrap.dedent(
                    text,
                )
            )


@pytest.fixture(name="conftest")
def conftest(pytester: pytest.Pytester) -> Conftest:
    return Conftest(path=pytester.path.joinpath("conftest.py"))


@pytest.fixture(name="enable_shimtax", autouse=True)
def enable_shimtax(conftest: Conftest) -> None:
    conftest.append(
        """
        import codecs

        import shimtax._core

        codecs.register(shimtax._core.search_function)
        """
    )


@pytest.fixture(name="enable_aaa_to_bbb")
def enable_aaa_to_bbb_fixture(conftest: Conftest) -> None:
    conftest.append(
        """
        import codecs

        import shimtax._tests.encodings.aaa_to_bbb

        codecs.register(shimtax._tests.encodings.aaa_to_bbb.search_function)
        """
    )


@pytest.fixture(name="enable_ccc_to_ddd")
def enable_ccc_to_ddd_fixture(conftest: Conftest) -> None:
    conftest.append(
        """
        import codecs

        import shimtax._tests.encodings.ccc_to_ddd

        codecs.register(shimtax._tests.encodings.ccc_to_ddd.search_function)
        """
    )
