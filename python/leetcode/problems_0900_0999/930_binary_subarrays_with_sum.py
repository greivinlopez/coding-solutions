# ------------------------------
# 930. Binary Subarrays With Sum
# ------------------------------

# Problem: https://leetcode.com/problems/binary-subarrays-with-sum/
# 
# Given a binary array nums and an integer goal, return the number of non-empty 
# subarrays with a sum goal.
# 
# A subarray is a contiguous part of the array.
# 
#  
# Example 1:
# 
# Input: nums = [1,0,1,0,1], goal = 2
# Output: 4
# Explanation: The 4 subarrays are bolded and underlined below:
# [1,0,1,0,1]
# [1,0,1,0,1]
# [1,0,1,0,1]
# [1,0,1,0,1]
# 
# Example 2:
# 
# Input: nums = [0,0,0,0,0], goal = 0
# Output: 15
#  
# 
# Constraints:
# 
#   1 <= nums.length <= 3 * 10^4
#   nums[i] is either 0 or 1.
#   0 <= goal <= nums.length

# Solution: https://youtu.be/j4JDr4-jvo4
# Credit: Navdeep Singh founder of NeetCode
def num_subarrays_with_sum(nums, goal):

    def helper(x):
        if x < 0: return 0

        res = 0
        l, cur = 0, 0
        for r in range(len(nums)):
            cur += nums[r]
            while cur > x:
                cur -= nums[l]
                l += 1
            res += (r - l + 1)
        return res
    
    return helper(goal) - helper(goal - 1)


def main():
    result = num_subarrays_with_sum(nums = [1,0,1,0,1], goal = 2)
    print(result) # 4

    result = num_subarrays_with_sum(nums = [0,0,0,0,0], goal = 0)
    print(result) # 15

if __name__ == "__main__":
    main()
