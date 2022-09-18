import codecs
import encodings

codec_name = "aaa_to_bbb"


def decode(input, errors="strict"):
    text, consumed_bytes = encodings.utf_8.StreamReader.decode(input, errors)
    return (text.replace("aaa", "bbb"), consumed_bytes)


def search_function(encoding):
    if encoding != codec_name:
        return None

    return codecs.CodecInfo(
        encode=lambda *args: None,
        decode=decode,
        name=codec_name,
    )
