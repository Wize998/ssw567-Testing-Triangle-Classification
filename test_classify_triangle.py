import unittest
from math import sqrt
from itertools import permutations
from io import StringIO
from unittest.mock import patch
import runpy

from classify_triangle import classify_triangle

INVALID_MSG = "InvalidInput, side can not be negative or zero"


class ClassifyTriangleTest(unittest.TestCase):

    def test_equilateral(self):
        self.assertEqual(classify_triangle(5, 5, 5), "Equilateral")

    def test_equilateral_condition(self):
        result = classify_triangle(7, 7, 7)
        self.assertTrue(result == "Equilateral")

    def test_isosceles(self):
        self.assertEqual(classify_triangle(5, 5, 3), "Isosceles")
        self.assertEqual(classify_triangle(3, 5, 5), "Isosceles")
        self.assertEqual(classify_triangle(5, 3, 5), "Isosceles")

    def test_isosceles_right(self):

        self.assertEqual(classify_triangle(1, 1, sqrt(2)), "IsoscelesRight")

    def test_scalene(self):
        self.assertEqual(classify_triangle(4, 5, 6), "Scalene")
        self.assertEqual(classify_triangle(4, 9, 10), "Scalene")

    def test_right_triangle(self):

        self.assertEqual(classify_triangle(3, 4, 5), "ScaleneRight")
        self.assertEqual(classify_triangle(5, 4, 3), "ScaleneRight")
        self.assertEqual(classify_triangle(4, 5, 3), "ScaleneRight")

    def test_right_triangle_permutations(self):

        for a, b, c in set(permutations((3, 4, 5), 3)):
            self.assertEqual(classify_triangle(a, b, c), "ScaleneRight")

    def test_float_right_triangle(self):

        self.assertEqual(classify_triangle(0.3, 0.4, 0.5), "ScaleneRight")

    def test_near_right_but_not_right(self):

        self.assertEqual(classify_triangle(3, 4, 5.1), "Scalene")

    def test_not_a_triangle(self):
        self.assertEqual(classify_triangle(1, 2, 3), "NotATriangle")
        self.assertEqual(classify_triangle(10, 2, 3), "NotATriangle")

    def test_invalid_zero_negative(self):
        self.assertEqual(classify_triangle(0, 1, 1), INVALID_MSG)
        self.assertEqual(classify_triangle(-1, 2, 2), INVALID_MSG)

    def test_invalid_non_numeric(self):

        self.assertEqual(classify_triangle("a", 2, 3), INVALID_MSG)

    def test_main_block_cli_prints(self):

        with patch("builtins.input", side_effect=["3", "4", "5"]), patch(
            "sys.stdout", new_callable=StringIO
        ) as buf:
            runpy.run_module("classify_triangle", run_name="__main__")
        out = buf.getvalue()
        self.assertIn("Triangle is:", out)
        self.assertIn("ScaleneRight", out)


if __name__ == "__main__":  # pragma: no cover
    unittest.main(exit=False, verbosity=2)


