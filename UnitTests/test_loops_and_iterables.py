import unittest


class TestLoopsAndIterables(unittest.TestCase):

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

    def test_while_loop(self):
        i = 0

        while i <= 10:
            print(i)
            i = i + 1
            if i == 4:
                break


