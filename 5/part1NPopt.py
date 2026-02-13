#!/usr/bin/env python3
# AOC 2025 Day 5 - Part 1: Cafeteria (NumPy Optimized)

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
    
    raw_ranges = []
    if parts[0]:
        for line in parts[0].splitlines():
            start, end = map(int, line.split('-'))
            raw_ranges.append((start, end))

    ids = []
    if len(parts) > 1 and parts[1]:
        ids = [int(line) for line in parts[1].splitlines()]

    return raw_ranges, ids

def merge_intervals(ranges):
    """
    Merges overlapping intervals.
    Standard Python is fine here as 'ranges' is usually small (ruleset).
    """
    if not ranges:
        return []

    # Sort by start time
    ranges.sort(key=lambda x: x[0])

    merged = [ranges[0]]

    for current_start, current_end in ranges[1:]:
        last_start, last_end = merged[-1]

        if current_start <= last_end + 1: 
            # Overlap or adjacent! Merge them.
            if current_start <= last_end:
                 merged[-1] = (last_start, max(last_end, current_end))
            else:
                 merged.append((current_start, current_end))
        else:
            merged.append((current_start, current_end))

    return merged

def solve_part1(filename='input.txt'):
    ranges, ids = parse_input(filename)
    if not ranges or not ids: 
        return 0

    # 1. Clean the Rules (Python)
    clean_ranges = merge_intervals(ranges)
    
    # 2. Vectorized Check (NumPy)
    # Convert to NumPy arrays
    ids_arr = np.array(ids)
    ranges_arr = np.array(clean_ranges) # Shape (N, 2)
    
    starts = ranges_arr[:, 0]
    ends = ranges_arr[:, 1]
    
    # 3. Binary Search for Membership (O(M log K))
    # For each ID, find the index 'i' in 'starts' where starts[i-1] <= ID < starts[i].
    # This identifies the ONLY range that *could* contain the ID.
    idx = np.searchsorted(starts, ids_arr, side='right') - 1
    
    # 4. Validation Logic
    # Filter out IDs that are smaller than the very first start time (idx == -1)
    valid_indices_mask = idx >= 0
    
    # Initialize result mask (default False)
    is_fresh = np.zeros_like(ids_arr, dtype=bool)
    
    # For valid candidates, check if ID <= end_time of the identified range
    # We use boolean indexing to only check the valid ones (preventing index errors)
    candidate_ids = ids_arr[valid_indices_mask]
    matching_range_ends = ends[idx[valid_indices_mask]]
    
    is_fresh[valid_indices_mask] = candidate_ids <= matching_range_ends
    
    return np.sum(is_fresh)

if __name__ == "__main__":
    result = solve_part1()
    if result is not None:
        print(f"Part 1 (Fresh Ingredients): {result}")
