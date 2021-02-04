
import unittest
from primesInRange import primesInRange




class PrimesInRangeTest(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    
    def test00_primesInRange(self):
        expected = [2, 3, 5, 7]
        actual = primesInRange(2, 10)
        print("*Testing: Valid Inputs")
        self.assertListEqual(expected, actual, "Test failed: Result differs!")
        print("Test passed!")
        
    def test01_InvalidInput(self):
        expected = None
        actual = primesInRange();
        print("*Testing: Invalid Parameters")
        self.assertEqual(actual, expected, "Test Failed!")
        print("Test passed!")
        
    def test02_InvalidLowerBound(self):
        expected = None
        actual = primesInRange(0, 10)
        print("*Testing: Invalid lower bound")
        self.assertEqual(actual,expected, "Test Failed")
        print("Test passed!");
        
    def test03_InvalidBounds(self):
        expected = None
        actual = primesInRange(1001, 1004)
        print("*Testing: Parameter out of range")
        self.assertEqual(actual,expected, "Test Failed")
        print("Test passed!")
        
    def test04_InvalidBounds(self):
        expected = None
        actual = primesInRange(998, 43)
        print("*Testing: Lower bound greater than Upper bound")
        self.assertEqual(actual,expected, "Test Failed")
        print("Test passed!")
        
    def test05_InvalidInputFormat(self):
        expected = None
        actual = primesInRange('a', 'b')
        print("*Testing: Input with invalid format")
        self.assertEqual(actual, expected, "Test Failed")
        print("Test passed!")
        
    def test06_EmptyList(self):
        expected = []
        actual = primesInRange(33, 34)
        print("*Testing: Result is empty list")
        self.assertListEqual(actual, expected, "Test Failed")
        print("Test passed!")