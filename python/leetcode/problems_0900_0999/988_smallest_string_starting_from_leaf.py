# ---------------------------------------
# 988. Smallest String Starting From Leaf
# ---------------------------------------

# Problem: https://leetcode.com/problems/smallest-string-starting-from-leaf
#
# You are given the root of a binary tree where each node has a value in the range
# [0, 25] representing the letters 'a' to 'z'.
# 
# Return the lexicographically smallest string that starts at a leaf of this tree
# and ends at the root.
# 
# As a reminder, any shorter prefix of a string is lexicographically smaller.
#         
#   * For example, "ab" is lexicographically smaller than "aba".
# 
# A leaf of a node is a node that has no children.
# 
# Example 1:
# 
# https://assets.leetcode.com/uploads/2019/01/30/tree1.png
# 
# Input: root = [0,1,2,3,4,3,4]
# Output: "dba"
# 
# Example 2:
# 
# https://assets.leetcode.com/uploads/2019/01/30/tree2.png
# 
# Input: root = [25,1,3,1,3,0,2]
# Output: "adz"
# 
# Example 3:
# 
# https://assets.leetcode.com/uploads/2019/02/01/tree3.png
# 
# Input: root = [2,2,1,null,1,0,null,0]
# Output: "abc"
# 
# 
# Constraints:
#         The number of nodes in the tree is in the range [1, 8500].
#         0 <= Node.val <= 25

import sys
import os

# Add the parent directory to sys.path to import miscelaneus tools
current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)

from tree import get_tree

# Solution: https://youtu.be/UvdWfxQ_ZDs
# Credit: Navdeep Singh founder of NeetCode
def smallest_from_leaf(root):
    
    def helper(root, cur):
        if not root:
            return
        cur = chr(ord('a') + root.val) + cur
        if root.left and root.right:
            return min(
                helper(root.left, cur),
                helper(root.right, cur)
            )
        if root.right:
            return helper(root.right, cur)
        if root.left:
            return helper(root.left, cur)
        return cur
    
    return helper(root, "")
    # Time: O(n * h)
    # Space: O(h²)     n² -> worst case, log²(n) -> best case
    # n = number of nodes in the tree
    # h = the height of the tree


def main():
    root = get_tree("[0,1,2,3,4,3,4]")
    result = smallest_from_leaf(root)
    print(result) # "dba"

    root = get_tree("[25,1,3,1,3,0,2]")
    result = smallest_from_leaf(root)
    print(result) # "adz"

    root = get_tree("[2,2,1,null,1,0,null,0]")
    result = smallest_from_leaf(root)
    print(result) # "abc"

if __name__ == "__main__":
    main()
