# ---------------------------
# 1695. Maximum Erasure Value
# ---------------------------

# Problem: https://leetcode.com/problems/maximum-erasure-value
#
# You are given an array of positive integers nums and want to erase a subarray
# containing unique elements. The score you get by erasing the subarray is equal
# to the sum of its elements.
# 
# Return the maximum score you can get by erasing exactly one subarray.
# 
# An array b is called to be a subarray of a if it forms a contiguous subsequence
# of a, that is, if it is equal to a[l],a[l+1],...,a[r] for some (l,r).
# 
# Example 1:
# 
# Input: nums = [4,2,4,5,6]
# Output: 17
# 
# Explanation: The optimal subarray here is [2,4,5,6].
# 
# Example 2:
# 
# Input: nums = [5,2,1,2,5,2,1,2,5]
# Output: 8
# 
# Explanation: The optimal subarray here is [5,2,1] or [1,2,5].
# 
# 
# Constraints:
#         1 <= nums.length <= 10⁵
#         1 <= nums[i] <= 10⁴


# Solution: https://algo.monster/liteproblems/1695
# Credit: AlgoMonster
def maximum_unique_subarray(nums):
    from itertools import accumulate

    # Create a dictionary to store the last seen index of each number
    # Using array instead of dict for O(1) access (assuming nums contains non-negative integers)
    last_seen_index = [0] * (max(nums) + 1)
    
    # Create prefix sum array for O(1) range sum calculation
    # prefix_sums[i] = sum of nums[0:i], so prefix_sums[0] = 0
    prefix_sums = list(accumulate(nums, initial=0))
    
    # Initialize result and left boundary of current valid window
    max_sum = 0
    left_boundary = 0
    
    # Iterate through the array with 1-indexed position
    for current_pos, current_value in enumerate(nums, 1):
        # Update left boundary to skip past the previous occurrence of current_value
        # This ensures all elements in window [left_boundary, current_pos) are unique
        left_boundary = max(left_boundary, last_seen_index[current_value])
        
        # Calculate sum of current window and update maximum
        # Window sum = prefix_sums[current_pos] - prefix_sums[left_boundary]
        current_window_sum = prefix_sums[current_pos] - prefix_sums[left_boundary]
        max_sum = max(max_sum, current_window_sum)
        
        # Update the last seen position of current value
        last_seen_index[current_value] = current_pos
    
    return max_sum
    # Time: O(n + m)
    # Space: O(n + m)


def main():
    result = maximum_unique_subarray(nums = [4,2,4,5,6])
    print(result) # 17

    result = maximum_unique_subarray(nums = [5,2,1,2,5,2,1,2,5])
    print(result) # 8

if __name__ == "__main__":
    main()
