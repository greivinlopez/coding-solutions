# --------------------------------------------------
# 1913. Maximum Product Difference Between Two Pairs
# --------------------------------------------------

# Problem: https://leetcode.com/problems/maximum-product-difference-between-two-pairs
#
# The product difference between two pairs (a, b) and (c, d) is defined as (a * b)
# - (c * d).
#         
#   * For example, the product difference between (5, 6) and (2, 7) is (5 * 6)
#     - (2 * 7) = 16.
# 
# Given an integer array nums, choose four distinct indices w, x, y, and z such
# that the product difference between pairs (nums[w], nums[x]) and (nums[y],
# nums[z]) is maximized.
# 
# Return the maximum such product difference.
# 
# Example 1:
# 
# Input: nums = [5,6,2,7,4]
# Output: 34
# 
# Explanation: We can choose indices 1 and 3 for the first pair (6, 7) and indices
# 2 and 4 for the second pair (2, 4).
# The product difference is (6 * 7) - (2 * 4) = 34.
# 
# Example 2:
# 
# Input: nums = [4,2,5,9,7,4,8]
# Output: 64
# 
# Explanation: We can choose indices 3 and 6 for the first pair (9, 8) and indices
# 1 and 5 for the second pair (2, 4).
# The product difference is (9 * 8) - (2 * 4) = 64.
# 
# 
# Constraints:
#         4 <= nums.length <= 10^4
#         1 <= nums[i] <= 10^4


# Solution: https://youtu.be/wBPoEm3r3EA
# Credit: Navdeep Singh founder of NeetCode
def max_product_difference(nums):
    max1 = max2 = 0  # largest, second largest
    min1 = min2 = float("inf")  # smallest, second smallest

    for n in nums:
        if n > max2:
            if n > max1:
                max1, max2 = n, max1
            else:
                max2 = n
        if n < min2:
            if n < min1:
                min1, min2 = n, min1
            else:
                min2 = n

    return (max1 * max2) - (min1 * min2)
    # Time: O(n)
    # Space: O(1)

def main():
    result = max_product_difference([5,6,2,7,4])
    print(result) # 34

    result = max_product_difference([4,2,5,9,7,4,8])
    print(result) # 64

if __name__ == "__main__":
    main()
