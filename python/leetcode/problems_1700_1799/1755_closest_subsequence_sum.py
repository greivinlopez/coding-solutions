# -----------------------------
# 1755. Closest Subsequence Sum
# -----------------------------

# Problem: https://leetcode.com/problems/closest-subsequence-sum
#
# You are given an integer array nums and an integer goal.
# 
# You want to choose a subsequence of nums such that the sum of its elements is
# the closest possible to goal. That is, if the sum of the subsequence's elements
# is sum, then you want to minimize the absolute difference abs(sum - goal).
# 
# Return the minimum possible value of abs(sum - goal).
# 
# Note that a subsequence of an array is an array formed by removing some elements
# (possibly all or none) of the original array.
# 
# Example 1:
# 
# Input: nums = [5,-7,3,5], goal = 6
# Output: 0
# 
# Explanation: Choose the whole array as a subsequence, with a sum of 6.
# This is equal to the goal, so the absolute difference is 0.
# 
# Example 2:
# 
# Input: nums = [7,-9,15,-2], goal = -5
# Output: 1
# 
# Explanation: Choose the subsequence [7,-9,-2], with a sum of -4.
# The absolute difference is abs(-4 - (-5)) = abs(1) = 1, which is the minimum.
# 
# Example 3:
# 
# Input: nums = [1,2,3], goal = -7
# Output: 7
# 
# 
# Constraints:
#         1 <= nums.length <= 40
#         -10⁷ <= nums[i] <= 10⁷
#         -10⁹ <= goal <= 10⁹


# Solution: https://algo.monster/liteproblems/1755
# Credit: AlgoMonster
def min_abs_difference(nums, goal):
    from bisect import bisect_left

    def get_subseq_sum(index, current_sum, array, result_set):
        # Base case: reached end of array
        if index == len(array):
            result_set.add(current_sum)
            return
        
        # Option 1: Exclude current element
        get_subseq_sum(index + 1, current_sum, array, result_set)
        
        # Option 2: Include current element
        get_subseq_sum(index + 1, current_sum + array[index], array, result_set)
    
    n = len(nums)
    
    # Split array into two halves for meet-in-the-middle approach
    left_sums = set()
    right_sums = set()
    
    # Generate all possible subsequence sums for each half
    get_subseq_sum(0, 0, nums[:n // 2], left_sums)
    get_subseq_sum(0, 0, nums[n // 2:], right_sums)
    
    # Sort right sums for binary search
    sorted_right_sums = sorted(right_sums)
    right_length = len(sorted_right_sums)
    
    min_difference = float('inf')
    
    # For each sum from left half, find the best matching sum from right half
    for left_sum in left_sums:
        # We need to find right_sum such that left_sum + right_sum is closest to goal
        target = goal - left_sum
        
        # Binary search for the closest value to target in sorted_right_sums
        insertion_point = bisect_left(sorted_right_sums, target)
        
        # Check the value at or after insertion point (ceiling value)
        if insertion_point < right_length:
            min_difference = min(min_difference, abs(target - sorted_right_sums[insertion_point]))
        
        # Check the value before insertion point (floor value)
        if insertion_point > 0:
            min_difference = min(min_difference, abs(target - sorted_right_sums[insertion_point - 1]))
    
    return min_difference
    # Time: O(2^(n/2) * n)
    # Space: O(2^(n/2))


def main():
    result = min_abs_difference(nums = [5,-7,3,5], goal = 6)
    print(result) # 0

    result = min_abs_difference(nums = [7,-9,15,-2], goal = -5)
    print(result) # 1

    result = min_abs_difference(nums = [1,2,3], goal = -7)
    print(result) # 7

if __name__ == "__main__":
    main()
