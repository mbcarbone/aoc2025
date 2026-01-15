#!/bin/bash

echo "--- AOC 2025 Day 2 Automation ---"

# 1. Run Unit Tests
echo "[1/3] Running Unit Tests..."
python3 -m unittest discover -p "test_*.py" -v
if [ $? -ne 0 ]; then
    echo "Tests Failed! Aborting."
    exit 1
fi

# 2. Run Part 1
echo ""
echo "[2/3] Executing Part 1..."
python3 part1.py

# 3. Run Part 2
echo ""
echo "[3/3] Executing Part 2..."
python3 part2.py

echo ""
echo "--- All Tasks Completed Successfully ---"
