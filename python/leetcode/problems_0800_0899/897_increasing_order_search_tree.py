# ---------------------------------
# 897. Increasing Order Search Tree
# ---------------------------------

# Problem: https://leetcode.com/problems/increasing-order-search-tree
#
# Given the root of a binary search tree, rearrange the tree in in-order so that
# the leftmost node in the tree is now the root of the tree, and every node has no
# left child and only one right child.
# 
# Example 1:
# 
# https://assets.leetcode.com/uploads/2020/11/17/ex1.jpg
# 
# Input: root = [5,3,6,2,4,null,8,1,null,null,null,7,9]
# Output: [1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]
# 
# Example 2:
# 
# https://assets.leetcode.com/uploads/2020/11/17/ex2.jpg
# 
# Input: root = [5,1,7]
# Output: [1,null,5,null,7]
# 
# 
# Constraints:
#         The number of nodes in the given tree will be in the range [1, 100].
#         0 <= Node.val <= 1000

import sys
import os

# Add the parent directory to sys.path to import miscelaneus tools
current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)

from tree import get_tree, TreeNode

# Solution: https://algo.monster/liteproblems/897
# Credit: AlgoMonster
def increasing_BST(root):
    
    def inorder_traverse(node):
        # Base case: if node is None, return
        if node is None:
            return
        
        # Use nonlocal to modify the prev variable from outer scope
        nonlocal prev
        
        # Process left subtree first (in-order traversal)
        inorder_traverse(node.left)
        
        # Connect previous node's right pointer to current node
        prev.right = node
        # Remove left pointer of current node (no left children in result)
        node.left = None
        # Update prev to current node for next iteration
        prev = node
        
        # Process right subtree
        inorder_traverse(node.right)
    
    # Create a dummy node to simplify edge cases
    # prev will track the last processed node during traversal
    dummy = prev = TreeNode(right=root)
    
    # Perform the in-order traversal and rearrangement
    inorder_traverse(root)
    
    # Return the actual root (skip dummy node)
    return dummy.right
    # Time: O(n)
    # Space: O(n)


def main():
    root = get_tree("[5,3,6,2,4,null,8,1,null,null,null,7,9]")
    result = increasing_BST(root)
    print(result) # [1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9]

    root = get_tree("[5,1,7]")
    result = increasing_BST(root)
    print(result) # [1, None, 5, None, 7]

if __name__ == "__main__":
    main()
