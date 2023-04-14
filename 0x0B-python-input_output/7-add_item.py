#!/usr/bin/python3
"""load, add, save"""


import sys
save_to_json = __import__("5-save_to_json_file").save_to_json_file
load_from_json = __import__("6-load_from_json_file").load_from_json_file


def add_items(args, filename):
    """ adds all arguments to a python list and then save the, to a file"""
    try:
        mylist = load_from_json(filename)

    except FileNotFoundError:
        mylist = []

    for i in args:
        mylist.append(i)
    save_to_json(mylist, filename)


if __name__ == "__main__":
    args = sys.argv[1:]
    filename = "add_item.json"
    add_item(args, filename)
