from os import path
from sys import argv, stderr


def checkFiles():
    # checks if the files passed as an argument exist
    if len(argv) <= 2:
        print("Usage: ./markdown2html.py README.md README.html")
        exit(1)
    elif not path.exists(argv[1]):
        print(f"Missing {argv[1]}", file=stderr)
        exit(1)
    else:
        exit(0)
