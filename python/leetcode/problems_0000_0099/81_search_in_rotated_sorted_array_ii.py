# --------------------------------------
# 81. Search in Rotated Sorted Array II
# --------------------------------------

# Problem: https://leetcode.com/problems/search-in-rotated-sorted-array-ii/
# 
# There is an integer array nums sorted in non-decreasing order (not necessarily with distinct values).
# 
# Before being passed to your function, nums is rotated at an unknown pivot 
# index k (0 <= k < nums.length) such that the resulting array is [nums[k], 
# nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). 
# For example, [0,1,2,4,4,4,5,6,6,7] might be rotated at pivot index 5 
# and become [4,5,6,6,7,0,1,2,4,4].
# 
# Given the array nums after the rotation and an integer target, return true 
# if target is in nums, or false if it is not in nums.
# 
# You must decrease the overall operation steps as much as possible.

# Solution: https://youtu.be/oUnF7o88_Xc
# Credit: Navdeep Singh founder of NeetCode
def search(nums, target):
    # Time: O(log(n))
    left,right = 0,len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return True

        #Left sorted portion
        if nums[left] < nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        #Right sorted portion
        elif nums[left] > nums[mid]:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
        else:
            left += 1
    return False 


def main():
    result = search(nums = [2,5,6,0,0,1,2], target = 0) # True
    print(result)
    result = search(nums = [2,5,6,0,0,1,2], target = 3) # False
    print(result)

if __name__ == "__main__":
    main()