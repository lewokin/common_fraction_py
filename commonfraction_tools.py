import math
from decimal import Decimal
from functools import singledispatch
from commonfraction import CommonFraction

@singledispatch
def to_CommonFraction(var: object) -> CommonFraction:
    raise TypeError(f"Conversion from type {type(var).__name__} is not supported")

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

# @to_CommonFraction.register(CommonFraction)
# def _(var: CommonFraction) -> CommonFraction:
#     pass

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