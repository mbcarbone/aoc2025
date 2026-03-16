#!/usr/bin/env python3
# AOC 2025 Day 6 - Part 1: Trash Compactor (Robust Split-First)

import math
import re

def solve_part1(filename='input.txt'):
    try:
        with open(filename, 'r') as f:
            lines = f.read().splitlines()
    except FileNotFoundError:
        return 0

    if not lines: return 0

    # 1. Find every column index that has a non-space character
    max_len = max(len(l) for l in lines)
    active_cols = [c for c in range(max_len) if any(len(l) > c and l[c] != ' ' for l in lines)]
    
    # 2. Group these indices into blocks
    blocks = []
    if not active_cols: return 0
    start = active_cols[0]
    for i in range(1, len(active_cols)):
        if active_cols[i] > active_cols[i-1] + 1:
            blocks.append((start, active_cols[i-1]))
            start = active_cols[i]
    blocks.append((start, active_cols[-1]))

    # 3. Process each block
    grand_total = 0
    for b_start, b_end in blocks:
        # Slice the block and clean it
        slice_data = [l[b_start:b_end+1].strip() for l in lines if l[b_start:b_end+1].strip()]
        if not slice_data: continue
        
        operator = slice_data[-1]
        
        # Extract numbers using regex
        nums = []
        for item in slice_data[:-1]:
            nums.extend([int(n) for n in re.findall(r'\d+', item)])
        
        if operator == '*':
            grand_total += math.prod(nums)
        else:
            grand_total += sum(nums)
            
    return grand_total

# THIS IS WHAT I FORGOT!
if __name__ == "__main__":
    result = solve_part1()
    print(f"Part 1 (Grand Total): {result}")
