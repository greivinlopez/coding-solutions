# ----------------------------------------
# 693. Binary Number with Alternating Bits
# ----------------------------------------

# Problem: https://leetcode.com/problems/binary-number-with-alternating-bits
#
# Given a positive integer, check whether it has alternating bits: namely, if two
# adjacent bits will always have different values.
# 
# Example 1:
# 
# Input: n = 5
# Output: true
# 
# Explanation: The binary representation of 5 is: 101
# 
# Example 2:
# 
# Input: n = 7
# Output: false
# 
# Explanation: The binary representation of 7 is: 111.
# 
# Example 3:
# 
# Input: n = 11
# Output: false
# 
# Explanation: The binary representation of 11 is: 1011.
# 
# 
# Constraints:
#         1 <= n <= 2³¹ - 1

# Credit: Jaweria Batool -> https://github.com/Jaweria-B
def has_alternating_bits_alt(n):
    binary = bin(n)[2: ]
    
    firstEle = binary[0]
    
    for i in range(1, len(binary)):
        if binary[i] != firstEle:
            firstEle = binary[i]
        else:
            return False
    
    return True
    # Time: O(log(n))
    # Space: O(log(n))


# My Solution
def has_alternating_bits(n):
    prev_bit = n % 2
    n = n // 2

    # Loop as long as there are bits to check
    while n > 0:
        # Get the current last bit
        current_bit = n % 2
        
        # If the current bit is the same as the previous one, it's not alternating
        if current_bit == prev_bit:
            return False
        
        # Update prev_bit and prepare for the next iteration
        prev_bit = current_bit
        n = n // 2
        
    return True
    # Time: O(log(n))
    # Space: O(1)


def main():
    result = has_alternating_bits(5)
    print(result) # True

    result = has_alternating_bits(7)
    print(result) # False

    result = has_alternating_bits(11)
    print(result) # False

if __name__ == "__main__":
    main()
