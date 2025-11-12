# -------------------------------------------------
# 1464. Maximum Product Of Two Elements In An Array
# -------------------------------------------------

# Problem: https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array
#
# Given the array of integers nums, you will choose two different indices i and j
# of that array. Return the maximum value of (nums[i]-1)*(nums[j]-1).
# 
# Example 1:
# 
# Input: nums = [3,4,5,2]
# Output: 12
# Explanation: If you choose the indices i=1 and j=2 (indexed from 0), you will
# get the maximum value, that is, (nums[1]-1)*(nums[2]-1) = (4-1)*(5-1) = 3*4 =
# 12.
# 
# Example 2:
# 
# Input: nums = [1,5,4,5]
# Output: 16
# Explanation: Choosing the indices i=1 and j=3 (indexed from 0), you will get the
# maximum value of (5-1)*(5-1) = 16.
# 
# Example 3:
# 
# Input: nums = [3,7]
# Output: 12
# 
# 
# Constraints:
#         2 <= nums.length <= 500
#         1 <= nums[i] <= 10^3


# Solution: No video found
# Credit: Navdeep Singh founder of NeetCode
def max_product(nums):
    high = secondHigh = 0
    for n in nums:
        if n > high:
            secondHigh = high
            high = n
        else:
            secondHigh = max(n, secondHigh)
    return (high - 1) * (secondHigh - 1)


def main():
    result = max_product([3,4,5,2])
    print(result) # 12

    result = max_product([1,5,4,5])
    print(result) # 16

    result = max_product([3,7])
    print(result) # 12

if __name__ == "__main__":
    main()
