#!/usr/bin/env python3
# AOC 1 - Part 2: Count Hits on Zero

def solve_part2(filename='input.txt'):
    """
    Counts how many times the dial passes or lands on '0'.
    Optimized: Uses 'Infinite Dial' logic (Absolute Position).
    """
    try:
        with open(filename, 'r') as f:
            # Convert "R50" -> 50 and "L20" -> -20 in one pass
            rotations = [(1 if x[0] == 'R' else -1) * int(x[1:]) for x in f.read().split()]
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
        return None

    pos = 50  # Absolute position (can go >100 or <0)
    answer = 0

    for move in rotations:
        prev = pos
        pos += move
        
        # Mathematical "Mic Drop":
        # Calculates how many "100 boundaries" were crossed between prev and pos.
        # (move < 0) acts as a boolean switch (0 or 1) to handle the Left-turn offset.
        answer += abs((pos - (move < 0)) // 100 - (prev - (move < 0)) // 100)

    return answer

if __name__ == "__main__":
    result = solve_part2()
    if result is not None:
        print(f"Part 2 (Password Count): {result}")
