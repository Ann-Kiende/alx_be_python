# test_simple_calculator.py

import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = SimpleCalculator()

    # --- Addition tests ---
    def test_addition_basic(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(0, 0), 0)

    def test_addition_floats_and_large(self):
        self.assertAlmostEqual(self.calc.add(1.5, 2.5), 4.0)
        self.assertEqual(self.calc.add(10**12, 1), 10**12 + 1)

    def test_addition_commutativity(self):
        pairs = [(2, 7), (-3, 5), (1.5, 2.5)]
        for a, b in pairs:
            with self.subTest(a=a, b=b):
                self.assertEqual(self.calc.add(a, b), self.calc.add(b, a))

    # --- Subtraction tests ---
    def test_subtraction_basic(self):
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(3, 5), -2)
        self.assertEqual(self.calc.subtract(0, 0), 0)

    def test_subtraction_floats(self):
        self.assertAlmostEqual(self.calc.subtract(2.5, 1.2), 1.3, places=7)
        self.assertEqual(self.calc.subtract(-1, -2), 1)

    # --- Multiplication tests ---
    def test_multiplication_basic(self):
        self.assertEqual(self.calc.multiply(3, 4), 12)
        self.assertEqual(self.calc.multiply(-2, 3), -6)
        self.assertEqual(self.calc.multiply(0, 5), 0)

    def test_multiplication_floats_and_large(self):
        self.assertAlmostEqual(self.calc.multiply(1.5, 2.0), 3.0)
        self.assertEqual(self.calc.multiply(10**6, 10**6), 10**12)

    # --- Division tests ---
    def test_division_basic(self):
        self.assertEqual(self.calc.divide(10, 2), 5.0)
        self.assertAlmostEqual(self.calc.divide(7, 2), 3.5)

    def test_division_negative_and_float(self):
        self.assertEqual(self.calc.divide(-6, 3), -2.0)
        self.assertAlmostEqual(self.calc.divide(5.0, 2.0), 2.5)

    def test_division_by_zero(self):
        # According to the provided implementation, divide returns None when dividing by zero
        self.assertIsNone(self.calc.divide(10, 0))
        self.assertIsNone(self.calc.divide(0, 0))

    # --- Non-numeric inputs (type errors) ---
    def test_non_numeric_inputs_raise_type_error(self):
        # The arithmetic operators will raise TypeError for mismatched / unsupported operands
        with self.assertRaises(TypeError):
            self.calc.add("a", 1)
        with self.assertRaises(TypeError):
            self.calc.subtract("5", 2)
        with self.assertRaises(TypeError):
            self.calc.multiply([], 3)
        with self.assertRaises(TypeError):
            self.calc.divide("ten", "two")

if __name__ == "__main__":
    unittest.main()
