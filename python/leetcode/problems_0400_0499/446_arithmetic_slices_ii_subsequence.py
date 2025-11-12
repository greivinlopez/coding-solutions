# ---------------------------------------
# 446. Arithmetic Slices II - Subsequence
# ---------------------------------------

# Problem: https://leetcode.com/problems/arithmetic-slices-ii-subsequence
#
# Given an integer array nums, return the number of all the arithmetic
# subsequences of nums.
# 
# A sequence of numbers is called arithmetic if it consists of at least three
# elements and if the difference between any two consecutive elements is the same.
#         
#   * For example, [1, 3, 5, 7, 9], [7, 7, 7, 7], and [3, -1, -5, -9] are
#     arithmetic sequences.
#   * For example, [1, 1, 2, 5, 7] is not an arithmetic sequence.
# 
# A subsequence of an array is a sequence that can be formed by removing some
# elements (possibly none) of the array.
#         
#   * For example, [2,5,10] is a subsequence of [1,2,1,2,4,1,5,10].
# 
# The test cases are generated so that the answer fits in 32-bit integer.
# 
# Example 1:
# 
# Input: nums = [2,4,6,8,10]
# Output: 7
# 
# Explanation: All arithmetic subsequence slices are:
# [2,4,6]
# [4,6,8]
# [6,8,10]
# [2,4,6,8]
# [4,6,8,10]
# [2,4,6,8,10]
# [2,6,10]
# 
# Example 2:
# 
# Input: nums = [7,7,7,7,7]
# Output: 16
# 
# Explanation: Any subsequence of this array is arithmetic.
# 
# 
# Constraints:
#         1  <= nums.length <= 1000
#         -2^31 <= nums[i] <= 2^31 - 1

from collections import defaultdict

# Solution: https://youtu.be/YIMwwT9JdIE
# Credit: Navdeep Singh founder of NeetCode
def number_of_arithmetic_slices(nums):
    n = len(nums)
    res = 0
    dp = [defaultdict(int) for _ in range(n)]

    for i in range(n):
        for j in range(i):
            diff = nums[i] - nums[j]
            dp[i][diff] += 1 + dp[j][diff]
            res += dp[j][diff]

    return res
    # Time: O(n²)
    # Space: O(n²)


def main():
    result = number_of_arithmetic_slices([2,4,6,8,10])
    print(result) # 7

    result = number_of_arithmetic_slices([7,7,7,7,7])
    print(result) # 16

if __name__ == "__main__":
    main()
