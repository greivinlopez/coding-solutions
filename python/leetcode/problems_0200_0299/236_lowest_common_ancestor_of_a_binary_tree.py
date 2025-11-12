# --------------------------------------------
# 236. Lowest Common Ancestor Of A Binary Tree
# --------------------------------------------

# Problem: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
# 
# Given a binary tree, find the lowest common ancestor (LCA) of two given nodes 
# in the tree.
# 
# According to the definition of LCA on Wikipedia: “The lowest common ancestor 
# is defined between two nodes p and q as the lowest node in T that has both p 
# and q as descendants (where we allow a node to be a descendant of itself).”
# 
#  
# Example 1:
# 
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
# Output: 3
# Explanation: The LCA of nodes 5 and 1 is 3.
# 
# 
# Example 2:
# 
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
# Output: 5
# Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.
# 
# 
# Example 3:
# 
# Input: root = [1,2], p = 1, q = 2
# Output: 1
# 
# 
# Constraints:
# 
# 	The number of nodes in the tree is in the range [2, 105].
# 	-109 <= Node.val <= 109
# 	All Node.val are unique.
# 	p != q
# 	p and q will exist in the tree.

import sys
import os

# Add the parent directory to sys.path to import miscelaneus tools
current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)

from tree import TreeNode

# Solution: Could not found the video
# Credit: Navdeep Singh founder of NeetCode
def lowest_common_ancestor(root, p, q):
    if not root:
        return
    if root == p or root == q:
        return root

    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)

    if left and right:
        return root

    if left:
        return left
    if right:
        return right

    return None

def example_1():
    # Initialize and allocate memory for tree nodes
    a = TreeNode(3)
    b = TreeNode(5)
    c = TreeNode(1)
    d = TreeNode(6)
    e = TreeNode(2)
    f = TreeNode(0)
    g = TreeNode(8)
    h = TreeNode(7)
    i = TreeNode(4)

    # Connect binary tree nodes
    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.left = f
    c.right = g
    e.left = h
    e.right = i

    return a, b, c

def example_2():
    # Initialize and allocate memory for tree nodes
    a = TreeNode(3)
    b = TreeNode(5)
    c = TreeNode(1)
    d = TreeNode(6)
    e = TreeNode(2)
    f = TreeNode(0)
    g = TreeNode(8)
    h = TreeNode(7)
    i = TreeNode(4)

    # Connect binary tree nodes
    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.left = f
    c.right = g
    e.left = h
    e.right = i

    return a, b, i

def main():
    root, p, q = example_1()
    result = lowest_common_ancestor(root, p, q)
    print(result.val) # 3

    root, p, q = example_2()
    result = lowest_common_ancestor(root, p, q)
    print(result.val) # 5

if __name__ == "__main__":
    main()
