from functools import singledispatch
from commonfraction import CommonFraction

@singledispatch
def to_CommonFraction(var: object) -> CommonFraction:
    raise TypeError(f"Conversion from type {type(var).__name__} is not supported")

@to_CommonFraction.register(int)
def _(var: int) -> CommonFraction:
    return CommonFraction(var, 1)

# @to_CommonFraction.register(float)
# def _(var: float) -> CommonFraction:
#     pass

# @to_CommonFraction.register(dict)
# def _(var: dict) -> CommonFraction:
#     pass

# @to_CommonFraction.register(str)
# def _(var: str) -> CommonFraction:
#     pass

# @to_CommonFraction.register(CommonFraction)
# def _(var: CommonFraction) -> CommonFraction:
#     pass
