#!/usr/bin/env python3
"""Define a type-annotated function."""

from typing import Union, Any, TypeVar, Mapping

# Define a type variable T
T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """
    Safely retrieve a value from a dictionary with optional default.

    This function takes a dictionary 'dct', a key 'key', and an optional
    default value 'default'.
    It checks if the 'key' exists in the 'dct', and if it does, it returns
    the corresponding value.
    If the 'key' is not found, the function returns the 'default' value.

    Parameters:
        dct (Mapping): The dictionary from which to retrieve the value.
        key (Any): The key to search for in the dictionary.
        default (Union[T, None], optional): The default value to return if the
        key is not found.
                                           Defaults to None.

    Returns:
        Union[Any, T]: The value associated with the 'key' if found in the
        'dct',
                       otherwise, the 'default' value.

    Example:
        >>> my_dict = {'a': 1, 'b': 2}
        >>> safely_get_value(my_dict, 'a')
        1
        >>> safely_get_value(my_dict, 'c', default='Not found')
        'Not found'
    """
    if key in dct:
        return dct[key]
    else:
        return default
