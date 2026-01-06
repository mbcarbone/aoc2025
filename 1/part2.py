#!/bin/python
# AOC 1 - Part 2 (Infinite Dial Variant)

with open('input.txt') as f:
    # Convert "R50" -> 50 and "L20" -> -20 in one pass
    rotations = [(1 if x[0] == 'R' else -1) * int(x[1:]) for x in f.read().split()]

pos = 50  # Absolute position (can go above 100 or below 0)
answer = 0

for move in rotations:
    prev = pos
    pos += move
    
    # Calculate how many "100 boundaries" exist between prev and pos
    if move > 0:
        answer += pos // 100 - prev // 100
    else:
        # For Left moves, we shift by -1 to handle the "landing on 0" logic correctly
        answer += (prev - 1) // 100 - (pos - 1) // 100

print(answer)
