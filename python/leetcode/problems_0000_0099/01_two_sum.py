# ------------
# 1. Two Sum
# ------------

# Problem: https://leetcode.com/problems/two-sum
#
# Given an array of integers nums and an integer target, return indices of the two
# numbers such that they add up to target.
# 
# You may assume that each input would have exactly one solution, and you may not
# use the same element twice.
# 
# You can return the answer in any order.
# 
# Example 1:
# 
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# 
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# 
# Example 2:
# 
# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# 
# Example 3:
# 
# Input: nums = [3,3], target = 6
# Output: [0,1]
# 
# 
# Constraints:
#         2 <= nums.length <= 10⁴
#         -10⁹ <= nums[i] <= 10⁹
#         -10⁹ <= target <= 10⁹
#         Only one valid answer exists.
# 
# Follow-up: Can you come up with an algorithm that is less than O(n²) time
# complexity?

# Solution: https://youtu.be/KLlXCFG5TnA
# Credit: Navdeep Singh founder of NeetCode 
def two_sum(nums, target):
    prevMap = {}  # val -> index

    for i, n in enumerate(nums):
        diff = target - n
        if diff in prevMap:
            return [prevMap[diff], i]
        prevMap[n] = i
    # Time: O(n)
    # Space: O(n)

# Solution: https://youtu.be/aRE7Nxb3Qfs
# Credit: Greg Hogg

# Brute Force Solution
def two_sum_brute(nums, target):
    n = len(nums)
    for i in range(n):
        for j in range(n):
            if nums[i] + nums[j] == target and i != j:
                return (i, j)
    # Time: O(n²)
    # Space: O(1)

# Better Brute Force Solution
def two_sum_brute_2(nums, target):
    n = len(nums)
    for i in range(n):
        for j in range(i+1, n):
            if nums[i] + nums[j] == target:
                return (i, j)
    # Time: O(n²)
    # Space: O(1)

# 2-Pass Optimal Solution
def two_sum_optimal_two_pass(nums, target):
    h = {}
    for i in range(len(nums)):
        h[nums[i]] = i

    for i in range(len(nums)):
        y = target - nums[i]

        if y in h and h[y] != i:
            return [i, h[y]]
    # Time: O(n)
    # Space: O(n)

# One-Pass Optimal Solution (For Bootcamp)
def two_sum_optimal_one_pass(nums, target):
    h = {}
    n = len(nums)
    for i, x in enumerate(nums):
        y = target - x
        if y in h:
            return [i, h[y]]
        else:
            h[x] = i
    # Time: O(n)
    # Space: O(n)


def main():
    result = two_sum([2,7,11,15], 9) # [0, 1]
    print(result)
    result = two_sum([3,2,4], 6) # [1, 2]
    print(result)
    result = two_sum([3,3], 6) # [0, 1]
    print(result)

if __name__ == "__main__":
    main()