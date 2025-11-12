# -------------------------------------
# 540. Single Element In A Sorted Array
# -------------------------------------

# Problem: https://leetcode.com/problems/single-element-in-a-sorted-array/
# 
# You are given a sorted array consisting of only integers where every element 
# appears exactly twice, except for one element which appears exactly once.
# 
# Return the single element that appears only once.
# 
# Your solution must run in O(log n) time and O(1) space.
# 
# 
# Example 1:
# Input: nums = [1,1,2,3,3,4,4,8,8]
# Output: 2
# Example 2:
# Input: nums = [3,3,7,7,10,11,11]
# Output: 10
# 
#  
# Constraints:
# 
# 	1 <= nums.length <= 10^5
# 	0 <= nums[i] <= 10^5


# Solution: https://youtu.be/HGtqdzyUJ3k
# Credit: Navdeep Singh founder of NeetCode
def single_non_duplicate(nums):
    def is_non_duplicate(i):
        is_left_different = i == 0 or nums[i-1] != nums[i]
        is_right_different = i == len(nums)-1 or nums[i+1] != nums[i]
        return is_left_different and is_right_different

    if len(nums) == 1:
        return nums[0]

    l, r = 0, len(nums) - 1
    while l <= r:
        mid = (l + r) // 2
        if is_non_duplicate(mid):
            return nums[mid]

        if mid % 2 == 0:
            if nums[mid+1] == nums[mid]:
                l = mid + 1
            else:
                r = mid - 1
        else:
            if nums[mid+1] == nums[mid]:
                r = mid - 1
            else:
                l = mid + 1


def main():
    result = single_non_duplicate([1,1,2,3,3,4,4,8,8])
    print(result) # 2

    result = single_non_duplicate([3,3,7,7,10,11,11])
    print(result) # 10

if __name__ == "__main__":
    main()
