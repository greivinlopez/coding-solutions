# ---------------------------------------
# 1373. Maximum Sum BST in Binary Tree 🌲
# ---------------------------------------

# Problem: https://leetcode.com/problems/maximum-sum-bst-in-binary-tree
#
# Given a binary tree root, return the maximum sum of all keys of any sub-tree
# which is also a Binary Search Tree (BST).
# 
# Assume a BST is defined as follows:
#         
#   * The left subtree of a node contains only nodes with keys less than the node's key.
#   * The right subtree of a node contains only nodes with keys greater than the node's key.
#   * Both the left and right subtrees must also be binary search trees.
# 
# Example 1:
# 
# https://assets.leetcode.com/uploads/2020/01/30/sample_1_1709.png
# 
# Input: root = [1,4,3,2,4,2,5,null,null,null,null,null,null,4,6]
# Output: 20
# 
# Explanation: Maximum sum in a valid Binary search tree is obtained in root node
# with key equal to 3.
# 
# Example 2:
# 
# https://assets.leetcode.com/uploads/2020/01/30/sample_2_1709.png
# 
# Input: root = [4,3,null,1,2]
# Output: 2
# 
# Explanation: Maximum sum in a valid Binary search tree is obtained in a single
# root node with key equal to 2.
# 
# Example 3:
# 
# Input: root = [-4,-2,-5]
# Output: 0
# 
# Explanation: All values are negatives. Return an empty BST.
# 
# 
# Constraints:
#         The number of nodes in the tree is in the range [1, 4 * 10⁴].
#         -4 * 10⁴ <= Node.val <= 4 * 10⁴

import sys
import os

# Add the parent directory to sys.path to import miscelaneus tools
current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)

from tree import get_tree

# Solution: https://algo.monster/liteproblems/1373
# Credit: AlgoMonster
def max_sum_BST(root):

    def dfs(node) -> tuple[int, int, int, int]:
        """
        Perform DFS to check if subtree is BST and calculate sum.
        
        Args:
            node: Current node being processed
            
        Returns:
            Tuple of (is_bst, min_value, max_value, sum_of_subtree)
            - is_bst: 1 if subtree is valid BST, 0 otherwise
            - min_value: Minimum value in the subtree
            - max_value: Maximum value in the subtree
            - sum_of_subtree: Sum of all nodes in the subtree
        """
        # Base case: empty node is a valid BST
        if node is None:
            return 1, float('inf'), float('-inf'), 0
        
        # Recursively process left and right subtrees
        left_is_bst, left_min, left_max, left_sum = dfs(node.left)
        right_is_bst, right_min, right_max, right_sum = dfs(node.right)
        
        # Check if current subtree forms a valid BST
        # Conditions: both subtrees are BSTs and current node value is in valid range
        if left_is_bst and right_is_bst and left_max < node.val < right_min:
            # Calculate sum of current BST subtree
            current_sum = left_sum + right_sum + node.val
            
            # Update global maximum sum
            nonlocal max_sum
            max_sum = max(max_sum, current_sum)
            
            # Return BST properties for current subtree
            return (1, 
                    min(left_min, node.val),  # Minimum value in subtree
                    max(right_max, node.val),  # Maximum value in subtree
                    current_sum)               # Sum of subtree
        
        # Current subtree is not a valid BST
        return 0, 0, 0, 0
    
    # Initialize maximum sum to 0 (empty BST has sum 0)
    max_sum = 0
    
    # Start DFS traversal from root
    dfs(root)
    
    return max_sum
    # Time: O(n)
    # Space: O(n)


def main():
    root = get_tree("[1,4,3,2,4,2,5,null,null,null,null,null,null,4,6]")
    result = max_sum_BST(root)
    print(result) # 20

    root = get_tree("[4,3,null,1,2]")
    result = max_sum_BST(root)
    print(result) # 2

    root = get_tree("[-4,-2,-5]")
    result = max_sum_BST(root)
    print(result) # 0

if __name__ == "__main__":
    main()
