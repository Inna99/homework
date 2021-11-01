"""
Vasya implemented nonoptimal Enum classes.
Remove duplications in variables declarations using metaclasses.
from enum import Enum
class ColorsEnum(Enum):
    RED = "RED"
    BLUE = "BLUE"
    ORANGE = "ORANGE"
    BLACK = "BLACK"
class SizesEnum(Enum):
    XL = "XL"
    L = "L"
    M = "M"
    S = "S"
    XS = "XS"
Should become:
class ColorsEnum(metaclass=SimplifiedEnum):
    __keys = ("RED", "BLUE", "ORANGE", "BLACK")
class SizesEnum(metaclass=SimplifiedEnum):
    __keys = ("XL", "L", "M", "S", "XS")
assert ColorsEnum.RED == "RED"
assert SizesEnum.XL == "XL"
"""


class SimplifiedEnum(type):
    def __get_keys(cls):
        return cls.__dict__.get(f"_{cls.__name__}__keys")

    def __init__(cls, name, bases, dct):
        for key in set(cls.__get_keys()):
            super().__setattr__(key, key)


class ColorsEnum(metaclass=SimplifiedEnum):
    __keys = ("RED", "BLUE", "ORANGE", "BLACK")
    left = 5
    _sink = "xggb"


class SizesEnum(metaclass=SimplifiedEnum):
    __keys = ("XL", "L", "M", "S", "XS")


if __name__ == "__main__":  # pragma: no cover
    color_example = ColorsEnum()
    size_example = SizesEnum()
    for key in ("RED", "BLUE", "ORANGE", "BLACK"):
        print(
            f"{color_example.__class__.__name__}.{key}={color_example.__getattribute__(key)}"
        )
    print()
    for key in ("XL", "L", "M", "S", "XS"):
        print(
            f"{size_example.__class__.__name__}.{key}={size_example.__getattribute__(key)}"
        )
