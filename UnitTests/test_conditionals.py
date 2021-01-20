import unittest


class TestConditionals(unittest.TestCase):

    def test_something(self):
        T = True
        F = False

        self.assertEqual(False, T and F)
        self.assertEqual(True, T or F)

    def test_ternary_conditional_operator(self):
        # In C#:
        # x_description = x == 1 ? '1' : '0';
        x = 1
        x_description = '1' if x == 1 else '0'
        self.assertEqual('1', x_description)

