from unittest import TestCase
from string_manipulation import StringManipulation


class TestStringManipulation(TestCase):

    def test_concat_and_replace(self):
        prefix = "Easy come, easy go,"
        suffix = "will you let me go?"
        full_str = prefix + suffix
        full_str = full_str.replace(",will", ". Will")
        self.assertEqual("Easy come, easy go. Will you let me go?", full_str)

    def test_partial_replace(self):
        s = "0 0 0 0 0 0"
        s = s.replace("0", "1", 3)
        self.assertEqual(s, "1 1 1 0 0 0")

    def test_count_substrings(self):
        s = "Simone Coglione"
        n = s.count("on")
        self.assertEqual(2, n)

    def test_string_format(self):
        # float_num is rounded and converted to string
        float_num = 1.2345678
        self.assertEqual("1.235", "{:.3f}".format(float_num))

        # padding (10 adds 8 spaces)
        n = 10
        self.assertEqual("        10", "{:10.0f}".format(n))

    def test_string_format_with_indices(self):
        s = "Simone"
        d = "dumb"
        self.assertEqual("Simone is dumb", "{0} is {1}".format(s, d))
        self.assertEqual("Simone is dumb", "{s} is {d}".format(
            s="Simone",
            d="dumb")
        )

    def test_string_split(self):
        s = "Rock'n'Roll"
        parts = s.split("'")
        self.assertEqual("n", parts[1])

