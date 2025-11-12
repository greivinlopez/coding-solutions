# ---------------
# 494. Target Sum
# ---------------

# Problem: https://leetcode.com/problems/target-sum/
# 
# You are given an integer array nums and an integer target.
# 
# You want to build an expression out of nums by adding one of the symbols '+' 
# and '-' before each integer in nums and then concatenate all the integers.
# 
# 
# 	For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 
#   1 and concatenate them to build the expression "+2-1".
# 
# 
# Return the number of different expressions that you can build, which evaluates 
# to target.
# 
#  
# Example 1:
# 
# Input: nums = [1,1,1,1,1], target = 3
# Output: 5
# Explanation: There are 5 ways to assign symbols to make the sum of nums be target 3.
# -1 + 1 + 1 + 1 + 1 = 3
# +1 - 1 + 1 + 1 + 1 = 3
# +1 + 1 - 1 + 1 + 1 = 3
# +1 + 1 + 1 - 1 + 1 = 3
# +1 + 1 + 1 + 1 - 1 = 3
# 
# 
# Example 2:
# 
# Input: nums = [1], target = 1
# Output: 1
# 
# 
# Constraints:
# 
# 	1 <= nums.length <= 20
# 	0 <= nums[i] <= 1000
# 	0 <= sum(nums[i]) <= 1000
# 	-1000 <= target <= 1000


# Solution: https://www.youtube.com/watch?v=dwMOrl85Xes
# Credit: Navdeep Singh founder of NeetCode
from collections import defaultdict
def find_target_sum_ways(nums, target):
    dp = defaultdict(int)
    dp[0] = 1 # (0 sum) -> 1 way : 1 way to sum to zero with first 0 elements

    for i in range(len(nums)):
        next_dp = defaultdict(int)
        for cur_sum, count in dp.items():
            next_dp[cur_sum + nums[i]] += count
            next_dp[cur_sum - nums[i]] += count
        dp = next_dp
    return dp[target]


def main():
    result = find_target_sum_ways(nums = [1,1,1,1,1], target = 3)
    print(result) # 5

    result = find_target_sum_ways(nums = [1], target = 1)
    print(result) # 1

if __name__ == "__main__":
    main()
