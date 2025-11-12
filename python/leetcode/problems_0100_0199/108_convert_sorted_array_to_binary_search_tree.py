# --------------------------------------------------
# 108. Convert Sorted Array to Binary Search Tree 🌲
# --------------------------------------------------

# Problem: https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
# 
# Given an integer array nums where the elements are sorted in ascending order, 
# convert it to a height-balanced binary search tree.

import sys
import os

# Add the parent directory to sys.path to import miscelaneus tools
current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)

from tree import get_tree, TreeNode

# Solution: https://youtu.be/0K0uCMYq5ng
# Credit: Navdeep Singh founder of NeetCode
def sorted_array_to_BST(nums):
    if not nums:
        return None
    mid = len(nums)//2
    root = TreeNode(nums[mid])
    root.left = sorted_array_to_BST(nums[:mid])
    root.right = sorted_array_to_BST(nums[mid+1:])
    return root


def main():
    result = sorted_array_to_BST([-10,-3,0,5,9])
    print(result) # [0, -3, 9, -10, None, 5]

    result = sorted_array_to_BST([1,3])
    print(result) # [3, 1]

if __name__ == "__main__":
    main()