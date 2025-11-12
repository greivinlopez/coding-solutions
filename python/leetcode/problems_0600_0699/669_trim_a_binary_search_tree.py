# ------------------------------
# 669. Trim A Binary Search Tree
# ------------------------------

# Problem: https://leetcode.com/problems/trim-a-binary-search-tree/
# 
# Given the root of a binary search tree and the lowest and highest boundaries 
# as low and high, trim the tree so that all its elements lies in [low, high]. 
# Trimming the tree should not change the relative structure of the elements 
# that will remain in the tree (i.e., any node's descendant should remain a 
# descendant). It can be proven that there is a unique answer.
# 
# Return the root of the trimmed binary search tree. Note that the root may 
# change depending on the given bounds.
# 
#  
# Example 1:
# 
# Input: root = [1,0,2], low = 1, high = 2
# Output: [1,null,2]
# 
# 
# Example 2:
# 
# Input: root = [3,0,4,null,2,null,null,1], low = 1, high = 3
# Output: [3,2,null,1]
# 
#  
# Constraints:
# 
# 	The number of nodes in the tree is in the range [1, 10^4].
# 	0 <= Node.val <= 10^4
# 	The value of each node in the tree is unique.
# 	root is guaranteed to be a valid binary search tree.
# 	0 <= low <= high <= 10^4

import sys
import os

# Add the parent directory to sys.path to import miscelaneus tools
current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)

# Import code needed for solutions
from tree import get_tree

# Solution: https://youtu.be/jwt5mTjEXGc
# Credit: Navdeep Singh founder of NeetCode
def trim_BST(root, low, high):
    if not root:
        return None

    if root.val > high:
        return trim_BST(root.left, low, high)

    if root.val < low:
        return trim_BST(root.right, low, high)

    else:
        root.left = trim_BST(root.left, low, high)
        root.right = trim_BST(root.right, low, high)
        return root


def main():
    root = get_tree("[1,0,2]")
    result = trim_BST(root, 1, 2)
    print(result) # [1, None, 2]

    root = get_tree("[3,0,4,null,2,null,null,1]")
    result = trim_BST(root, 1, 3)
    print(result) # [3, 2, None, 1]

if __name__ == "__main__":
    main()
