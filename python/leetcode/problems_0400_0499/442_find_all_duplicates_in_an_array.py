# ------------------------------------
# 442. Find All Duplicates In An Array
# ------------------------------------

# Problem: https://leetcode.com/problems/find-all-duplicates-in-an-array/
# 
# Given an integer array nums of length n where all the integers of nums are in 
# the range [1, n] and each integer appears at most twice, return an array of 
# all the integers that appears twice.
# 
# You must write an algorithm that runs in O(n) time and uses only constant 
# auxiliary space, excluding the space needed to store the output
# 
#  
# Example 1:
# Input: nums = [4,3,2,7,8,2,3,1]
# Output: [2,3]
# 
# Example 2:
# Input: nums = [1,1,2]
# Output: [1]
# 
# Example 3:
# Input: nums = [1]
# Output: []
# 
#  
# Constraints:
# 
# 	n == nums.length
# 	1 <= n <= 10^5
# 	1 <= nums[i] <= n
# 	Each element in nums appears once or twice.


# Solution: https://youtu.be/Y8x0iAVEITo
# Credit: Navdeep Singh founder of NeetCode
def find_duplicates(nums):
    res = []

    for n in nums:
        n = abs(n)
        if nums[n - 1] < 0:
            res.append(n)
        nums[n - 1] = -nums[n - 1]
    
    return res


def main():
    result = find_duplicates([4,3,2,7,8,2,3,1])
    print(result) # [2,3]

    result = find_duplicates([1,1,2])
    print(result) # [1]

    result = find_duplicates([1])
    print(result) # []

if __name__ == "__main__":
    main()
