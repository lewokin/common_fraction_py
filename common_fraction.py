from __future__ import annotations

import sys
if sys.version_info < (3, 10):
    raise RuntimeError("CommonFraction requires Python 3.10 or newer.")

from functools import total_ordering

#@total_ordering
class CommonFraction:
    def __init__(self, numerator: int, denominator: int) -> None:
        self.numerator = numerator
        self.denominator = denominator

    # def __str__(self) -> str:
    #     pass

    # def __repr__(self) -> str:
    #     return f"CommonFraction({self.numerator}, {self.denominator})"
    
    # def __add__(self, other: CommonFraction) -> CommonFraction:
    #     pass

    # def __radd__(self, other: CommonFraction) -> CommonFraction:
    #     return self.__add__(other)

    # def __sub__(self, other: CommonFraction) -> CommonFraction:
    #     pass

    # def __rsub__(self, other: CommonFraction) -> CommonFraction:
    #     pass

    # def __mul__(self, other: CommonFraction) -> CommonFraction:
    #     pass

    # def __rmul__(self, other: CommonFraction) -> CommonFraction:
    #     return self.__mul__(other)

    # def __truediv__(self, other: CommonFraction) -> CommonFraction:
    #     pass

    # def __rtruediv__(self, other: CommonFraction) -> CommonFraction:
    #     pass

    # def __pow__(self, other: int) -> CommonFraction:
    #     pass

    # def __eq__(self, other: object) -> bool:
    #     pass

    # def __lt__(self, other: CommonFraction | int | float) -> bool:
    #     pass

    # def __neg__(self) -> CommonFraction:
    #     pass

    # def __abs__(self) -> CommonFraction:
    #     pass

    # def __float__(self) -> float:
    #     pass

    # def __int__(self) -> int:
    #     pass

    # def __hash__(self) -> int:
    #     pass
