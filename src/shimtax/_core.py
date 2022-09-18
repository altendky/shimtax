import codecs
import encodings
import re
import typing

import shimtax.errors

codec_name = "shimtax"
pattern = re.compile("shimtax(?P<rest>(:[a-z_ -]+)*)(\b|\n|$)")


def get_codec_names(text: str) -> typing.List[str]:
    found = next(pattern.finditer(text), None)
    if found is None:
        raise shimtax.errors.CodingNotFound()
    if found["rest"] == "":
        return []
    return found["rest"][1:].split(":")


def register() -> None:
    codecs.register(search_function)


def decode(input: bytes, errors: str = "strict") -> typing.Tuple[str, int]:
    text, consumed_bytes = encodings.utf_8.StreamReader.decode(input, errors)

    names = get_codec_names(text)
    decoders = [codecs.getdecoder(name) for name in names]

    for decoder in decoders:
        back_to_bytes = text.encode("utf-8")
        text, _ = decoder(back_to_bytes, errors=errors)

    return (text, consumed_bytes)


def search_function(encoding: str) -> typing.Optional[codecs.CodecInfo]:
    if encoding != codec_name:
        return None

    return codecs.CodecInfo(
        encode=encodings.utf_8.StreamReader.encode,
        decode=decode,
        name=codec_name,
    )
