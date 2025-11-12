# ---------------------------------------
# 783. Minimum Distance Between Bst Nodes
# ---------------------------------------

# Problem: https://leetcode.com/problems/minimum-distance-between-bst-nodes/
# 
# Given the root of a Binary Search Tree (BST), return the minimum difference 
# between the values of any two different nodes in the tree.
#  
# Example 1:
# 
# Input: root = [4,2,6,1,3]
# Output: 1
# 
# 
# Example 2:
# 
# Input: root = [1,0,48,null,null,12,49]
# Output: 1
# 
# 
# Constraints:
# 
# 	The number of nodes in the tree is in the range [2, 100].
#   0 <= Node.val <= 10^5

import sys
import os

# Add the parent directory to sys.path to import miscelaneus tools
current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)

# Import code needed for solutions
from tree import get_tree

# Solution: https://youtu.be/joxx4hTYwcw
# Credit: Navdeep Singh founder of NeetCode
def min_diff_in_BST(root):
    curr_smallest, prev = float("inf"), None
    
    def inorder(node):
        nonlocal curr_smallest, prev
        if node is None:
            return
        
        inorder(node.left)
        if prev is not None:
            curr_smallest = min(curr_smallest, node.val-prev.val)
        prev = node
        inorder(node.right)

    inorder(root)
    return curr_smallest


def main():
    root = get_tree("[4,2,6,1,3]")
    result = min_diff_in_BST(root)
    print(result) # 1

    root = get_tree("[1,0,48,null,null,12,49]")
    result = min_diff_in_BST(root)
    print(result) # 1

if __name__ == "__main__":
    main()
