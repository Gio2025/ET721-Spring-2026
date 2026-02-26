"""
George Athanasopoulos
Feb 26, 2026
Lab 9, unit testing
"""

import unittest
from calculation import *
# Example 1: simple unit testing
# unit
def addtwonumbers(a,b):
    return a+b

# unit test
class TestAddFunction(unittest.TestCase):
    def test_add(self):
        self.assertEqual(addtwonumbers(1,2), 3)
        # test that when passed 1 and 2, the return of the function is 3

    # Example 2: unit testing calculation.py file
    # unit test for subtraction
    def test_subtraction(self):
        self.assertEqual(subtracttwonumbers(6,4), 2)
        self.assertEqual(subtracttwonumbers(4,6), -2)
        self.assertEqual(subtracttwonumbers(5), 5)
        self.assertEqual(subtracttwonumbers(0), 0)
    
    # unit test for multiplication function
    def test_multiplication(self):
        self.assertEqual(multiplythreenumbers(1,2,3), 6)
        self.assertEqual(multiplythreenumbers(1,-2,3), -6)
        self.assertEqual(multiplythreenumbers(1,-2,-3), 6)
        self.assertEqual(multiplythreenumbers(-1,-2,-3), -6)

    # unit test for division function
    def test_division(self):
        self.assertEqual(dividetwonumbers(6,3), 2)
        self.assertAlmostEqual(dividetwonumbers(10,3), 3.3333, places = 4)
    # unit test for division by zero
    def test_divisionbyzero(self):
        # assertion none (not returning) or some known return value
        self.assertIsNone(dividetwonumbers(10,0))
    
        # unit test for value error
        self.assertIsNone(dividetwonumbers(10, "a"))
        self.assertIsNone(dividetwonumbers("Peter", 2))

    # unit test for other possible errors by mocking
    def test_unexpected_exception(self):
        # inspect an exception to occur
        with self.assertRaises(Exception):
            # passing no values to function
            dividetwonumbers()     



if __name__ == "__main__":
    unittest.main()


