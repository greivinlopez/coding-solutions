# -----------------------------------
# 300. Longest Increasing Subsequence
# -----------------------------------

# Problem: https://leetcode.com/problems/longest-increasing-subsequence/
# 
# Given an integer array nums, return the length of the longest strictly 
# increasing subsequence.
# 
#  
# Example 1:
# 
# Input: nums = [10,9,2,5,3,7,101,18]
# Output: 4
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
# 
# 
# Example 2:
# 
# Input: nums = [0,1,0,3,2,3]
# Output: 4
# 
# 
# Example 3:
# 
# Input: nums = [7,7,7,7,7,7,7]
# Output: 1
# 
# 
# Constraints:
# 
# 	1 <= nums.length <= 2500
# 	-104 <= nums[i] <= 104
# 
# Follow up: Can you come up with an algorithm that runs in O(n log(n)) time complexity?


# Solution: https://youtu.be/cjWnW0hdF1Y
# Credit: Navdeep Singh founder of NeetCode
def length_of_lis(nums):
    # Time: O(n^2)
    # Space: O(n)
    LIS = [1] * len(nums)

    for i in range(len(nums) - 1, -1, -1):
        for j in range(i + 1, len(nums)):
            if nums[i] < nums[j]:
                LIS[i] = max(LIS[i], 1 + LIS[j])
    return max(LIS)

# Solution: https://youtu.be/MrPa5EFcDCU
# Credit: Greg Hogg
# Same Solution
def length_of_lis(nums):
    # Bottom Up DP (Tabulation)
    # Time: O(n^2)
    # Space: O(n)
    
    n = len(nums)
    dp = [1] * n

    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)

def main():
    result = length_of_lis([10,9,2,5,3,7,101,18])
    print(result) # 4

    result = length_of_lis([0,1,0,3,2,3])
    print(result) # 4

    result = length_of_lis([7,7,7,7,7,7,7])
    print(result) # 1

if __name__ == "__main__":
    main()
