import unittest
import os
from part1 import solve_part1

class TestDay6Part1(unittest.TestCase):
    def setUp(self):
        # Point to the file you already created
        self.test_file = 'input_test.txt'

    # We removed tearDown entirely so it never deletes your file!

    def test_worksheet_parsing(self):
        # 1. Check if your file is there
        if not os.path.exists(self.test_file):
            self.fail(f"Could not find {self.test_file}. Make sure it is saved in the 6/ folder.")

        # 2. Run the engine on your raw file
        result = solve_part1(self.test_file)
        
        # 3. Verify the grand total
        self.assertEqual(result, 4277556)

if __name__ == '__main__':
    unittest.main()
