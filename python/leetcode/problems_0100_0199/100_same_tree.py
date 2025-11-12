# -----------------------
# 100. Same Tree 🌳 ? 🌲
# -----------------------

# Problem: https://leetcode.com/problems/same-tree
# 
# Given the roots of two binary trees p and q, write a function to check if 
# they are the same or not.
# 
# Two binary trees are considered the same if they are structurally identical, 
# and the nodes have the same value.

import sys
import os

# Add the parent directory to sys.path to import miscelaneus tools
current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)

# Import code needed for solutions
from tree import TreeNode

# Solution: https://youtu.be/vRbbcKXCxOw
# Credit: Navdeep Singh founder of NeetCode
def is_same_tree(p, q):
    # Time: O(n + m)
    # Space: O(n + m)
    # m is number of nodes in p, n is number of nodes in Q.
    if not p and not q:
        return True
    if p and q and p.val == q.val:
        return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)
    else:
        return False
    
# Same Solution Different Video: https://youtu.be/jK6XXYezw2g
# Credit: Greg Hogg

def example_1():
    # Initialize and allocate memory for tree nodes
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)

    # Connect binary tree nodes
    a.left = b
    a.right = c

    # Initialize and allocate memory for tree nodes
    d = TreeNode(1)
    e = TreeNode(2)
    f = TreeNode(3)

    # Connect binary tree nodes
    d.left =e
    d.right = f

    return a, d

def example_2():
    # Initialize and allocate memory for tree nodes
    a = TreeNode(1)
    b = TreeNode(2)

    # Connect binary tree nodes
    a.left = b

    # Initialize and allocate memory for tree nodes
    c = TreeNode(1)
    d = TreeNode(2)

    # Connect binary tree nodes
    c.right = d

    return a, c

def main():
    p, q = example_1()
    result = is_same_tree(p, q)
    print(result) # True

    p, q = example_2()
    result = is_same_tree(p, q)
    print(result) # False

if __name__ == "__main__":
    main()