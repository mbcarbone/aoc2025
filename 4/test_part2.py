import unittest
import os
from part2 import solve_part2

class TestDay4Part2(unittest.TestCase):
    def setUp(self):
        self.test_file = 'test_input.txt'

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def create_input(self, content):
        with open(self.test_file, 'w') as f:
            f.write(content)

    def test_iterative_removal(self):
        # The example from Part 2 prompt (Expected Total: 43)
        data = (
            "..@@.@@@@.\n"
            "@@@.@.@.@@\n"
            "@@@@@.@.@@\n"
            "@.@@@@..@.\n"
            "@@.@@@@.@@\n"
            ".@@@@@@@.@\n"
            ".@.@.@.@@@\n"
            "@.@@@.@@@@\n"
            ".@@@@@@@@.\n"
            "@.@.@@@.@."
        )
        self.create_input(data)
        result = solve_part2(self.test_file)
        self.assertEqual(result, 43)

if __name__ == '__main__':
    unittest.main()
