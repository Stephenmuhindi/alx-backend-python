#!/usr/bin/env python3
"""correct duck-typed annotations augmentation"""
from typing import Any, Union, Sequence


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """retuens first element or none if empty"""
    if lst:
        return lst[0]
    else:
        return None
