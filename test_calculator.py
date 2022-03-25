import Calculator
import unittest

class calculator(unittest.TestCase):

    def setUp(self):
        self.x = 34
        self.y = 30

    def tearDown(self):
        self.x = 0
        self.y = 0

    def test_case_add(self):
        #Arrange
        result = Calculator.add(self.x,self.y)
        self.assertEqual(result, self.x+self.y)

    def test_case_sub(self):
        x = 15
        y = 10
        result = Calculator.sub(self.x,self.y)
        self.assertEqual(result, self.x-self.y)

    def test_case_multi(self):
        x = 15
        y = 10
        result = Calculator.multi(self.x,self.y)
        self.assertEqual(result, self.x*self.y)

    def test_case_div(self):
        x = 15
        y = 10
        result = Calculator.div(self.x,self.y)
        self.assertEqual(result, self.x/self.y)

if __name__ == "__main__":
    unittest.main