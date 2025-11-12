# --------------------------------
# 513. Find Bottom Left Tree Value
# --------------------------------

# Problem: https://leetcode.com/problems/find-bottom-left-tree-value/
# 
# Given the root of a binary tree, return the leftmost value in the last row of 
# the tree.
# 
#  
# Example 1:
# 
# Input: root = [2,1,3]
# Output: 1
# 
# 
# Example 2:
# 
# Input: root = [1,2,3,4,null,5,6,null,null,7]
# Output: 7
# 
#  
# Constraints:
# 
# 	The number of nodes in the tree is in the range [1, 104].
# 	-2^31 <= Node.val <= 2^31 - 1

import sys
import os

# Add the parent directory to sys.path to import miscelaneus tools
current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)

from tree import get_tree
from collections import deque

# Solution: https://youtu.be/u_by_cTsNJA
# Credit: Navdeep Singh founder of NeetCode
# Iterative
def find_bottom_left_value(root):
    res = []
    q = deque()
    q.append(root)
    while q:
        qlen = len(q)
        level = []
        for i in range(qlen):
            node = q.popleft()
            if node:
                q.append(node.left)
                q.append(node.right)
                level.append(node.val)
        if level:
            res.append(level)
    return res[-1][0]

# Recursive
def find_bottom_left_value_rec(root):
    max_height = -1
    res = -1
    def dfs(root, depth):
        nonlocal max_height, res
        if not root:
            return
        if depth > max_height:
            max_height = max(depth, max_height)
            res = root.val
        dfs(root.left, depth + 1)
        dfs(root.right, depth + 1)
    
    dfs(root, 0)
    return res


def main():
    root = get_tree("[2,1,3]")
    result = find_bottom_left_value(root)
    print(result) # 1

    root = get_tree("[1,2,3,4,null,5,6,null,null,7]")
    result = find_bottom_left_value(root)
    print(result) # 7

if __name__ == "__main__":
    main()
