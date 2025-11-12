# -----------------------------
# 152. Maximum Product Subarray
# -----------------------------

# Problem: https://leetcode.com/problems/maximum-product-subarray/
# 
# Given an integer array nums, find a subarray that has the largest product, 
# and return the product.
# 
# The test cases are generated so that the answer will fit in a 32-bit integer.
#  
# Example 1:
# 
# Input: nums = [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.
# 
# 
# Example 2:
# 
# Input: nums = [-2,0,-1]
# Output: 0
# Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
# 
# 
# Constraints:
# 
# 	1 <= nums.length <= 2 * 104
# 	-10 <= nums[i] <= 10
# 	The product of any subarray of nums is guaranteed to fit in a 32-bit integer.


# Solution: https://youtu.be/lXVy6YWFcRM
# Credit: Navdeep Singh founder of NeetCode
def max_product(nums):
    # O(n)/O(1) : Time/Memory
    res = nums[0]
    curMin, curMax = 1, 1

    for n in nums:

        tmp = curMax * n
        curMax = max(n * curMax, n * curMin, n)
        curMin = min(tmp, n * curMin, n)
        res = max(res, curMax)
    return res


def main():
    result = max_product([2,3,-2,4])
    print(result) # 6

    result = max_product([-2,0,-1])
    print(result) # 0

if __name__ == "__main__":
    main()
