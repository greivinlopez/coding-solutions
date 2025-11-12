# ------------------------------------
# 33. Search in Rotated Sorted Array
# ------------------------------------

# Problem: https://leetcode.com/problems/search-in-rotated-sorted-array/
# There is an integer array nums sorted in ascending order (with distinct values).
# 
# Prior to being passed to your function, nums is possibly left rotated at an unknown 
# index k (1 <= k < nums.length) such that the resulting array is 
# [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). 
# For example, [0,1,2,4,5,6,7] might be left rotated by 3 indices and become [4,5,6,7,0,1,2].
# 
# Given the array nums after the possible rotation and an integer target, return the index 
# of target if it is in nums, or -1 if it is not in nums.
# 
# You must write an algorithm with O(log n) runtime complexity.

# Solution: https://youtu.be/U8XENwh8Oy8
# Credit: Navdeep Singh founder of NeetCode 
def search(nums, target):
    l, r = 0, len(nums) - 1

    while l <= r:
        mid = (l + r) // 2
        if target == nums[mid]:
            return mid

        # left sorted portion
        if nums[l] <= nums[mid]:
            if target > nums[mid] or target < nums[l]:
                l = mid + 1
            else:
                r = mid - 1
        # right sorted portion
        else:
            if target < nums[mid] or target > nums[r]:
                r = mid - 1
            else:
                l = mid + 1
    return -1

# Solution: https://youtu.be/4Ik1nCLjwcI
# Credit: Greg Hog
def search_alt(nums, target):
    # Time: O(log(n))
    # Space: O(1)
    n = len(nums)
    l = 0
    r = n - 1

    while l < r:
        m = (l + r) // 2

        if nums[m] > nums[r]:
            l = m + 1
        else:
            r = m

    min_i = l

    if min_i == 0:
        l, r = 0, n - 1
    elif target >= nums[0] and target <= nums[min_i - 1]:
        l, r = 0, min_i - 1
    else:
        l, r = min_i, n - 1

    while l <= r:
        m = (l + r) // 2
        if nums[m] == target:
            return m
        elif nums[m] < target:
            l = m + 1
        else:
            r = m - 1
    return -1

def main():
    result = search(nums = [4,5,6,7,0,1,2], target = 0) # 4
    print(result)
    result = search(nums = [4,5,6,7,0,1,2], target = 3) # -1
    print(result)
    result = search(nums = [1], target = 0) # -1
    print(result)

if __name__ == "__main__":
    main()