# ----------------------------------------------
# 1457. Pseudo-Palindromic Paths in a Binary Tree
# ----------------------------------------------

# Problem: https://leetcode.com/problems/pseudo-palindromic-paths-in-a-binary-tree
#
# Given a binary tree where node values are digits from 1 to 9. A path in the
# binary tree is said to be pseudo-palindromic if at least one permutation of the
# node values in the path is a palindrome.
# 
# Return the number of pseudo-palindromic paths going from the root node to leaf
# nodes.
# 
# Example 1:
# 
# Input: root = [2,3,1,3,1,null,1]
# Output: 2
# 
# Explanation: The figure above represents the given binary tree. There are three
# paths going from the root node to leaf nodes: the red path [2,3,3], the green
# path [2,1,1], and the path [2,3,1]. Among these paths only red path and green
# path are pseudo-palindromic paths since the red path [2,3,3] can be rearranged
# in [3,2,3] (palindrome) and the green path [2,1,1] can be rearranged in [1,2,1]
# (palindrome).
# 
# Example 2:
# 
# Input: root = [2,1,1,1,3,null,null,null,null,null,1]
# Output: 1
# 
# Explanation: The figure above represents the given binary tree. There are three
# paths going from the root node to leaf nodes: the green path [2,1,1], the path
# [2,1,3,1], and the path [2,1]. Among these paths only the green path is pseudo-
# palindromic since [2,1,1] can be rearranged in [1,2,1] (palindrome).
# 
# Example 3:
# 
# Input: root = [9]
# Output: 1
# 
# 
# Constraints:
#         The number of nodes in the tree is in the range [1, 10^5].
#         1 <= Node.val <= 9

import sys
import os

# Add the parent directory to sys.path to import miscelaneus tools
current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)

# Import code needed for solutions
from tree import get_tree
from collections import defaultdict

# Solution: https://youtu.be/MBsSpQnaFzg
# Credit: Navdeep Singh founder of NeetCode
def pseudo_palindromic_paths(root):
    count = defaultdict(int)
    odd = 0  # digits with odd count

    def dfs(curr):
        nonlocal odd
        if not curr:
            return 0

        count[curr.val] += 1
        odd_change = 1 if count[curr.val] % 2 == 1 else -1
        odd += odd_change

        if not curr.left and not curr.right:
            res = 1 if odd <= 1 else 0
        else:
            res = dfs(curr.left) + dfs(curr.right)
        
        odd -= odd_change
        count[curr.val] -= 1
        return res

    return dfs(root)
    # Time: O(n)
    # Space: O(h) h being the height


def main():
    root = get_tree("[2,3,1,3,1,null,1]")
    result = pseudo_palindromic_paths(root)
    print(result) # 2

    root = get_tree("[2,1,1,1,3,null,null,null,null,null,1]")
    result = pseudo_palindromic_paths(root)
    print(result) # 1

if __name__ == "__main__":
    main()
