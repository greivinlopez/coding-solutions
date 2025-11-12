# ----------------------------------------------------------
# 1008. Construct Binary Search Tree from Preorder Traversal
# ----------------------------------------------------------

# Problem: https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal
#
# Given an array of integers preorder, which represents the preorder traversal of
# a BST (i.e., binary search tree), construct the tree and return its root.
# 
# It is guaranteed that there is always possible to find a binary search tree with
# the given requirements for the given test cases.
# 
# A binary search tree is a binary tree where for every node, any descendant of
# Node.left has a value strictly less than Node.val, and any descendant of
# Node.right has a value strictly greater than Node.val.
# 
# A preorder traversal of a binary tree displays the value of the node first, then
# traverses Node.left, then traverses Node.right.
# 
# Example 1:
# 
# https://assets.leetcode.com/uploads/2019/03/06/1266.png
# 
# Input: preorder = [8,5,1,7,10,12]
# Output: [8,5,10,1,7,null,12]
# 
# Example 2:
# 
# Input: preorder = [1,3]
# Output: [1,null,3]
# 
# 
# Constraints:
#         1 <= preorder.length <= 100
#         1 <= preorder[i] <= 1000
#         All the values of preorder are unique.

import sys
import os

# Add the parent directory to sys.path to import miscelaneus tools
current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)

from tree import TreeNode

# Solution: https://algo.monster/liteproblems/1008
# Credit: AlgoMonster
def bst_from_preorder(preorder):

    def build_subtree(left, right):
        # Base case: invalid range means empty subtree
        if left > right:
            return None
        
        # First element in preorder range is always the root
        root_val = preorder[left]
        root = TreeNode(root_val)
        
        # Binary search to find the partition point between left and right subtrees
        # All values in left subtree < root_val, all values in right subtree > root_val
        search_left, search_right = left + 1, right + 1
        
        while search_left < search_right:
            mid = (search_left + search_right) >> 1  # Equivalent to // 2
            
            if preorder[mid] > root_val:
                # Mid element belongs to right subtree, search in left half
                search_right = mid
            else:
                # Mid element belongs to left subtree, search in right half
                search_left = mid + 1
        
        # search_left now points to the first element of right subtree (or beyond array)
        # Recursively build left subtree: elements from (left + 1) to (search_left - 1)
        root.left = build_subtree(left + 1, search_left - 1)
        
        # Recursively build right subtree: elements from search_left to right
        root.right = build_subtree(search_left, right)
        
        return root
    
    # Start building tree with entire preorder array
    return build_subtree(0, len(preorder) - 1)
    # Time: O(n * log(n))
    # Space: O(n)


def main():
    result = bst_from_preorder(preorder = [8,5,1,7,10,12])
    print(result) # [8, 5, 10, 1, 7, None, 12]

    result = bst_from_preorder(preorder = [1,3])
    print(result) # [1, None, 3]

if __name__ == "__main__":
    main()
