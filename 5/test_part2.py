import unittest
import os
from part2 import solve_part2

class TestDay5Part2(unittest.TestCase):
    def setUp(self):
        self.test_file = 'test_input_part2.txt'

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def create_input(self, content):
        with open(self.test_file, 'w') as f:
            f.write(content)

    def test_total_capacity(self):
        # Example from Prompt (Section 1 only)
        data = (
            "3-5\n"
            "10-14\n"
            "16-20\n"
            "12-18\n"
        )
        self.create_input(data)
        result = solve_part2(self.test_file)
        
        # Ranges merge to 3-5 and 10-20.
        # Size of 3-5 is 3. Size of 10-20 is 11. Total = 14.
        self.assertEqual(result, 14)

if __name__ == '__main__':
    unittest.main()
