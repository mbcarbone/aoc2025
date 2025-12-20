#!/bin/python
# AOC 1
import sys
sys.path.insert(0, '.')

"""
AOC 1 & 2
MBC - 12/2025
"""

def stepone():
    # open and close input.txt
    data = open('input.txt', 'r')
    rotations = data.read().split()
    data.close()

    # initial dial setting
    dial = 50
    answer = 0

    for i in range(len(rotations)):
        amount = int(rotations[i][1:])
        direction = rotations[i][0]
        if direction == 'R':
            dial = (dial + amount) % 100
        elif direction == 'L':
            dial = (dial - amount) % 100
    
    # Check if we landed on 0
    if dial == 0:
        answer += 1  # Count the occurrence, don't add the amount!
    
    print(answer)


if __name__ == "__stepone_":
    stepone()
