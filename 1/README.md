# Advent of Code 2025 - Day 1: The Security Dial

**Author:** MBC  
**Date:** December 2025  
**Language:** Python 3.12.3

## Project Overview

This repository contains the solution for Day 1 of the Advent of Code 2025 challenge. The puzzle involves calculating the movements of a security dial (numbered 0-99) based on a series of rotational instructions (e.g., `R50`, `L20`).

### The Challenge

* **Part 1:** Calculate the final position of the dial after all rotations.
* **Part 2:** Determine a generated "password" by counting how many times the dial crosses or lands on `0` during the rotations (Method `0x434C49434B`).

## Project Structure

```text
/
├── input.txt              # The raw puzzle input
├── part1.py               # Part 1 solution (Simulation approach)
├── part2.py               # Part 2 solution (Mathematical O(1) approach)
├── test_part1.py          # Unit tests for Part 1
└── test_part2.py          # Unit tests for Part 2
```

```shell
pip install numpy
./run_all.sh
```
### Execution
1.  Paste the code into the `1/` folder files.
2.  Run the tests (`./run_all.sh`).
3.  If they pass, paste your input and get that star!
