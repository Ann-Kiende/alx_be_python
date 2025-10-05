# test_simple_calculator.py

import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = SimpleCalculator()

    def test_addition(self):
        # Basic integers
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)

        # Zero and large numbers
        self.assertEqual(self.calc.add(0, 0), 0)
        self.assertEqual(self.calc.add(10**6, 1), 10**6 + 1)

        # Floats
        self.assertAlmostEqual(self.calc.add(1.5, 2.5), 4.0)

    def test_subtraction(self):
        # Basic integers
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(3, 5), -2)

        # Zero and negatives
        self.assertEqual(self.calc.subtract(0, 0), 0)
        self.assertEqual(self.calc.subtract(-1, -2), 1)

        # Floats
        self.assertAlmostEqual(self.calc.subtract(2.5, 1.2), 1.3, places=7)

    def test_multiply(self):
        # Basic integers
        self.assertEqual(self.calc.multiply(3, 4), 12)
        self.assertEqual(self.calc.multiply(-2, 3), -6)

        # Zero and large numbers
        self.assertEqual(self.calc.multiply(0, 5), 0)
        self.assertEqual(self.calc.multiply(10**3, 10**3), 10**6)

        # Floats
        self.assertAlmostEqual(self.calc.multiply(1.5, 2.0), 3.0)

    def test_divide(self):
        # Normal division
        self.assertEqual(self.calc.divide(10, 2), 5.0)
        self.assertAlmostEqual(self.calc.divide(7, 2), 3.5)

        # Negative and floats
        self.assertEqual(self.calc.divide(-6, 3), -2.0)
        self.assertAlmostEqual(self.calc.divide(5.0, 2.0), 2.5)

        # Division by zero: per implementation, should return None
        self.assertIsNone(self.calc.divide(10, 0))
        self.assertIsNone(self.calc.divide(0, 0))

if __name__ == "__main__":
    unittest.main()
