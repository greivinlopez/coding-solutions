# --------------------------------------
# 902. Numbers At Most N Given Digit Set
# --------------------------------------

# Problem: https://leetcode.com/problems/numbers-at-most-n-given-digit-set
#
# Given an array of digits which is sorted in non-decreasing order. You can write
# numbers using each digits[i] as many times as we want. For example, if digits =
# ['1','3','5'], we may write numbers such as '13', '551', and '1351315'.
# 
# Return the number of positive integers that can be generated that are less than
# or equal to a given integer n.
# 
# Example 1:
# 
# Input: digits = ["1","3","5","7"], n = 100
# Output: 20
# 
# Explanation:
# The 20 numbers that can be written are:
# 1, 3, 5, 7, 11, 13, 15, 17, 31, 33, 35, 37, 51, 53, 55, 57, 71, 73, 75, 77.
# 
# Example 2:
# 
# Input: digits = ["1","4","9"], n = 1000000000
# Output: 29523
# 
# Explanation:
# We can write 3 one digit numbers, 9 two digit numbers, 27 three digit numbers,
# 81 four digit numbers, 243 five digit numbers, 729 six digit numbers,
# 2187 seven digit numbers, 6561 eight digit numbers, and 19683 nine digit
# numbers.
# In total, this is 29523 integers that can be written using the digits array.
# 
# Example 3:
# 
# Input: digits = ["7"], n = 8
# Output: 1
# 
# 
# Constraints:
#         1 <= digits.length <= 9
#         digits[i].length == 1
#         digits[i] is a digit from '1' to '9'.
#         All the values in digits are unique.
#         digits is sorted in non-decreasing order.
#         1 <= n <= 10⁹


# Solution: https://algo.monster/liteproblems/902
# Credit: AlgoMonster
def at_most_n_given_digit_set(digits, n):
    from functools import cache
    
    # Convert n to string for digit-by-digit processing
    n_str = str(n)
    # Convert digit strings to a set of integers for O(1) lookup
    available_digits = {int(digit) for digit in digits}
    
    @cache
    def count_valid_numbers(position, is_leading_zero, is_bounded):
        # Base case: reached the end of the number
        if position >= len(n_str):
            # Return 1 if we've placed at least one non-zero digit (valid number formed)
            # Return 0 if we only have leading zeros (no number formed)
            return 0 if is_leading_zero else 1
        
        # Determine the maximum digit we can place at this position
        max_digit = int(n_str[position]) if is_bounded else 9
        
        total_count = 0
        
        # Try each possible digit from 0 to max_digit
        for digit in range(max_digit + 1):
            if digit == 0 and is_leading_zero:
                # Skip this position (extend leading zeros)
                # Stay bounded if we were bounded and placed the max digit
                total_count += count_valid_numbers(
                    position + 1, 
                    True, 
                    is_bounded and (digit == max_digit)
                )
            elif digit in available_digits:
                # Place this digit (it's in our allowed set)
                # No longer have leading zeros after placing a non-zero digit
                # Stay bounded if we were bounded and placed the max digit
                total_count += count_valid_numbers(
                    position + 1, 
                    False, 
                    is_bounded and (digit == max_digit)
                )
        
        return total_count
    
    # Start from position 0, with leading zeros, and bounded by n
    return count_valid_numbers(0, True, True)
    # Time: O(log(n) * |digits|)
    # Space: O(log(n))


def main():
    result = at_most_n_given_digit_set(digits = ["1","3","5","7"], n = 100)
    print(result) # 20

    result = at_most_n_given_digit_set(digits = ["1","4","9"], n = 1000000000)
    print(result) # 29523

    result = at_most_n_given_digit_set(digits = ["7"], n = 8)
    print(result) # 1

if __name__ == "__main__":
    main()
