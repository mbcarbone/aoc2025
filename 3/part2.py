#!/usr/bin/env python3
# AOC 2025 Day 3 - Part 2: Maximize 12-Digit Sequence

def solve_part2(filename='input.txt'):
    """
    Finds the largest subsequence of length 12 from each line.
    Strategy: Monotonic Stack (Greedy Removal).
    We remove (len - 12) digits such that the resulting number is maximized.
    """
    try:
        with open(filename, 'r') as f:
            lines = f.read().splitlines()
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
        return None

    total_joltage = 0
    TARGET_LENGTH = 12

    for line in lines:
        if len(line) < TARGET_LENGTH:
            continue
            
        # Determine how many digits we are allowed to drop
        # e.g., if line is 15 chars, we can drop 3.
        drops_allowed = len(line) - TARGET_LENGTH
        
        stack = []
        
        for digit in line:
            # While we can still drop digits, AND the stack isn't empty,
            # AND the current digit is BIGGER than the one we last picked...
            # Kick the small one out!
            while drops_allowed > 0 and stack and stack[-1] < digit:
                stack.pop()
                drops_allowed -= 1
            
            stack.append(digit)
            
        # If we finished the loop and still have drops allowed (e.g., "9876..."),
        # we just trim from the end.
        result_digits = stack[:TARGET_LENGTH]
        
        # Join and sum
        val = int("".join(result_digits))
        total_joltage += val

    return total_joltage

if __name__ == "__main__":
    result = solve_part2()
    if result is not None:
        print(f"Part 2 (Total Output Joltage): {result}")
