#!/usr/bin/python3
"""low memory cost"""


class LockedClass:
    """class without attributes that prevents user from dynamically
    creating new instance attributes"""
    __slots__ = ["first_name"]
