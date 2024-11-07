import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    # Add the following test methods to the TestCalculator class:

    def  test_add_negative(self):
        self.assertEqual(self.calc.add(-1,-2), -3)

    def test_subtract (self):
        self.assertEqual(self.calc.subtract(4,3), 1)

    def test_subtract_negative (self):
        self.assertEqual(self.calc.subtract(4,-3), 7)

    def test_mutiply (self):
        self.assertEqual(self.calc.multiply(12,7),84)

    def test_mutiply_negative_two (self):
        self.assertEqual(self.calc.multiply(-2,-2),4)
    def test_mutiply_negative_one (self):
        self.assertEqual(self.calc.multiply(0,-2),0)

    def test_divide (self):
        self.assertEqual(self.calc.divide(12,6),2)
    def test_divide_negative (self):
        self.assertEqual(self.calc.divide(-2,0),"invalide")
    def test_divide_negative (self):
        self.assertEqual(self.calc.divide(0,-2),0)
    def test_divide_negative (self):
        self.assertEqual(self.calc.divide(5,2),2)

    def test_modulo (self):
        self.assertEqual(self.calc.modulo(11,6),5)
    def test_modulo_0 (self):
        self.assertEqual(self.calc.modulo(6,6),0)

if __name__ == '__main__':
    unittest.main()