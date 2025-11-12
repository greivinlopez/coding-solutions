# -------------------------------
# 1486. XOR Operation in an Array
# -------------------------------

# Problem: https://leetcode.com/problems/xor-operation-in-an-array
#
# You are given an integer n and an integer start.
# 
# Define an array nums where nums[i] = start + 2 * i (0-indexed) and n ==
# nums.length.
# 
# Return the bitwise XOR of all elements of nums.
# 
# Example 1:
# 
# Input: n = 5, start = 0
# Output: 8
# 
# Explanation: Array nums is equal to [0, 2, 4, 6, 8] where (0 ^ 2 ^ 4 ^ 6 ^ 8) = 8.
# Where "^" corresponds to bitwise XOR operator.
# 
# Example 2:
# 
# Input: n = 4, start = 3
# Output: 8
# 
# Explanation: Array nums is equal to [3, 5, 7, 9] where (3 ^ 5 ^ 7 ^ 9) = 8.
# 
# 
# Constraints:
#         1 <= n <= 1000
#         0 <= start <= 1000
#         n == nums.length

from functools import reduce
from operator import xor

# Solution: https://algo.monster/liteproblems/1486
# Credit: AlgoMonster
def xor_operation(n, start):
    # Generate array elements using the formula: start + 2 * i
    # where i ranges from 0 to n-1
    # Then apply XOR operation across all elements using reduce
    return reduce(xor, (start + 2 * i for i in range(n)))
    # Time: O(n)
    # Space: O(1)


def main():
    result = xor_operation(n = 5, start = 0)
    print(result) # 8

    result = xor_operation(n = 4, start = 3)
    print(result) # 8

if __name__ == "__main__":
    main()
