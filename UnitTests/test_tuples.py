import unittest


class TestTuples(unittest.TestCase):

    def test_tuple(self):
        # same as list but immutable
        weekdays = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun')
        self.assertEqual('Mon', weekdays[0])

        # assignment not supported
        # weekdays[0]='' <-- ex

    def test_tuple_create_from_list(self):
        weekdayList = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
        weekdays = tuple(weekdayList)
        self.assertEqual('Mon', weekdays[0])

    def test_tuple_assignment(self):
        weekend = ('Sat', 'Sun')
        (sat, sun) = weekend
        self.assertEqual('Sat', sat)



