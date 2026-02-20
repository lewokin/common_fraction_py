from __future__ import annotations

import sys
if sys.version_info < (3, 10):
    raise RuntimeError("CommonFraction requires Python 3.10 or newer.")

from functools import total_ordering
import math

@total_ordering
class CommonFraction:
    def __init__(self, numerator: int, denominator: int) -> None:
        if denominator == 0:
            raise ZeroDivisionError("Error. Denominator can't eqaul 0.")
        
        if denominator < 0:
            denominator = -denominator
            numerator = -numerator

        gdc = math.gcd(numerator, denominator)
        self.numerator = numerator // gdc
        self.denominator = denominator // gdc

    def __str__(self) -> str:
        if self.denominator == 1:
            return str(self.numerator)
        
        return f"{self.numerator}/{self.denominator}"

    def __repr__(self) -> str:
        return f"CommonFraction({self.numerator}, {self.denominator})"
    
    def __add__(self, other: CommonFraction) -> CommonFraction:
        new_self_numerator = self.numerator * other.denominator
        new_other_numerator = other.numerator * self.denominator

        new_denominator = self.denominator * other.denominator

        return CommonFraction(new_self_numerator + new_other_numerator, new_denominator)

    def __radd__(self, other: CommonFraction) -> CommonFraction:
        return self.__add__(other)

    def __sub__(self, other: CommonFraction) -> CommonFraction:
        new_self_numerator = self.numerator * other.denominator
        new_other_numerator = other.numerator * self.denominator

        new_denominator = self.denominator * other.denominator

        return CommonFraction(new_self_numerator - new_other_numerator, new_denominator)

    def __rsub__(self, other: CommonFraction) -> CommonFraction:
        new_self_numerator = self.numerator * other.denominator
        new_other_numerator = other.numerator * self.denominator

        new_denominator = self.denominator * other.denominator

        return CommonFraction(new_other_numerator - new_self_numerator, new_denominator)

    def __mul__(self, other: CommonFraction) -> CommonFraction:
        return CommonFraction(self.numerator * other.numerator, self.denominator * other.denominator)

    def __rmul__(self, other: CommonFraction) -> CommonFraction:
        return self.__mul__(other)

    def __truediv__(self, other: CommonFraction) -> CommonFraction:
        return CommonFraction(self.numerator * other.denominator, self.denominator * other.numerator)

    def __rtruediv__(self, other: CommonFraction) -> CommonFraction:
        return CommonFraction(other.numerator * self.denominator, other.denominator * self.numerator)

    def __pow__(self, other: int) -> CommonFraction:
        if other < 0:
            return CommonFraction(self.denominator ** abs(other), self.denominator ** abs(other))

        return CommonFraction(self.numerator ** other, self.denominator ** other)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, CommonFraction):
            return NotImplemented
        
        return self.numerator == other.numerator and self.denominator == other.denominator

    def __lt__(self, other: CommonFraction) -> bool:
        new_self_numerator = self.numerator * other.denominator
        new_other_numerator = other.numerator * self.denominator
        
        return new_self_numerator < new_other_numerator

    def __neg__(self) -> CommonFraction:
        return CommonFraction(-self.numerator, self.denominator)

    def __abs__(self) -> CommonFraction:
        return CommonFraction(abs(self.numerator), self.denominator)

    def __float__(self) -> float:
        return self.numerator / self.denominator

    def __int__(self) -> int:
        return int(float(self))

    # def __hash__(self) -> int:
    #     pass
