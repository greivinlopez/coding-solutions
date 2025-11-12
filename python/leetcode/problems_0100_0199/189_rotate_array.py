# -----------------
# 189. Rotate Array
# -----------------

# Problem: https://leetcode.com/problems/rotate-array/
# 
# Given an integer array nums, rotate the array to the right by k steps, where k
# is non-negative.
# 
#  
# Example 1:
# 
# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]
# 
# 
# Example 2:
#  
# Input: nums = [-1,-100,3,99], k = 2
# Output: [3,99,-1,-100]
# Explanation: 
# rotate 1 steps to the right: [99,-1,-100,3]
# rotate 2 steps to the right: [3,99,-1,-100]
# 
# 
# Constraints:
# 
# 	1 <= nums.length <= 105
# 	-231 <= nums[i] <= 231 - 1
# 	0 <= k <= 105
# 
#  
# Follow up:
# 
# 	Try to come up with as many solutions as you can. There are at least three different ways to solve this problem.
# 	Could you do it in-place with O(1) extra space?


# Solution: https://youtu.be/BHr381Guz3Y
# Credit: Navdeep Singh founder of NeetCode
def rotate(nums, k):
    """
    Do not return anything, modify nums in-place instead.
    """
    k = k % len(nums)
    l, r = 0, len(nums) - 1
    while l < r:
        nums[l], nums[r] = nums[r], nums[l]
        l, r = l + 1, r - 1
        
    l, r = 0, k - 1
    while l < r:
        nums[l], nums[r] = nums[r], nums[l]
        l, r = l + 1, r - 1
        
    l, r = k, len(nums) - 1
    while l < r:
        nums[l], nums[r] = nums[r], nums[l]
        l, r = l + 1, r - 1


def main():
    array = [1,2,3,4,5,6,7]
    rotate(array, 3)
    print(array) # [5,6,7,1,2,3,4]

    array = [-1,-100,3,99]
    rotate(array, 2)
    print(array) # [3,99,-1,-100]

if __name__ == "__main__":
    main()
