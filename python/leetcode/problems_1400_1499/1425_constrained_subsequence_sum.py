# ---------------------------------
# 1425. Constrained Subsequence Sum
# ---------------------------------

# Problem: https://leetcode.com/problems/constrained-subsequence-sum
#
# Given an integer array nums and an integer k, return the maximum sum of a non-
# empty subsequence of that array such that for every two consecutive integers in
# the subsequence, nums[i] and nums[j], where i < j, the condition j - i <= k is
# satisfied.
# 
# A subsequence of an array is obtained by deleting some number of elements (can
# be zero) from the array, leaving the remaining elements in their original order.
# 
# Example 1:
# 
# Input: nums = [10,2,-10,5,20], k = 2
# Output: 37
#
# Explanation: The subsequence is [10, 2, 5, 20].
# 
# Example 2:
# 
# Input: nums = [-1,-2,-3], k = 1
# Output: -1
# 
# Explanation: The subsequence must be non-empty, so we choose the largest number.
# 
# Example 3:
# 
# Input: nums = [10,-2,-10,-5,20], k = 2
# Output: 23
# 
# Explanation: The subsequence is [10, -2, -5, 20].
# 
# 
# Constraints:
#         1 <= k <= nums.length <= 10^5
#         -10^4 <= nums[i] <= 10^4

import heapq

# Solution: https://youtu.be/-IYZv-nOSys
# Credit: Navdeep Singh founder of NeetCode
def constrained_subset_sum(nums, k):
    res = nums[0]
    max_heap = [(-nums[0], 0)]  # max_sum, index

    for i in range(1, len(nums)):
        while i - max_heap[0][1] > k:
            heapq.heappop(max_heap)
        
        cur_max = max(nums[i], nums[i] - max_heap[0][0])
        res = max(res, cur_max)
        heapq.heappush(max_heap, (-cur_max, i))
    
    return res
    # Time: O(n * log(k))
    # Space: O(k) 

def main():
    result = constrained_subset_sum(nums = [10,2,-10,5,20], k = 2)
    print(result) # 37

    result = constrained_subset_sum(nums = [-1,-2,-3], k = 1)
    print(result) # -1

    result = constrained_subset_sum(nums = [10,-2,-10,-5,20], k = 2)
    print(result) # 23

if __name__ == "__main__":
    main()
