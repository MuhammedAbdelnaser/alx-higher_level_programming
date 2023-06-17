#!/usr/bin/python3
"""Defines a class-checking function."""


def is_same_class(object, a_class):
    """Check if an objectect is exactly an instance of a given class.

    Args:
        object (any): The objectect to check.
        a_class (type): The class to match the type of object to.
    Returns:
        If object is exactly an instance of a_class - True.
        Otherwise - False.
    """
    if type(object) == a_class:
        return True
    return False
