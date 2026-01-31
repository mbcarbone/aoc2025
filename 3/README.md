# Advent of Code 2025 - Day 3: Lobby (Battery Joltages)

**Author:** MBC
**Date:** January 2026
**Language:** Python 3.12.3

## Project Overview

Solution for Day 3 of the Advent of Code 2025 challenge. The puzzle involves optimizing battery configurations by selecting specific subsequences of digits from a larger string to maximize the resulting numerical value.

### The Challenge

* **Part 1:** Select exactly **two** batteries from each bank (line) to form the largest possible 2-digit number.
* **Part 2:** Select exactly **twelve** batteries from each bank to form the largest possible 12-digit number.

## Solution Strategy

### Part 1: Greedy Selection (Place Value)
To maximize a 2-digit number, the **tens place** is the dominant factor.
1.  Find the largest digit available in the bank (excluding the very last position).
2.  If that digit appears multiple times, check which occurrence is followed by the largest possible **ones digit**.
3.  **Complexity:** $O(N)$ (Linear Scan).

### Part 2: Monotonic Stack (Global Optimization)
To maximize a 12-digit subsequence, we effectively need to **remove** $K$ digits (where $K = \text{Length} - 12$) such that the remaining digits form the largest lexical sequence.
1.  Iterate through digits from left to right.
2.  Maintain a "Stack" of selected digits.
3.  **The Drop Rule:** If the current digit is **larger** than the last digit in the stack, and we still have "removals" allowed, pop the smaller digit off the stack.
4.  **Complexity:** $O(N)$ (Each digit is pushed/popped at most once).

## Project Structure

```text
/
├── input.txt              # The raw puzzle input (Battery Banks)
├── part1.py               # Part 1 solution (Greedy Pair Search)
├── part2.py               # Part 2 solution (Monotonic Stack)
├── test_part1.py          # Unit tests for Part 1
├── test_part2.py          # Unit tests for Part 2=
└── run_all.sh             # Automation script (Tests + Execution)
