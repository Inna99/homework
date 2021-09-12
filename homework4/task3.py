"""
Write a function that will receive a string and write it to stderr
if line starts with "error" and to the stdout otherwise.
my_precious_logger("error: file not found")
# stderr
'error: file not found'
my_precious_logger("OK")
# stdout
'OK'
Definition of done:
 - function is created
 - function is properly formatted
 - function has positive tests
You will learn:
 - how to write to stderr
 - how to test output to the stderr and stdout
"""
from sys import stderr, stdout
import sys
import io
from contextlib import redirect_stdout


def my_precious_logger(text: str):
    #
    # with redirect_stdout(f):
        # print(f.getvalue())
    # f = io.StringIO()
    # with redirect_stdout(f):
    #     stdout = open('Output.txt', 'w')
    #     sys.stdout.write("zdvdkjnjknkjn")
    #
    #     if text.startswith("error"):
    #         stderr.write("error: file not found\n")
    #     else:
    #         stdout.write("OK\n")
    #     print(f.getvalue())

    old_stdout = sys.stdout
    new_stdout = io.StringIO()
    sys.stdout = new_stdout

    print("Hello World")
    print("Hello Universe")

    output = new_stdout.getvalue()

    sys.stdout = old_stdout

    print(output)



my_precious_logger(": file not found")

