# ---------------------------
# 998. Maximum Binary Tree II
# ---------------------------

# Problem: https://leetcode.com/problems/maximum-binary-tree-ii
#
# A maximum tree is a tree where every node has a value greater than any other
# value in its subtree.
# 
# You are given the root of a maximum binary tree and an integer val.
# 
# Just as in the previous problem, the given tree was constructed from a list a
# (root = Construct(a)) recursively with the following Construct(a) routine:
#         
#   * If a is empty, return null.
#   * Otherwise, let a[i] be the largest element of a. Create a root node with
#     the value a[i].
#   * The left child of root will be Construct([a[0], a[1], ..., a[i - 1]]).
#   * The right child of root will be Construct([a[i + 1], a[i + 2], ...,
#     a[a.length - 1]]).
#   * Return root.
# 
# Note that we were not given a directly, only a root node root = Construct(a).
# 
# Suppose b is a copy of a with the value val appended to it. It is guaranteed
# that b has unique values.
# 
# Return Construct(b).
# 
# Example 1:
# 
# https://assets.leetcode.com/uploads/2021/08/09/maxtree1.JPG
# 
# Input: root = [4,1,3,null,null,2], val = 5
# Output: [5,4,null,1,3,null,null,2]
# 
# Explanation: a = [1,4,2,3], b = [1,4,2,3,5]
# 
# Example 2:
# 
# https://assets.leetcode.com/uploads/2021/08/09/maxtree21.JPG
# 
# Input: root = [5,2,4,null,1], val = 3
# Output: [5,2,4,null,1,null,3]
# 
# Explanation: a = [2,1,5,4], b = [2,1,5,4,3]
# 
# Example 3:
# 
# https://assets.leetcode.com/uploads/2021/08/09/maxtree3.JPG
# 
# Input: root = [5,2,3,null,1], val = 4
# Output: [5,2,4,null,1,3]
# 
# Explanation: a = [2,1,5,3], b = [2,1,5,3,4]
# 
# 
# Constraints:
#         The number of nodes in the tree is in the range [1, 100].
#         1 <= Node.val <= 100
#         All the values of the tree are unique.
#         1 <= val <= 100

import sys
import os

# Add the parent directory to sys.path to import miscelaneus tools
current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)

from tree import get_tree, TreeNode

# Solution: https://algo.monster/liteproblems/998
# Credit: AlgoMonster
def insert_into_max_tree(root, val):
    # Case 1: Empty tree or new value is greater than root
    # The new value becomes the new root with the old tree as its left child
    if root is None or root.val < val:
        return TreeNode(val, root)
    
    # Case 2: New value is smaller than root
    # Since the value is appended to the end of the array,
    # it must go to the right subtree
    root.right = insert_into_max_tree(root.right, val)
    
    return root
    # Time: O(n)
    # Space: O(n)


def main():
    root = get_tree("[4,1,3,null,null,2]")
    result = insert_into_max_tree(root, 5)
    print(result) # [5, 4, None, 1, 3, None, None, 2]

    root = get_tree("[5,2,4,null,1]")
    result = insert_into_max_tree(root, 3)
    print(result) # [5, 2, 4, None, 1, None, 3]

    root = get_tree("[5,2,3,null,1]")
    result = insert_into_max_tree(root, 4)
    print(result) # [5, 2, 4, None, 1, 3]

if __name__ == "__main__":
    main()
