# ----------------------
# 910. Smallest Range II
# ----------------------

# Problem: https://leetcode.com/problems/smallest-range-ii
#
# You are given an integer array nums and an integer k.
# 
# For each index i where 0 <= i < nums.length, change nums[i] to be either nums[i]
# + k or nums[i] - k.
# 
# The score of nums is the difference between the maximum and minimum elements in
# nums.
# 
# Return the minimum score of nums after changing the values at each index.
# 
# Example 1:
# 
# Input: nums = [1], k = 0
# Output: 0
# 
# Explanation: The score is max(nums) - min(nums) = 1 - 1 = 0.
# 
# Example 2:
# 
# Input: nums = [0,10], k = 2
# Output: 6
# 
# Explanation: Change nums to be [2, 8]. The score is max(nums) - min(nums) = 8 -
# 2 = 6.
# 
# Example 3:
# 
# Input: nums = [1,3,6], k = 3
# Output: 3
# 
# Explanation: Change nums to be [4, 6, 3]. The score is max(nums) - min(nums) = 6
# - 3 = 3.
# 
# 
# Constraints:
#         1 <= nums.length <= 10⁴
#         0 <= nums[i] <= 10⁴
#         0 <= k <= 10⁴


# Solution: https://algo.monster/liteproblems/910
# Credit: AlgoMonster
def smallest_range_ii(nums, k):
    # Sort the array to analyze potential split points
    nums.sort()
    
    # Initial answer: range when all elements move in same direction
    # (either all +k or all -k gives the same range)
    min_range = nums[-1] - nums[0]
    
    # Try each possible split point
    # Elements before index i get +k, elements from index i get -k
    for i in range(1, len(nums)):
        # After the split:
        # - Elements [0, i-1] are increased by k
        # - Elements [i, n-1] are decreased by k
        
        # The new minimum is either:
        # - The smallest element increased by k (nums[0] + k)
        # - The element at split point decreased by k (nums[i] - k)
        new_min = min(nums[0] + k, nums[i] - k)
        
        # The new maximum is either:
        # - The element just before split increased by k (nums[i - 1] + k)
        # - The largest element decreased by k (nums[-1] - k)
        new_max = max(nums[i - 1] + k, nums[-1] - k)
        
        # Update the minimum range if this split gives a better result
        min_range = min(min_range, new_max - new_min)
    
    return min_range
    # Time: O(n * log(n))
    # Space: O(log(n))


def main():
    result = smallest_range_ii(nums = [1], k = 0)
    print(result) # 0

    result = smallest_range_ii(nums = [0,10], k = 2)
    print(result) # 6

    result = smallest_range_ii(nums = [1,3,6], k = 3)
    print(result) # 3

if __name__ == "__main__":
    main()
