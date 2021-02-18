import unittest

# Stacks and Queues are almost identical in Python
# append() is used for both PUSH and ENQUEUE, but...
#
# Stack:
# To POP last added item: pop()
#
# Queue:
# To DEQUEUE first added item: pop(0)
class TestStackAndQueues(unittest.TestCase):

    def test_stack(self):

        # Push
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
        self.assertEqual(3, pop_val)
        self.assertEqual(2, len(stack))


    def test_queue(self):

        # Enqueue
        queue = []
        queue.append(1)
        queue.append(2)
        queue.append(3)
        self.assertEqual(3, len(queue))

        # No peek... do it manually
        peek_val = queue[-1]
        self.assertEqual(3, peek_val)

        # Dequeue
        dequeue_val = queue.pop(0)
        self.assertEqual(1, dequeue_val)
        self.assertEqual(2, len(queue))

