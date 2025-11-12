# -------------
# 89. Gray Code
# -------------

# Problem: https://leetcode.com/problems/gray-code
#
# An n-bit gray code sequence is a sequence of 2n integers where:
# 
#   * Every integer is in the inclusive range [0, 2n - 1],
#   * The first integer is 0,
#   * An integer appears no more than once in the sequence,
#   * The binary representation of every pair of adjacent integers differs by
#     exactly one bit, and
#   * The binary representation of the first and last integers differs by
#     exactly one bit.
# 
# Given an integer n, return any valid n-bit gray code sequence.
# 
# Example 1:
# 
# Input: n = 2
# Output: [0,1,3,2]
# 
# Explanation:
# The binary representation of [0,1,3,2] is [00,01,11,10].
# - 00 and 01 differ by one bit
# - 01 and 11 differ by one bit
# - 11 and 10 differ by one bit
# - 10 and 00 differ by one bit
# [0,2,3,1] is also a valid gray code sequence, whose binary representation is
# [00,10,11,01].
# - 00 and 10 differ by one bit
# - 10 and 11 differ by one bit
# - 11 and 01 differ by one bit
# - 01 and 00 differ by one bit
# 
# Example 2:
# 
# Input: n = 1
# Output: [0,1]
# 
# 
# onstraints:
#         1 <= n <= 16


# Credit: Jeel Gajera -> https://github.com/JeelGajera
def gray_code(n):
    if n == 0:
        return [0]

    g_code = [0, 1]

    for i in range(1, n):
        size = len(g_code)
        
        for j in range(size - 1, -1, -1):
            g_code.append((1 << i) | g_code[j])

    return g_code
    # Time: O(2ⁿ)
    # Space: O(2ⁿ)

# Credit: Jaweria Batool -> https://github.com/Jaweria-B
def gray_code_alt(n):
    codes = [0]
    offset = 1
    for i in range(n):
        for j in range(len(codes)-1, -1, -1):
            codes.append(codes[j]+offset)
        offset = offset << 1
    return codes
    # Time: O(2ⁿ)
    # Space: O(2ⁿ)


def main():
    result = gray_code(2)
    print(result) # [0,1,3,2]

    result = gray_code(1)
    print(result) # [0,1]

if __name__ == "__main__":
    main()
