#!/usr/bin/env python3
"""Converts a python variable to key value pair"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Converts a python variable to key value pair"""
    return k, v ** 2
