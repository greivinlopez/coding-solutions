# ---------------------------------
# 94. Binary Tree Inorder Traversal
# ---------------------------------

# Problem: https://leetcode.com/problems/binary-tree-inorder-traversal/description/
# 
# Given the root of a binary tree, return the inorder traversal of its nodes' values.
# 
# Example 1:
# 
# Input: root = [1,null,2,3]
# Output: [1,3,2]
# 
# Example 2:
# 
# Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]
# Output: [4,2,6,5,7,1,3,9,8]
# 
# Example 3:
# 
# Input: root = []
# Output: []
# 
# Example 4:
# 
# Input: root = [1]
# Output: [1]
# 
# 
# Constraints:
# 
#   The number of nodes in the tree is in the range [0, 100].
#   -100 <= Node.val <= 100

import sys
import os

# Add the parent directory to sys.path to import miscelaneus tools
current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)

# Import code needed for solutions
from tree import get_tree

# Solution: https://youtu.be/g_S5WuasWUE
# Credit: Navdeep Singh founder of NeetCode
def inorder_traversal(root):
    # Iterative
    res, stack = [], []
    cur = root

    while cur or stack:
        while cur:
            stack.append(cur)
            cur = cur.left
        cur = stack.pop()
        res.append(cur.val)
        cur = cur.right
    return res
    # Time: O(n)
    # Space: O(n)

def inorder_traversal_rec(root):
    # Recursive
    res = []

    def helper(root):
        if not root:
            return
        helper(root.left)
        res.append(root.val)
        helper(root.right)

    helper(root)
    return res
    # Time: O(n)
    # Space: O(n)


def main():
    root = get_tree("[1,null,2,3]")
    result = inorder_traversal(root)
    print(result) # [1,3,2]

    root = get_tree("[1,2,3,4,5,null,8,null,null,6,7,9]")
    result = inorder_traversal(root)
    print(result) # [4,2,6,5,7,1,3,9,8]

    root = get_tree("[]")
    result = inorder_traversal(root)
    print(result) # []

    root = get_tree("[1]")
    result = inorder_traversal(root)
    print(result) # [1]


if __name__ == "__main__":
    main()