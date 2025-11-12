# ----------------------------------------------------------------
# 889. Construct Binary Tree from Preorder and Postorder Traversal
# ----------------------------------------------------------------

# Problem: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal
#
# Given two integer arrays, preorder and postorder where preorder is the preorder
# traversal of a binary tree of distinct values and postorder is the postorder
# traversal of the same tree, reconstruct and return the binary tree.
# 
# If there exist multiple answers, you can return any of them.
# 
# Example 1:
# 
# https://assets.leetcode.com/uploads/2021/07/24/lc-prepost.jpg
# 
# Input: preorder = [1,2,4,5,3,6,7], postorder = [4,5,2,6,7,3,1]
# Output: [1,2,3,4,5,6,7]
# 
# Example 2:
# 
# Input: preorder = [1], postorder = [1]
# Output: [1]
# 
# 
# Constraints:
#         1 <= preorder.length <= 30
#         1 <= preorder[i] <= preorder.length
#         All the values of preorder are unique.
#         postorder.length == preorder.length
#         1 <= postorder[i] <= postorder.length
#         All the values of postorder are unique.
#         It is guaranteed that preorder and postorder are the preorder traversal
# and postorder traversal of the same binary tree.

import sys
import os

# Add the parent directory to sys.path to import miscelaneus tools
current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)

from tree import TreeNode

# Solution: https://youtu.be/H1nBu3L-2gQ
# Credit: Navdeep Singh founder of NeetCode
def construct_from_pre_post(preorder, postorder):
    N = len(postorder)
    post_val_to_idx = {}
    for i, n in enumerate(postorder):
        post_val_to_idx[n] = i

    def build(i1, i2, j1):
        if i1 > i2:
            return None
        
        root = TreeNode(preorder[i1])
        if i1 != i2:
            left_val = preorder[i1 + 1]
            mid = post_val_to_idx[left_val]
            left_size = mid - j1 + 1
            root.left = build(i1 + 1, i1 + left_size, j1)
            root.right = build(i1 + left_size + 1, i2, mid + 1)
        
        return root

    return build(0, N - 1, 0)

# Time: O(n) 
# Space: O(n)


def main():
    result = construct_from_pre_post(preorder = [1,2,4,5,3,6,7], postorder = [4,5,2,6,7,3,1])
    print(result) # [1, 2, 3, 4, 5, 6, 7]

    result = construct_from_pre_post(preorder = [1], postorder = [1])
    print(result) # [1]

if __name__ == "__main__":
    main()
