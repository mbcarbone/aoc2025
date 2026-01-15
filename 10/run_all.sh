#!/bin/bash
echo "--- AOC 2025 Day 10 ---"
echo "[1/3] Running Tests..."
python3 -m unittest discover -p "test_*.py" -v
if [ $? -ne 0 ]; then echo "Tests Failed"; exit 1; fi
echo ""
echo "[2/3] Running Part 1..."
python3 part1.py
echo ""
echo "[3/3] Running Part 2..."
python3 part2.py
