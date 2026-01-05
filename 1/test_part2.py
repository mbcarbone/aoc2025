import unittest
import os
# Ensure this matches your actual filename (part2.py or part2_optimized.py)
from part2 import solve_part2

class TestAOCPart2(unittest.TestCase):

    def setUp(self):
        self.test_file = 'test_input_p2.txt'

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def create_input(self, content):
        with open(self.test_file, 'w') as f:
            f.write(content)

    def test_example_scenario(self):
        # Scenario: Start 50
        # R50 -> Lands on 0 (1 hit) -> Dial is 0
        # R100 -> Full circle (1 hit) -> Dial remains 0
        # L50 -> Moves 0 to 50 (0 hits) -> Dial is 50
        # L100 -> Full circle (1 hit) -> Dial remains 50
        # Total expected: 3
        self.create_input("R50 R100 L50 L100")
        result = solve_part2(self.test_file)
        self.assertEqual(result, 3)

    def test_passing_zero_multiple_times(self):
        # Scenario: Start 50
        # R250 -> 2 full loops (2 hits) + 50 remainder (lands on 0 -> 1 hit)
        # Total expected: 3
        self.create_input("R250")
        result = solve_part2(self.test_file)
        self.assertEqual(result, 3)

    def test_left_from_zero(self):
        # CRITICAL EDGE CASE
        # Start 50 -> R50 -> Lands on 0. (Hit 1)
        # Now at 0 -> L10 -> Moves to 90. (Should NOT count as a hit)
        # Now at 90 -> L90 -> Lands on 0. (Hit 2)
        # Total expected: 2
        self.create_input("R50 L10 L90")
        result = solve_part2(self.test_file)
        self.assertEqual(result, 2)

if __name__ == '__main__':
    unittest.main()
