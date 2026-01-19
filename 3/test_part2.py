import unittest
import os
from part2 import solve_part2

class TestDay3Part2(unittest.TestCase):
    def setUp(self):
        self.test_file = 'test_input.txt'

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def create_input(self, content):
        with open(self.test_file, 'w') as f:
            f.write(content)

    def test_extended_example(self):
        # The complex example from the prompt
        data = (
            "987654321111111\n"
            "811111111111119\n"
            "234234234234278\n"
            "818181911112111"
        )
        self.create_input(data)
        result = solve_part2(self.test_file)
        self.assertEqual(result, 3121910778619)

    def test_simple_drop(self):
        # Real logic test!
        # Input: "123456789012345" (Length 15) -> Needs Length 12
        # Logic: We can drop 3 digits.
        # 1. Compare '1' and '2'. '2' is bigger. Drop '1'. (Drops left: 2)
        # 2. Compare '2' and '3'. '3' is bigger. Drop '2'. (Drops left: 1)
        # 3. Compare '3' and '4'. '4' is bigger. Drop '3'. (Drops left: 0)
        # 4. Now we have 0 drops allowed. Keep the rest.
        # Expected Result: 456789012345
        
        self.create_input("123456789012345")
        result = solve_part2(self.test_file)
        self.assertEqual(result, 456789012345)

if __name__ == '__main__':
    unittest.main()
