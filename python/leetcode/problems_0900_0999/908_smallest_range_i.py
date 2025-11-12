# ---------------------
# 908. Smallest Range I
# ---------------------

# Problem: https://leetcode.com/problems/smallest-range-i
#
# You are given an integer array nums and an integer k.
# 
# In one operation, you can choose any index i where 0 <= i < nums.length and
# change nums[i] to nums[i] + x where x is an integer from the range [-k, k]. You
# can apply this operation at most once for each index i.
# 
# The score of nums is the difference between the maximum and minimum elements in
# nums.
# 
# Return the minimum score of nums after applying the mentioned operation at most
# once for each index in it.
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
# Output: 0
# 
# Explanation: Change nums to be [4, 4, 4]. The score is max(nums) - min(nums) = 4
# - 4 = 0.
# 
# 
# Constraints:
#         1 <= nums.length <= 10⁴
#         0 <= nums[i] <= 10⁴
#         0 <= k <= 10⁴


# Solution: https://algo.monster/liteproblems/908
# Credit: AlgoMonster
def smallest_range_i(nums, k):
    # Find the maximum and minimum values in the original array
    max_value = max(nums)
    min_value = min(nums)
    
    # Calculate the minimum possible difference
    # The best strategy is to decrease max_value by k and increase min_value by k
    # This gives us a potential difference of (max_value - min_value - 2*k)
    # If this difference is negative, it means we can make all values equal (return 0)
    min_difference = max_value - min_value - 2 * k
    
    # Return 0 if we can make all values equal, otherwise return the minimum difference
    return max(0, min_difference)
    # Time: O(n)
    # Space: O(1)


def main():
    result = smallest_range_i(nums = [1], k = 0)
    print(result) # 0

    result = smallest_range_i(nums = [0,10], k = 2)
    print(result) # 6

    result = smallest_range_i(nums = [1,3,6], k = 3)
    print(result) # 0

if __name__ == "__main__":
    main()
