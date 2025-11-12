# ------------------------------------------------------------
# 34. Find First and Last Position of Element in Sorted Array
# ------------------------------------------------------------

# Problem: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
# Given an array of integers nums sorted in non-decreasing order, find the starting and ending 
# position of a given target value.
# 
# If target is not found in the array, return [-1, -1].
# 
# You must write an algorithm with O(log n) runtime complexity.

# Solution: https://youtu.be/4sQL7R5ySUU
# Credit: Navdeep Singh founder of NeetCode 
def search_range(nums, target):
    # Time: O(log(n))
    left = bin_search(nums, target, True)
    right = bin_search(nums, target, False)
    return [left, right]

# leftBias=[True/False], if false, res is rightBiased
def bin_search(nums, target, leftBias):
    l, r = 0, len(nums) - 1
    i = -1
    while l <= r:
        m = (l + r) // 2
        if target > nums[m]:
            l = m + 1
        elif target < nums[m]:
            r = m - 1
        else:
            i = m
            if leftBias:
                r = m - 1
            else:
                l = m + 1
    return i

def main():
    result = search_range(nums = [5,7,7,8,8,10], target = 8) # [3, 4]
    print(result)
    result = search_range(nums = [5,7,7,8,8,10], target = 6) # [-1, -1]
    print(result)
    result = search_range(nums = [], target = 0) # [-1, -1]
    print(result)

if __name__ == "__main__":
    main()