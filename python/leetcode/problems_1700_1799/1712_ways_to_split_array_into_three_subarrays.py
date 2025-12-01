# ----------------------------------------------
# 1712. Ways to Split Array Into Three Subarrays
# ----------------------------------------------

# Problem: https://leetcode.com/problems/ways-to-split-array-into-three-subarrays
#
# A split of an integer array is good if:
#         
#   * The array is split into three non-empty contiguous subarrays - named
#     left, mid, right respectively from left to right.
#   * The sum of the elements in left is less than or equal to the sum of the
#     elements in mid, and the sum of the elements in mid is less than or equal to the
#     sum of the elements in right.
# 
# Given nums, an array of non-negative integers, return the number of good ways to
# split nums. As the number may be too large, return it modulo 10⁹ + 7.
# 
# Example 1:
# 
# Input: nums = [1,1,1]
# Output: 1
# 
# Explanation: The only good way to split nums is [1] [1] [1].
# 
# Example 2:
# 
# Input: nums = [1,2,2,2,5,0]
# Output: 3
# 
# Explanation: There are three good ways of splitting nums:
# [1] [2] [2,2,5,0]
# [1] [2,2] [2,5,0]
# [1,2] [2,2] [5,0]
# 
# Example 3:
# 
# Input: nums = [3,2,1]
# Output: 0
# 
# Explanation: There is no good way to split nums.
# 
# 
# Constraints:
#         3 <= nums.length <= 10⁵
#         0 <= nums[i] <= 10⁴


# Solution: https://algo.monster/liteproblems/1712
# Credit: AlgoMonster
def ways_to_split(nums):
    from bisect import bisect_left, bisect_right
    from itertools import accumulate

    MOD = 10**9 + 7

    # Calculate prefix sums for efficient range sum queries
    prefix_sums = list(accumulate(nums))
    total_sum = prefix_sums[-1]
    n = len(nums)
    result = 0

    # Iterate through possible positions for the first split (end of left part)
    # i is the last index of the left part
    for i in range(n - 2):  # Need at least 1 element for middle and 1 for right
        left_sum = prefix_sums[i]

        # Find the minimum valid position for the second split
        # Middle sum >= left sum means: prefix_sums[j] - left_sum >= left_sum
        # Which simplifies to: prefix_sums[j] >= 2 * left_sum
        min_j = bisect_left(prefix_sums, left_sum * 2, i + 1, n - 1)

        # Find the maximum valid position for the second split
        # Right sum >= middle sum means: total_sum - prefix_sums[j] >= prefix_sums[j] - left_sum
        # Which simplifies to: prefix_sums[j] <= (total_sum + left_sum) / 2
        max_j = bisect_right(prefix_sums, (total_sum + left_sum) // 2, min_j, n - 1)

        # Add the number of valid positions for the second split
        result += max_j - min_j

    return result % MOD
    # Time: O(n * log n)
    # Space: O(n)


def main():
    result = ways_to_split(nums = [1,1,1])
    print(result) # 1

    result = ways_to_split(nums = [1,2,2,2,5,0])
    print(result) # 3

    result = ways_to_split(nums = [3,2,1])
    print(result) # 0

if __name__ == "__main__":
    main()
