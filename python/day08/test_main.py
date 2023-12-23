import unittest
import main


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here

    @unittest.skip("demonstrating skipping")
    def test_read_input(self):
        lines = main.read_input('test_input.txt')
        self.assertEqual(lines, ['JKT = KFV, CFQ', 'KFV = ', 'CFQ = '])



if __name__ == '__main__':
    unittest.main()
