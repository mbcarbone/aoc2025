#!/usr/bin/env python3
# AOC 1 - Part 1: Count Zero Hits (End of Rotation)
from itertools import accumulate

def solve_part1(filename='input.txt'):
    """
    Counts how many times the dial lands EXACTLY on 0 
    at the END of a rotation.
    """
    try:
        with open(filename, 'r') as f:
            # 1. Parse movements into a list of integers (R=+ve, L=-ve)
            moves = [
                int(x[1:]) if x[0] == 'R' else -int(x[1:]) 
                for x in f.read().split()
            ]
            
        # 2. Use accumulate to calculate the running total at each step
        #    Start at 50.
        #    (50 + running_sum) % 100 checks the position at every stop.
        #    We count how many times that result is 0.
        
        # 'initial=0' ensures we start counting FROM the first move, not the start pos.
        running_positions = (
            (50 + current_sum) % 100 
            for current_sum in accumulate(moves)
        )
        
        # Count the zeros
        return sum(1 for pos in running_positions if pos == 0)

    except FileNotFoundError:
        print(f"Error: {filename} not found.")
        return None

if __name__ == "__main__":
    result = solve_part1()
    if result is not None:
        print(f"Part 1 (Zero Hits): {result}")
