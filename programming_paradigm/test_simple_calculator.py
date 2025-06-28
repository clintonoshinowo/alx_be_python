# test_simple_calculator.py

import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method with various scenarios."""
        self.assertEqual(self.calc.add(2, 3), 5)         # Positive numbers
        self.assertEqual(self.calc.add(-1, 1), 0)        # Negative and positive
        self.assertEqual(self.calc.add(-1, -5), -6)      # Negative numbers
        self.assertEqual(self.calc.add(0, 0), 0)         # Zeros
        self.assertEqual(self.calc.add(100, 200), 300)   # Larger numbers
        self.assertEqual(self.calc.add(2.5, 3.5), 6.0)   # Float numbers
        self.assertEqual(self.calc.add(-2.5, 2.5), 0.0)  # Float numbers with zero sum

    def test_subtraction(self):
        """Test the subtract method with various scenarios."""
        self.assertEqual(self.calc.subtract(5, 3), 2)        # Positive result
        self.assertEqual(self.calc.subtract(3, 5), -2)       # Negative result
        self.assertEqual(self.calc.subtract(-1, -5), 4)      # Negative minus negative
        self.assertEqual(self.calc.subtract(0, 0), 0)        # Zeros
        self.assertEqual(self.calc.subtract(10, 0), 10)      # Subtracting zero
        self.assertEqual(self.calc.subtract(0, 10), -10)     # Zero minus positive
        self.assertEqual(self.calc.subtract(7.5, 2.5), 5.0)  # Float numbers

    def test_multiply(self):
        """Test the multiply method with various scenarios."""
        self.assertEqual(self.calc.multiply(2, 3), 6)         # Positive numbers
        self.assertEqual(self.calc.multiply(-1, 5), -5)       # Negative by positive
        self.assertEqual(self.calc.multiply(5, -1), -5)       # Positive by negative
        self.assertEqual(self.calc.multiply(-2, -3), 6)       # Negative by negative
        self.assertEqual(self.calc.multiply(0, 5), 0)         # Multiply by zero
        self.assertEqual(self.calc.multiply(5, 0), 0)         # Multiply by zero (commutative)
        self.assertEqual(self.calc.multiply(1, 100), 100)     # Multiply by one
        self.assertEqual(self.calc.multiply(10.5, 2), 21.0)   # Float numbers

    def test_divide(self):
        """Test the divide method with various scenarios, including division by zero."""
        self.assertEqual(self.calc.divide(6, 3), 2)         # Normal division
        self.assertEqual(self.calc.divide(5, 2), 2.5)       # Float result
        self.assertEqual(self.calc.divide(-6, 3), -2)       # Negative numerator
        self.assertEqual(self.calc.divide(6, -3), -2)       # Negative denominator
        self.assertEqual(self.calc.divide(-6, -3), 2)       # Both negative
        self.assertEqual(self.calc.divide(0, 5), 0)         # Zero numerator
        self.assertIsNone(self.calc.divide(5, 0))          # Division by zero (should return None)
        self.assertIsNone(self.calc.divide(0, 0))          # Division by zero with zero numerator
        self.assertAlmostEqual(self.calc.divide(10, 3), 3.333333, places=6) # Recurring decimal for precision
