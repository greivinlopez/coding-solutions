# -----------------------------------
# 700. Search in a Binary Search Tree
# -----------------------------------

# Problem: https://leetcode.com/problems/search-in-a-binary-search-tree
#
# You are given the root of a binary search tree (BST) and an integer val.
# 
# Find the node in the BST that the node's value equals val and return the subtree
# rooted with that node. If such a node does not exist, return null.
# 
# Example 1:
# 
# https://assets.leetcode.com/uploads/2021/01/12/tree1.jpg
# 
# Input: root = [4,2,7,1,3], val = 2
# Output: [2,1,3]
# 
# Example 2:
# 
# https://assets.leetcode.com/uploads/2021/01/12/tree2.jpg
# 
# Input: root = [4,2,7,1,3], val = 5
# Output: []
# 
# 
# Constraints:
#         The number of nodes in the tree is in the range [1, 5000].
#         1 <= Node.val <= 10⁷
#         root is a binary search tree.
#         1 <= val <= 10⁷

import sys
import os

# Add the parent directory to sys.path to import miscelaneus tools
current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)

from tree import get_tree

# Solution: https://algo.monster/liteproblems/700
# Credit: AlgoMonster
def search_BST(root, val):
    # Base case: if root is None or we found the target value
    if root is None or root.val == val:
        return root
    
    # BST property: if target is less than current node, search left subtree
    if root.val > val:
        return search_BST(root.left, val)
    # Otherwise, target is greater than current node, search right subtree
    else:
        return search_BST(root.right, val)
    # Time: O(h)
    # Space: O(h)
    # h = the height of the tree.


def main():
    root = get_tree("[4,2,7,1,3]")
    result = search_BST(root, 2)
    print(result) # [2,1,3]

    root = get_tree("[4,2,7,1,3]")
    result = search_BST(root, 5)
    print(result) # []

if __name__ == "__main__":
    main()
