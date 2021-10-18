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
    files = dir_path.cwd().glob("*." + file_extension)
    if tokenizer is None:
        for fl in files:
            with open(fl, "r") as f:
                count += f.read().count("\n")
    else:
        """здесь такая реализация, так как не очень ясно почему передайм в функцию не split или 'split', а str.split
        А если я захочу передать туда кастомную функцию tokenize(text: str) -> int:
        """
        for fl in files:
            with open(fl, "r") as f:
                count += len((f.read()).split())
    return count


if __name__ == "__main__":
    cur_dir = Path()
    print(universal_file_counter(cur_dir, "txt", str.split))