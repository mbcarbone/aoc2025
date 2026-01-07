import unittest
import os
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
        # R50 (hit), R100 (hit), L50 (no hit), L100 (hit) -> Total 3
        self.create_input("R50 R100 L50 L100")
        result = solve_part2(self.test_file)
        self.assertEqual(result, 3)

    def test_left_from_zero(self):
        # Start 50 -> R50 (Hit 1, at 0). 
        # L10 (No hit, moves away). 
        # L90 (Hit 2, lands on 0).
        self.create_input("R50 L10 L90")
        result = solve_part2(self.test_file)
        self.assertEqual(result, 2)

if __name__ == '__main__':
    unittest.main()
