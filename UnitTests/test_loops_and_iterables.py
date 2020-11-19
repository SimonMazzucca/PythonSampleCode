import unittest


class TestLoopsAndIterables(unittest.TestCase):

    def test_iterator(self):
        nums = [1, 2, 3, 4, 5, 6]
        iterator = iter(nums)

        while True:
            try:
                next_element = next(iterator)
                print(next_element)
            except StopIteration:
                break

    def test_for_loop(self):
        a = [4, 5, 6]
        self.assertEqual(True, 5 in a)

        # foreach
        print("foreach")
        for num in [2, 4, 6, 8, 10]:
            print(num)

        # for by index
        print("for by index")
        for i in range(0, 5):
            print(i)

        print("for by index")
        nums = [1, 2, 3, 4, 5]
        for i in range(len(nums)):
            print(i)

        print("for loop with tuple collection")
        for i, j in [(1, 2), (3, 4), (5, 6)]:
            print(i, j)

        print("for loop with HT key/value, using dic.items()")
        dic = {'foo': 1, 'bar': 2, 'baz': 3}
        for k, v in dic.items():
            print(k, v)

        print("for loop with index and item, using enumerate(lists)")
        lists = [[1, 2, 3], [4, 5], [6]]
        for index, item in enumerate(lists):
            print(index, item)

    def test_while_loop(self):
        i = 0

        while i <= 10:
            print(i)
            i = i + 1
            if i == 4:
                break
