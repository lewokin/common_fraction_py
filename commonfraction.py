from __future__ import annotations

import sys
if sys.version_info < (3, 10):
    raise RuntimeError("CommonFraction requires Python 3.10 or newer.")

from functools import total_ordering
from decimal import Decimal
from functools import singledispatch
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
        return f"CommonFraction(numerator={self.numerator}, denominator={self.denominator}) at {(hex(id(self)))}"
    
    def __add__(self, other: object) -> CommonFraction:
        other = to_CommonFraction(other)
        return CommonFraction((self.numerator * other.denominator) + (other.numerator * self.denominator), 
                              self.denominator * other.denominator)

    def __radd__(self, other: object) -> CommonFraction:
        return self.__add__(other)

    def __sub__(self, other: object) -> CommonFraction:
        other = to_CommonFraction(other)
        return CommonFraction((self.numerator * other.denominator) - (other.numerator * self.denominator), 
                              self.denominator * other.denominator)

    def __rsub__(self, other: object) -> CommonFraction:
        other = to_CommonFraction(other)
        return CommonFraction((other.numerator * self.denominator) - (self.numerator * other.denominator), 
                              self.denominator * other.denominator)

    def __mul__(self, other: object) -> CommonFraction:
        other = to_CommonFraction(other)
        return CommonFraction(self.numerator * other.numerator, self.denominator * other.denominator)

    def __rmul__(self, other: object) -> CommonFraction:
        other = to_CommonFraction(other)
        return self.__mul__(other)

    def __truediv__(self, other: object) -> CommonFraction:
        other = to_CommonFraction(other)
        return CommonFraction(self.numerator * other.denominator, self.denominator * other.numerator)

    def __rtruediv__(self, other: object) -> CommonFraction:
        other = to_CommonFraction(other)
        return CommonFraction(other.numerator * self.denominator, other.denominator * self.numerator)

    def __pow__(self, other: int) -> CommonFraction:
        if other < 0:
            return CommonFraction(self.denominator ** abs(other), self.numerator ** abs(other))

        return CommonFraction(self.numerator ** other, self.denominator ** other)

    def __eq__(self, other: object) -> bool:
        other = to_CommonFraction(other)
        return self.numerator == other.numerator and self.denominator == other.denominator

    def __lt__(self, other: object) -> bool:
        other = to_CommonFraction(other)        
        return (self.numerator * other.denominator) < (other.numerator * self.denominator)

    def __neg__(self) -> CommonFraction:
        return CommonFraction(-self.numerator, self.denominator)

    def __abs__(self) -> CommonFraction:
        return CommonFraction(abs(self.numerator), self.denominator)

    def __float__(self) -> float:
        return self.numerator / self.denominator

    def __int__(self) -> int:
        return int(float(self))

    def __hash__(self) -> int:
        return hash((type(self), self.numerator, self.denominator))
    
    def reciprocal(self) -> CommonFraction:
        return CommonFraction(self.denominator, self.numerator)

    def to_dict(self) -> dict[str, int]:
        return self.__dict__
    
    def to_decimal(self) -> Decimal:
        return Decimal(self.numerator) / Decimal(self.denominator)

@singledispatch
def to_CommonFraction(var: object) -> CommonFraction:
    raise TypeError(f"Conversion from type {type(var).__name__} is not supported")

@to_CommonFraction.register(CommonFraction)
def _(var: CommonFraction) -> CommonFraction:
    return var

@to_CommonFraction.register(int)
def _(var: int) -> CommonFraction:
    return CommonFraction(var, 1)

@to_CommonFraction.register(float)
def _(var: float, max_denominator: int = 1_000_000) -> CommonFraction:
    return CommonFraction(*approximate_to_fraction(var, max_denominator))

@to_CommonFraction.register(Decimal)
def _(var: Decimal, max_denominator: int = 1_000_000) -> CommonFraction:
    return CommonFraction(*approximate_to_fraction(var, max_denominator))

@to_CommonFraction.register(dict)
def _(var: dict) -> CommonFraction:
    if len(var) != 2:
        raise TypeError("Variable cannot be converted to CommonFraction: dict have incorrect format.")
    
    if ("numerator" not in var) or ("denominator" not in var):
        raise TypeError("Variable cannot be converted to CommonFraction: dict have incorrect format.")
    
    if type(var["numerator"]) != int:
        raise TypeError("Variable cannot be converted to CommonFraction: value of numerator has to be int type")
    
    if type(var["denominator"]) != int:
        raise TypeError("Variable cannot be converted to CommonFraction: value of denominator has to be int type")
    
    return CommonFraction(var['numerator'], var["denominator"])

@to_CommonFraction.register(str)
def _(var: str) -> CommonFraction:
    parts = var.split("/")

    if len(parts) != 2:
        raise ValueError("Variable cannot be converted to CommonFraction: str has incorrect format.")
    
    try:
        numerator = int(parts[0])
        denominator = int(parts[1])
    except ValueError:
        raise TypeError("Variable cannot be converted to CommonFraction: numerator and denominator must be integers.")
        
    return CommonFraction(numerator, denominator)

def approximate_to_fraction(var: float | Decimal, max_denominator: int) -> tuple[int, int]:
    if var == 0:
        return (0, 1)
    
    if var % 1 == 0:
        return (int(var), 1)
    
    sign = -1 if var < 0 else 1
    var = abs(var)

    h0, h1 = 0, 1
    k0, k1 = 1, 0
    r = var
    while True:
        a = math.floor(r)

        h2 = a * h1 + h0
        k2 = a * k1 + k0

        if k2 > max_denominator:
            break

        h0, h1 = h1, h2
        k0, k1 = k1, k2

        fractional_part = r - a

        if isinstance(var, float):
            if fractional_part < 1e-10: 
                break
        else:
            if fractional_part < Decimal("1e-10"): 
                break

        r = 1 / fractional_part
    
    return (sign * h1, k1)
