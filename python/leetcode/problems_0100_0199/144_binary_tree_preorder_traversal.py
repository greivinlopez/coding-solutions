# -----------------------------------
# 144. Binary Tree Preorder Traversal
# -----------------------------------

# Problem: https://leetcode.com/problems/binary-tree-preorder-traversal/
# 
# Given the root of a binary tree, return the preorder traversal of its nodes' values.
#  
# Example 1:
# 
# Input: root = [1,null,2,3]
# Output: [1,2,3]
# 
# 
# Example 2:
# 
# Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]
# Output: [1,2,4,5,6,7,3,8,9]
# 
# 
# Example 3:
# 
# Input: root = []
# Output: []
# 
# 
# Example 4:
# 
# Input: root = [1]
# Output: [1]
# 
#  
# Constraints:
# 
# 	The number of nodes in the tree is in the range [0, 100].
# 	-100 <= Node.val <= 100
# 
# Follow up: Recursive solution is trivial, could you do it iteratively?

import sys
import os

# Add the parent directory to sys.path to import miscelaneus tools
current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)

from tree import get_tree, TreeNode

# Solution: https://youtu.be/afTpieEZXck
# Credit: Navdeep Singh founder of NeetCode
def preorder_traversal(root):
    cur, stack = root, []
    res = []
    while cur or stack:
        if cur:
            res.append(cur.val)
            stack.append(cur.right)
            cur = cur.left
        else:
            cur = stack.pop()
    return res


def main():
    root = get_tree("[1,null,2,3]")
    result = preorder_traversal(root)
    print(result) # [1,2,3]

    root = get_tree("[1,2,3,4,5,null,8,null,null,6,7,9]")
    result = preorder_traversal(root)
    print(result) # [1,2,4,5,6,7,3,8,9]

    result = preorder_traversal(None)
    print(result) # []

    result = preorder_traversal(TreeNode(1))
    print(result) # [1]

if __name__ == "__main__":
    main()
