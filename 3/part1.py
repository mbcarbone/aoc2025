#!/usr/bin/env python3
# AOC 2025 Day 3 - Part 1: Battery Joltages

def solve_part1(filename='input.txt'):
    """
    For each bank (line), find the largest 2-digit number possible
    by picking two digits in their original order.
    Strategy: Find max digit for Tens place, then max digit after it for Ones place.
    """
    try:
        with open(filename, 'r') as f:
            lines = f.read().splitlines()
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
        return None

    total_joltage = 0

    for line in lines:
        if not line: continue
        
        # Convert string to list of integers for easier handling
        digits = [int(c) for c in line]
        
        # 1. Identify candidates for the Tens place.
        # It can be any digit except the very last one.
        tens_candidates = digits[:-1]
        max_tens_val = max(tens_candidates)
        
        # 2. Check all occurrences of this best Tens digit
        # (There might be multiple, e.g., '9...9...')
        best_bank_score = 0
        
        for i, d in enumerate(digits[:-1]):
            if d == max_tens_val:
                # Find the biggest digit to the right of this position
                remaining = digits[i+1:]
                max_ones_val = max(remaining)
                
                score = (d * 10) + max_ones_val
                if score > best_bank_score:
                    best_bank_score = score
        
        total_joltage += best_bank_score

    return total_joltage

if __name__ == "__main__":
    result = solve_part1()
    if result is not None:
        print(f"Part 1 (Total Output Joltage): {result}")
