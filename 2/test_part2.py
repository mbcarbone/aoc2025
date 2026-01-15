import unittest
import os
from part2 import solve_part2

class TestAOCDay2Part2(unittest.TestCase):

    def setUp(self):
        self.test_file = 'test_input_p2.txt'

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def create_input(self, content):
        with open(self.test_file, 'w') as f:
            f.write(content)

    def test_extended_example(self):
        # Example from Part 2 prompt (Includes 111, 999, 565656, etc.)
        # Sum: 4174379265
        data = (
            "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,"
            "1698522-1698528,446443-446449,38593856-38593862,565653-565659,"
            "824824821-824824827,2121212118-2121212124"
        )
        self.create_input(data)
        result = solve_part2(self.test_file)
        self.assertEqual(result, 4174379265)

    def test_triple_repeat(self):
        # 123123123 should be caught
        # Range 123123120 - 123123125
        self.create_input("123123120-123123125")
        result = solve_part2(self.test_file)
        self.assertEqual(result, 123123123)

if __name__ == '__main__':
    unittest.main()
