#!/usr/bin/env python3
def solve_day2_generator():
    # 1. Parse Input
    try:
        with open('input.txt', 'r') as f:
            raw_data = f.read().strip()
    except FileNotFoundError:
        # Fallback to the example data if file is missing
        raw_data = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862"
        print("Using Example Data (Input file not found)...")

    # Parse ranges into a list of [start, end]
    ranges = [list(map(int, x.split('-'))) for x in raw_data.split(',')]
    
    # Calculate the maximum possible number we need to check
    # This tells us how many digits our generator needs to go up to.
    max_val = max(r[1] for r in ranges)
    max_digits = len(str(max_val))

    total_sum = 0
    
    # 2. The Generator Loop
    # We iterate through "half-lengths".
    # If max_val is 1000 (4 digits), we need halves of length 1 and 2.
    # half_len = 1 -> Generates 11, 22...
    # half_len = 2 -> Generates 1010, 1212...
    
    # We go up to max_digits // 2 because the ID is length 2 * L
    for L in range(1, (max_digits // 2) + 1):
        
        # Calculate start and end for the "seed"
        # Length 1: 1 to 9
        # Length 2: 10 to 99
        # Length 3: 100 to 999
        start_seed = 10**(L - 1)
        end_seed = 10**L  # The range function stops before this
        
        for seed in range(start_seed, end_seed):
            # Construct the candidate (e.g., 12 -> "1212" -> 1212)
            candidate = int(str(seed) + str(seed))
            
            # Optimization: If we passed the absolute max of all ranges, we can stop early
            if candidate > max_val:
                break
                
            # 3. Check if this candidate is in ANY of our ranges
            # This is the "Verification" step.
            for r_start, r_end in ranges:
                if r_start <= candidate <= r_end:
                    total_sum += candidate
                    # Break here so we don't double-count if ranges overlap (though usually they don't)
                    break 

    print(f"Final Sum: {total_sum}")

if __name__ == "__main__":
    solve_day2_generator()
