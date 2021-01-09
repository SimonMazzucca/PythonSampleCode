import unittest


class TestConversionsAndCasting(unittest.TestCase):

    def test_cast_binary_to_into(self):
        bin = "1001001"
        dec = int(bin, 2)
        self.assertEqual(73, dec)

    def test_format_int_as_binary(self):
        dec = 73
        bin = "{0:b}".format(dec)
        self.assertEqual("1001001", bin)

