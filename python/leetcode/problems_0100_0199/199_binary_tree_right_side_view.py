# --------------------------------
# 199. Binary Tree Right Side View
# --------------------------------

# Problem: https://leetcode.com/problems/binary-tree-right-side-view/
# 
# Given the root of a binary tree, imagine yourself standing on the right side 
# of it, return the values of the nodes you can see ordered from top to bottom.
# 
#  
# Example 1:
# 
# Input: root = [1,2,3,null,5,null,4]
# 
# Output: [1,3,4]
# 
# 
# Example 2:
# 
# Input: root = [1,2,3,4,null,null,null,5]
# 
# Output: [1,3,4,5]
# 
# 
# Example 3:
# 
# Input: root = [1,null,3]
# 
# Output: [1,3]
# 
# 
# Example 4:
# 
# Input: root = []
# 
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

from tree import get_tree, TreeNode
from collections import deque

# Solution: https://youtu.be/d4zLyf32e3I
# Credit: Navdeep Singh founder of NeetCode
def right_side_view(root):
    res = []
    q = deque([root])

    while q:
        rightSide = None
        qLen = len(q)

        for i in range(qLen):
            node = q.popleft()
            if node:
                rightSide = node
                q.append(node.left)
                q.append(node.right)
        if rightSide:
            res.append(rightSide.val)
    return res


def main():
    root = get_tree("[1,2,3,null,5,null,4]")
    result = right_side_view(root)
    print(result) # [1,3,4]

    root = get_tree("[1,2,3,4,null,null,null,5]")
    result = right_side_view(root)
    print(result) # [1,3,4,5]

    root = get_tree("[1,null,3]")
    result = right_side_view(root)
    print(result) # [1,3]

if __name__ == "__main__":
    main()
