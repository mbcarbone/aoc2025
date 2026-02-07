# Advent of Code 2025 - Day 4: Printing Department (Paper Rolls)

**Author:** MBC
**Date:** February 2026
**Language:** Python 3.12.3 (with NumPy)

## Project Overview

Solution for Day 4 of the Advent of Code 2025 challenge. The puzzle involves optimizing a warehouse grid by identifying and removing paper rolls based on their proximity to other rolls.

**Key Technical Shift:** Unlike previous days which used standard Python loops, this solution leverages **NumPy Vectorization** and **Matrix Operations** to process the grid in parallel.

### The Challenge

* **Part 1:** Identify "accessible" paper rolls. A roll is accessible if it has fewer than 4 adjacent neighbors (including diagonals).
* **Part 2:** Simulate a recursive removal process. Once an accessible roll is removed, it may reveal new accessible rolls behind it. Count the total number of rolls that can be removed until the system stabilizes.

## Solution Strategy

### Vectorization (No Loops)
Instead of iterating through every cell $(x, y)$ to count neighbors ($O(N)$ Python loops), we treat the grid as a numerical matrix.

1.  **Sliding Window View:** We create a $3 \times 3$ view of every cell using `numpy.lib.stride_tricks.sliding_window_view`.
2.  **Summation:** We sum these $3 \times 3$ windows instantly to get the neighbor count for the entire grid in one operation.
3.  **Boolean Masking:** We apply logic filters across the whole matrix at once:
    ```python
    mask = (grid == 1) & (neighbor_count < 4)
    ```

### Part 1: Static Snapshot
* Load grid as a Boolean Matrix (1 for `@`, 0 for `.`).
* Apply Sliding Window to count neighbors.
* Sum the mask to find the total count.

### Part 2: Cellular Automaton (Simulation)
* Wrap the vector logic in a `while True` loop.
* **Pruning Step:** In each iteration, identify valid candidates using the mask.
* **Update:** Set the identified cells to `0` (removing them).
* **Stop:** Break the loop when the number of removed items in a round is 0.

## Project Structure

```text
/
├── input.txt              # The raw puzzle input (Grid of . and @)
├── part1.py               # Part 1 solution (NumPy Sliding Window)
├── part2.py               # Part 2 solution (Iterative Simulation)
├── test_part1.py          # Unit tests for Part 1
├── test_part2.py          # Unit tests for Part 2
└── run_all.sh             # Automation script (Tests + Execution)
```
```shell
pip install numpy
./run_all.sh
```
