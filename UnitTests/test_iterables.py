import unittest


class TestIterators(unittest.TestCase):

    def test_iterator(self):
        nums = [1, 2, 3, 4, 5, 6]
        iterator = iter(nums)

        while True:
            try:
                next_element = next(iterator)
                print(next_element)
            except StopIteration:
                break
