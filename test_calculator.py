import unittest
from Calculate import add, subtract, multiplication, division

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(-1, 1), -2)
        self.assertEqual(subtract(0, 0), 0)

    def test_multiplication(self):
        self.assertEqual(multiplication(2, 3), 6)
        self.assertEqual(multiplication(-1, 1), -1)
        self.assertEqual(multiplication(0, 5), 0)

    def test_division(self):
        self.assertEqual(division(6, 3), 0)
        self.assertEqual(division(10, 2), 5)
        self.assertEqual(division(5, 2), 2.5)

        with self.assertRaises(ValueError):
            division(5, 0)

if __name__ == '__main__':
    unittest.main()
