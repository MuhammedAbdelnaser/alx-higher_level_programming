#!/usr/bin/python3
"""Defines an inherited class-checking function."""


def inherits_from(object, a_class):
    """Checks if an objectect is an inherited instance of a class.

    Args:
        object (any): The object to check.
        a_class (type): The class to match the type of object to.
    Returns:
        If object is an inherited instance of a_class - True.
        Otherwise - False.
    """
    if issubclass(type(object), a_class) and type(object) != a_class:
        return True
    return False
