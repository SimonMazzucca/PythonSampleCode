import datetime
import unittest


class TestFunctions(unittest.TestCase):

    # helper functions
    def add(self, a, b, c):
        return a + b + c

    def add(self, *nums):
        return sum(nums)

    def record_time(self, message, time=datetime.datetime.now()):
        print("{:}, time: {:}".format(message, time))

    def reverse(self, s):
        res = ""
        for i in range(len(s)):
            res += s[len(s) - i - 1]
        return res

    def fib(self, n):
        if n <= 1:
            return 1

        return self.fib(n-1) + self.fib(n-2)

    def is_palindrome(self, s):
        for i in range(len(s) // 2):
            if s[i] != s[len(s) - i - 1]:
                return False
        return True

    # test methods
    def test_arguments(self):
        self.assertEqual(3, self.add(1, 1, 1))

    def test_parameters(self):
        self.assertEqual(12, self.add(3, 3, 3, 3))

    def test_optional_params(self):
        self.record_time("Yo mama")

    def test_string_reverse(self):
        s = "enomis"
        self.assertEqual("simone", self.reverse(s))

    def test_palindrome(self):
        s = "abba"
        self.assertEqual(True, self.is_palindrome(s))

    def test_fibonacci(self):
        for i in range(10):
            print("{0}: {1}".format(i, self.fib(i)))

        self.assertEqual(8, self.fib(5))


