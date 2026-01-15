#!/bin/bash
# Usage: ./new_day.sh <day_n> [day_n ...]
# Example: ./new_day.sh 3 4 5

if [ -z "$1" ]; then
    echo "Usage: $0 <day_number> [additional_days...]"
    exit 1
fi

for DAY in "$@"; do
    # ---------------------------------------------------------
    # VALIDATION: Ensure input is a pure integer
    # ---------------------------------------------------------
    if [[ ! "$DAY" =~ ^[0-9]+$ ]]; then
        echo "  [!] Error: '$DAY' is not a valid day number. Skipping."
        continue
    fi

    DIR="$DAY"
    echo "--- Checking Day $DAY in directory '$DIR/' ---"

    # 1. Ensure Directory Exists (Idempotent)
    if [ ! -d "$DIR" ]; then
        mkdir -p "$DIR"
        echo "  [+] Created directory: $DIR"
    fi

    # 2. Check input.txt
    if [ ! -f "$DIR/input.txt" ]; then
        touch "$DIR/input.txt"
        echo "  [+] Created input.txt"
    else
        echo "  [~] input.txt exists (Skipped)"
    fi

    # 3. Check part1.py
    if [ ! -f "$DIR/part1.py" ]; then
        cat <<EOT > "$DIR/part1.py"
#!/usr/bin/env python3
# AOC 2025 Day $DAY - Part 1

def solve_part1(filename='input.txt'):
    try:
        with open(filename, 'r') as f:
            data = f.read().strip()
    except FileNotFoundError:
        return None

    # TODO: Implement Logic Here
    return 0

if __name__ == "__main__":
    print(f"Part 1: {solve_part1()}")
EOT
        echo "  [+] Created part1.py"
        chmod +x "$DIR/part1.py"
    else
        echo "  [~] part1.py exists (Skipped)"
    fi

    # 4. Check part2.py
    if [ ! -f "$DIR/part2.py" ]; then
        cat <<EOT > "$DIR/part2.py"
#!/usr/bin/env python3
# AOC 2025 Day $DAY - Part 2

def solve_part2(filename='input.txt'):
    try:
        with open(filename, 'r') as f:
            data = f.read().strip()
    except FileNotFoundError:
        return None

    # TODO: Implement Logic Here
    return 0

if __name__ == "__main__":
    print(f"Part 2: {solve_part2()}")
EOT
        echo "  [+] Created part2.py"
        chmod +x "$DIR/part2.py"
    else
        echo "  [~] part2.py exists (Skipped)"
    fi

    # 5. Check test_part1.py
    if [ ! -f "$DIR/test_part1.py" ]; then
        cat <<EOT > "$DIR/test_part1.py"
import unittest
import os
from part1 import solve_part1

class TestDay${DAY}Part1(unittest.TestCase):
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
        # result = solve_part1(self.test_file)
        # self.assertEqual(result, EXPECTED_VALUE)
        pass

if __name__ == '__main__':
    unittest.main()
EOT
        echo "  [+] Created test_part1.py"
    else
        echo "  [~] test_part1.py exists (Skipped)"
    fi

    # 6. Check test_part2.py
    if [ ! -f "$DIR/test_part2.py" ]; then
        cat <<EOT > "$DIR/test_part2.py"
import unittest
import os
from part2 import solve_part2

class TestDay${DAY}Part2(unittest.TestCase):
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
EOT
        echo "  [+] Created test_part2.py"
    else
        echo "  [~] test_part2.py exists (Skipped)"
    fi

    # 7. Check run_all.sh
    if [ ! -f "$DIR/run_all.sh" ]; then
        cat <<EOT > "$DIR/run_all.sh"
#!/bin/bash
echo "--- AOC 2025 Day $DAY ---"
echo "[1/3] Running Tests..."
python3 -m unittest discover -p "test_*.py" -v
if [ \$? -ne 0 ]; then echo "Tests Failed"; exit 1; fi
echo ""
echo "[2/3] Running Part 1..."
python3 part1.py
echo ""
echo "[3/3] Running Part 2..."
python3 part2.py
EOT
        chmod +x "$DIR/run_all.sh"
        echo "  [+] Created run_all.sh"
    else
        echo "  [~] run_all.sh exists (Skipped)"
    fi

    # 8. Check README.md
    if [ ! -f "$DIR/README.md" ]; then
        cat <<EOT > "$DIR/README.md"
# Advent of Code 2025 - Day $DAY

**Author:** MBC
**Date:** $(date +%B) 2025
**Language:** Python 3.12.3

## Challenge
* **Part 1:** [Pending]
* **Part 2:** [Pending]
EOT
        echo "  [+] Created README.md"
    else
        echo "  [~] README.md exists (Skipped)"
    fi
    
    echo "  [Done] Day $DAY is ready."
    echo ""
done
