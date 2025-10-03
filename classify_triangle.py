"""Triangle classifier module."""

from typing import Union

Number = Union[int, float]
_TOL = 1e-9


def classify_triangle(a: Number, b: Number, c: Number) -> str:
    """Classify a triangle given side lengths a, b, c.

    Returns one of:
      - "InvalidInput, side can not be negative or zero"
      - "NotATriangle"
      - "Equilateral"
      - "Isosceles" or "IsoscelesRight"
      - "Scalene"  or "ScaleneRight"

    Behavior matches the original function; only code quality is improved.
    """

    try:
        a, b, c = float(a), float(b), float(c)
    except (TypeError, ValueError):
        return "InvalidInput, side can not be negative or zero"
    if a <= 0 or b <= 0 or c <= 0:
        return "InvalidInput, side can not be negative or zero"

    s1, s2, s3 = sorted((a, b, c))

    if s1 + s2 <= s3:
        return "NotATriangle"

    if abs(s1 - s2) < _TOL and abs(s2 - s3) < _TOL:
        return "Equilateral"

    label = "Isosceles" if abs(s1 - s2) < _TOL or abs(s2 - s3) < _TOL else "Scalene"

    is_right = abs((s1 * s1 + s2 * s2) - (s3 * s3)) < _TOL
    return label + "Right" if is_right else label


if __name__ == "__main__":
    side_a = float(input("Enter side a: "))
    side_b = float(input("Enter side b: "))
    side_c = float(input("Enter side c: "))
    print("Triangle is:", classify_triangle(side_a, side_b, side_c))
