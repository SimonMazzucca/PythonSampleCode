import unittest


class TestStackAndQueues(unittest.TestCase):

    def test_stack(self):

        # push
        stack = []
        stack.append(1)
        stack.append(2)
        stack.append(3)
        self.assertEqual(3, len(stack))

        # No peek... do it manually
        peek_val = stack[-1]
        self.assertEqual(3, peek_val)

        # Pop
        pop_val = stack.pop()
        self.assertEqual(3, peek_val)
        self.assertEqual(2, len(stack))

