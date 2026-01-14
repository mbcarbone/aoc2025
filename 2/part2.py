#!/usr/bin/env python3
def solve_day2_extended():
    # 1. Parse Input
    try:
        with open('input.txt', 'r') as f:
            raw_data = f.read().strip()
    except FileNotFoundError:
        # Example data from your prompt
        raw_data = (
            "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,"
            "1698522-1698528,446443-446449,38593856-38593862,565653-565659,"
            "824824821-824824827,2121212118-2121212124"
        )
        print("Using Example Data (Input file not found)...")

    # Parse ranges
    ranges = [list(map(int, x.split('-'))) for x in raw_data.split(',')]
    
    # Find the ceiling (Optimization)
    max_val = max(r[1] for r in ranges)
    
    # 2. Generate ALL Candidates
    candidates = set()
    
    # We iterate seeds starting from 1. 
    # We stop when even the smallest repetition (seed + seed) is bigger than max_val.
    # The max seed is roughly max_val // 10 (since it needs to be repeated at least once).
    # But checking "start_candidate > max_val" inside the loop is safer and easier.
    
    seed = 1
    while True:
        s_seed = str(seed)
        
        # Start with 2 repetitions
        current_str = s_seed + s_seed
        current_val = int(current_str)
        
        # If even the smallest repetition is too big, we are done generating seeds.
        if len(current_str) > len(str(max_val)) and current_val > max_val:
            break
            
        # Generate repetitions: 2x, 3x, 4x...
        while current_val <= max_val:
            candidates.add(current_val)
            
            # Add another copy of the seed
            current_str += s_seed
            current_val = int(current_str)
        
        seed += 1

    # 3. Sum Valid Candidates
    total_sum = 0
    
    # Filter: Only keep candidates that are actually inside one of the requested ranges
    # We sort candidates just to be orderly, though not strictly required for sum
    for cand in sorted(candidates):
        for r_start, r_end in ranges:
            if r_start <= cand <= r_end:
                total_sum += cand
                break # Count it once, even if ranges somehow overlapped

    print(f"Final Sum: {total_sum}")

if __name__ == "__main__":
    solve_day2_extended()
