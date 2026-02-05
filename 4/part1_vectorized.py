#!/usr/bin/env python3
# AOC 2025 Day 4 - Part 1: Printing Department (NumPy Version)

import numpy as np

def solve_part1(filename='input.txt'):
    """
    Counts accessible paper rolls using Vectorized Operations.
    Accessible = Is a Roll ('@') AND has < 4 neighbors.
    """
    try:
        with open(filename, 'r') as f:
            # Read lines, strip whitespace
            lines = [list(line.strip()) for line in f if line.strip()]
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
        return None

    # 1. Parse into a Boolean Matrix (1 for '@', 0 for '.')
    # We use ord() or just comparison to make it numeric
    grid = np.array(lines) == '@'  # Boolean Array
    grid = grid.astype(int)        # Convert True/False to 1/0
    
    # 2. Calculate Neighbor Counts using Padding + Slicing
    # We want to look at the 8 neighbors.
    # The easiest way in pure numpy is to pad the grid with 0s,
    # then add up the 8 shifted versions of the grid.
    
    padded = np.pad(grid, pad_width=1, mode='constant', constant_values=0)
    
    # neighbor_count starts at 0
    neighbor_count = np.zeros_like(grid, dtype=int)
    
    # Add all 8 directions:
    # rows: 0:-2 is "shifted up", 2: is "shifted down", 1:-1 is "center"
    # cols: same logic
    
    neighbor_count += padded[0:-2, 0:-2] # Top-Left
    neighbor_count += padded[0:-2, 1:-1] # Top-Center
    neighbor_count += padded[0:-2, 2:]   # Top-Right
    
    neighbor_count += padded[1:-1, 0:-2] # Mid-Left
    neighbor_count += padded[1:-1, 2:]   # Mid-Right
    
    neighbor_count += padded[2:, 0:-2]   # Bottom-Left
    neighbor_count += padded[2:, 1:-1]   # Bottom-Center
    neighbor_count += padded[2:, 2:]     # Bottom-Right
    
    # 3. Apply the Rules (Vectorized Boolean Logic)
    # Rule A: Must be a roll (@) -> grid == 1
    # Rule B: Neighbors < 4      -> neighbor_count < 4
    
    accessible_mask = (grid == 1) & (neighbor_count < 4)
    
    # 4. Count the results
    return np.sum(accessible_mask)

if __name__ == "__main__":
    result = solve_part1()
    if result is not None:
        print(f"Part 1 (Accessible Rolls): {result}")
