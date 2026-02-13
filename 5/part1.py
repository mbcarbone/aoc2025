#!/usr/bin/env python3
# AOC 2025 Day 5 - Part 1: Cafeteria (NumPy Vectorized)

import numpy as np

def parse_input(filename):
    """Parses the two-section input: Ranges and IDs."""
    try:
        with open(filename, 'r') as f:
            content = f.read().strip()
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
        return [], []

    parts = content.split('\n\n')
    
    # Parse Ranges
    raw_ranges = []
    for line in parts[0].splitlines():
        start, end = map(int, line.split('-'))
        raw_ranges.append((start, end))

    # Parse IDs
    ids = [int(line) for line in parts[1].splitlines()]

    return raw_ranges, ids

def merge_intervals(ranges):
    """Sorts and merges overlapping intervals."""
    if not ranges: return []
    ranges.sort(key=lambda x: x[0])
    merged = [ranges[0]]
    for current_start, current_end in ranges[1:]:
        last_start, last_end = merged[-1]
        if current_start <= last_end:
             merged[-1] = (last_start, max(last_end, current_end))
        else:
             merged.append((current_start, current_end))
    return merged

def solve_part1(filename='input.txt'):
    ranges, ids = parse_input(filename)
    if not ranges or not ids: return 0

    # 1. Clean the ranges
    clean_ranges = merge_intervals(ranges)

    # 2. Convert to NumPy Arrays
    # Convert ids to a column vector: shape (N, 1)
    np_ids = np.array(ids)[:, np.newaxis] 
    
    # Convert ranges to row vectors: shape (1, M)
    starts = np.array([r[0] for r in clean_ranges])
    ends = np.array([r[1] for r in clean_ranges])

    # 3. Vectorized Check (The "Broadcasting" Magic)
    # This creates a boolean matrix of shape (N, M) in C-level code!
    # True if the ID is >= start AND <= end for that specific range.
    valid_matrix = (np_ids >= starts) & (np_ids <= ends)

    # 4. Collapse and Sum
    # .any(axis=1) checks each row. If an ID hit ANY valid range, it becomes True.
    fresh_mask = valid_matrix.any(axis=1)
    
    return np.sum(fresh_mask)

if __name__ == "__main__":
    result = solve_part1()
    if result is not None:
        print(f"Part 1 (Fresh Ingredients): {result}")
