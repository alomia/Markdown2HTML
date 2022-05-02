#!/usr/bin/python3
# Markdown to HTML

from os import path
from sys import argv, stderr

if len(argv) <= 2:
    print("Usage: ./markdown2html.py README.md README.html")
    exit(1)
elif not path.exists(argv[1]):
    print(f"Missing {argv[1]}", file=stderr)
    exit(1)
else:
    exit(0)

if __name__ == "__main__":
    pass