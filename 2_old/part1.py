def solve_day2():
    # 1. The Parser
    def parse_ranges(data_str):
        # Cleans whitespace and parses "1-2, 3-4" into integers
        return [list(map(int, x.split('-'))) for x in data_str.strip().split(',')]

    # 2. The Logic Check (Is it an invalid ID?)
    def is_invalid(num):
        s = str(num)
        length = len(s)
        
        # Optimization: Must be even length to have two equal halves
        if length % 2 != 0:
            return False
        
        # Split in half
        mid = length // 2
        return s[:mid] == s[mid:]

    # ---------------------------------------------------------
    # TEST: Verify against the examples in your prompt
    # ---------------------------------------------------------
    example_data = (
        "11-22,95-115,998-1012,1188511880-1188511890,"
        "222220-222224,1698522-1698528,446443-446449,"
        "38593856-38593862"
    )
    
    test_ranges = parse_ranges(example_data)
    test_sum = 0
    
    print("--- Verifying Example Data ---")
    for start, end in test_ranges:
        for num in range(start, end + 1):
            if is_invalid(num):
                print(f"Found Invalid ID: {num}")
                test_sum += num
                
    print(f"Example Checksum: {test_sum}")
    print(f"Matches Expected (1227775554)? {test_sum == 1227775554}")
    print("-" * 30)

    # ---------------------------------------------------------
    # REAL RUN: Process 'input.txt'
    # ---------------------------------------------------------
    try:
        with open('input.txt', 'r') as f:
            real_data = f.read()
            
        real_ranges = parse_ranges(real_data)
        total_sum = 0
        
        for start, end in real_ranges:
            for num in range(start, end + 1):
                if is_invalid(num):
                    total_sum += num
                    
        print(f"\nFinal Answer (Sum of Invalid IDs): {total_sum}")
        
    except FileNotFoundError:
        print("\nError: 'input.txt' not found. Please ensure the file is in the folder.")

if __name__ == "__main__":
    solve_day2()
