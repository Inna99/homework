"""
Write a function that merges integer from sorted files and returns an iterator

file1.txt:
1
3
5

file2.txt:
2
4
6

"""
import tempfile
from pathlib import Path
from typing import Iterator


def merge_sorted_files(file_list: list) -> Iterator:
    """
    >>> list(merge_sorted_files(["file1.txt", "file2.txt"]))
    [1, 2, 3, 4, 5, 6]
    """
    file1, file2 = file_list
    with open(file1, "r") as f:
        with open(file2, "r") as f2:
            it1 = iter(f.readlines())
            it2 = iter(f2.readlines())
            el1 = next(it1, None)
            el2 = next(it2, None)
            while el1 is not None or el2 is not None:
                if el1 is None or (el2 is not None and el2 < el1):
                    yield int(el2.rstrip())  # type: ignore
                    el2 = next(it2, None)
                else:
                    yield int(el1.rstrip())
                    el1 = next(it1, None)


if __name__ == "__main__":  # pragma: no cover
    cur_dir = Path("file1.txt")
    cur_dir2 = Path("file2.txt")
    print(list(merge_sorted_files([cur_dir, cur_dir2])))

    with tempfile.NamedTemporaryFile(mode="w", delete=False) as tp1:
        tp1.write("1\n3\n5\n")
    with tempfile.NamedTemporaryFile(mode="w", delete=False) as tp2:
        tp2.write("2\n4\n6\n")

    print(list(merge_sorted_files([tp1.name, tp2.name])))
