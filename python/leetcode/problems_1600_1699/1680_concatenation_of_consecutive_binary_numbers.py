# -------------------------------------------------
# 1680. Concatenation of Consecutive Binary Numbers
# -------------------------------------------------

# Problem: https://leetcode.com/problems/concatenation-of-consecutive-binary-numbers
#
# Given an integer n, return the decimal value of the binary string formed by
# concatenating the binary representations of 1 to n in order, modulo 10⁹ + 7.
# 
# Example 1:
# 
# Input: n = 1
# Output: 1
# 
# Explanation: "1" in binary corresponds to the decimal value 1.
# 
# Example 2:
# 
# Input: n = 3
# Output: 27
# 
# Explanation: In binary, 1, 2, and 3 corresponds to "1", "10", and "11".
# After concatenating them, we have "11011", which corresponds to the decimal
# value 27.
# 
# Example 3:
# 
# Input: n = 12
# Output: 505379714
# 
# Explanation: The concatenation results in
# "1101110010111011110001001101010111100".
# The decimal value of that is 118505380540.
# After modulo 109 + 7, the result is 505379714.
# 
# 
# Constraints:
#         1 <= n <= 10⁵


# Solution: https://algo.monster/liteproblems/1680
# Credit: AlgoMonster
def concatenated_binary(n):
    # Define modulo constant to prevent integer overflow
    MOD = 10**9 + 7
    
    # Initialize result accumulator
    result = 0
    
    # Iterate through each number from 1 to n
    for current_num in range(1, n + 1):
        # Get the number of bits required to represent current_num
        num_bits = current_num.bit_length()
        
        # Left shift result by num_bits positions to make room for current_num
        # Then use bitwise OR to append current_num's binary representation
        # Apply modulo to keep the number within bounds
        result = ((result << num_bits) | current_num) % MOD
        
    return result
    # Time: O(n)
    # Space: O(1)


def main():
    result = concatenated_binary(n = 1)
    print(result) # 1

    result = concatenated_binary(n = 3)
    print(result) # 27

    result = concatenated_binary(n = 12)
    print(result) # 505379714

if __name__ == "__main__":
    main()
