#!/usr/bin/python3
class LockedClass:
    """class without attributes that prevents user from dynamically
    creating new instance attributes"""
    __slots__ = ["first_name"]
