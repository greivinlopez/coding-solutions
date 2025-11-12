# -----------------------------------------
# 102. Binary Tree Level Order Traversal 🌲
# -----------------------------------------

# Problem: https://leetcode.com/problems/binary-tree-level-order-traversal/
# 
# Given the root of a binary tree, return the level order traversal of 
# its nodes' values. (i.e., from left to right, level by level).

import sys
import os

# Add the parent directory to sys.path to import miscelaneus tools
current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)

from tree import get_tree
from collections import deque

# Solution: https://youtu.be/6ZnyEApgFYg
# Credit: Navdeep Singh founder of NeetCode
def level_order(root):
    # Time: O(n)
    # Space: O(n)
    res = []
    q = deque()
    if root:
        q.append(root)

    while q:
        val = []

        for i in range(len(q)):
            node = q.popleft()
            val.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        res.append(val)
    return res
    
# Solution: https://youtu.be/2_tm34ZtYT4
# Credit: Greg Hogg
def level_order_alt(root):
    # Time: O(n)
    # Space: O(n)
    if root is None:
        return None
    
    queue = deque()
    queue.append(root)
    ans = []
    
    while queue:
        level = []
        n = len(queue)
        for i in range(n):
            node = queue.popleft()
            level.append(node.val)

            if node.left: queue.append(node.left)                
            if node.right: queue.append(node.right)
        
        ans.append(level)

    return ans


def main():
    root = get_tree("[3,9,20,null,null,15,7]")
    result = level_order(root)
    print(result) # True

    root = get_tree("[1]")
    result = level_order(root)
    print(result) # True

if __name__ == "__main__":
    main()