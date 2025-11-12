# ----------------------------------------------------
# 1413. Minimum Value to Get Positive Step by Step Sum
# ----------------------------------------------------

# Problem: https://leetcode.com/problems/minimum-value-to-get-positive-step-by-step-sum
#
# Given an array of integers nums, you start with an initial positive value
# startValue.
# 
# In each iteration, you calculate the step by step sum of
# startValue plus elements in nums (from left to right).
# 
# Return the minimum positive value of startValue such that the step by step sum
# is never less than 1.
# 
# Example 1:
# 
# Input: nums = [-3,2,-3,4,2]
# Output: 5
# 
# Explanation: If you choose startValue = 4, in the third iteration your step by
# step sum is less than 1.
# step by step sum
# startValue = 4 | startValue = 5 | nums
#   (4 -3 ) = 1  | (5 -3 ) = 2    |  -3
#   (1 +2 ) = 3  | (2 +2 ) = 4    |   2
#   (3 -3 ) = 0  | (4 -3 ) = 1    |  -3
#   (0 +4 ) = 4  | (1 +4 ) = 5    |   4
#   (4 +2 ) = 6  | (5 +2 ) = 7    |   2
# 
# Example 2:
# 
# Input: nums = [1,2]
# Output: 1
# 
# Explanation: Minimum start value should be positive.
# 
# Example 3:
# 
# Input: nums = [1,-2,-3]
# Output: 5
# 
# 
# Constraints:
#         1 <= nums.length <= 100
#         -100 <= nums[i] <= 100


# Solution: https://algo.monster/liteproblems/1413
# Credit: AlgoMonster
def min_start_value(nums):
    # Initialize cumulative sum and minimum cumulative sum
    cumulative_sum = 0
    min_cumulative_sum = float('inf')
    
    # Iterate through the array to find the minimum cumulative sum
    for num in nums:
        cumulative_sum += num
        min_cumulative_sum = min(min_cumulative_sum, cumulative_sum)
    
    # Calculate the minimum start value
    # If min_cumulative_sum is negative, we need 1 - min_cumulative_sum to ensure step sum >= 1
    # If min_cumulative_sum is non-negative, we just need start value = 1
    return max(1, 1 - min_cumulative_sum)
    # Time: O(n)
    # Space: O(1)


def main():
    result = min_start_value(nums = [-3,2,-3,4,2])
    print(result) # 5

    result = min_start_value(nums = [1,2])
    print(result) # 1

    result = min_start_value(nums = [1,-2,-3])
    print(result) # 5

if __name__ == "__main__":
    main()
