# ------------------------------------------------------------------------------
# 1577. Number of Ways Where Square of Number Is Equal to Product of Two Numbers
# ------------------------------------------------------------------------------

# Problem: https://leetcode.com/problems/number-of-ways-where-square-of-number-is-equal-to-product-of-two-numbers
#
# Given two arrays of integers nums1 and nums2, return the number of triplets
# formed (type 1 and type 2) under the following rules:
#         
#   * Type 1: Triplet (i, j, k) if nums1[i]² == nums2[j] * nums2[k] where 
#     0 <= i < nums1.length and 0 <= j < k < nums2.length.
#   * Type 2: Triplet (i, j, k) if nums2[i]² == nums1[j] * nums1[k] where 
#     0 <= i < nums2.length and 0 <= j < k < nums1.length.
# 
# Example 1:
# 
# Input: nums1 = [7,4], nums2 = [5,2,8,9]
# Output: 1
# 
# Explanation: Type 1: (1, 1, 2), nums1[1]2 = nums2[1] * nums2[2]. (42 = 2 * 8).
# 
# Example 2:
# 
# Input: nums1 = [1,1], nums2 = [1,1,1]
# Output: 9
# 
# Explanation: All Triplets are valid, because 12 = 1 * 1.
# Type 1: (0,0,1), (0,0,2), (0,1,2), (1,0,1), (1,0,2), (1,1,2).  nums1[i]2 =
# nums2[j] * nums2[k].
# Type 2: (0,0,1), (1,0,1), (2,0,1). nums2[i]2 = nums1[j] * nums1[k].
# 
# Example 3:
# 
# Input: nums1 = [7,7,8,3], nums2 = [1,2,9,7]
# Output: 2
# 
# Explanation: There are 2 valid triplets.
# Type 1: (3,0,2).  nums1[3]2 = nums2[0] * nums2[2].
# Type 2: (3,0,1).  nums2[3]2 = nums1[0] * nums1[1].
# 
# 
# Constraints:
#         1 <= nums1.length, nums2.length <= 1000
#         1 <= nums1[i], nums2[i] <= 10⁵

from collections import Counter

# Solution: https://algo.monster/liteproblems/1577
# Credit: AlgoMonster
def num_triplets(nums1, nums2):
  
    def count_products(nums):
        product_counter = Counter()
        
        # Iterate through all unique pairs (j, k) where j < k
        for j in range(len(nums)):
            for k in range(j + 1, len(nums)):
                product = nums[j] * nums[k]
                product_counter[product] += 1
                
        return product_counter
    
    def calculate_triplets(nums, product_counter) :
        total = 0
        
        # For each number, check if its square matches any product
        for num in nums:
            square = num * num
            total += product_counter[square]
            
        return total
    
    # Count all possible products for both arrays
    products_nums1 = count_products(nums1)
    products_nums2 = count_products(nums2)
    
    # Calculate Type 1 triplets (nums2[i]^2 = nums1[j] * nums1[k])
    # and Type 2 triplets (nums1[i]^2 = nums2[j] * nums2[k])
    type1_triplets = calculate_triplets(nums2, products_nums1)
    type2_triplets = calculate_triplets(nums1, products_nums2)
    
    return type1_triplets + type2_triplets
    # Time: O(m² + n² + m + n)
    # Space: O(m² + n²)


def main():
    result = num_triplets(nums1 = [7,4], nums2 = [5,2,8,9])
    print(result) # 1

    result = num_triplets(nums1 = [1,1], nums2 = [1,1,1])
    print(result) # 9

    result = num_triplets(nums1 = [7,7,8,3], nums2 = [1,2,9,7])
    print(result) # 2

if __name__ == "__main__":
    main()
