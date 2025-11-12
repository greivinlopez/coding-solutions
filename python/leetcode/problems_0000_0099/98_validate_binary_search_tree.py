# --------------------------------
# 98. Validate Binary Search Tree
# --------------------------------

# Problem: https://leetcode.com/problems/validate-binary-search-tree/
# 
# Given the root of a binary tree, determine if it is a valid binary search tree (BST).
# 
# A valid BST is defined as follows:
# 
# - The left subtree of a node contains only nodes with keys strictly less than the node's key.
# - The right subtree of a node contains only nodes with keys strictly greater than the node's key.
# - Both the left and right subtrees must also be binary search trees.

import sys
import os

# Add the parent directory to sys.path to import miscelaneus tools
current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)

from tree import get_tree

# Solution: https://youtu.be/s6ATEkipzow
# Credit: Navdeep Singh founder of NeetCode
def is_valid_BST(root):
    def valid(node, left, right):
        if not node:
            return True
        if not (left < node.val < right):
            return False

        return valid(node.left, left, node.val) and valid(
            node.right, node.val, right
        )

    return valid(root, float("-inf"), float("inf"))
    # Time: O(n)
    # Space: O(h) 
    # h = height of tree

# Solution: https://youtu.be/nTXuWuqIka4
# Credit: Greg Hogg
def is_valid_BST(root):
    stk = [(root, float('-inf'), float('inf'))]

    while stk:
        node, minn, maxx = stk.pop()

        if node.val <= minn or node.val >= maxx:
            return False
        else:
            if node.left:
                stk.append((node.left, minn, node.val))
            
            if node.right:
                stk.append((node.right, node.val, maxx))
    
    return True
    # Time: O(n)
    # Space: O(h) 
    # h = height of tree


def main():
    root = get_tree("[2,1,3]")
    result = is_valid_BST(root)
    print(result) # True

    root = get_tree("[5,1,4,null,null,3,6]")
    result = is_valid_BST(root)
    print(result) # False

if __name__ == "__main__":
    main()