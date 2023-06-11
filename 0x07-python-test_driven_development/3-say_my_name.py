#!/usr/bin/python3
"""Defines a name-printing function."""


def say_my_name(firstName, lastName=""):
    """Print a name.

    Args:
        firstName (str): The first name to print.
        lastName (str): The last name to print.
    Raises:
        TypeError: If either of firstName or lastName are not strings.
    """
    if not isinstance(firstName, str):
        raise TypeError("firstName must be a string")
    if not isinstance(lastName, str):
        raise TypeError("lastName must be a string")
    print("My name is {} {}".format(firstName, lastName))
