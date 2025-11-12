# --------------------------------------------
# 1038. Binary Search Tree to Greater Sum Tree
# --------------------------------------------

# Problem: https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree
#
# Given the root of a Binary Search Tree (BST), convert it to a Greater Tree such
# that every key of the original BST is changed to the original key plus the sum
# of all keys greater than the original key in BST.
# 
# As a reminder, a binary search tree is a tree that satisfies these constraints:
#         
#   * The left subtree of a node contains only nodes with keys less than the
#     node's key.
#   * The right subtree of a node contains only nodes with keys greater than
#     the node's key.
#   * Both the left and right subtrees must also be binary search trees.
# 
# Example 1:
# 
# https://assets.leetcode.com/uploads/2019/05/02/tree.png
# 
# Input: root = [4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
# Output: [30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]
# 
# Example 2:
# 
# Input: root = [0,null,1]
# Output: [1,null,1]
# 
# 
# Constraints:
#         The number of nodes in the tree is in the range [1, 100].
#         0 <= Node.val <= 100
#         All the values in the tree are unique.
# 
# Note: This question is the same as 538: 
# https://leetcode.com/problems/convert-bst-to-greater-tree/

import sys
import os

# Add the parent directory to sys.path to import miscelaneus tools
current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)

from tree import get_tree

# Solution: https://algo.monster/liteproblems/1038
# Credit: AlgoMonster
def bst_to_gst(root):

    def reverse_inorder_traversal(node):
        # Base case: if node is None, return
        if node is None:
            return
        
        # First, traverse the right subtree (larger values in BST)
        reverse_inorder_traversal(node.right)
        
        # Process current node: add its value to running sum
        nonlocal running_sum
        running_sum += node.val
        
        # Update current node's value to the accumulated sum
        node.val = running_sum
        
        # Finally, traverse the left subtree (smaller values in BST)
        reverse_inorder_traversal(node.left)
    
    # Initialize running sum to track cumulative sum of visited nodes
    running_sum = 0
    
    # Start the reverse in-order traversal from root
    reverse_inorder_traversal(root)
    
    # Return the modified tree
    return root
    # Time: O(n)
    # Space: O(n)


def main():
    root = get_tree("[4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]")
    result = bst_to_gst(root)
    print(result) # [30, 36, 21, 36, 35, 26, 15, None, None, None, 33, None, None, None, 8]

    root = get_tree("[0,null,1]")
    result = bst_to_gst(root)
    print(result) # [1, None, 1]

if __name__ == "__main__":
    main()
