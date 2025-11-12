# -----------------------
# 226. Invert Binary Tree
# -----------------------

# Problem: https://leetcode.com/problems/invert-binary-tree/
# 
# Given the root of a binary tree, invert the tree, and return its root.
# 
#  
# Example 1:
# 
# Input: root = [4,2,7,1,3,6,9]
# Output: [4,7,2,9,6,3,1]
# 
# 
# Example 2:
# 
# Input: root = [2,1,3]
# Output: [2,3,1]
# 
# 
# Example 3:
# 
# Input: root = []
# Output: []
# 
# 
# Constraints:
# 
# 	The number of nodes in the tree is in the range [0, 100].
# 	-100 <= Node.val <= 100

import sys
import os

# Add the parent directory to sys.path to import miscelaneus tools
current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)

from tree import get_tree


# Solution: https://youtu.be/OnSn2XEQ4MY
# Credit: Navdeep Singh founder of NeetCode
def invert_tree(root):
    if not root:
        return None
    
    # swap the children
    root.left, root.right = root.right, root.left
    
    # make 2 recursive calls
    invert_tree(root.left)
    invert_tree(root.right)
    return root


# Solution: https://youtu.be/6ScBLgESFas
# Credit: Greg Hogg

# YouTube Solution
def invert_tree_yt(root):

    if not root:
        return None

    root.left, root.right = root.right, root.left

    invert_tree_yt(root.left)
    invert_tree_yt(root.right)

    return root
    # Time Complexity: O(n)
    # Space Complexity: O(h) { here "h" is the height of the tree }


# Solution for Bootcamp
def invert_tree_boot(root):
    def invert(node):
        if not node:
            return
            
        node.left, node.right = node.right, node.left
        invert(node.left)
        invert(node.right)

    invert(root)
    return root
    # Time Complexity: O(n)
    # Space Complexity: O(h) { here "h" is the height of the tree }


def main():
    root = get_tree("[4,2,7,1,3,6,9]")
    result = invert_tree(root)
    print(result) # [4,7,2,9,6,3,1]

    root = get_tree("[2,1,3]")
    result = invert_tree(root)
    print(result) # [2,3,1]

if __name__ == "__main__":
    main()
