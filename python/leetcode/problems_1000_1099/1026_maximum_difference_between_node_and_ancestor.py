# --------------------------------------------------
# 1026. Maximum Difference Between Node and Ancestor
# --------------------------------------------------

# Problem: https://leetcode.com/problems/maximum-difference-between-node-and-ancestor
#
# Given the root of a binary tree, find the maximum value v for which there exist
# different nodes a and b where v = |a.val - b.val| and a is an ancestor of b.
# 
# A node a is an ancestor of b if either: any child of a is equal to b or any
# child of a is an ancestor of b.
# 
# Example 1:
# 
# https://assets.leetcode.com/uploads/2020/11/09/tmp-tree.jpg
# 
# Input: root = [8,3,10,1,6,null,14,null,null,4,7,13]
# Output: 7
# 
# Explanation: We have various ancestor-node differences, some of which are given
# below :
# |8 - 3| = 5
# |3 - 7| = 4
# |8 - 1| = 7
# |10 - 13| = 3
# Among all possible differences, the maximum value of 7 is obtained by |8 - 1| =
# 7.
# 
# Example 2:
# 
# https://assets.leetcode.com/uploads/2020/11/09/tmp-tree-1.jpg
# 
# Input: root = [1,null,2,null,0,3]
# Output: 3
# 
# 
# Constraints:
#         The number of nodes in the tree is in the range [2, 5000].
#         0 <= Node.val <= 10⁵

import sys
import os

# Add the parent directory to sys.path to import miscelaneus tools
current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)

from tree import get_tree

# Credit: Jeel Gajera -> https://github.com/JeelGajera
def max_ancestor_diff(root):
    max_diff = 0
    def traversTree(root, low, high):
        nonlocal max_diff
        if root:
            max_diff = max(max_diff, abs(root.val - low), abs(root.val - high))
            l, h = min(root.val, low), max(root.val, high)
            traversTree(root.left,l,h)
            traversTree(root.right,l,h)

    traversTree(root, root.val, root.val)
    return max_diff
    # Time: O(n)
    # Space: O(h)
    # n = the number of nodes
    # h = the height of the tree


def main():
    root = get_tree("[8,3,10,1,6,null,14,null,null,4,7,13]")
    result = max_ancestor_diff(root)
    print(result) # 7

    root = get_tree("[1,null,2,null,0,3]")
    result = max_ancestor_diff(root)
    print(result) # 3

if __name__ == "__main__":
    main()
