#!/usr/bin/env python3
# AOC 2025 Day 6 - Part 1: Trash Compactor (Optimized Slicing)

import math

def solve_part1(filename='input.txt'):
    try:
        with open(filename, 'r') as f:
            lines = f.read().splitlines()
    except FileNotFoundError:
        return 0

    if not lines:
        return 0

    # 1. Pad the grid
    max_len = max(len(l) for l in lines)
    grid = [l.ljust(max_len) for l in lines]

    # 2. Find indices of completely empty columns
    empty_cols = [i for i in range(max_len) if all(row[i] == ' ' for row in grid)]

    # 3. Create cut boundaries (adding virtual edges at the start and end)
    boundaries = [-1] + empty_cols + [max_len]

    grand_total = 0

    # 4. Use zip to pair up [start, end] boundaries cleanly
    for start, end in zip(boundaries, boundaries[1:]):
        # Skip consecutive empty columns (width of 1)
        if start + 1 == end:
            continue
        
        # Extract the block vertically, strip spaces, and ignore empty lines
        block = [row[start+1:end].strip() for row in grid if row[start+1:end].strip()]
        
        if block:
            operator = block[-1]
            numbers = [int(x) for x in block[:-1]]
            
            # Execute math
            grand_total += math.prod(numbers) if operator == '*' else sum(numbers)

    return grand_total

if __name__ == "__main__":
    result = solve_part1()
    if result:
        print(f"Part 1 (Grand Total): {result}")
