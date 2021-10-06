import pytest
import tempfile

from homework9.task1 import merge_sorted_files


def test_merge_sorted_files():
    fp1 = tempfile.TemporaryFile()
    fp1.write(b'1\n3\n5\n')
    fp2 = tempfile.TemporaryFile()
    fp2.write(b'2\n4\n6\n')
    assert list(merge_sorted_files([fp1.name, fp2])) == ['1', '2', '3', '4', '5', '6']
