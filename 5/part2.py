#!/usr/bin/env python3
# AOC 2025 Day 5 - Part 2: Total Fresh Capacity

def parse_ranges(filename):
    """Parses only the first section of the input (the ranges)."""
    try:
        with open(filename, 'r') as f:
            content = f.read().strip()
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
        return []

    # Split on double newline, but we only care about the first block
    parts = content.split('\n\n')
    
    raw_ranges = []
    if parts[0]:
        for line in parts[0].splitlines():
            # Skip any empty lines that might sneak in
            if not line.strip():
                continue
            start, end = map(int, line.strip().split('-'))
            raw_ranges.append((start, end))

    return raw_ranges

def merge_intervals(ranges):
    """
    Merges overlapping intervals.
    """
    if not ranges:
        return []

    ranges.sort(key=lambda x: x[0])
    merged = [ranges[0]]

    for current_start, current_end in ranges[1:]:
        last_start, last_end = merged[-1]

        # Overlap or adjacent check
        if current_start <= last_end + 1: 
            merged[-1] = (last_start, max(last_end, current_end))
        else:
            merged.append((current_start, current_end))

    return merged

def solve_part2(filename='input.txt'):
    raw_ranges = parse_ranges(filename)
    
    # If the file wasn't found or was empty, this prevents a crash
    if not raw_ranges:
        print(f"DEBUG: No ranges found in {filename}!")
        return 0

    # 1. Clean the Rules
    clean_ranges = merge_intervals(raw_ranges)
    
    # 2. Calculate Total Capacity
    total_fresh = 0
    for start, end in clean_ranges:
        # Inclusive range length formula
        total_fresh += (end - start + 1)
        
    return total_fresh

if __name__ == "__main__":
    result = solve_part2()
    if result is not None:
        print(f"Part 2 (Total Fresh IDs): {result}")
