class ShimtaxError(Exception):
    pass


class CodingNotFound(ShimtaxError):
    def __init__(self) -> None:
        super().__init__("Unable to find shimtax coding")
