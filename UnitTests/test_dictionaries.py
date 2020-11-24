from pprint import pprint as pretty_print
import unittest


class TestDictionaries(unittest.TestCase):
    bands = {
        1: "Aerosmith",
        2: "Megadeth",
        3: "GnR",
        4: "Foo Fighters"
    }

    bands_set = set()
    bands_set.add("Aerosmith")
    bands_set.add("Megadeth")
    bands_set.add("GnR")
    bands_set.add("Foo Fighters")

    contacts = {
        'Tizio': {
            'phone': '555-1234',
            'email': 'tizio@aol.com'
        },
        'Caio': {
            'phone': '555-7890',
            'email': 'caio@aol.com'
        }
    }

    def test_dictionary_access(self):
        self.assertEqual("Aerosmith", self.bands[1])

    def test_dictionary_contains(self):
        found = 3 in self.bands
        self.assertEqual(True, found)
        found = 404 in self.bands
        self.assertEqual(False, found)

    def test_dictionary_add(self):
        # add Ozzy to bands
        self.bands[5] = "Ozzy"
        self.assertEqual("Ozzy", self.bands[5])

        pretty_print(self.bands)

    def test_dic_loop(self):
        for contact in self.contacts:
            print("\n{0}'s contact info:".format(contact))
            print("Phone: {0}".format(self.contacts[contact]['phone']))
            print("Email: {0}".format(self.contacts[contact]['email']))

    def test_set(self):
        found = "GnR" in self.bands_set
        self.assertEqual(True, found)
        found = "gnr" in self.bands_set
        self.assertEqual(False, found)

    def test_list_to_set_conversion(self):
        nums = [1, 1, 2, 2]
        self.assertEqual(4, len(nums))
        unique = set(nums)
        self.assertEqual(2, len(unique))
