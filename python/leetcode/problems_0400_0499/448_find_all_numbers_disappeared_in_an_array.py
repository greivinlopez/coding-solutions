# ---------------------------------------------
# 448. Find All Numbers Disappeared In An Array
# ---------------------------------------------

# Problem: https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
# 
# Given an array nums of n integers where nums[i] is in the range [1, n], return 
# an array of all the integers in the range [1, n] that do not appear in nums.
# 
#  
# Example 1:
# Input: nums = [4,3,2,7,8,2,3,1]
# Output: [5,6]
# 
# Example 2:
# Input: nums = [1,1]
# Output: [2]
# 
#  
# Constraints:
# 
# 	n == nums.length
# 	1 <= n <= 105
# 	1 <= nums[i] <= n
# 
# Follow up: Could you do it without extra space and in O(n) runtime? You may 
# assume the returned list does not count as extra space.


# Solution: https://youtu.be/8i-f24YFWC4
# Credit: Navdeep Singh founder of NeetCode
def find_disappeared_numbers(nums):
    for n in nums:
        i = abs(n) - 1
        nums[i] = -1 * abs(nums[i])

    res = []
    for i, n in enumerate(nums):
        if n > 0:
            res.append(i + 1)
    return res


def main():
    result = find_disappeared_numbers([4,3,2,7,8,2,3,1])
    print(result) # [5,6]

    result = find_disappeared_numbers([1,1])
    print(result) # [2]

if __name__ == "__main__":
    main()
