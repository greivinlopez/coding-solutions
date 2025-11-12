# -------------------------------------------------
# 103. Binary Tree Zigzag Level Order Traversal 🌲
# -------------------------------------------------

# Problem: https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
# 
# Given the root of a binary tree, return the zigzag level order traversal of its 
# nodes' values. (i.e., from left to right, then right to left for the next level 
# and alternate between).

import sys
import os

# Add the parent directory to sys.path to import miscelaneus tools
current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)

from tree import get_tree, TreeNode

# Solution: https://youtu.be/igbboQbiwqw
# Credit: Navdeep Singh founder of NeetCode
def zigzag_level_order(root):
    if root is None:
        return
    result, zigzagDirection = [], 1
    q = [root]
    while q:
        level, queueLength = [], len(q)
        for i in range(queueLength):
            node = q.pop(0)
            level.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        result.append(level[::zigzagDirection])
        zigzagDirection *= -1
    return result


def main():
    root = get_tree("[3,9,20,null,null,15,7]")
    result = zigzag_level_order(root)
    print(result) # [[3],[20,9],[15,7]]

    result = zigzag_level_order(TreeNode(1))
    print(result) # [[1]]

if __name__ == "__main__":
    main()