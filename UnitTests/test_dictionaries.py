from pprint import pprint as pretty_print
import unittest


class TestDictionaries(unittest.TestCase):

    bands = {
        1: "Aerosmith",
        2: "Megadeth",
        3: "GnR",
        4: "Foo Fighters"
    }

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






