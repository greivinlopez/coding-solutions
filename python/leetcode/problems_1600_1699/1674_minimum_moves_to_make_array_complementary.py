# -----------------------------------------------
# 1674. Minimum Moves to Make Array Complementary
# -----------------------------------------------

# Problem: https://leetcode.com/problems/minimum-moves-to-make-array-complementary
#
# You are given an integer array nums of even length n and an integer limit. In
# one move, you can replace any integer from nums with another integer between 1
# and limit, inclusive.
# 
# The array nums is complementary if for all indices i (0-indexed), nums[i] +
# nums[n - 1 - i] equals the same number. For example, the array [1,2,3,4] is
# complementary because for all indices i, nums[i] + nums[n - 1 - i] = 5.
# 
# Return the minimum number of moves required to make nums complementary.
# 
# Example 1:
# 
# Input: nums = [1,2,4,3], limit = 4
# Output: 1
# 
# Explanation: In 1 move, you can change nums to [1,2,2,3] (underlined elements
# are changed).
# nums[0] + nums[3] = 1 + 3 = 4.
# nums[1] + nums[2] = 2 + 2 = 4.
# nums[2] + nums[1] = 2 + 2 = 4.
# nums[3] + nums[0] = 3 + 1 = 4.
# Therefore, nums[i] + nums[n-1-i] = 4 for every i, so nums is complementary.
# 
# Example 2:
# 
# Input: nums = [1,2,2,1], limit = 2
# Output: 2
# 
# Explanation: In 2 moves, you can change nums to [2,2,2,2]. You cannot change any
# number to 3 since 3 > limit.
# 
# Example 3:
# 
# Input: nums = [1,2,1,2], limit = 2
# Output: 0
# 
# Explanation: nums is already complementary.
# 
# 
# Constraints:
#         n == nums.length
#         2 <= n <= 10⁵
#         1 <= nums[i] <= limit <= 10⁵
#         n is even.


# Solution: https://algo.monster/liteproblems/1674
# Credit: AlgoMonster
def min_moves(nums, limit):
    from itertools import accumulate

    # Initialize difference array for tracking move costs
    # Size is 2*limit+2 to handle all possible sums from 2 to 2*limit
    diff_array = [0] * (2 * limit + 2)
    n = len(nums)
    
    # Process each pair (nums[i], nums[n-1-i])
    for i in range(n // 2):
        left_val = nums[i]
        right_val = nums[n - 1 - i]
        
        # Ensure left_val <= right_val for consistent processing
        if left_val > right_val:
            left_val, right_val = right_val, left_val
        
        # Build difference array using range update technique:
        # - Start with 2 moves needed for all sums (worst case)
        diff_array[2] += 2
        
        # - From sum (left_val + 1) onwards, only 1 move needed
        diff_array[left_val + 1] -= 2
        diff_array[left_val + 1] += 1
        
        # - At exact sum (left_val + right_val), 0 moves needed
        diff_array[left_val + right_val] -= 1
        
        # - After exact sum, back to 1 move needed
        diff_array[left_val + right_val + 1] += 1
        
        # - Beyond (right_val + limit), back to 2 moves needed
        diff_array[right_val + limit + 1] -= 1
        diff_array[right_val + limit + 1] += 2
    
    # Apply prefix sum to get actual move counts for each target sum
    # Return minimum moves needed (skip indices 0 and 1 as sums start from 2)
    return min(accumulate(diff_array[2:]))
    # Time: O(n + limit)
    # Space: O(limit)


def main():
    result = min_moves(nums = [1,2,4,3], limit = 4)
    print(result) # 1

    result = min_moves(nums = [1,2,2,1], limit = 2)
    print(result) # 2

    result = min_moves(nums = [1,2,1,2], limit = 2)
    print(result) # 0

if __name__ == "__main__":
    main()
