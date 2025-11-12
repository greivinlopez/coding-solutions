# -------------------------
# 665. Non Decreasing Array
# -------------------------

# Problem: https://leetcode.com/problems/non-decreasing-array/
# 
# Given an array nums with n integers, your task is to check if it could become
#  non-decreasing by modifying at most one element.
# 
# We define an array is non-decreasing if nums[i] <= nums[i + 1] holds for 
# every i (0-based) such that (0 <= i <= n - 2).
# 
#  
# Example 1:
# 
# Input: nums = [4,2,3]
# Output: true
# Explanation: You could modify the first 4 to 1 to get a non-decreasing array.
# 
# 
# Example 2:
# 
# Input: nums = [4,2,1]
# Output: false
# Explanation: You cannot get a non-decreasing array by modifying at most one 
# element.
# 
# 
# Constraints:
# 
# 	n == nums.length
# 	1 <= n <= 10^4
# 	-10^5 <= nums[i] <= 10^5


# Solution: https://youtu.be/RegQckCegDk
# Credit: Navdeep Singh founder of NeetCode
def check_possibility(nums):
    if len(nums) <= 2:
        return True
    changed = False
    for i, num in enumerate(nums):
        if i == len(nums) - 1 or num <= nums[i + 1]:
            continue
        if changed:
            return False
        if i == 0 or nums[i + 1] >= nums[i - 1]:
            nums[i] = nums[i + 1]
        else:
            nums[i + 1] = nums[i]
        changed = True
    return True


def main():
    result = check_possibility([4,2,3])
    print(result) # True

    result = check_possibility([4,2,1])
    print(result) # False

if __name__ == "__main__":
    main()
