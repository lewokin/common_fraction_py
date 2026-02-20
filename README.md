# ➗ Common Fraction
**CommonFraction** is a robust, safe, and precise implementation of common fractions in Python.

The main goal of this library is to perform mathematical operations **without the loss of precision** inherent in floating-point arithmetic (`float`). The class handles automatic simplification, sign normalization, and mathematical edge cases internally.

## ✨ Key Features
* **Automatic Simplification:** Fractions like `2/4` are immediately converted to `1/2` upon initialization (using GCD).
* **Sign Normalization:** The negative sign is always normalized to the numerator (e.g., `1/-2` becomes `-1/2`).
* **Full Arithmetic:** Supports addition, subtraction, multiplication, and division.
* **Safe Exponentiation:** Handles negative exponents without converting to `float` (returns the reciprocal fraction).
* **Rich Comparisons:** Full support for comparison operators (`==`, `!=`, `<`, `>`, `<=`, `>=`).
* **Static Typing:** Fully type-hinted and compatible with static analysis tools like `mypy`.

## 🛠️ Requirements
Python 3.10+

## 🚀 Installation & Usage
Simply import the `CommonFraction` class into your project.

```python
from common_fraction import CommonFraction

# Creating a fraction (automatic simplification)
f1 = CommonFraction(2, 4)  # Result: 1/2
f2 = CommonFraction(3, 4)

print(f"My fraction: {f1}")  # Output: 1/2
```

## 🛡️ Safety & Error Handling
The class implements several safeguards:
* ZeroDivisionError: Prevents the creation of a fraction with a denominator of 0.
* Type Safety: Comparison operators (like ==) gracefully return False or NotImplemented instead of crashing when compared with incompatible types (e.g., str).
* Immutability: Arithmetic operations return new instances, leaving the original operands unchanged.

## 🧮 Examples
**Basic Arithmetic**
```python
# Addition
result = f1 + f2  # 1/2 + 3/4 = 5/4
print(result)     # Output: 5/4

# Multiplication
result = f1 * f2  # 1/2 * 3/4 = 3/8
```

**Exponentiation**
The class supports negative exponents while maintaining the fraction form (avoiding floats)
```python
f = CommonFraction(2, 3)

# Negative exponent flips the fraction!
result = f ** -2  
# Math logic: (2/3)^-2 = (3/2)^2 = 9/4
print(result)  # Output: 9/4
```

**Comparisons**
```python
f1 = CommonFraction(1, 2)
f2 = CommonFraction(2, 4)

print(f1 == f2)  # True (since 2/4 is simplified to 1/2)
print(f1 < CommonFraction(3, 4))  # True
```


# ⚠ Important information
Due to the assumptions used in the design, the CommonFraction class is a **CLOSED** ecosystem and cannot be used with standard Python classes (int, float). Only conversion from CommonFraction to int/float/str is possible. Performing the operation in the other direction is **IMPOSSIBLE**. This is required to ensure the correctness of calculations and ease of use.

# 🐍 List of supported methods
| Method | Support |
| :------: | :------: |
| str | ✅ |
| repr | ✅ |
| add | ✅ |
| radd | ✅ |
| sub | ✅ |
| rsub | ✅ |
| mul | ✅ |
| rmul | ✅ |
| truediv | ✅ |
| rtruediv | ✅ |
| pow[^1] | ✅ |
| eq[^2] | ✅ |
| lt[^3] | ✅ |
| neg | ✅ |
| abs | ✅ |
| float | ✅ |
| int | ✅ |
| hash | ✅ |
| reciprocal | 🚧 |
| to_dict | 🚧 |

✅: implemented \
🚧: during implementation \
💡: planned for future implementation

[^1]: The only method where you can use the int class on the CommonFraction class
[^2]: Due to the way Python logic works, the ‘ne’ method is also supported.
[^3]: Thanks to the use of the total_ordering decorator, the ‘le’, ‘gt’, and ‘ge’ methods are also supported.

## 📄 License
This project is open-source and available under the [MIT License](/LICENSE).
