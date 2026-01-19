import unittest
import os
from part1 import solve_part1

class TestDay3Part1(unittest.TestCase):
    def setUp(self):
        self.test_file = 'test_input.txt'

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def create_input(self, content):
        with open(self.test_file, 'w') as f:
            f.write(content)

    def test_prompt_example(self):
        # The example from the prompt
        data = (
            "987654321111111\n"
            "811111111111119\n"
            "234234234234278\n"
            "818181911112111"
        )
        # Expected: 98 + 89 + 78 + 92 = 357
        self.create_input(data)
        result = solve_part1(self.test_file)
        self.assertEqual(result, 357)

    def test_simple_greedy(self):
        # '12345' -> Max is 4 (tens) then 5 (ones) = 45.
        # (NOT 35, NOT 25, NOT 15)
        self.create_input("12345")
        result = solve_part1(self.test_file)
        self.assertEqual(result, 45)

    def test_duplicate_tens(self):
        # '9195'
        # 1st '9' is followed by '195' (max 9) -> 99
        # 2nd '9' is followed by '5' (max 5) -> 95
        # Best should be 99
        self.create_input("9195")
        result = solve_part1(self.test_file)
        self.assertEqual(result, 99)

if __name__ == '__main__':
    unittest.main()
