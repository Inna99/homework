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
from pathlib import Path
import tempfile, os
from typing import List, Union, Iterator



# def merge_sorted_files(file_list: List[Union[Path, str], ...]) -> Iterator:
def merge_sorted_files(file_list: list) -> Iterator:
    """
    >>> list(merge_sorted_files(["file1.txt", "file2.txt"]))
    [1, 2, 3, 4, 5, 6]
    """
    file1, file2 = file_list
    with open(file1, 'r') as f:
        with open(file2, 'r') as f2:
            it1 = iter(f.readlines())
            it2 = iter(f2.readlines())
            el1 = next(it1, None)
            el2 = next(it2, None)
            while el1 is not None or el2 is not None:
                if el1 is None or (el2 is not None and el2 < el1):
                    yield el2.rstrip()
                    el2 = next(it2, None)
                else:
                    yield el1.rstrip()
                    el1 = next(it1, None)


if __name__ == '__main__':
#     p = Path('/homework9')
#     u1 = Union[p, "file1.txt"]
#     u2 = Union[p, "file2.txt"]
#     lst = List[u1, u2, ...]
#     merge_sorted_files(lst)
    # merge_sorted_files(["file1.txt", "file2.txt", ...])
    # print(list(merge_sorted_files(["file1.txt", "file2.txt"])))
    fp1 = tempfile.TemporaryFile()
    fp1.write(b'1\n3\n5\n')
    fp2 = tempfile.TemporaryFile()
    fp2.write(b'2\n4\n6\n')
    print([fp1.name, fp2.name])
    with tempfile.NamedTemporaryFile(suffix='.csv', prefix=os.path.basename(__file__)) as tf:
        tf_directory = os.path.dirname(tf.name)
    assert list(merge_sorted_files([fp1.name, fp2.name])) == ['1', '2', '3', '4', '5', '6']
