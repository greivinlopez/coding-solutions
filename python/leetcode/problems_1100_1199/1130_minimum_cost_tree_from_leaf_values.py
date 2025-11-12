# ----------------------------------------
# 1130. Minimum Cost Tree From Leaf Values
# ----------------------------------------

# Problem: https://leetcode.com/problems/minimum-cost-tree-from-leaf-values
#
# Given an array arr of positive integers, consider all binary trees such that:
#         
#   * Each node has either 0 or 2 children;
#   * The values of arr correspond to the values of each leaf in an in-order
#     traversal of the tree.
#   * The value of each non-leaf node is equal to the product of the largest
#     leaf value in its left and right subtree, respectively.
# 
# Among all possible binary trees considered, return the smallest possible sum of
# the values of each non-leaf node. It is guaranteed this sum fits into a 32-bit
# integer.
# 
# A node is a leaf if and only if it has zero children.
# 
# Example 1:
# 
# https://assets.leetcode.com/uploads/2021/08/10/tree1.jpg
# 
# Input: arr = [6,2,4]
# Output: 32
# 
# Explanation: There are two possible trees shown.
# The first has a non-leaf node sum 36, and the second has non-leaf node sum 32.
# 
# Example 2:
# 
# https://assets.leetcode.com/uploads/2021/08/10/tree2.jpg
# 
# Input: arr = [4,11]
# Output: 44
# 
# Constraints:
#         2 <= arr.length <= 40
#         1 <= arr[i] <= 15
#         It is guaranteed that the answer fits into a 32-bit signed integer
# (i.e., it is less than 2³¹).


# Solution: https://algo.monster/liteproblems/1130
# Credit: AlgoMonster
def mct_from_leaf_values(arr):
    from functools import cache
    
    @cache
    def dp(left, right):
        # Base case: single leaf node
        if left == right:
            return 0, arr[left]
        
        # Initialize minimum sum and maximum value for this range
        min_sum = float('inf')
        max_value = -1
        
        # Try all possible split points
        for split_point in range(left, right):
            # Recursively solve left and right subtrees
            left_sum, left_max = dp(left, split_point)
            right_sum, right_max = dp(split_point + 1, right)
            
            # Calculate total sum for this split
            # Sum = left subtree sum + right subtree sum + product of max values
            current_sum = left_sum + right_sum + left_max * right_max
            
            # Update minimum sum and corresponding maximum value
            if min_sum > current_sum:
                min_sum = current_sum
                max_value = max(left_max, right_max)
        
        return min_sum, max_value
    
    # Return only the minimum sum (first element of tuple)
    return dp(0, len(arr) - 1)[0]
    # Time: O(n³)
    # Space: O(n²)


def main():
    result = mct_from_leaf_values(arr = [6,2,4])
    print(result) # 32

    result = mct_from_leaf_values(arr = [4,11])
    print(result) # 44

if __name__ == "__main__":
    main()
