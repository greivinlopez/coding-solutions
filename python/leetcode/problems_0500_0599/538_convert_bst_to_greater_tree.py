# --------------------------------
# 538. Convert BST to Greater Tree
# --------------------------------

# Problem: https://leetcode.com/problems/convert-bst-to-greater-tree
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
#         The number of nodes in the tree is in the range [0, 10^4].
#         -10^4 <= Node.val <= 10^4
#         All the values in the tree are unique.
#         root is guaranteed to be a valid binary search tree.
# 
# Note: This question is the same as 1038: https://leetcode.com/problems/binary-
# search-tree-to-greater-sum-tree/

import sys
import os

# Add the parent directory to sys.path to import miscelaneus tools
current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)

# Import code needed for solutions
from tree import get_tree

# Solution: https://youtu.be/7vVEJwVvAlI
# Credit: Navdeep Singh founder of NeetCode
def convert_bst(root):
    cur_sum = 0
    
    def dfs(node):
        nonlocal cur_sum
        if not node:
            return

        dfs(node.right)
        tmp = node.val
        node.val += cur_sum
        cur_sum += tmp
        dfs(node.left)

    dfs(root)
    return root
    # Time: O(n)
    # Space: O(h)

def main():
    root = get_tree("[4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]")
    result = convert_bst(root)
    print(result) # [30, 36, 21, 36, 35, 26, 15, None, None, None, 33, None, None, None, 8]

    root = get_tree("[0,null,1]")
    result = convert_bst(root)
    print(result) # [1, None, 1]

if __name__ == "__main__":
    main()
