from homework11.task1 import ColorsEnum, SizesEnum

color_example = ColorsEnum()
size_example = SizesEnum()


def test_colors():
    for key in ("RED", "BLUE", "ORANGE", "BLACK"):
        assert color_example.__getattribute__(key) == key


def test_sizes():
    for key in ("XL", "L", "M", "S", "XS"):
        assert size_example.__getattribute__(key) == key
