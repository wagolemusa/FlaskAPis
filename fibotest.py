import unittest
# from fibonacci import fibonacciNumbers
from fibonacciNumbers import *
class testFibonacciNumbers(unittest.TestCase):
    def test_fibonacci(self):
        self.assertEqual(fibonacciNumbers().fibonacci(10),
        [1, 2, 3, 5, 8, 13, 21, 34, 55, 89])
        self.assertEqual(len(fibonacciNumbers().fibonacci(10)),
        10)
        self.assertEqual(fibonacciNumbers().fibonacci(10)[8],
        55)
    def test_sum_of_even_fibonacci(self):
        self.assertEqual(fibonacciNumbers().sum_of_even_fibonacci(10),44)
        self.assertEqual(fibonacciNumbers().sum_of_even_fibonacci(),4613732)
if __name__ == '__main__':
    unittest.main()