# -------------------------------------------
# 80. Remove Duplicates from Sorted Array II
# -------------------------------------------

# Problem: https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/
# 
# Given an integer array nums sorted in non-decreasing order, remove some duplicates 
# in-place such that each unique element appears at most twice. The relative order of 
# the elements should be kept the same.
# 
# Since it is impossible to change the length of the array in some languages, you must 
# instead have the result be placed in the first part of the array nums. 
# More formally, if there are k elements after removing the duplicates, then the first 
# k elements of nums should hold the final result. It does not matter what you leave 
# beyond the first k elements.
# 
# Return k after placing the final result in the first k slots of nums.
# 
# Do not allocate extra space for another array. You must do this by modifying the input 
# array in-place with O(1) extra memory.

# Solution: https://youtu.be/ycAq8iqh0TI
# Credit: Navdeep Singh founder of NeetCode
def remove_duplicates(nums):
    l, r = 0, 0

    while r < len(nums):
        count = 1
        while r + 1 < len(nums) and nums[r] == nums[r + 1]:
            r += 1
            count += 1
        
        for i in range(min(2, count)):
            nums[l] = nums[r]
            l += 1
        r += 1
    return l

# Solution: https://youtu.be/Jg4zXJAH_Kg
# Credit: Greg Hogg
def remove_duplicates_alt(nums):
    j = 1
    count = 1
    n = len(nums)

    for i in range(1, n):
        if nums[i] == nums[i-1]:
            count += 1
        else:
            count = 1
        
        if count <= 2:
            nums[j] = nums[i]
            j += 1
    
    return j
    
def main():
    nums = [1,1,1,2,2,3]
    result = remove_duplicates_alt(nums)
    print(result) # 5
    print(nums)   # [1,1,2,2,3,_]
    nums = [0,0,1,1,1,1,2,3,3]
    result = remove_duplicates_alt(nums)
    print(result) # 7
    print(nums)   # [0,0,1,1,2,3,3,_,_]

if __name__ == "__main__":
    main()