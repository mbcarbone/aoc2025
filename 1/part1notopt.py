#!/bin/python
# AOC 1 - Part 1 (Optimized)
import sys

def solve_part1(filename='input.txt'):
    """
    Calculates how many times the dial lands EXACTLY on 0 
    at the END of a rotation.
    """
    try:
        with open(filename, 'r') as f:
            rotations = f.read().split()
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
        return 0

    dial = 50
    answer = 0

    for item in rotations:
        direction = item[0]
        amount = int(item[1:])
        
        if direction == 'R':
            dial = (dial + amount) % 100
        elif direction == 'L':
            # Python modulo handles negatives correctly (-1 % 100 = 99)
            dial = (dial - amount) % 100
            
        # Check if we landed on 0 at the END of the turn
        if dial == 0:
            answer += 1

    return answer

if __name__ == "__main__":
    result = solve_part1()
    print(f"Part 1 Answer: {result}")
