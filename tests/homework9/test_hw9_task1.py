import tempfile
from pathlib import Path

import pytest

from homework9.task1 import merge_sorted_files


def test_merge_sorted_files():
    """checking work with temporary files"""
    with tempfile.NamedTemporaryFile(mode="w", delete=False) as tp1:
        tp1.write("1\n3\n5\n")
    with tempfile.NamedTemporaryFile(mode="w", delete=False) as tp2:
        tp2.write("2\n4\n6\n")
    assert list(merge_sorted_files([tp1.name, tp2.name])) == [1, 2, 3, 4, 5, 6]


@pytest.mark.xfail
def test_merge_sorted_files_sourse():
    """checking work with physical files"""
    cur_dir1 = Path("file1.txt")
    cur_dir2 = Path("file2.txt")
    assert list(merge_sorted_files([cur_dir1, cur_dir2])) == [1, 2, 3, 4, 5, 6]
