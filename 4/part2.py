#!/usr/bin/env python3
# AOC 2025 Day 4 - Part 2: Iterative Removal (Simulation)

import numpy as np
from numpy.lib.stride_tricks import sliding_window_view

def solve_part2(filename='input.txt'):
    """
    Simulates the iterative removal of paper rolls.
    1. Identify accessible rolls (neighbors < 4).
    2. Remove them.
    3. Repeat until no rolls can be removed.
    """
    try:
        with open(filename, 'r') as f:
            lines = [list(line.strip()) for line in f if line.strip()]
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
        return None

    # 1. Parse into a Boolean Matrix (1 for '@', 0 for '.')
    # We use int type so we can do math on it
    grid = (np.array(lines) == '@').astype(int)
    
    total_removed = 0
    iteration = 0
    
    while True:
        # --- Step A: Calculate Neighbors (Same as Part 1) ---
        
        # Pad the grid
        padded = np.pad(grid, pad_width=1, mode='constant', constant_values=0)
        
        # Create Sliding Windows
        windows = sliding_window_view(padded, window_shape=(3, 3))
        
        # Sum windows (gives center + neighbors)
        window_sums = windows.sum(axis=(2, 3))
        
        # Subtract center to get neighbor count
        neighbor_count = window_sums - grid
        
        # --- Step B: Apply "Pruning" Logic ---
        
        # Mask of items to remove THIS round
        # Rule: Must be existing roll (1) AND neighbors < 4
        removable_mask = (grid == 1) & (neighbor_count < 4)
        
        count = np.sum(removable_mask)
        
        # --- Step C: Check Stop Condition ---
        if count == 0:
            break
            
        # --- Step D: Update State ---
        total_removed += count
        
        # Remove the items from the grid (Set to 0)
        # NumPy lets us index with the boolean mask directly!
        grid[removable_mask] = 0
        
        iteration += 1
        # Optional: Print progress for large grids
        # print(f"Round {iteration}: Removed {count} rolls.")

    return total_removed

if __name__ == "__main__":
    result = solve_part2()
    if result is not None:
        print(f"Part 2 (Total Removed): {result}")
