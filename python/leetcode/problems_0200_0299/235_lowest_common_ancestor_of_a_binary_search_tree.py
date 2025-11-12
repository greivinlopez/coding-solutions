# ---------------------------------------------------
# 235. Lowest Common Ancestor Of A Binary Search Tree
# ---------------------------------------------------

# Problem: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
# 
# Given a binary search tree (BST), find the lowest common ancestor (LCA) node 
# of two given nodes in the BST.
# 
# According to the definition of LCA on Wikipedia: “The lowest common ancestor 
# is defined between two nodes p and q as the lowest node in T that has both p
# and q as descendants (where we allow a node to be a descendant of itself).”
# 
#  
# Example 1:
# 
# Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
# Output: 6
# Explanation: The LCA of nodes 2 and 8 is 6.
# 
# 
# Example 2:
# 
# Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
# Output: 2
# Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.
# 
# 
# Example 3:
# 
# Input: root = [2,1], p = 2, q = 1
# Output: 2
# 
# 
# Constraints:
# 
# 	The number of nodes in the tree is in the range [2, 105].
# 	-109 <= Node.val <= 109
# 	All Node.val are unique.
# 	p != q
# 	p and q will exist in the BST.

import sys
import os

# Add the parent directory to sys.path to import miscelaneus tools
current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)

from tree import TreeNode

# Solution: https://youtu.be/gs2LMfuOR9k
# Credit: Navdeep Singh founder of NeetCode
def lowest_common_ancestor(root, p, q):
    while True:
        if root.val < p.val and root.val < q.val:
            root = root.right
        elif root.val > p.val and root.val > q.val:
            root = root.left
        else:
            return root

# Solution: https://youtu.be/r6AXIfdi9oQ
# Credit: Greg Hogg
def lowest_common_ancestor_alt(root, p, q):
    lca = [root]

    def search(root):
        if not root:
            return

        lca[0] = root
        if root is p or root is q:
            return
        elif root.val < p.val and root.val < q.val:
            search(root.right)
        elif root.val > p.val and root.val > q.val:
            search(root.left)
        else:
            return

    search(root)
    return lca[0]
    # Time Complexity: O(h) { here "h" is the height of the binary search tree }
    # Space Complexity: O(h) { here "h" is the height of the binary search tree }

def example_1():
    # Initialize and allocate memory for tree nodes
    a = TreeNode(6)
    b = TreeNode(2)
    c = TreeNode(8)
    d = TreeNode(0)
    e = TreeNode(4)
    f = TreeNode(7)
    g = TreeNode(9)
    h = TreeNode(3)
    i = TreeNode(5)

    # Connect binary tree nodes
    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.left = f
    c.right = g
    e.left = h
    e.right = i

    return a, b, c

def example_2():
    # Initialize and allocate memory for tree nodes
    a = TreeNode(6)
    b = TreeNode(2)
    c = TreeNode(8)
    d = TreeNode(0)
    e = TreeNode(4)
    f = TreeNode(7)
    g = TreeNode(9)
    h = TreeNode(3)
    i = TreeNode(5)

    # Connect binary tree nodes
    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.left = f
    c.right = g
    e.left = h
    e.right = i

    return a, b, e

def main():
    root, p, q = example_1()
    result = lowest_common_ancestor(root, p, q)
    print(result.val) # 6

    root, p, q = example_2()
    result = lowest_common_ancestor(root, p, q)
    print(result.val) # 2

if __name__ == "__main__":
    main()
