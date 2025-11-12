# ---------------------------------------------
# 1339. Maximum Product of Splitted Binary Tree
# ---------------------------------------------

# Problem: https://leetcode.com/problems/maximum-product-of-splitted-binary-tree
#
# Given the root of a binary tree, split the binary tree into two subtrees by
# removing one edge such that the product of the sums of the subtrees is
# maximized.
# 
# Return the maximum product of the sums of the two subtrees. Since the answer may
# be too large, return it modulo 10⁹ + 7.
# 
# Note that you need to maximize the answer before taking the mod and not after
# taking it.
# 
# Example 1:
# 
# https://assets.leetcode.com/uploads/2020/01/21/sample_1_1699.png
# 
# Input: root = [1,2,3,4,5,6]
# Output: 110
# 
# Explanation: Remove the red edge and get 2 binary trees with sum 11 and 10.
# Their product is 110 (11*10)
# 
# Example 2:
# 
# https://assets.leetcode.com/uploads/2020/01/21/sample_2_1699.png
# 
# Input: root = [1,null,2,3,4,null,null,5,6]
# Output: 90
# 
# Explanation: Remove the red edge and get 2 binary trees with sum 15 and 6.Their
# product is 90 (15*6)
# 
# 
# Constraints:
#         The number of nodes in the tree is in the range [2, 5 * 10⁴].
#         1 <= Node.val <= 10⁴

import sys
import os

# Add the parent directory to sys.path to import miscelaneus tools
current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)

from tree import get_tree


# Solution: https://algo.monster/liteproblems/1339
# Credit: AlgoMonster
def max_product(root):
    
    def calculate_total_sum(node):
        if node is None:
            return 0
        
        # Recursively sum current node value with left and right subtree sums
        return node.val + calculate_total_sum(node.left) + calculate_total_sum(node.right)
    
    def find_max_product(node):
        if node is None:
            return 0
        
        # Calculate the sum of the current subtree
        subtree_sum = node.val + find_max_product(node.left) + find_max_product(node.right)
        
        # Update the maximum product if we remove the edge above this node
        # One part has sum 'subtree_sum', the other has sum 'total_sum - subtree_sum'
        nonlocal max_product, total_sum
        if subtree_sum < total_sum:  # Ensure we don't count the entire tree
            max_product = max(max_product, subtree_sum * (total_sum - subtree_sum))
        
        return subtree_sum
    
    # Constants and initialization
    MOD = 10**9 + 7
    
    # First pass: calculate the total sum of all nodes
    total_sum = calculate_total_sum(root)
    
    # Initialize the maximum product
    max_product = 0
    
    # Second pass: find the maximum product by trying each edge removal
    find_max_product(root)
    
    # Return the result modulo MOD
    return max_product % MOD
    # Time: O(n)
    # Space: O(h)
    # n = the number of nodes in the binary tree
    # h = the height of the binary tree.


def main():
    root = get_tree("[1,2,3,4,5,6]")
    result = max_product(root)
    print(result) # 110

    root = get_tree("[1,null,2,3,4,null,null,5,6]")
    result = max_product(root)
    print(result) # 90

if __name__ == "__main__":
    main()
