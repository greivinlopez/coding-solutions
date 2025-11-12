# ----------------------------------------
# 992. Subarrays with K Different Integers
# ----------------------------------------

# Problem: https://leetcode.com/problems/subarrays-with-k-different-integers
#
# Given an integer array nums and an integer k, return the number of good
# subarrays of nums.
# 
# A good array is an array where the number of different integers in that array is
# exactly k.
#         
#   * For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.
# 
# A subarray is a contiguous part of an array.
# 
# Example 1:
# 
# Input: nums = [1,2,1,2,3], k = 2
# Output: 7
# 
# Explanation: Subarrays formed with exactly 2 different integers: [1,2], [2,1],
# [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2]
# 
# Example 2:
# 
# Input: nums = [1,2,1,3,4], k = 3
# Output: 3
# 
# Explanation: Subarrays formed with exactly 3 different integers: [1,2,1,3],
# [2,1,3], [1,3,4].
# 
# 
# Constraints:
#         1 <= nums.length <= 2 * 10^4
#         1 <= nums[i], k <= nums.length

from collections import defaultdict

# Solution: https://youtu.be/etI6HqWVa8U
# Credit: Navdeep Singh founder of NeetCode
def subarrays_with_k_distinct(nums, k):
    count = defaultdict(int)
    res = 0
    l_far = 0
    l_near = 0
    for r in range(len(nums)):
        count[nums[r]] += 1

        while len(count) > k:
            count[nums[l_near]] -= 1
            if count[nums[l_near]] == 0:
                count.pop(nums[l_near])
            l_near += 1
            l_far = l_near

        while count[nums[l_near]] > 1:
            count[nums[l_near]] -= 1
            l_near += 1
        
        if len(count) == k:
            res += l_near - l_far + 1
            
    return res
    # Time: O(n) 
    # Space: O(k) where k is the given integer


def main():
    result = subarrays_with_k_distinct(nums = [1,2,1,2,3], k = 2)
    print(result) # 7

    result = subarrays_with_k_distinct(nums = [1,2,1,3,4], k = 3)
    print(result) # 3

if __name__ == "__main__":
    main()
