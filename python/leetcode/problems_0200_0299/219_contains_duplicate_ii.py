# --------------------------
# 219. Contains Duplicate II
# --------------------------

# Problem: https://leetcode.com/problems/contains-duplicate-ii/
# 
# Given an integer array nums and an integer k, return true if there are two 
# distinct indices i and j in the array such that nums[i] == nums[j] and 
# abs(i - j) <= k.
# 
#  
# Example 1:
# 
# Input: nums = [1,2,3,1], k = 3
# Output: true
# 
# 
# Example 2:
# 
# Input: nums = [1,0,1,1], k = 1
# Output: true
# 
# 
# Example 3:
# 
# Input: nums = [1,2,3,1,2,3], k = 2
# Output: false
# 
#  
# Constraints:
# 
# 	1 <= nums.length <= 105
# 	-109 <= nums[i] <= 109
# 	0 <= k <= 105


# Solution: https://youtu.be/ypn0aZ0nrL4
# Credit: Navdeep Singh founder of NeetCode
def contains_nearby_duplicate(nums, k):
    window = set()
    L = 0

    for R in range(len(nums)):
        if R - L > k:
            window.remove(nums[L])
            L += 1
        if nums[R] in window:
            return True
        window.add(nums[R])
    return False


# Solution: 
# Credit: Greg Hogg


def main():
    result = contains_nearby_duplicate(nums = [1,2,3,1], k = 3)
    print(result) # True

    result = contains_nearby_duplicate(nums = [1,0,1,1], k = 1)
    print(result) # True

    result = contains_nearby_duplicate([1,2,3,1,2,3], k = 2)
    print(result) # False

if __name__ == "__main__":
    main()
