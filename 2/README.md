# Advent of Code 2025 - Day 2: The Invalid IDs

**Author:** MBC  
**Date:** January 2026  
**Language:** Python 3.12.3

## Project Overview

Solution for Day 2 of the Advent of Code 2025 challenge. The puzzle involves scanning ranges of numbers to identify "Invalid IDs" based on repeating patterns.

### The Challenge

* **Part 1:** Find IDs that consist of two identical halves (e.g., `1212`, `99`).
  * *Approach:* Iterative string slicing check $O(N)$.
* **Part 2:** Find IDs that consist of ANY sequence repeated 2 or more times (e.g., `123123`, `111`).
  * *Approach:* Generator Factory Pattern $O(\sqrt{N})$ to handle large search spaces efficiently.

## Project Structure

```text
/
├── input.txt              # The raw puzzle input (CSV ranges)
├── part1.py               # Part 1 solution (Iterative Check)
├── part2.py               # Part 2 solution (Generator Factory)
├── test_part1.py          # Unit tests for Part 1
├── test_part2.py          # Unit tests for Part 2
└── run_all.sh             # Automation script
