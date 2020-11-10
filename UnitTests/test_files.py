import unittest


class TestFiles(unittest.TestCase):

    def test_file_read_all(self):
        path = "C:\\Users\\simon\\.gitconfig"
        gc_file = open(path)
        gc_text = gc_file.read()
        print(gc_text)
        gc_file.close()

        self.assertEqual(True, gc_file.closed)

    def test_file_read_with_loop(self):
        path = "C:\\Users\\simon\\.gitconfig"
        with open(path) as gc_file:
            for line in gc_file:
                print(line.rstrip())
        self.assertEqual(True, gc_file.closed)
        self.assertEqual("r", gc_file.mode)

