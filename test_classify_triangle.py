import unittest
from classify_triangle import classify_triangle


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

    def test_scalene(self):
        self.assertEqual(classify_triangle(4, 5, 6), "Scalene")
        self.assertEqual(classify_triangle(4, 9, 10), "Scalene")

    def test_right_triangle(self):

        self.assertEqual(classify_triangle(3, 4, 5), "ScaleneRight")
        self.assertEqual(classify_triangle(5, 4, 3), "ScaleneRight")
        self.assertEqual(classify_triangle(4, 5, 3), "ScaleneRight")

    def test_not_a_triangle(self):
        self.assertEqual(classify_triangle(1, 2, 3), "NotATriangle")
        self.assertEqual(classify_triangle(10, 2, 3), "NotATriangle")

    def test_invalid_zero_negative(self):
        self.assertEqual(
            classify_triangle(0, 1, 1), "InvalidInput, side can not be negative or zero"
        )
        self.assertEqual(
            classify_triangle(-1, 2, 2),
            "InvalidInput, side can not be negative or zero",
        )

    def test_type_error_non_numeric(self):
        with self.assertRaises(TypeError):
            classify_triangle("a", 2, 3)


if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)
