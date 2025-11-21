# -----------------------------------------------------
# 1569. Number of Ways to Reorder Array to Get Same BST
# -----------------------------------------------------

# Problem: https://leetcode.com/problems/number-of-ways-to-reorder-array-to-get-same-bst
#
# Given an array nums that represents a permutation of integers from 1 to n. We
# are going to construct a binary search tree (BST) by inserting the elements of
# nums in order into an initially empty BST. Find the number of different ways to
# reorder nums so that the constructed BST is identical to that formed from the
# original array nums.
#         
#   * For example, given nums = [2,1,3], we will have 2 as the root, 1 as a
#     left child, and 3 as a right child. The array [2,3,1] also yields the same BST
#     but [3,2,1] yields a different BST.
# 
# Return the number of ways to reorder nums such that the BST formed is identical
# to the original BST formed from nums.
# 
# Since the answer may be very large, return it modulo 10⁹ + 7.
# 
# Example 1:
# 
# https://assets.leetcode.com/uploads/2020/08/12/bb.png
# 
# Input: nums = [2,1,3]
# Output: 1
# 
# Explanation: We can reorder nums to be [2,3,1] which will yield the same BST.
# There are no other ways to reorder nums which will yield the same BST.
# 
# Example 2:
# 
# https://assets.leetcode.com/uploads/2020/08/12/ex1.png
# 
# Input: nums = [3,4,5,1,2]
# Output: 5
# 
# Explanation: The following 5 arrays will yield the same BST:
# [3,1,2,4,5]
# [3,1,4,2,5]
# [3,1,4,5,2]
# [3,4,1,2,5]
# [3,4,1,5,2]
# 
# Example 3:
# 
# https://assets.leetcode.com/uploads/2020/08/12/ex4.png
# 
# Input: nums = [1,2,3]
# Output: 0
# 
# Explanation: There are no other orderings of nums that will yield the same BST.
# 
# 
# Constraints:
#         1 <= nums.length <= 1000
#         1 <= nums[i] <= nums.length
#         All integers in nums are distinct.


# Solution: https://algo.monster/liteproblems/1569
# Credit: AlgoMonster
def num_of_ways(nums):

    def count_bst_permutations(arr):
        # Base case: arrays with less than 2 elements have only 1 permutation
        if len(arr) < 2:
            return 1
        
        # Split array into left and right subtrees based on first element (root)
        root = arr[0]
        left_subtree = [x for x in arr if x < root]
        right_subtree = [x for x in arr if x > root]
        
        # Get sizes of left and right subtrees
        left_size = len(left_subtree)
        right_size = len(right_subtree)
        
        # Recursively count permutations for left and right subtrees
        left_permutations = count_bst_permutations(left_subtree)
        right_permutations = count_bst_permutations(right_subtree)
        
        # Calculate total permutations using combinations
        # C(left_size + right_size, left_size) represents ways to interleave
        # left and right subtree elements while maintaining their relative order
        total_size = left_size + right_size
        combinations = binomial_coefficients[total_size][left_size]
        
        # Total permutations = combinations * left_permutations * right_permutations
        result = (combinations * left_permutations % MOD) * right_permutations % MOD
        return result
    
    # Initialize constants
    n = len(nums)
    MOD = 10**9 + 7
    
    # Precompute binomial coefficients using Pascal's triangle
    # binomial_coefficients[i][j] represents C(i, j) = i! / (j! * (i-j)!)
    binomial_coefficients = [[0] * n for _ in range(n)]
    binomial_coefficients[0][0] = 1
    
    for i in range(1, n):
        binomial_coefficients[i][0] = 1  # C(i, 0) = 1
        for j in range(1, i + 1):
            # Pascal's triangle formula: C(i, j) = C(i-1, j) + C(i-1, j-1)
            binomial_coefficients[i][j] = (
                binomial_coefficients[i - 1][j] + 
                binomial_coefficients[i - 1][j - 1]
            ) % MOD
    
    # Calculate total permutations and subtract 1 (excluding original arrangement)
    total_permutations = count_bst_permutations(nums)
    return (total_permutations - 1 + MOD) % MOD
    # Time: O(n²)
    # Space: O(n²)


def main():
    result = num_of_ways(nums = [2,1,3])
    print(result) # 1

    result = num_of_ways(nums = [3,4,5,1,2])
    print(result) # 5

    result = num_of_ways(nums = [1,2,3])
    print(result) # 0

if __name__ == "__main__":
    main()
