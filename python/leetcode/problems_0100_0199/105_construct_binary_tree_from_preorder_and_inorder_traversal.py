# -----------------------------------------------------------------
# 105. Construct Binary Tree from Preorder and Inorder Traversal 🌲
# -----------------------------------------------------------------

# Problem: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
# 
# Given two integer arrays preorder and inorder where preorder is the preorder 
# traversal of a binary tree and inorder is the inorder traversal of the same 
# tree, construct and return the binary tree.

import sys
import os

# Add the parent directory to sys.path to import miscelaneus tools
current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)

from tree import TreeNode

# Helper function
def is_same_tree(p, q):
    if not p and not q:
        return True
    if p and q and p.val == q.val:
        return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)
    else:
        return False

# Solution: https://youtu.be/ihj4IQGZ2zc
# Credit: Navdeep Singh founder of NeetCode
def build_tree(preorder, inorder):
    if not preorder or not inorder:
        return None

    root = TreeNode(preorder[0])
    mid = inorder.index(preorder[0])
    root.left = build_tree(preorder[1 : mid + 1], inorder[:mid])
    root.right = build_tree(preorder[mid + 1 :], inorder[mid + 1 :])
    return root


def main():
    result = build_tree(preorder = [3,9,20,15,7], inorder = [9,3,15,20,7])
    print(result) # [3, 9, 20, None, None, 15, 7]

    result = build_tree(preorder = [-1], inorder = [-1])
    print(result) # [-1]

if __name__ == "__main__":
    main()