import unittest
import os
from part1 import solve_part1

class TestAOCPart1(unittest.TestCase):
    
    def setUp(self):
        # Create a dummy input file for testing
        self.test_file = 'test_input.txt'
        with open(self.test_file, 'w') as f:
            # Example Scenario:
            # Start at 50
            # R50 -> Lands on 0 (Count 1)
            # L20 -> Lands on 80
            # R20 -> Lands on 0 (Count 2)
            # L100 -> Lands on 0 (Count 3)
            f.write("R50 L20 R20 L100")

    def tearDown(self):
        # Clean up the dummy file after tests run
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_solve_part1(self):
        # Run the solver on our dummy file
        result = solve_part1(self.test_file)
        
        # We expect 3 hits on zero based on the setup above
        self.assertEqual(result, 3)

    def test_no_hits(self):
        # Test a case where it never hits zero
        with open('no_hit.txt', 'w') as f:
            f.write("R10 R10 R10")
        
        result = solve_part1('no_hit.txt')
        self.assertEqual(result, 0)
        os.remove('no_hit.txt')

if __name__ == '__main__':
    unittest.main()
