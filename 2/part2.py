#!/usr/bin/env python3
# AOC 2025 Day 2 - Part 2: Repeated Sequences

def solve_part2(filename='input.txt'):
    """
    Calculates the sum of invalid IDs based on Repetition.
    Invalid ID: A number made of a sequence repeated 2+ times (e.g., 123123 or 111).
    Strategy: Generator Approach (O(sqrt N)).
    """
    try:
        with open(filename, 'r') as f:
            data = f.read().strip()
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
        return None

    ranges = [list(map(int, x.split('-'))) for x in data.split(',')]
    
    if not ranges:
        return 0

    max_val = max(r[1] for r in ranges)
    candidates = set()
    
    # Generate all repeating numbers up to max_val
    seed = 1
    while True:
        s_seed = str(seed)
        
        # Start with 2 repetitions
        current_str = s_seed + s_seed
        
        # If the smallest repetition is already too long/large, stop generating seeds
        if len(current_str) > len(str(max_val)) and int(current_str) > max_val:
            break
            
        current_val = int(current_str)
        
        # Generate repetitions: 2x, 3x, 4x...
        while current_val <= max_val:
            candidates.add(current_val)
            current_str += s_seed
            current_val = int(current_str)
        
        seed += 1

    # Sum only candidates that fall within the requested ranges
    total_sum = 0
    for cand in candidates:
        for r_start, r_end in ranges:
            if r_start <= cand <= r_end:
                total_sum += cand
                break 

    return total_sum

if __name__ == "__main__":
    result = solve_part2()
    if result is not None:
        print(f"Part 2 (Sum of Repeated IDs): {result}")
