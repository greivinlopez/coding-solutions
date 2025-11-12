# -----------------------
# 872. Leaf-Similar Trees
# -----------------------

# Problem: https://leetcode.com/problems/leaf-similar-trees
#
# Consider all the leaves of a binary tree, from left to right order, the values
# of those leaves form a leaf value sequence.
# 
# https://s3-lc-upload.s3.amazonaws.com/uploads/2018/07/16/tree.png
# 
# For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).
# 
# Two binary trees are considered leaf-similar if their leaf value sequence is the
# same.
# 
# Return true if and only if the two given trees with head nodes root1 and root2
# are leaf-similar.
# 
# Example 1:
# 
# https://assets.leetcode.com/uploads/2020/09/03/leaf-similar-1.jpg
# 
# Input: root1 = [3,5,1,6,2,9,8,null,null,7,4], root2 =
# [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]
# Output: true
# 
# Example 2:
# 
# https://assets.leetcode.com/uploads/2020/09/03/leaf-similar-2.jpg
# 
# Input: root1 = [1,2,3], root2 = [1,3,2]
# Output: false
# 
# 
# Constraints:
#         The number of nodes in each tree will be in the range [1, 200].
#         Both of the given trees will have values in the range [0, 200].

import sys
import os

# Add the parent directory to sys.path to import miscelaneus tools
current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)

# Import code needed for solutions
from tree import get_tree

# Solution: https://youtu.be/Nr8dbnL0_cM
# Credit: Navdeep Singh founder of NeetCode
def leaf_similar(root1, root2):
    def dfs(root, leaf):
        if not root:
            return

        if not root.left and not root.right:
            leaf.append(root.val)
            return

        dfs(root.left, leaf)
        dfs(root.right, leaf)

    leaf1, leaf2 = [], []
    dfs(root1, leaf1)
    dfs(root2, leaf2)
    return leaf1 == leaf2
    # Time: O(n1 + n2)   n1, n2 = number of nodes of root1 and root2
    # Space: O(n1 + n2)


def main():
    r1 = get_tree("[3,5,1,6,2,9,8,null,null,7,4]")
    r2 = get_tree("[3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]")
    result = leaf_similar(r1, r2)
    print(result) # True

    r1 = get_tree("[1,2,3]")
    r2 = get_tree("[1,3,2]")
    result = leaf_similar(r1, r2)
    print(result) # False

if __name__ == "__main__":
    main()
