# ----------------------------
# 829. Consecutive Numbers Sum
# ----------------------------

# Problem: https://leetcode.com/problems/consecutive-numbers-sum
#
# Given an integer n, return the number of ways you can write n as the sum of
# consecutive positive integers.
# 
# Example 1:
# 
# Input: n = 5
# Output: 2
# 
# Explanation: 5 = 2 + 3
# 
# Example 2:
# 
# Input: n = 9
# Output: 3
# 
# Explanation: 9 = 4 + 5 = 2 + 3 + 4
# 
# Example 3:
# 
# Input: n = 15
# Output: 4
# 
# Explanation: 15 = 8 + 7 = 4 + 5 + 6 = 1 + 2 + 3 + 4 + 5
# 
# 
# Constraints:
#         1 <= n <= 10⁹


# Solution: https://algo.monster/liteproblems/829
# Credit: AlgoMonster
def consecutive_numbers_sum(n):
    # Double n to avoid floating point arithmetic
    # This allows us to work with 2n = k * (2x + k - 1)
    doubled_n = n << 1
    
    # Initialize counter for valid ways and starting sequence length
    count = 0
    sequence_length = 1
    
    # Iterate through possible sequence lengths
    # k * (k + 1) represents the minimum sum for k consecutive numbers starting from 1
    # If k * (k + 1) > 2n, then we can't form a valid sequence
    while sequence_length * (sequence_length + 1) <= doubled_n:
        # Check two conditions:
        # 1. doubled_n is divisible by sequence_length
        # 2. The starting number would be a positive integer
        #    (doubled_n // sequence_length - sequence_length + 1) must be even
        #    to ensure the starting number is an integer
        if (doubled_n % sequence_length == 0 and 
            (doubled_n // sequence_length - sequence_length + 1) % 2 == 0):
            count += 1
        
        sequence_length += 1
    
    return count
    # Time: O(√n)
    # Space: O(1)


def main():
    result = consecutive_numbers_sum(5)
    print(result) # 2

    result = consecutive_numbers_sum(9)
    print(result) # 3

    result = consecutive_numbers_sum(15)
    print(result) # 4

if __name__ == "__main__":
    main()
