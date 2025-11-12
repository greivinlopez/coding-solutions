# ----------------------------------------------------------
# 1671. Minimum Number of Removals to Make Mountain Array ⛰️
# ----------------------------------------------------------

# Problem: https://leetcode.com/problems/minimum-number-of-removals-to-make-mountain-array
#
# You may recall that an array arr is a mountain array if and only if:
# 
#   * arr.length >= 3
#   * There exists some index i (0-indexed) with 0 < i < arr.length - 1 such that:
#                 arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
#                 arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
# 
# Given an integer array nums​​​, return the minimum number of elements to remove
# to make nums​​​ a mountain array.
# 
# Example 1:
# 
# Input: nums = [1,3,1]
# Output: 0
# 
# Explanation: The array itself is a mountain array so we do not need to remove
# any elements.
# 
# Example 2:
# 
# Input: nums = [2,1,1,5,6,2,3,1]
# Output: 3
# 
# Explanation: One solution is to remove the elements at indices 0, 1, and 5,
# making the array nums = [1,5,6,3,1].
# 
# 
# Constraints:
#         3 <= nums.length <= 1000
#         1 <= nums[i] <= 10^9
#         It is guaranteed that you can make a mountain array out of nums.


# Solution: https://youtu.be/Ys-q9qPpleY
# Credit: Navdeep Singh founder of NeetCode
def minimum_mountain_removals(nums):
    n = len(nums)
    lis = [1] * n
    for i in range(n):
        for j in range(i):
            if nums[j] < nums[i]:
                lis[i] = max(lis[i], 1 + lis[j])

    lds = [1] * n
    for i in reversed(range(n)):
        for j in range(i + 1, n):
            if nums[j] < nums[i]:
                lds[i] = max(lds[i], 1 + lds[j])

    res = n
    for i in range(1, n - 1):
        if lis[i] > 1 and lds[i] > 1:
            res = min(res, n - lis[i] - lds[i] + 1)
    
    return res
    # Time: O(n) 
    # Space: O(n)


def main():
    result = minimum_mountain_removals([1,3,1])
    print(result) # 0

    result = minimum_mountain_removals([2,1,1,5,6,2,3,1])
    print(result) # 3

if __name__ == "__main__":
    main()
