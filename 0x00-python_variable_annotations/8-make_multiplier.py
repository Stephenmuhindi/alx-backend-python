#!/usr/bin/env python3
"""multiplies a float by a multipier"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    multiplies a float by a multipier
    multiplies afloat by multiplier
    """

    def multiplier_func(number: float) -> float:
        """multiplies a float by amultiplier"""
        return multiplier * number

    return multiplier_func
