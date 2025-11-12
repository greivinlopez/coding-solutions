# -----------------------------------
# 1800. Maximum Ascending Subarray Sum
# -----------------------------------

# Problem: https://leetcode.com/problems/maximum-ascending-subarray-sum
#
# Given an array of positive integers nums, return the maximum possible sum of an
# strictly increasing subarray in nums.
# 
# A subarray is defined as a contiguous sequence of numbers in an array.
# 
# Example 1:
# 
# Input: nums = [10,20,30,5,10,50]
# Output: 65
# Explanation: [5,10,50] is the ascending subarray with the maximum sum of 65.
# 
# Example 2:
# 
# Input: nums = [10,20,30,40,50]
# Output: 150
# Explanation: [10,20,30,40,50] is the ascending subarray with the maximum sum of
# 150.
# 
# Example 3:
# 
# Input: nums = [12,17,15,13,10,11,12]
# Output: 33
# Explanation: [10,11,12] is the ascending subarray with the maximum sum of 33.
# 
# 
# Constraints:
#         1 <= nums.length <= 100
#         1 <= nums[i] <= 100


# Solution: https://youtu.be/NcsmaL_e_Zg
# Credit: Navdeep Singh founder of NeetCode
def max_ascending_sum(nums):
    curSum = results = nums[0]

    for i in range(1, len(nums)):
        if nums[i] <= nums[i - 1]:
            curSum = 0
        curSum += nums[i]
        results = max(curSum, results)

    return results


def main():
    result = max_ascending_sum([10,20,30,5,10,50])
    print(result) # 65

    result = max_ascending_sum([10,20,30,40,50])
    print(result) # 150

    result = max_ascending_sum([12,17,15,13,10,11,12])
    print(result) # 33

if __name__ == "__main__":
    main()
