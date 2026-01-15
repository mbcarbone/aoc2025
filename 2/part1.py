#!/usr/bin/env python3
# AOC 2025 Day 2 - Part 1: Invalid IDs (Equal Halves)

def solve_part1(filename='input.txt'):
    """
    Calculates the sum of invalid IDs.
    Invalid ID: A number composed of two equal halves (e.g., 1212).
    """
    try:
        with open(filename, 'r') as f:
            data = f.read().strip()
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
        return None

    # Helper: Parse ranges
    ranges = [list(map(int, x.split('-'))) for x in data.split(',')]
    
    total_sum = 0
    
    for start, end in ranges:
        for num in range(start, end + 1):
            s = str(num)
            length = len(s)
            
            # Must be even length to have two equal halves
            if length % 2 == 0:
                mid = length // 2
                if s[:mid] == s[mid:]:
                    total_sum += num
                    
    return total_sum

if __name__ == "__main__":
    result = solve_part1()
    if result is not None:
        print(f"Part 1 (Sum of Halved IDs): {result}")
