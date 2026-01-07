import unittest
import os
from part1 import solve_part1

class TestAOCPart1(unittest.TestCase):
    
    def setUp(self):
        self.test_file = 'test_input_p1.txt'

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def create_input(self, content):
        with open(self.test_file, 'w') as f:
            f.write(content)

    def test_single_hit(self):
        # Scenario: Start 50 -> R50 
        # Lands on 0. 
        # Total Hits: 1
        self.create_input("R50")
        result = solve_part1(self.test_file)
        self.assertEqual(result, 1)

    def test_complex_movement(self):
        # Scenario: Start 50
        # R50 -> Lands on 0 (Hit 1). Current Dial: 0
        # L20 -> Lands on 80.        Current Dial: 80
        # R30 -> Lands on 10.        Current Dial: 10
        # Total Hits: 1
        self.create_input("R50 L20 R30")
        result = solve_part1(self.test_file)
        self.assertEqual(result, 1)

    def test_multiple_hits(self):
        # Scenario: Start 50
        # R50 -> Lands on 0 (Hit 1)
        # L20 -> Lands on 80
        # R20 -> Lands on 0 (Hit 2)
        # L100 -> Lands on 0 (Hit 3)
        self.create_input("R50 L20 R20 L100")
        result = solve_part1(self.test_file)
        self.assertEqual(result, 3)

    def test_no_hits(self):
        # Scenario: Start 50
        # R10 -> 60
        # R10 -> 70
        # Total Hits: 0
        self.create_input("R10 R10")
        result = solve_part1(self.test_file)
        self.assertEqual(result, 0)

if __name__ == '__main__':
    unittest.main()
