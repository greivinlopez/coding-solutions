# --------------------------------------------------
# 1031. Maximum Sum of Two Non-Overlapping Subarrays
# --------------------------------------------------

# Problem: https://leetcode.com/problems/maximum-sum-of-two-non-overlapping-subarrays
#
# Given an integer array nums and two integers firstLen and secondLen, return the
# maximum sum of elements in two non-overlapping subarrays with lengths firstLen
# and secondLen.
# 
# The array with length firstLen could occur before or after the array with length
# secondLen, but they have to be non-overlapping.
# 
# A subarray is a contiguous part of an array.
# 
# Example 1:
# 
# Input: nums = [0,6,5,2,2,5,1,9,4], firstLen = 1, secondLen = 2
# Output: 20
# 
# Explanation: One choice of subarrays is [9] with length 1, and [6,5] with length
# 2.
# 
# Example 2:
# 
# Input: nums = [3,8,1,3,2,1,8,9,0], firstLen = 3, secondLen = 2
# Output: 29
# 
# Explanation: One choice of subarrays is [3,8,1] with length 3, and [8,9] with
# length 2.
# 
# Example 3:
# 
# Input: nums = [2,1,5,6,0,9,5,0,3,8], firstLen = 4, secondLen = 3
# Output: 31
# 
# Explanation: One choice of subarrays is [5,6,0,9] with length 4, and [0,3,8]
# with length 3.
# 
# 
# Constraints:
#         1 <= firstLen, secondLen <= 1000
#         2 <= firstLen + secondLen <= 1000
#         firstLen + secondLen <= nums.length <= 1000
#         0 <= nums[i] <= 1000

from itertools import accumulate

# Solution: https://algo.monster/liteproblems/1031
# Credit: AlgoMonster
def max_sum_two_no_overlap(nums, firstLen, secondLen):
    n = len(nums)
    # Build prefix sum array for O(1) range sum queries
    # prefix_sum[i] = sum of nums[0:i]
    prefix_sum = list(accumulate(nums, initial=0))
    
    max_total_sum = 0
    
    # Case 1: First array comes before second array
    max_first_sum = 0
    # Iterate through possible ending positions for the second array
    for end_of_second in range(firstLen + secondLen, n + 1):
        # Update max sum of first array that can fit before current position
        start_of_second = end_of_second - secondLen
        end_of_first = start_of_second
        start_of_first = end_of_first - firstLen
        current_first_sum = prefix_sum[end_of_first] - prefix_sum[start_of_first]
        max_first_sum = max(max_first_sum, current_first_sum)
        
        # Calculate sum of second array at current position
        current_second_sum = prefix_sum[end_of_second] - prefix_sum[start_of_second]
        
        # Update maximum total sum
        max_total_sum = max(max_total_sum, max_first_sum + current_second_sum)
    
    # Case 2: Second array comes before first array
    max_second_sum = 0
    # Iterate through possible ending positions for the first array
    for end_of_first in range(secondLen + firstLen, n + 1):
        # Update max sum of second array that can fit before current position
        start_of_first = end_of_first - firstLen
        end_of_second = start_of_first
        start_of_second = end_of_second - secondLen
        current_second_sum = prefix_sum[end_of_second] - prefix_sum[start_of_second]
        max_second_sum = max(max_second_sum, current_second_sum)
        
        # Calculate sum of first array at current position
        current_first_sum = prefix_sum[end_of_first] - prefix_sum[start_of_first]
        
        # Update maximum total sum
        max_total_sum = max(max_total_sum, max_second_sum + current_first_sum)
    
    return max_total_sum
    # Time: O(n) 
    # Space: O(n)


def main():
    result = max_sum_two_no_overlap(nums = [0,6,5,2,2,5,1,9,4], firstLen = 1, secondLen = 2)
    print(result) # 20

    result = max_sum_two_no_overlap(nums = [3,8,1,3,2,1,8,9,0], firstLen = 3, secondLen = 2)
    print(result) # 29

    result = max_sum_two_no_overlap(nums = [2,1,5,6,0,9,5,0,3,8], firstLen = 4, secondLen = 3)
    print(result) # 31

if __name__ == "__main__":
    main()
