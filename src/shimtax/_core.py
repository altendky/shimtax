import codecs
import typing

codec_name = "shimtax"


def register() -> None:
    codecs.register(search_function)


def search_function(encoding: str) -> typing.Optional[codecs.CodecInfo]:
    encoding_base, *rest = encoding.split("_")

    if encoding_base != codec_name:
        return None
