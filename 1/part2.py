#!/bin/python
# AOC 1 - Part 2 (Optimized Math Approach)

def solve_part2(filename='input.txt'):
    with open(filename, 'r') as f:
        rotations = f.read().split()

    dial = 50
    answer = 0

    for item in rotations:
        direction = item[0]
        amount = int(item[1:])

        # 1. Full Loops
        # Every 100 steps guarantees we pass zero exactly once
        full_loops, remainder = divmod(amount, 100)
        answer += full_loops

        # 2. Partial Turn (The Remainder)
        if remainder > 0:
            if direction == 'R':
                # Moving Right (Addition): 
                # We hit 0 if we reach or exceed the wrap-point (100)
                if dial + remainder >= 100:
                    answer += 1
                dial = (dial + remainder) % 100

            elif direction == 'L':
                # Moving Left (Subtraction):
                # We hit 0 if we touch or go below 0.
                # EXCEPTION: If we start at 0, moving Left leaves 0 immediately, so no hit.
                if dial != 0 and (dial - remainder) <= 0:
                    answer += 1
                dial = (dial - remainder) % 100

    return answer

# --- Execution & Quick Test ---
if __name__ == "__main__":
    # 1. Real Run
    try:
        result = solve_part2()
        print(f"Final Password: {result}")
    except FileNotFoundError:
        print("Error: input.txt not found.")

    # 2. Mini Logic Verification (Optional Debugging)
    # Let's verify the tricky "Left from 0" case we discussed
    print("\n--- Verifying Logic ---")
    
    # Case A: Start 0, move Left (Should NOT count)
    dial = 0
    rem = 10
    hits = 1 if (dial != 0 and (dial - rem) <= 0) else 0
    print(f"Start 0, L10 -> Hits: {hits} (Expected: 0)")
    
    # Case B: Start 5, move Left past 0 (Should count)
    dial = 5
    rem = 6
    hits = 1 if (dial != 0 and (dial - rem) <= 0) else 0
    print(f"Start 5, L6  -> Hits: {hits} (Expected: 1)")
