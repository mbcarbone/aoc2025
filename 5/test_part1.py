import unittest
import os
from part1 import solve_part1, merge_intervals

class TestDay5Part1(unittest.TestCase):
    def setUp(self):
        self.test_file = 'test_input.txt'

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def create_input(self, content):
        with open(self.test_file, 'w') as f:
            f.write(content)

    def test_example_scenario(self):
        # Example from Prompt
        data = (
            "3-5\n"
            "10-14\n"
            "16-20\n"
            "12-18\n\n"
            "1\n5\n8\n11\n17\n32"
        )
        self.create_input(data)
        result = solve_part1(self.test_file)
        # Expected: 5, 11, 17 are fresh. Total 3.
        self.assertEqual(result, 3)

    def test_merge_logic(self):
        # Test the interval merging specifically
        raw = [(10, 14), (12, 18), (16, 20)]
        # 10-14 overlaps 12-18 -> 10-18
        # 10-18 overlaps 16-20 -> 10-20
        expected = [(10, 20)]
        self.assertEqual(merge_intervals(raw), expected)

    def test_no_overlap(self):
        raw = [(1, 5), (10, 15)]
        self.assertEqual(merge_intervals(raw), [(1, 5), (10, 15)])

if __name__ == '__main__':
    unittest.main()
