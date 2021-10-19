import os
import tempfile
from pathlib import Path

from homework9.task3 import universal_file_counter


def test_universal_file_counter_three_parameters():
    """checks operation with three parameters"""
    with tempfile.TemporaryDirectory() as dir:
        for i in range(4):
            with open(os.path.join(dir, "tmp" + str(i) + ".txt"), "w") as file:
                file.write("fg dfg dfg df")
        cur_dir = Path(dir)
        assert universal_file_counter(cur_dir, "txt", str.split) == 16


def test_universal_file_counter_two_parameters():
    """checks operation with two parameters"""
    with tempfile.TemporaryDirectory() as dir:
        for i in range(4):
            with open(os.path.join(dir, "tmp" + str(i) + ".txt"), "w") as file:
                file.write("fg \ndfg dfg df\n")
        cur_dir = Path(dir)
        assert universal_file_counter(cur_dir, "txt") == 8


def test_universal_file_counter_without_extension():
    """a negative test checks that when working with files of another extension, zero is returned"""
    with tempfile.TemporaryDirectory() as dir:
        with open(os.path.join(dir, "tmp"), "w") as file:
            file.write("fg \ndfg dfg df\n")
        cur_dir = Path(dir)
        assert not universal_file_counter(cur_dir, "txt") == 8
