# -------------------------------------
# 1262. Greatest Sum Divisible by Three
# -------------------------------------

# Problem: https://leetcode.com/problems/greatest-sum-divisible-by-three
#
# Given an integer array nums, return the maximum possible sum of elements of the
# array such that it is divisible by three.
# 
# Example 1:
# 
# Input: nums = [3,6,5,1,8]
# Output: 18
# 
# Explanation: Pick numbers 3, 6, 1 and 8 their sum is 18 (maximum sum divisible
# by 3).
# 
# Example 2:
# 
# Input: nums = [4]
# Output: 0
#
# Explanation: Since 4 is not divisible by 3, do not pick any number.
# 
# Example 3:
# 
# Input: nums = [1,2,3,4,4]
# Output: 12
# 
# Explanation: Pick numbers 1, 3, 4 and 4 their sum is 12 (maximum sum divisible
# by 3).
# 
# 
# Constraints:
#         1 <= nums.length <= 4 * 10⁴
#         1 <= nums[i] <= 10⁴


# Solution: https://algo.monster/liteproblems/1262
# Credit: AlgoMonster
def max_sum_div_three(nums):
    n = len(nums)
    
    # Initialize DP table
    # dp[i][j] = maximum sum using first i elements where sum % 3 == j
    # Use -inf for impossible states
    dp = [[-float('inf')] * 3 for _ in range(n + 1)]
    
    # Base case: using 0 elements, sum is 0 (which is divisible by 3)
    dp[0][0] = 0
    
    # Process each number
    for i in range(1, n + 1):
        current_num = nums[i - 1]
        
        # For each possible remainder (0, 1, 2)
        for remainder in range(3):
            # Option 1: Don't include current number
            dp[i][remainder] = dp[i - 1][remainder]
            
            # Option 2: Include current number
            # Find what remainder we need from previous state
            prev_remainder = (remainder - current_num) % 3
            dp[i][remainder] = max(
                dp[i][remainder], 
                dp[i - 1][prev_remainder] + current_num
            )
    
    # Return maximum sum divisible by 3 (remainder = 0)
    return dp[n][0]
    # Time: O(n)
    # Space: O(n)


def main():
    result = max_sum_div_three(nums = [3,6,5,1,8])
    print(result) # 18

    result = max_sum_div_three(nums = [4])
    print(result) # 0

    result = max_sum_div_three(nums = [1,2,3,4,4])
    print(result) # 12

if __name__ == "__main__":
    main()
