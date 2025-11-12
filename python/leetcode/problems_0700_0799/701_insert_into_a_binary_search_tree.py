# -------------------------------------
# 701. Insert Into A Binary Search Tree
# -------------------------------------

# Problem: https://leetcode.com/problems/insert-into-a-binary-search-tree/
# 
# You are given the root node of a binary search tree (BST) and a value to 
# insert into the tree. Return the root node of the BST after the insertion.
# It is guaranteed that the new value does not exist in the original BST.
# 
# Notice that there may exist multiple valid ways for the insertion, as long 
# as the tree remains a BST after insertion. You can return any of them.
# 
# 
# Example 1:
# 
# Input: root = [4,2,7,1,3], val = 5
# Output: [4,2,7,1,3,5]
# 
# Explanation: Another accepted tree is:
# 
# Example 2:
# 
# Input: root = [40,20,60,10,30,50,70], val = 25
# Output: [40,20,60,10,30,50,70,null,null,25]
# 
# Example 3:
# 
# Input: root = [4,2,7,1,3,null,null,null,null,null,null], val = 5
# Output: [4,2,7,1,3,5]
#  
# 
# Constraints:
# 
#   The number of nodes in the tree will be in the range [0, 10^4].
#   -10^8 <= Node.val <= 10^8
#   All the values Node.val are unique.
#   -10^8 <= val <= 10^8
#   It's guaranteed that val does not exist in the original BST.

import sys
import os

# Add the parent directory to sys.path to import miscelaneus tools
current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)

# Import code needed for solutions
from tree import get_tree, TreeNode


# Solution: https://youtu.be/Cpg8f79luEA
# Credit: Navdeep Singh founder of NeetCode
def insert_into_BST(root, val):
    if not root:
        return TreeNode(val)
    if val > root.val:
        root.right = insert_into_BST(root.right, val)
    else:
        root.left = insert_into_BST(root.left, val)
    return root


def main():
    root = get_tree("[4,2,7,1,3]")
    result = insert_into_BST(root, 5)
    print(result) # [4, 2, 7, 1, 3, 5]

    root = get_tree("[40,20,60,10,30,50,70]")
    result = insert_into_BST(root, 25)
    print(result) # [40, 20, 60, 10, 30, 50, 70, None, None, 25]

    root = get_tree("[4,2,7,1,3,null,null,null,null,null,null]")
    result = insert_into_BST(root, 5)
    print(result) # [4, 2, 7, 1, 3, 5]

if __name__ == "__main__":
    main()
