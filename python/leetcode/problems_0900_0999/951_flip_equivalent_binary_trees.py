# ---------------------------------
# 951. Flip Equivalent Binary Trees
# ---------------------------------

# Problem: https://leetcode.com/problems/flip-equivalent-binary-trees
#
# For a binary tree T, we can define a flip operation as follows: choose any node,
# and swap the left and right child subtrees.
# 
# A binary tree X is flip equivalent to a binary tree Y if and only if we can make
# X equal to Y after some number of flip operations.
# 
# Given the roots of two binary trees root1 and root2, return true if the two
# trees are flip equivalent or false otherwise.
# 
# Example 1:
# 
# https://assets.leetcode.com/uploads/2018/11/29/tree_ex.png
# 
# Input: root1 = [1,2,3,4,5,6,null,null,null,7,8], root2 =
# [1,3,2,null,6,4,5,null,null,null,null,8,7]
# Output: true
# 
# Explanation: We flipped at nodes with values 1, 3, and 5.
# 
# Example 2:
# 
# Input: root1 = [], root2 = []
# Output: true
# 
# Example 3:
# 
# Input: root1 = [], root2 = [1]
# Output: false
# 
# 
# Constraints:
#         The number of nodes in each tree is in the range [0, 100].
#         Each tree will have unique node values in the range [0, 99].

import sys
import os

# Add the parent directory to sys.path to import miscelaneus tools
current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)

from tree import get_tree

# Solution: https://youtu.be/izRDc1il9Pk
# Credit: Navdeep Singh founder of NeetCode
def flip_equiv(r1, r2):
    if not r1 or not r2:
        return not r1 and not r2
    if r1.val != r2.val:
        return False
    
    a = flip_equiv(r1.left, r2.left) and flip_equiv(r1.right, r2.right)
    return a or (flip_equiv(r1.left, r2.right) and flip_equiv(r1.right, r2.left))
    # Time: O(min(n, m))
    # Space: O(min(n, m))
    # n = number of nodes in r1
    # m = number of nodes in r2


def main():
    root1 = get_tree("[1,2,3,4,5,6,null,null,null,7,8]")
    root2 = get_tree("[1,3,2,null,6,4,5,null,null,null,null,8,7]")
    result = flip_equiv(root1, root2)
    print(result) # True

    root1 = get_tree("[]")
    root2 = get_tree("[]")
    result = flip_equiv(root1, root2)
    print(result) # True

    root1 = get_tree("[]")
    root2 = get_tree("[1]")
    result = flip_equiv(root1, root2)
    print(result) # False

if __name__ == "__main__":
    main()
