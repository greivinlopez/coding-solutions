# ----------------
# 283. Move Zeroes
# ----------------

# Problem: https://leetcode.com/problems/move-zeroes/
# 
# Given an integer array nums, move all 0's to the end of it while maintaining 
# the relative order of the non-zero elements.
# 
# Note that you must do this in-place without making a copy of the array.
# 
#  
# Example 1:
# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Example 2:
# Input: nums = [0]
# Output: [0]
# 
#  
# Constraints:
# 
# 	1 <= nums.length <= 104
# 	-231 <= nums[i] <= 231 - 1
# 
# Follow up: Could you minimize the total number of operations done?


# Solution: https://youtu.be/aayNRwUN3Do
# Credit: Navdeep Singh founder of NeetCode
def move_zeroes(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    slow = 0
    for fast in range(len(nums)):
        
        if nums[fast] != 0 and nums[slow] == 0:
            nums[slow], nums[fast] = nums[fast], nums[slow]

        if nums[slow] != 0:
            slow += 1


def main():
    nums = [0,1,0,3,12]
    move_zeroes(nums)
    print(nums) # [1,3,12,0,0]

    nums = [0]
    move_zeroes(nums)
    print(nums) # [0]

if __name__ == "__main__":
    main()
