# --------------------
# 198. House Robber 👮
# --------------------

# Problem: https://leetcode.com/problems/house-robber/
# 
# You are a professional robber planning to rob houses along a street. Each 
# house has a certain amount of money stashed, the only constraint stopping 
# you from robbing each of them is that adjacent houses have security systems 
# connected and it will automatically contact the police if two adjacent 
# houses were broken into on the same night.
# 
# Given an integer array nums representing the amount of money of each house, 
# return the maximum amount of money you can rob tonight without alerting 
# the police.
# 
# 
# Example 1:
# 
# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
# Total amount you can rob = 1 + 3 = 4.
# 
# 
# Example 2:
# 
# Input: nums = [2,7,9,3,1]
# Output: 12
# Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
# Total amount you can rob = 2 + 9 + 1 = 12.
# 
#  
# Constraints:
# 
# 	1 <= nums.length <= 100
# 	0 <= nums[i] <= 400


# Solution: https://youtu.be/73r3KWiEvyk
# Credit: Navdeep Singh founder of NeetCode
def rob(nums):
    rob1, rob2 = 0, 0

    for n in nums:
        temp = max(n + rob1, rob2)
        rob1 = rob2
        rob2 = temp
    return rob2

# Solution: https://youtu.be/kIII1uT6F8Y
# Credit: Greg Hogg
def rob_rec(nums):
    # Time: O(2^n)
    # Space: O(n)
    n = len(nums)

    def helper(i):
        if i == 0:
            return nums[0]
        if i == 1:
            return max(nums[0], nums[1])
        
        return max(nums[i] + helper(i-2),
                    helper(i-1))
    
    return helper(n-1)

def rob_memo(nums):
    # Time: O(n)
    # Space: O(n)
    n = len(nums)
    if n == 1:
        return nums[0]
    if n == 2:
        return max(nums[0], nums[1])

    memo = {0:nums[0], 1:max(nums[0], nums[1])}

    def helper(i):
        if i in memo:
            return memo[i]
        else:
            memo[i] = max(nums[i] + helper(i-2),
                            helper(i-1))
            return memo[i]
    
    return helper(n-1)

def main():
    result = rob([1,2,3,1])
    print(result) # 4

    result = rob([2,7,9,3,1])
    print(result) # 12

if __name__ == "__main__":
    main()
