import unittest
import os
from part2 import solve_part2

class TestDay8Part2(unittest.TestCase):
    def setUp(self):
        self.test_file = 'test_input.txt'

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def create_input(self, content):
        with open(self.test_file, 'w') as f:
            f.write(content)

    def test_example(self):
        # self.create_input("EXAMPLE_DATA")
        # result = solve_part2(self.test_file)
        # self.assertEqual(result, EXPECTED_VALUE)
        pass

if __name__ == '__main__':
    unittest.main()
