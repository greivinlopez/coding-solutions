# ---------------------
# 461. Hamming Distance
# ---------------------

# Problem: https://leetcode.com/problems/hamming-distance
#
# The Hamming distance between two integers is the number of positions at which
# the corresponding bits are different.
# 
# Given two integers x and y, return the Hamming distance between them.
# 
# Example 1:
# 
# Input: x = 1, y = 4
# Output: 2
# 
# Explanation:
# 1   (0 0 0 1)
# 4   (0 1 0 0)
#        ↑   ↑
# The above arrows point to positions where the corresponding bits are different.
# 
# Example 2:
# 
# Input: x = 3, y = 1
# Output: 1
# 
# Constraints:
#         0 <= x, y <= 2³¹ - 1
# 
# Note: This question is the same as  2220: Minimum Bit Flips to Convert Number.


# Solution: https://algo.monster/liteproblems/461
# Credit: AlgoMonster
def hamming_distance(x, y):
    return bin(x ^ y).count('1')

# Version for Python 3.10+
def hamming_distance_alt(x, y):
    xor_result = x ^ y
    return xor_result.bit_count()


def main():
    result = hamming_distance(x = 1, y = 4)
    print(result) # 2

    result = hamming_distance(x = 3, y = 1)
    print(result) # 1

if __name__ == "__main__":
    main()
