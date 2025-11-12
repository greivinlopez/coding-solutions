# ---------------------------------
# 713. Subarray Product Less Than K
# ---------------------------------

# Problem: https://leetcode.com/problems/subarray-product-less-than-k
#
# Given an array of integers nums and an integer k, return the number of
# contiguous subarrays where the product of all the elements in the subarray is
# strictly less than k.
# 
# Example 1:
# 
# Input: nums = [10,5,2,6], k = 100
# Output: 8
# 
# Explanation: The 8 subarrays that have product less than 100 are:
# [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]
# Note that [10, 5, 2] is not included as the product of 100 is not strictly less
# than k.
# 
# Example 2:
# 
# Input: nums = [1,2,3], k = 0
# Output: 0
# 
# 
# Constraints:
#         1 <= nums.length <= 3 * 10^4
#         1 <= nums[i] <= 1000
#         0 <= k <= 10^6


# Solution: https://youtu.be/Cg6_nF7YIks
# Credit: Navdeep Singh founder of NeetCode
def num_subarray_product_less_than_k(nums, k):
    res = 0
    l = 0
    product = 1
    for r in range(len(nums)):
        product *= nums[r]
        while l <= r and product >= k:
            product = product // nums[l]
            l += 1
        res += (r - l + 1)
    return res
    # Time: O(n)
    # Space: O(1)


def main():
    result = num_subarray_product_less_than_k(nums = [10,5,2,6], k = 100)
    print(result) # 8

    result = num_subarray_product_less_than_k(nums = [1,2,3], k = 0)
    print(result) # 0

if __name__ == "__main__":
    main()
