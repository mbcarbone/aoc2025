#!/usr/bin/env python3
# AOC 2025 Day 4 - Part 1: KNN / Point Cloud Approach

import numpy as np
from sklearn.neighbors import KDTree

def solve_part1_knn(filename='input.txt'):
    try:
        with open(filename, 'r') as f:
            lines = [list(line.strip()) for line in f if line.strip()]
    except FileNotFoundError:
        return None

    # 1. Convert Grid to Coordinate List (Point Cloud)
    # np.argwhere gives us the indices (y, x) of every '@'
    grid = np.array(lines)
    points = np.argwhere(grid == '@')

    if len(points) == 0:
        return 0

    # 2. Build the Tree
    # We use Chebyshev metric because in a grid with diagonals:
    # A neighbor is anyone where max(|dx|, |dy|) <= 1
    tree = KDTree(points, metric='chebyshev')

    # 3. Query for Neighbors
    # query_radius returns the indices of points within 'r'.
    # r=1.0 gets all 8 surrounding cells.
    # count_only=True gives us just the numbers.
    neighbor_counts = tree.query_radius(points, r=1.0, count_only=True)

    # 4. Filter
    # Note: query_radius includes the point itself!
    # So "fewer than 4 neighbors" means "fewer than 5 items in the radius" 
    # (1 self + 3 neighbors = 4 total items).
    accessible_count = np.sum(neighbor_counts < 5)

    return accessible_count

if __name__ == "__main__":
    print(f"Part 1 (KNN): {solve_part1_knn()}")
