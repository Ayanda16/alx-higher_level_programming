#!/usr/bin/python3
"""Text indentation"""


def text_indentation(text):
    """finction that prints a text with two lines after ., ?, : chars"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for letter in text:
        buf += letter
        if letter == "." or letter == "?" or letter == ":":
            while buf[0] == " ":
                buf = buf[1:]
            print(buf)
            print()
            buf = ""
    if len(buf) != 0:
        try:
            while buf[0] == " ":
                buf = buf[1:]
        except:
            pass
        print(buf, end="")
