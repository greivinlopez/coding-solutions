# ----------------------------
# 813. Largest Sum of Averages
# ----------------------------

# Problem: https://leetcode.com/problems/largest-sum-of-averages
#
# You are given an integer array nums and an integer k. You can partition the
# array into at most k non-empty adjacent subarrays. The score of a partition is
# the sum of the averages of each subarray.
# 
# Note that the partition must use every integer in nums, and that the score is
# not necessarily an integer.
# 
# Return the maximum score you can achieve of all the possible partitions. Answers
# within 10⁻⁶ of the actual answer will be accepted.
# 
# Example 1:
# 
# Input: nums = [9,1,2,3,9], k = 3
# Output: 20.00000
# 
# Explanation:
# The best choice is to partition nums into [9], [1, 2, 3], [9]. The answer is 9 +
# (1 + 2 + 3) / 3 + 9 = 20.
# We could have also partitioned nums into [9, 1], [2], [3, 9], for example.
# That partition would lead to a score of 5 + 2 + 6 = 13, which is worse.
# 
# Example 2:
# 
# Input: nums = [1,2,3,4,5,6,7], k = 4
# Output: 20.50000
# 
# 
# Constraints:
#         1 <= nums.length <= 100
#         1 <= nums[i] <= 10⁴
#         1 <= k <= nums.length


# Solution: https://algo.monster/liteproblems/813
# Credit: AlgoMonster
def largest_sum_of_averages(nums, k):
    from functools import cache
    from itertools import accumulate
    
    @cache
    def dp(start_idx, groups_left):
        # Base case: reached end of array
        if start_idx == array_length:
            return 0
        
        # Base case: only one group left, take average of remaining elements
        if groups_left == 1:
            remaining_sum = prefix_sum[array_length] - prefix_sum[start_idx]
            remaining_count = array_length - start_idx
            return remaining_sum / remaining_count
        
        max_sum = 0
        # Try all possible end positions for current group
        for end_idx in range(start_idx + 1, array_length):
            # Calculate average of current group [start_idx, end_idx)
            current_group_sum = prefix_sum[end_idx] - prefix_sum[start_idx]
            current_group_size = end_idx - start_idx
            current_average = current_group_sum / current_group_size
            
            # Recursively calculate maximum for remaining elements
            remaining_max = dp(end_idx, groups_left - 1)
            
            # Update maximum sum of averages
            max_sum = max(max_sum, current_average + remaining_max)
        
        return max_sum
    
    # Initialize variables
    array_length = len(nums)
    # Create prefix sum array for efficient range sum calculation
    prefix_sum = list(accumulate(nums, initial=0))
    
    # Start dynamic programming from index 0 with k groups
    return dp(0, k)
    # Time: O(n² * k)
    # Space: O(n * k)


def main():
    result = largest_sum_of_averages(nums = [9,1,2,3,9], k = 3)
    print(result) # 20.0

    result = largest_sum_of_averages(nums = [1,2,3,4,5,6,7], k = 4)
    print(result) # 20.5

if __name__ == "__main__":
    main()
