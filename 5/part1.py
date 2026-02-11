#!/usr/bin/env python3
# AOC 2025 Day 5 - Part 1: Cafeteria (Interval Merging)

def parse_input(filename):
    """Parses the two-section input: Ranges and IDs."""
    try:
        with open(filename, 'r') as f:
            content = f.read().strip()
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
        return [], []

    # Split on the double newline that separates the sections
    parts = content.split('\n\n')
    
    # Parse Ranges (Section 1)
    # Format: "3-5" -> (3, 5)
    raw_ranges = []
    for line in parts[0].splitlines():
        start, end = map(int, line.split('-'))
        raw_ranges.append((start, end))

    # Parse IDs (Section 2)
    # Format: "1" -> 1
    ids = [int(line) for line in parts[1].splitlines()]

    return raw_ranges, ids

def merge_intervals(ranges):
    """
    Takes a list of (start, end) tuples and merges overlaps.
    Example: [(10, 14), (12, 18)] -> [(10, 18)]
    Complexity: O(N log N) due to sorting.
    """
    if not ranges:
        return []

    # 1. Sort by start time
    ranges.sort(key=lambda x: x[0])

    merged = [ranges[0]]

    for current_start, current_end in ranges[1:]:
        last_start, last_end = merged[-1]

        if current_start <= last_end + 1: 
            # Overlap or adjacent! Merge them.
            # (We use +1 because ranges are inclusive integers, so 3-5 and 6-8 should technically merge to 3-8)
            # Actually, the problem logic implies standard overlap, 
            # but let's stick to strict overlap (current_start <= last_end) based on the prompt's examples.
            # Prompt Example: 10-14 and 16-20 do NOT merge.
            # Prompt Example: 12-18 and 16-20 DO merge.
            
            if current_start <= last_end:
                 # Extend the previous range to the max end
                 merged[-1] = (last_start, max(last_end, current_end))
            else:
                 # No overlap, start a new range
                 merged.append((current_start, current_end))
        else:
            merged.append((current_start, current_end))

    return merged

def solve_part1(filename='input.txt'):
    ranges, ids = parse_input(filename)
    if not ranges: return 0

    # Optimize the ranges
    clean_ranges = merge_intervals(ranges)

    fresh_count = 0
    for pid in ids:
        # Check if ID exists in ANY of the clean ranges
        # Since they are disjoint, we can break as soon as we find one.
        for start, end in clean_ranges:
            if start <= pid <= end:
                fresh_count += 1
                break
    
    return fresh_count

if __name__ == "__main__":
    result = solve_part1()
    if result is not None:
        print(f"Part 1 (Fresh Ingredients): {result}")
