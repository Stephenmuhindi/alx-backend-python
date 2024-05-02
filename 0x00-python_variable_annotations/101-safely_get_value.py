#!/usr/bin/env python3
"""safely get value from dict"""
from typing import Mapping, Any, Union, TypeVar, Optional

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Optional[T] = None) -> Union[Any, T]:
    """
    safely get value from dict
    safely get value from dict
    """
    if key in dct:
        return dct[key]
    else:
        return default
