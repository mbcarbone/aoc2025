# Advent of Code 2025 - Day 5: Cafeteria (Inventory Management)

**Author:** MBC
**Date:** February 2026
**Language:** Python 3.12.3

## Project Overview

Solution for Day 5 of the Advent of Code 2025 challenge. The puzzle requires validating a list of Ingredient IDs against a set of valid ID ranges ("Fresh" ingredients).

**Key Algorithm:** **Interval Merging**. The problem presents ranges that may overlap (e.g., `10-14` and `12-18`). To efficiently process queries, we first sort and merge these into a minimal set of disjoint ranges.

### The Challenge

* **Part 1:** Parse a database of overlapping ranges and available IDs. Determine how many of the available IDs fall within at least one valid range.

## Solution Strategy

### Range Optimization (Merge Intervals)
Instead of checking an ID against every single raw range (which could be redundant), we clean the dataset first:
1.  **Sort** the ranges by their start value.
2.  **Iterate** through the sorted list.
3.  **Merge** any range that starts before the previous one ends (e.g., `[10, 14]` and `[12, 18]` become `[10, 18]`).

This reduces the complexity of checking an ID from $O(M)$ (raw ranges) to $O(K)$ (merged ranges), where $K \le M$.

## Project Structure

```text
/
├── input.txt              # Raw input (Ranges \n\n IDs)
├── part1.py               # Part 1 solution (Interval Merging)
├── test_part1.py          # Unit tests
└── run_all.sh             # Automation script
```
```shell
./run_all.sh
```
### Execution
1.  Paste the code into the `5/` folder files.
2.  Run the tests (`./run_all.sh`).
3.  If they pass, paste your input and get that star!
