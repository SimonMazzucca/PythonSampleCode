import unittest


class TestConditionals(unittest.TestCase):

    def test_something(self):
        T = True
        F = False

        self.assertEqual(False, T and F)
        self.assertEqual(True, T or F)
