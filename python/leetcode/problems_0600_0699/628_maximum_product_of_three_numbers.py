# -------------------------------------
# 628. Maximum Product of Three Numbers
# -------------------------------------

# Problem: https://leetcode.com/problems/maximum-product-of-three-numbers
#
# Given an integer array nums, find three numbers whose product is maximum and
# return the maximum product.
# 
# Example 1:
# 
# Input: nums = [1,2,3]
# Output: 6
# 
# Example 2:
# 
# Input: nums = [1,2,3,4]
# Output: 24
# 
# Example 3:
# 
# Input: nums = [-1,-2,-3]
# Output: -6
# 
# 
# Constraints:
#         3 <= nums.length <= 10⁴
#         -1000 <= nums[i] <= 1000

import heapq

# Solution: https://algo.monster/liteproblems/628
# Credit: AlgoMonster
def maximum_product(nums):
    # Sort the array in ascending order
    nums.sort()
    
    # Calculate product of three largest numbers
    # This handles the case where all numbers are positive
    # or when the largest positive numbers give the maximum product
    product_three_largest = nums[-1] * nums[-2] * nums[-3]
    
    # Calculate product of two smallest numbers and the largest number
    # This handles the case where two negative numbers (when multiplied become positive)
    # combined with the largest positive number give the maximum product
    product_two_smallest_one_largest = nums[-1] * nums[0] * nums[1]
    
    # Return the maximum of the two possible products
    return max(product_three_largest, product_two_smallest_one_largest)
    # Time: O(n * log(n))
    # Space: O(log(n))


# Alternative Solution: https://leetcode.com/problems/maximum-product-of-three-numbers/solutions/6760205/most-pythonic-solution-beauty-and-fast-solution-o-n-with-heapq-97-74-beats
def maximum_product_heap(nums):
    max1, max2, max3 = heapq.nlargest(3, nums)
    min1, min2 = heapq.nsmallest(2, nums)
    
    return max(max1 * max2 * max3, min1 * min2 * max1)
    # Time: O(n)
    # Space: O(1)


def main():
    result = maximum_product([1,2,3])
    print(result) # 6

    result = maximum_product([1,2,3,4])
    print(result) # 24

    result = maximum_product([-1,-2,-3])
    print(result) # -6

if __name__ == "__main__":
    main()
