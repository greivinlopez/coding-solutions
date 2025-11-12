# ------------------------
# 623. Add One Row to Tree
# ------------------------

# Problem: https://leetcode.com/problems/add-one-row-to-tree
#
# Given the root of a binary tree and two integers val and depth, add a row of
# nodes with value val at the given depth depth.
# 
# Note that the root node is at depth 1.
# 
# The adding rule is:
#         
#   * Given the integer depth, for each not null tree node cur at the depth
#     depth - 1, create two tree nodes with value val as cur's left subtree root and
#     right subtree root.
#   * cur's original left subtree should be the left subtree of the new left subtree root.
#   * cur's original right subtree should be the right subtree of the new right subtree root.
#   * If depth == 1 that means there is no depth depth - 1 at all, then create
#     a tree node with value val as the new root of the whole original tree, and the
#     original tree is the new root's left subtree.
# 
# Example 1:
# 
# https://assets.leetcode.com/uploads/2021/03/15/addrow-tree.jpg
# 
# Input: root = [4,2,6,3,1,5], val = 1, depth = 2
# Output: [4,1,1,2,null,null,6,3,1,5]
# 
# Example 2:
# 
# https://assets.leetcode.com/uploads/2021/03/11/add2-tree.jpg
# 
# Input: root = [4,2,null,3,1], val = 1, depth = 3
# Output: [4,2,null,1,1,3,null,null,1]
# 
# 
# Constraints:
#         The number of nodes in the tree is in the range [1, 10⁴].
#         The depth of the tree is in the range [1, 10⁴].
#         -100 <= Node.val <= 100
#         -10⁵ <= val <= 10⁵
#         1 <= depth <= the depth of tree + 1

import sys
import os

# Add the parent directory to sys.path to import miscelaneus tools
current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)

from tree import get_tree, TreeNode

# Credit: Jaweria Batool -> https://github.com/Jaweria-B
def add_one_row(root, val, depth):

    def add(root, val, depth, curr):
        if not root:
            return None

        if curr == depth - 1:
            lTemp = root.left
            rTemp = root.right

            root.left = TreeNode(val)
            root.right = TreeNode(val)
            root.left.left = lTemp
            root.right.right = rTemp

            return root

        root.left = add(root.left, val, depth, curr + 1)
        root.right = add(root.right, val, depth, curr + 1)

        return root

    if depth == 1:
        newRoot = TreeNode(val)
        newRoot.left = root
        return newRoot

    return add(root, val, depth, 1)
    # Time: O(n)
    # Space: O(d)
    # n = the total number of nodes
    # d = the specified depth


def main():
    root = get_tree("[4,2,6,3,1,5]")
    result = add_one_row(root, 1, 2)
    print(result) # [4, 1, 1, 2, None, None, 6, 3, 1, 5]

    root = get_tree("[4,2,null,3,1]")
    result = add_one_row(root, 1, 3)
    print(result) # [4, 2, None, 1, 1, 3, None, None, 1]

if __name__ == "__main__":
    main()
