#!/usr/bin/env python3
# AOC 2025 Day 4 - Part 1: Printing Department (NumPy Sliding Window) - Yes I know ... SciPy

import numpy as np
from numpy.lib.stride_tricks import sliding_window_view

def solve_part1(filename='input.txt'):
    """
    Counts accessible paper rolls using NumPy Sliding Windows.
    Accessible = Is a Roll ('@') AND has < 4 neighbors.
    """
    try:
        with open(filename, 'r') as f:
            lines = [list(line.strip()) for line in f if line.strip()]
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
        return None

    # 1. Parse into a Boolean Matrix (1 for '@', 0 for '.')
    grid = (np.array(lines) == '@').astype(int)
    
    # 2. Pad the grid so edges have neighbors (value 0)
    padded = np.pad(grid, pad_width=1, mode='constant', constant_values=0)
    
    # 3. Create 3x3 Sliding Windows
    # This creates a view of shape (Rows, Cols, 3, 3)
    windows = sliding_window_view(padded, window_shape=(3, 3))
    
    # 4. Calculate Neighbor Counts
    # Sum over the last two axes (the 3x3 window dimensions)
    # This gives us the sum of the center + all 8 neighbors
    window_sums = windows.sum(axis=(2, 3))
    
    # Subtract the center cell itself to leave only the neighbor count
    neighbor_count = window_sums - grid
    
    # 5. Apply Rules
    # Rule: Is a roll (grid==1) AND has < 4 neighbors
    accessible_mask = (grid == 1) & (neighbor_count < 4)
    
    return np.sum(accessible_mask)

if __name__ == "__main__":
    result = solve_part1()
    if result is not None:
        print(f"Part 1 (Accessible Rolls): {result}")
