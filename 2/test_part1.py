import unittest
import os
from part1 import solve_part1

class TestAOCDay2Part1(unittest.TestCase):

    def setUp(self):
        self.test_file = 'test_input_p1.txt'

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def create_input(self, content):
        with open(self.test_file, 'w') as f:
            f.write(content)

    def test_example_scenario(self):
        # Example from prompt
        # Invalid IDs found: 11, 22, 99, 1010, 1188511885, 222222, 446446, 38593859
        # Sum: 1227775554
        data = (
            "11-22,95-115,998-1012,1188511880-1188511890,"
            "222220-222224,1698522-1698528,446443-446449,"
            "38593856-38593862"
        )
        self.create_input(data)
        result = solve_part1(self.test_file)
        self.assertEqual(result, 1227775554)

    def test_simple_case(self):
        # 1212 is valid, 1213 is not
        self.create_input("1210-1215")
        result = solve_part1(self.test_file)
        self.assertEqual(result, 1212)

if __name__ == '__main__':
    unittest.main()
