# -------------------------------------
# 104. Maximum Depth of Binary Tree 🌲
# -------------------------------------

# Problem: https://leetcode.com/problems/maximum-depth-of-binary-tree/
# 
# Given the root of a binary tree, return its maximum depth.
# 
# A binary tree's maximum depth is the number of nodes along the longest path 
# from the root node down to the farthest leaf node.

import sys
import os

# Add the parent directory to sys.path to import miscelaneus tools
current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)

from tree import get_tree
from collections import deque

# Solution: https://youtu.be/hTM3phVI6YQ
# Credit: Navdeep Singh founder of NeetCode
def max_depth(root):
    # RECURSIVE DFS
    # Time: O(n)
    # Space: O(h) { here "h" is the height of the binary tree }
    if not root:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))

def max_depth_iter(root):
    # ITERATIVE DFS
    stack = [[root, 1]]
    res = 0

    while stack:
        node, depth = stack.pop()

        if node:
            res = max(res, depth)
            stack.append([node.left, depth + 1])
            stack.append([node.right, depth + 1])
    return res

def max_depth_bfs(root):
    # BFS
    # Time: O(n)
    # Space: O(n)
    q = deque()
    if root:
        q.append(root)

    level = 0

    while q:
        for i in range(len(q)):
            node = q.popleft()
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        level += 1
    return level

# Same Solution Different Video: https://youtu.be/ScvTcU2Aifs
# Credit: Greg Hogg


def main():
    root = get_tree("[3,9,20,null,null,15,7]")
    result = max_depth_bfs(root)
    print(result) # 3

    root = get_tree("[1,null,2]")
    result = max_depth_bfs(root)
    print(result) # 2

if __name__ == "__main__":
    main()