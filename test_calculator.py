import Calculator
import unittest

class calculator(unittest.TestCase):
    def test_case_add(self):
        x = 10
        y = 15
        result = Calculator.add(x,y)
        self.assertEqual(result, x+y)

    def test_case_sub(self):
        x = 15
        y = 10
        result = Calculator.sub(x,y)
        self.assertEqual(result, x-y)

    def test_case_multi(self):
        x = 15
        y = 10
        result = Calculator.multi(x,y)
        self.assertEqual(result, x*y)

    def test_case_div(self):
        x = 15
        y = 10
        result = Calculator.div(x,y)
        self.assertEqual(result, x/y)

if __name__ == "__main__":
    unittest.main