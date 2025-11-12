# -----------------------------------
# 1009. Complement of Base 10 Integer
# -----------------------------------

# Problem: https://leetcode.com/problems/complement-of-base-10-integer
#
# The complement of an integer is the integer you get when you flip all the 0's to
# 1's and all the 1's to 0's in its binary representation.
#         
#   * For example, The integer 5 is "101" in binary and its complement is
#     "010" which is the integer 2.
# 
# Given an integer n, return its complement.
# 
# Example 1:
# 
# Input: n = 5
# Output: 2
# 
# Explanation: 5 is "101" in binary, with complement "010" in binary, which is 2
# in base-10.
# 
# Example 2:
# 
# Input: n = 7
# Output: 0
# 
# Explanation: 7 is "111" in binary, with complement "000" in binary, which is 0
# in base-10.
# 
# Example 3:
# 
# Input: n = 10
# Output: 5
# 
# Explanation: 10 is "1010" in binary, with complement "0101" in binary, which is
# 5 in base-10.
# 
# 
# Constraints:
#         0 <= n < 10⁹
# 
# Note: This question is the same as 476: 
# https://leetcode.com/problems/number-complement/


# Solution: https://algo.monster/liteproblems/1009
# Credit: AlgoMonster
def bitwise_complement(n):
    # Special case: complement of 0 is 1
    if n == 0:
        return 1
    
    # Initialize result and bit position counter
    result = 0
    bit_position = 0
    
    # Process each bit of n from right to left
    while n > 0:
        # Get the rightmost bit, flip it (XOR with 1), 
        # shift it to the correct position, and add to result
        flipped_bit = (n & 1) ^ 1
        result |= flipped_bit << bit_position
        
        # Move to the next bit position
        bit_position += 1
        
        # Right shift n to process the next bit
        n >>= 1
    
    return result
    # Time: O(log(n))
    # Space: O(1)


def main():
    result = bitwise_complement(5)
    print(result) # 2

    result = bitwise_complement(7)
    print(result) # 0

    result = bitwise_complement(10)
    print(result) # 5

if __name__ == "__main__":
    main()
