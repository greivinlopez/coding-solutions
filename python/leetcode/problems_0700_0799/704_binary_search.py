# ------------------
# 704. Binary Search
# ------------------

# Problem: https://leetcode.com/problems/binary-search/
# 
# Given an array of integers nums which is sorted in ascending order, and an 
# integer target, write a function to search target in nums. If target exists, 
# then return its index. Otherwise, return -1.
# 
# You must write an algorithm with O(log n) runtime complexity.
# 
#  
# Example 1:
# 
# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4
# Explanation: 9 exists in nums and its index is 4
# 
# Example 2:
# 
# Input: nums = [-1,0,3,5,9,12], target = 2
# Output: -1
# Explanation: 2 does not exist in nums so return -1
#  
# 
# Constraints:
# 
#   1 <= nums.length <= 10⁴
#   -10⁴ < nums[i], target < 10⁴
#   All the integers in nums are unique.
#   nums is sorted in ascending order.


# Solution: https://youtu.be/s4DPM8ct1pI
# Credit: Navdeep Singh founder of NeetCode
def search(nums, target):
    l, r = 0, len(nums) - 1

    while l <= r:
        m = l + ((r - l) // 2)  # (l + r) // 2 can lead to overflow
        if nums[m] > target:
            r = m - 1
        elif nums[m] < target:
            l = m + 1
        else:
            return m
    return -1
    # Time: O(log(n))
    # Space: O(1)

# Solution: https://youtu.be/Dt4FKOF25ZY
# Credit: Greg Hogg

# Brute Force Solution
def search_brute(nums, target):
    n = len(nums)
    for i in range(n):
        if nums[i] == target:
            return i
    return -1
    # Time: O(n)
    # Space: O(1)

def search_alt(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        middle = (right + left) // 2

        if nums[middle] == target:
            return middle
        elif nums[middle] > target:
            right = middle - 1
        else:
            left = middle + 1

    return -1
    # Time: O(log(n))
    # Space: O(1)


def main():
    result = search(nums = [-1,0,3,5,9,12], target = 9)
    print(result) # 4

    result = search(nums = [-1,0,3,5,9,12], target = 2)
    print(result) # -1

if __name__ == "__main__":
    main()
