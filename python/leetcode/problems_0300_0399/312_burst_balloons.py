# -------------------
# 312. Burst Balloons
# -------------------

# Problem: https://leetcode.com/problems/burst-balloons/
# 
# You are given n balloons, indexed from 0 to n - 1. Each balloon is painted 
# with a number on it represented by an array nums. You are asked to burst 
# all the balloons.
# 
# If you burst the ith balloon, you will get nums[i - 1] * nums[i] * nums[i + 1] 
# coins. If i - 1 or i + 1 goes out of bounds of the array, then treat it as if 
# there is a balloon with a 1 painted on it.
# 
# Return the maximum coins you can collect by bursting the balloons wisely.
# 
#  
# Example 1:
# 
# Input: nums = [3,1,5,8]
# Output: 167
# Explanation:
# nums = [3,1,5,8] --> [3,5,8] --> [3,8] --> [8] --> []
# coins =  3*1*5    +   3*5*8   +  1*3*8  + 1*8*1 = 167
# 
# Example 2:
# 
# Input: nums = [1,5]
# Output: 10
# 
#  
# Constraints:
# 
# 	n == nums.length
# 	1 <= n <= 300
# 	0 <= nums[i] <= 100


# Solution: https://youtu.be/VFskby7lUbw
# Credit: Navdeep Singh founder of NeetCode
def max_coins(nums):
    cache = {}
    nums = [1] + nums + [1]

    for offset in range(2, len(nums)):
        for left in range(len(nums) - offset):
            right = left + offset
            for pivot in range(left + 1, right):
                coins = nums[left] * nums[pivot] * nums[right]
                coins += cache.get((left, pivot), 0) + cache.get((pivot, right), 0)
                cache[(left, right)] = max(coins, cache.get((left, right), 0))
    return cache.get((0, len(nums) - 1), 0)


def main():
    result = max_coins([3,1,5,8])
    print(result) # 167

    result = max_coins([1,5])
    print(result) # 10

if __name__ == "__main__":
    main()
