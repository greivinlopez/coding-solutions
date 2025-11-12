# ---------------------------------------
# 114. Flatten Binary Tree to Linked List
# ---------------------------------------

# Problem: https://leetcode.com/problems/flatten-binary-tree-to-linked-list
#
# Given the root of a binary tree, flatten the tree into a "linked list":
#         
#   * The "linked list" should use the same TreeNode class where the right
#     child pointer points to the next node in the list and the left child pointer is
#     always null.
#   * The "linked list" should be in the same order as a pre-order traversal
#     of the binary tree.
# 
# Example 1:
# 
# https://assets.leetcode.com/uploads/2021/01/14/flaten.jpg
# 
# Input: root = [1,2,5,3,4,null,6]
# Output: [1,null,2,null,3,null,4,null,5,null,6]
# 
# Example 2:
# 
# Input: root = []
# Output: []
# 
# Example 3:
# 
# Input: root = [0]
# Output: [0]
# 
# 
# Constraints:
#         The number of nodes in the tree is in the range [0, 2000].
#         -100 <= Node.val <= 100
# 
# Follow up: Can you flatten the tree in-place (with O(1) extra space)?

import sys
import os

# Add the parent directory to sys.path to import miscelaneus tools
current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)

from tree import get_tree

# Solution: https://youtu.be/rKnD7rLT0lI
# Credit: Navdeep Singh founder of NeetCode
def flatten_tree(root):
    """
    Do not return anything, modify root in-place instead.
    """
    # flatten the root tree and return the list tail
    def dfs(root):
        if not root:
            return None

        leftTail = dfs(root.left)
        rightTail = dfs(root.right)

        if root.left:
            leftTail.right = root.right
            root.right = root.left
            root.left = None

        last = rightTail or leftTail or root
        return last

    dfs(root)
    # Time: O(n)    n = number of nodes in the binary tree
    # Space: O(h)   h = the height of the binary tree


def main():
    root = get_tree("[1,2,5,3,4,null,6]")
    flatten_tree(root)
    print(root) # [1, None, 2, None, 3, None, 4, None, 5, None, 6]ue

    root2 = get_tree("[]")
    flatten_tree(root2)
    print(root2) # None

    root3 = get_tree("[0]")
    flatten_tree(root3)
    print(root3) # [0]

if __name__ == "__main__":
    main()
