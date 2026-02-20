import unittest
import os
from part1 import solve_part1

class TestDay6Part1(unittest.TestCase):
    def setUp(self):
        self.test_file = 'test_input.txt'

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def create_input(self, content):
        with open(self.test_file, 'w') as f:
            f.write(content)

    def test_worksheet_parsing(self):
        # CORRECTED: Exact spacing from the puzzle prompt
        data = (
            "123 328  51 64\n"
            " 45 64  387 23\n"
            "  6 98  215 314\n"
            "* +   * +  "
        )
        self.create_input(data)
        result = solve_part1(self.test_file)
        
        self.assertEqual(result, 4277556)

if __name__ == '__main__':
    unittest.main()
