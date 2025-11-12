# ---------------------------------
# 1012. Numbers With Repeated Digits
# ---------------------------------

# Problem: https://leetcode.com/problems/numbers-with-repeated-digits
#
# Given an integer n, return the number of positive integers in the range [1, n]
# that have at least one repeated digit.
# 
# Example 1:
# 
# Input: n = 20
# Output: 1
# 
# Explanation: The only positive number (<= 20) with at least 1 repeated digit is
# 11.
# 
# Example 2:
# 
# Input: n = 100
# Output: 10
# 
# Explanation: The positive numbers (<= 100) with atleast 1 repeated digit are 11,
# 22, 33, 44, 55, 66, 77, 88, 99, and 100.
# 
# Example 3:
# 
# Input: n = 1000
# Output: 262
# 
# 
# Constraints:
#         1 <= n <= 10⁹


# Solution: https://algo.monster/liteproblems/1012
# Credit: AlgoMonster
def num_dup_digits_at_most_n(n):
    from functools import cache
    
    # Convert n to string for digit-by-digit processing
    digits_str = str(n)
    
    @cache
    def count_unique_digit_numbers(
        position, 
        used_digits_mask, 
        has_leading_zeros, 
        is_bounded):
        # Base case: processed all digits
        if position >= len(digits_str):
            # Return 1 if we've formed a valid number (not just leading zeros)
            return 0 if has_leading_zeros else 1
        
        # Determine the maximum digit we can place at this position
        max_digit = int(digits_str[position]) if is_bounded else 9
        
        total_count = 0
        
        # Try each possible digit at current position
        for digit in range(max_digit + 1):
            # Handle leading zeros case
            if has_leading_zeros and digit == 0:
                # Continue with leading zeros, no longer bounded
                total_count += count_unique_digit_numbers(
                    position + 1, 
                    used_digits_mask, 
                    True, 
                    False
                )
            # Check if digit hasn't been used yet (bit is 0 in mask)
            elif (used_digits_mask >> digit) & 1 == 0:
                # Mark digit as used and continue
                new_mask = used_digits_mask | (1 << digit)
                # Stay bounded only if we're currently bounded AND using max digit
                new_bounded = is_bounded and (digit == max_digit)
                
                total_count += count_unique_digit_numbers(
                    position + 1, 
                    new_mask, 
                    False, 
                    new_bounded
                )
        
        return total_count
    
    # Count numbers without repeated digits from 1 to n
    unique_digit_count = count_unique_digit_numbers(0, 0, True, True)
    
    # Numbers with repeated digits = total numbers - numbers without repeated digits
    return n - unique_digit_count
    # Time: O(D² * 2¹⁰)
    # Space: O(D * 2¹⁰)


def main():
    result = num_dup_digits_at_most_n(20)
    print(result) # 1

    result = num_dup_digits_at_most_n(100)
    print(result) # 10

    result = num_dup_digits_at_most_n(1000)
    print(result) # 262

if __name__ == "__main__":
    main()
