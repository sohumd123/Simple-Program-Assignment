import program
import unittest

class TestAddNumbers(unittest.TestCase):
    def test_integer(self):
        self.assertEqual(program.add_numbers(100, 100), 200)

if __name__ == '__main__':
    unittest.main()