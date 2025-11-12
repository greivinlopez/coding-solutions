# ------------------------------------
# 124. Binary Tree Maximum Path Sum 🌲
# ------------------------------------

# Problem: https://leetcode.com/problems/binary-tree-maximum-path-sum/
# 
# A path in a binary tree is a sequence of nodes where each pair of adjacent 
# nodes in the sequence has an edge connecting them. A node can only appear 
# in the sequence at most once. Note that the path does not need to pass 
# through the root.
# 
# The path sum of a path is the sum of the node's values in the path.
# 
# Given the root of a binary tree, return the maximum path sum of any 
# non-empty path.

import sys
import os

# Add the parent directory to sys.path to import miscelaneus tools
current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)

from tree import get_tree

# Solution: https://youtu.be/LSKQyOz_P8I
# Credit: Navdeep Singh founder of NeetCode
def max_path_sum(root):
    res = [root.val]

    # return max path sum without split
    def dfs(root):
        if not root:
            return 0

        leftMax = dfs(root.left)
        rightMax = dfs(root.right)
        leftMax = max(leftMax, 0)
        rightMax = max(rightMax, 0)

        # compute max path sum WITH split
        res[0] = max(res[0], root.val + leftMax + rightMax)
        return root.val + max(leftMax, rightMax)

    dfs(root)
    return res[0]


def main():
    root = get_tree("[1,2,3]")
    result = max_path_sum(root)
    print(result) # 6

    root = get_tree("[-10,9,20,null,null,15,7]")
    result = max_path_sum(root)
    print(result) # 42

if __name__ == "__main__":
    main()