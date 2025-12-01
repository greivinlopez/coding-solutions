# --------------------------------------------------
# 1703. Minimum Adjacent Swaps for K Consecutive Ones
# --------------------------------------------------

# Problem: https://leetcode.com/problems/minimum-adjacent-swaps-for-k-consecutive-ones
#
# You are given an integer array, nums, and an integer k. nums comprises of only
# 0's and 1's. In one move, you can choose two adjacent indices and swap their
# values.
# 
# Return the minimum number of moves required so that nums has k consecutive 1's.
# 
# Example 1:
# 
# Input: nums = [1,0,0,1,0,1], k = 2
# Output: 1
# 
# Explanation: In 1 move, nums could be [1,0,0,0,1,1] and have 2 consecutive 1's.
# 
# Example 2:
# 
# Input: nums = [1,0,0,0,0,0,1,1], k = 3
# Output: 5
# 
# Explanation: In 5 moves, the leftmost 1 can be shifted right until nums =
# [0,0,0,0,0,1,1,1].
# 
# Example 3:
# 
# Input: nums = [1,1,0,1], k = 2
# Output: 0
# 
# Explanation: nums already has 2 consecutive 1's.
# 
# 
# Constraints:
#         1 <= nums.length <= 10⁵
#         nums[i] is 0 or 1.
#         1 <= k <= sum(nums)


# Solution: https://algo.monster/liteproblems/1703
# Credit: AlgoMonster
def min_moves(nums, k):
    from itertools import accumulate

    # Extract indices where nums[i] == 1
    ones_indices = [i for i, value in enumerate(nums) if value == 1]
    
    # Create prefix sum array for quick range sum calculations
    # prefix_sums[i] contains sum of first i elements from ones_indices
    prefix_sums = list(accumulate(ones_indices, initial=0))
    
    min_moves = float('inf')
    
    # Split k into left and right parts around a center position
    # left_count: number of ones to collect on the left side (including center if k is odd)
    # right_count: number of ones to collect on the right side
    left_count = (k + 1) // 2
    right_count = k - left_count
    
    # Try each possible center position for collecting k ones
    for center_idx in range(left_count - 1, len(ones_indices) - right_count):
        # Get the actual position in nums array for the center
        center_pos = ones_indices[center_idx]
        
        # Calculate sum of positions for left group using prefix sums
        # Elements from index (center_idx - left_count + 1) to center_idx
        left_sum = prefix_sums[center_idx + 1] - prefix_sums[center_idx + 1 - left_count]
        
        # Calculate sum of positions for right group using prefix sums
        # Elements from index (center_idx + 1) to (center_idx + right_count)
        right_sum = prefix_sums[center_idx + 1 + right_count] - prefix_sums[center_idx + 1]
        
        # Calculate moves needed for left group
        # Target positions: center_pos - left_count + 1, ..., center_pos
        # Sum of target positions using arithmetic sequence formula
        left_target_sum = (center_pos + center_pos - left_count + 1) * left_count // 2
        left_moves = left_target_sum - left_sum
        
        # Calculate moves needed for right group
        # Target positions: center_pos + 1, ..., center_pos + right_count
        # Sum of target positions using arithmetic sequence formula
        right_target_sum = (center_pos + 1 + center_pos + right_count) * right_count // 2
        right_moves = right_sum - right_target_sum
        
        # Update minimum moves
        total_moves = left_moves + right_moves
        min_moves = min(min_moves, total_moves)
    
    return min_moves
    # Time: O(n + m)
    # Space: O(m)


def main():
    result = min_moves(nums = [1,0,0,1,0,1], k = 2)
    print(result) # 1

    result = min_moves(nums = [1,0,0,0,0,0,1,1], k = 3)
    print(result) # 5

    result = min_moves(nums = [1,1,0,1], k = 2)
    print(result) # 0

if __name__ == "__main__":
    main()
