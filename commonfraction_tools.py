import math
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
    if var == 0.0:
        return CommonFraction(0, 1)
    
    if var.is_integer():
        return CommonFraction(int(var), 1)
    
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

        if fractional_part < 1e-10: 
            break

        r = 1.0 / fractional_part
    
    return CommonFraction(sign * h1, k1)

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

# @to_CommonFraction.register(str)
# def _(var: str) -> CommonFraction:
#     pass

# @to_CommonFraction.register(CommonFraction)
# def _(var: CommonFraction) -> CommonFraction:
#     pass
