# Advent of Code 2025 - Day 5: Cafeteria (Inventory Management)

**Author:** MBC
**Date:** February 2026
**Language:** Python 3.12.3 (with NumPy)

## Project Overview

Solution for Day 5 of the Advent of Code 2025 challenge. The puzzle requires validating a massive list of Inventory IDs against a database of valid, overlapping ID ranges ("Fresh" ingredients).

**Key Technical Shift:** Transitioned from brute-force linear scanning to **Interval Merging** combined with **Vectorized Binary Search**, reducing time complexity from $O(M \times N)$ to $O(M \log K)$.

### The Challenge

* **Part 1:** Parse a database of overlapping ranges and a list of candidate IDs. Determine exactly how many candidate IDs fall within at least one valid range.
* **Part 2:** Ignore the candidate IDs. Calculate the total capacity of all valid ranges combined (how many total IDs are theoretically considered "fresh").

## Solution Strategy

### 1. Range Optimization (Merge Intervals)
Raw input ranges often overlap (e.g., `10-14` and `12-18`). To process queries efficiently, we first clean the dataset:
1.  **Sort** the ranges by their start value.
2.  **Iterate** and **Merge** any range that starts before the previous one ends (resulting in `10-18`).
This creates a minimal set of perfectly disjoint rules.

### 2. Part 1: Vectorized Binary Search (`np.searchsorted`)
Instead of iterating through rules for every ID, we use NumPy:
* Identify the *only possible* valid range for each ID using a binary search.
* Apply a parallel, C-speed comparison to verify if the ID is less than or equal to that specific range's end value.

### 3. Part 2: O(1) Capacity Math
Because the DevSecOps architecture in Part 1 perfectly cleaned the overlapping rules, Part 2 is reduced to simple arithmetic. We iterate through the disjoint ranges and apply the inclusive size formula: `(End - Start) + 1`.

## Project Structure

```text
/
├── input.txt              # Raw input (Ranges \n\n IDs)
├── part1.py               # Part 1 solution (Interval Merge + Binary Search)
├── part2.py               # Part 2 solution (Disjoint Capacity Math)
├── test_part1.py          # Unit tests for Part 1
├── test_part2.py          # Unit tests for Part 2
└── run_all.sh             # Automation script
```

## Usage
Requires NumPy:
```python
pip install numpy
```
Run all tests and solutions:
```shell
./run_all.sh
```

