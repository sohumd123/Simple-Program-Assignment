import program
import unittest

class TestAddNumbers(unittest.TestCase):
    def test_integer(self):
        self.assertEqual(program.add_numbers(2, 2), 4)

if __name__ == '__main__':
    unittest.main()