from unittest import TestCase
from pprint import pprint as pretty_print
from copy import copy, deepcopy


class TestLists(TestCase):

    def test_int_collection(self):
        # access element, then delete it
        nums = [5, -6, 2]
        self.assertEqual(-6, nums[1])
        del nums[1]
        self.assertEqual([5, 2], nums)

        s = "Simone"
        self.assertEqual("S", s[0])

    def test_list_methods(self):
        # append
        nums = [1, 2]
        nums.append(3)
        self.assertEqual([1, 2, 3], nums)

        # check index
        i = nums.index(1)
        self.assertEqual(0, i)

        # remove item by value
        nums.remove(1)
        self.assertEqual([2, 3], nums)

        # remove item by index
        del nums[-1]
        self.assertEqual([2], nums)

    def test_advanced_list_methods(self):
        alpha1 = ["s", "i", "m", "o", "n", "e"]

        # sort list
        alpha1.sort()
        self.assertEqual(['e', 'i', 'm', 'n', 'o', 's'], alpha1)

        # insert item in first position
        alpha1.insert(0, 'x')
        self.assertEqual(['x', 'e', 'i', 'm', 'n', 'o', 's'], alpha1)

        # join
        s = ''.join(alpha1)
        self.assertEqual("xeimnos", s)

        s = ','.join(alpha1)
        self.assertEqual("x,e,i,m,n,o,s", s)

    def test_built_in_list_functions(self):
        numbers = [3.14, -5, 10, 10 ** 4]
        self.assertEqual(-5, min(numbers))
        self.assertEqual(10 ** 4, max(numbers))
        self.assertEqual(10008.14, sum(numbers))
        self.assertEqual(4, len(numbers))

        alpha = "Hello bitches!"
        self.assertEqual(" ", min(alpha))
        self.assertEqual("t", max(alpha))
        self.assertEqual(14, len(alpha))

    def test_2d_arrays(self):
        m = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
        ]
        self.assertEqual(5, m[1][1])

        # prints:
        # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        pretty_print(m)

        # reference copy
        letters = ["A", "B", "C"]
        letters_2d = [letters, letters, letters]
        pretty_print(letters_2d)
        letters_2d[0][0] = '_'
        pretty_print(letters_2d)

        # deep copy
        letters = ["A", "B", "C"]
        letters_2d_copy = [copy(letters), copy(letters), copy(letters)]
        pretty_print(letters_2d_copy)
        letters_2d_copy[0][0] = '_'
        pretty_print(letters_2d_copy)

    def test_list_slicing(self):
        # create list from 0 to 4
        a = list(range(0, 10))
        self.assertEqual([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], a)

        # second param is count (1 based)
        self.assertEqual([0, 1, 2], a[0:3])

        # get from index 2 (val 2) to the end
        self.assertEqual([5, 6, 7, 8, 9], a[5:])

        # get full list step 2 (every other)
        self.assertEqual([0, 2, 4, 6, 8], a[::2])

        # get from 1 to 8 step 2
        self.assertEqual([1, 4, 7], a[1:8:3])

        # get next to last item in array
        self.assertEqual(8, a[-2])

        # get partial array
        self.assertEqual([2, 3, 4, 5, 6, 7], a[2:-2])

        # reverse array
        self.assertEqual([9, 8, 7, 6, 5, 4, 3, 2, 1, 0], a[::-1])

