from calculator import Calculator
import unittest

class CalculatorTests(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()
    
    def test_add_numbers(self):
        result = self.calculator.add(2, 3)
        self.assertEqual(5, result)

    def test_subtract_numbers(self):
        result = self.calculator.subtract(5, 2)
        self.assertEqual(3, result)

    def test_multiply_numbers(self):
        result = self.calculator.multiply(2, 6)
        self.assertEqual(12, result)

    def test_divide_numbers(self):
        result = self.calculator.divide(6, 3)
        self.assertEqual(2, result)

    def tearDown(self):
        print("TEAR DOWN")

unittest.main()









