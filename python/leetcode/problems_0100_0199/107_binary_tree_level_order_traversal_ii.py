# -----------------------------------------
# 107. Binary Tree Level Order Traversal II
# -----------------------------------------

# Problem: https://leetcode.com/problems/binary-tree-level-order-traversal-ii
#
# Given the root of a binary tree, return the bottom-up level order traversal of
# its nodes' values. (i.e., from left to right, level by level from leaf to root).
# 
# Example 1:
# 
# https://assets.leetcode.com/uploads/2021/02/19/tree1.jpg
# 
# Input: root = [3,9,20,null,null,15,7]
# Output: [[15,7],[9,20],[3]]
# 
# Example 2:
# 
# Input: root = [1]
# Output: [[1]]
# 
# Example 3:
# Input: root = []
# Output: []
# 
# 
# Constraints:
#         The number of nodes in the tree is in the range [0, 2000].
#         -1000 <= Node.val <= 1000

import sys
import os

# Add the parent directory to sys.path to import miscelaneus tools
current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)

from tree import get_tree
from collections import deque

# Solution: https://leetcode.com/problems/binary-tree-level-order-traversal-ii/solutions/6894527/beats-92-using-bfs-java-python-c-javascript
# Credit: Pradhuman Gupta -> https://leetcode.com/u/PradhumanGupta/
def level_order_bottom(root):
    if not root: return []
    res = deque()
    queue = deque([root])

    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
        res.appendleft(level)

    return list(res)
    # Time: O(n)
    # Space: O(n)


def main():
    root = get_tree("[3,9,20,null,null,15,7]")
    result = level_order_bottom(root)
    print(result) # [[15, 7], [9, 20], [3]]

    root = get_tree("[1]")
    result = level_order_bottom(root)
    print(result) # [[1]]

    root = get_tree("[]")
    result = level_order_bottom(root)
    print(result) # []

if __name__ == "__main__":
    main()
