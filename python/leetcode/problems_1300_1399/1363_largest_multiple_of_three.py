# -------------------------------
# 1363. Largest Multiple of Three
# -------------------------------

# Problem: https://leetcode.com/problems/largest-multiple-of-three
#
# Given an array of digits digits, return the largest multiple of three that can
# be formed by concatenating some of the given digits in any order. If there is no
# answer return an empty string.
# 
# Since the answer may not fit in an integer data type, return the answer as a
# string. Note that the returning answer must not contain unnecessary leading
# zeros.
# 
# Example 1:
# 
# Input: digits = [8,1,9]
# Output: "981"
# 
# Example 2:
# 
# Input: digits = [8,6,7,1,0]
# Output: "8760"
# 
# Example 3:
# 
# Input: digits = [1]
# Output: ""
# 
# 
# Constraints:
#         1 <= digits.length <= 10⁴
#         0 <= digits[i] <= 9


# Solution: https://algo.monster/liteproblems/1363
# Credit: AlgoMonster
def largest_multiple_of_three(digits):
    # Sort digits in ascending order for later reconstruction
    digits.sort()
    num_digits = len(digits)
    
    # Dynamic programming table
    # dp[i][j] represents the maximum number of digits we can use 
    # from the first i digits to form a number with remainder j when divided by 3
    dp = [[-float('inf')] * 3 for _ in range(num_digits + 1)]
    
    # Base case: using 0 digits gives remainder 0 with 0 digits used
    dp[0][0] = 0
    
    # Fill the DP table
    for i, digit in enumerate(digits, 1):
        for remainder in range(3):
            # Option 1: Don't include current digit
            dont_include = dp[i - 1][remainder]
            
            # Option 2: Include current digit
            # Calculate what remainder we need before adding this digit
            prev_remainder = (remainder - digit % 3 + 3) % 3
            include = dp[i - 1][prev_remainder] + 1
            
            # Take the maximum of both options
            dp[i][remainder] = max(dont_include, include)
    
    # If we can't form a number divisible by 3, return empty string
    if dp[num_digits][0] <= 0:
        return ""
    
    # Reconstruct the solution by backtracking through the DP table
    result_digits = []
    current_remainder = 0
    
    # Traverse from the last digit to the first
    for i in range(num_digits, 0, -1):
        current_digit = digits[i - 1]
        
        # Calculate what the remainder would have been before including this digit
        prev_remainder = (current_remainder - current_digit % 3 + 3) % 3
        
        # Check if this digit was included in the optimal solution
        if dp[i - 1][prev_remainder] + 1 == dp[i][current_remainder]:
            # This digit was included, add it to result
            result_digits.append(current_digit)
            current_remainder = prev_remainder
    
    # Remove leading zeros, keeping at least one digit
    leading_zero_index = 0
    while leading_zero_index < len(result_digits) - 1 and result_digits[leading_zero_index] == 0:
        leading_zero_index += 1
    
    # Convert digits to string and return
    return "".join(map(str, result_digits[leading_zero_index:]))
    # Time: O(n * log n)
    # Space: O(n)


def main():
    result = largest_multiple_of_three(digits = [8,1,9])
    print(result) # "981"

    result = largest_multiple_of_three(digits = [8,6,7,1,0])
    print(result) # "8760"

    result = largest_multiple_of_three(digits = [1])
    print(result) # ""

if __name__ == "__main__":
    main()
