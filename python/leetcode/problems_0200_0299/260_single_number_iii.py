# ----------------------
# 260. Single Number III
# ----------------------

# Problem: https://leetcode.com/problems/single-number-iii
#
# Given an integer array nums, in which exactly two elements appear only once and
# all the other elements appear exactly twice. Find the two elements that appear
# only once. You can return the answer in any order.
# 
# You must write an algorithm that runs in linear runtime complexity and uses only
# constant extra space.
# 
# Example 1:
# 
# Input: nums = [1,2,1,3,2,5]
# Output: [3,5]
# 
# Explanation:  [5, 3] is also a valid answer.
# 
# Example 2:
# 
# Input: nums = [-1,0]
# Output: [-1,0]
# 
# Example 3:
# 
# Input: nums = [0,1]
# Output: [1,0]
# 
# 
# Constraints:
#   2 <= nums.length <= 3 * 10^4
#   -2^31 <= nums[i] <= 2^31 - 1
#   Each integer in nums will appear twice, only two integers will appear once.


# Solution: https://youtu.be/faoVORjd-T8
# Credit: Navdeep Singh founder of NeetCode
def single_number(nums):
    xor = 0
    for n in nums:
        xor ^= n
    
    diff_bit = 1
    while not (xor & diff_bit):
        diff_bit = diff_bit << 1
    
    a, b = 0, 0
    for n in nums:
        if diff_bit & n:
            a = a ^ n
        else:
            b = b ^ n
    return [a, b]
    # Time: O(n)
    # Space: O(1)


def main():
    result = single_number([1,2,1,3,2,5])
    print(result) # [3,5]

    result = single_number([-1,0])
    print(result) # [-1,0]

    result = single_number([0,1])
    print(result) # [1,0]

if __name__ == "__main__":
    main()
