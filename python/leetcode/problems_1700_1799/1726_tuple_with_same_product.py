# -----------------------------
# 1726. Tuple with Same Product
# -----------------------------

# Problem: https://leetcode.com/problems/tuple-with-same-product
#
# Given an array nums of distinct positive integers, return the number of tuples
# (a, b, c, d) such that a * b = c * d where a, b, c, and d are elements of nums,
# and a != b != c != d.
# 
# Example 1:
# 
# Input: nums = [2,3,4,6]
# Output: 8
# 
# Explanation: There are 8 valid tuples:
# (2,6,3,4) , (2,6,4,3) , (6,2,3,4) , (6,2,4,3)
# (3,4,2,6) , (4,3,2,6) , (3,4,6,2) , (4,3,6,2)
# 
# Example 2:
# 
# Input: nums = [1,2,4,5,10]
# Output: 16
# 
# Explanation: There are 16 valid tuples:
# (1,10,2,5) , (1,10,5,2) , (10,1,2,5) , (10,1,5,2)
# (2,5,1,10) , (2,5,10,1) , (5,2,1,10) , (5,2,10,1)
# (2,10,4,5) , (2,10,5,4) , (10,2,4,5) , (10,2,5,4)
# (4,5,2,10) , (4,5,10,2) , (5,4,2,10) , (5,4,10,2)
# 
# 
# Constraints:
#         1 <= nums.length <= 1000
#         1 <= nums[i] <= 10^4
#         All elements in nums are distinct.

from collections import defaultdict

# Solution: https://youtu.be/SSwvMoOhiq0
# Credit: Navdeep Singh founder of NeetCode
def tuple_same_product(nums):
    product_cnt = defaultdict(int)  # n1 * n2 -> count
    
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            product = nums[i] * nums[j]
            product_cnt[product] += 1
    
    # 1 count -> 0 pair -> 0 tuples
    # 2 count -> 1 pair -> 8 tuples
    # 3 count -> 3 pairs -> 24 tuples
    # 4 count -> 6 pairs -> 48 tuples
    # 5 count -> 10 pairs -> 80 tuples
    
    res = 0
    for cnt in product_cnt.values():
        pairs = (cnt * (cnt - 1)) // 2
        res += 8 * pairs
    return res
    # Time: O(n^2) 
    # Space: O(k) where k is the number of unique products


def main():
    result = tuple_same_product(nums = [2,3,4,6])
    print(result) # True

    result = tuple_same_product(nums = [1,2,4,5,10])
    print(result) # True

if __name__ == "__main__":
    main()
