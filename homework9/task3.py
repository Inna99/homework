"""
Write a function that takes directory path, a file extension and an optional tokenizer.
It will count lines in all files with that extension if there are no tokenizer.
If a the tokenizer is not none, it will count tokens.
For dir with two files from hw1.py:
>>> universal_file_counter(test_dir, "txt")
6
>>> universal_file_counter(test_dir, "txt", str.split)
6
"""
from pathlib import Path
from typing import Callable, Optional


def universal_file_counter(
    dir_path: Path, file_extension: str, tokenizer: Optional[Callable] = None
) -> int:
    count = 0
    files = dir_path.glob("*." + file_extension)
    if tokenizer is None:
        for fl in files:
            with open(fl, "r") as f:
                count += f.read().count("\n")
    else:
        for fl in files:
            with open(fl, "r") as f:
                count += len((f.read()).split())
    return count


if __name__ == "__main__":  # pragma: no cover
    cur_dir = Path()
    print(universal_file_counter(cur_dir, "txt", str.split))
