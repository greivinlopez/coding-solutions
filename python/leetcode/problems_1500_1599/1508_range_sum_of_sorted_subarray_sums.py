# ---------------------------------------
# 1508. Range Sum of Sorted Subarray Sums
# ---------------------------------------

# Problem: https://leetcode.com/problems/range-sum-of-sorted-subarray-sums
#
# You are given the array nums consisting of n positive integers. You computed the
# sum of all non-empty continuous subarrays from the array and then sorted them in
# non-decreasing order, creating a new array of n * (n + 1) / 2 numbers.
# 
# Return the sum of the numbers from index left to index right (indexed from 1),
# inclusive, in the new array. Since the answer can be a huge number return it
# modulo 109 + 7.
# 
# Example 1:
# 
# Input: nums = [1,2,3,4], n = 4, left = 1, right = 5
# Output: 13
# 
# Explanation: All subarray sums are 1, 3, 6, 10, 2, 5, 9, 3, 7, 4. After sorting
# them in non-decreasing order we have the new array [1, 2, 3, 3, 4, 5, 6, 7, 9,
# 10]. The sum of the numbers from index le = 1 to ri = 5 is 1 + 2 + 3 + 3 + 4 =
# 13.
# 
# Example 2:
# 
# Input: nums = [1,2,3,4], n = 4, left = 3, right = 4
# Output: 6
# 
# Explanation: The given array is the same as example 1. We have the new array [1,
# 2, 3, 3, 4, 5, 6, 7, 9, 10]. The sum of the numbers from index le = 3 to ri = 4
# is 3 + 3 = 6.
# 
# Example 3:
# 
# Input: nums = [1,2,3,4], n = 4, left = 1, right = 10
# Output: 50
# 
# 
# Constraints:
#         n == nums.length
#         1 <= nums.length <= 1000
#         1 <= nums[i] <= 100
#         1 <= left <= right <= n * (n + 1) / 2

import heapq

# Solution: https://youtu.be/7XTGlO6b16A
# Credit: Navdeep Singh founder of NeetCode
def range_sum(nums, n, left, right):
    MOD = 10**9 + 7
    minHeap = [(n, i) for i, n in enumerate(nums)]
    heapq.heapify(minHeap)

    res = 0
    for i in range(right):
        num, index = heapq.heappop(minHeap)
        if i >= left - 1:
            res = (res + num) % MOD
        if index + 1 < n:
            next_pair = (num + nums[index + 1], index + 1)
            heapq.heappush(minHeap, next_pair)

    return res
    # Time: O(n * log(n))
    # Space: O(n)


def main():
    result = range_sum(nums = [1,2,3,4], n = 4, left = 1, right = 5)
    print(result) # 13

    result = range_sum(nums = [1,2,3,4], n = 4, left = 3, right = 4)
    print(result) # 6

    result = range_sum(nums = [1,2,3,4], n = 4, left = 1, right = 10)
    print(result) # 50

if __name__ == "__main__":
    main()
