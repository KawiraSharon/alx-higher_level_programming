#!/usr/bin/python3
"""Definition of function(text-indentation)"""


def text_indentation(text):
    """Print text '.' , '?', ':'

    Args:
        text (string): text being printed
    Raises:
        TypeError: for not string text
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    c = 0
    while c < len(text) and text[c] == ' ':
        c += 1

    while c < len(text):
        print(text[c], end="")
        if text[c] == "\n" or text[c] in ".?:":
            if text[c] in ".?:":
                print("\n")
            c += 1
            while c < len(text) and text[c] == ' ':
                c += 1
            continue
        c += 1
