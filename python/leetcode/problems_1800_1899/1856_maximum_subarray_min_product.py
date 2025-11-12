# ----------------------------------
# 1856. Maximum Subarray Min-Product
# ----------------------------------

# Problem: https://leetcode.com/problems/maximum-subarray-min-product
#
# The min-product of an array is equal to the minimum value in the array
# multiplied by the array's sum.
#         
#   * For example, the array [3,2,5] (minimum value is 2) has a min-product of
#     2 * (3+2+5) = 2 * 10 = 20.
# 
# Given an array of integers nums, return the maximum min-product of any non-empty
# subarray of nums. Since the answer may be large, return it modulo 109 + 7.
# 
# Note that the min-product should be maximized before performing the modulo
# operation. Testcases are generated such that the maximum min-product without
# modulo will fit in a 64-bit signed integer.
# 
# A subarray is a contiguous part of an array.
# 
# Example 1:
# 
# Input: nums = [1,2,3,2]
# Output: 14
# 
# Explanation: The maximum min-product is achieved with the subarray [2,3,2]
# (minimum value is 2).
# 2 * (2+3+2) = 2 * 7 = 14.
# 
# Example 2:
# 
# Input: nums = [2,3,3,1,2]
# Output: 18
# 
# Explanation: The maximum min-product is achieved with the subarray [3,3]
# (minimum value is 3).
# 3 * (3+3) = 3 * 6 = 18.
# 
# Example 3:
# 
# Input: nums = [3,1,5,6,4,2]
# Output: 60
# 
# Explanation: The maximum min-product is achieved with the subarray [5,6,4]
# (minimum value is 4).
# 4 * (5+6+4) = 4 * 15 = 60.
# 
# 
# Constraints:
#         1 <= nums.length <= 10^5
#         1 <= nums[i] <= 10^7


# Solution: https://youtu.be/YLesLbNkyjA
# Credit: Navdeep Singh founder of NeetCode
def max_sum_min_product(nums):
    res = 0
    stack = []
    prefix = [0]
    for n in nums:
        prefix.append(prefix[-1] + n)

    for i, n in enumerate(nums):
        new_start = i
        while stack and stack[-1][1] > n:
            start, val = stack.pop()
            total = prefix[i] - prefix[start]
            res = max(res, val * total)
            new_start = start
        stack.append((new_start, n))

    for start, val in stack:
        total = prefix[len(nums)] - prefix[start]
        res = max(res, val * total)

    return res % (10**9 + 7)
    # Time: O(n)
    # Space: O(n)


def main():
    result = max_sum_min_product(nums = [1,2,3,2])
    print(result) # 14

    result = max_sum_min_product(nums = [2,3,3,1,2])
    print(result) # 18

    result = max_sum_min_product(nums = [3,1,5,6,4,2])
    print(result) # 60

if __name__ == "__main__":
    main()
