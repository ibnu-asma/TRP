import unittest

from fibonacci import fibonacci, fibonacci_recursive


class TestFibonacci(unittest.TestCase):
    def test_values(self):
        cases = {0: 0, 1: 1, 2: 1, 3: 2, 4: 3, 5: 5, 10: 55}
        for n, expected in cases.items():
            self.assertEqual(fibonacci(n), expected)
            self.assertEqual(fibonacci_recursive(n), expected)

    def test_negative(self):
        with self.assertRaises(ValueError):
            fibonacci(-1)
        with self.assertRaises(ValueError):
            fibonacci_recursive(-1)


if __name__ == "__main__":
    unittest.main()
