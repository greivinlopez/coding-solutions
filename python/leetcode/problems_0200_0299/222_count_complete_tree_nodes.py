# ------------------------------
# 222. Count Complete Tree Nodes
# ------------------------------

# Problem: https://leetcode.com/problems/count-complete-tree-nodes
#
# Given the root of a complete binary tree, return the number of the nodes in the
# tree.
# 
# According to Wikipedia, every level, except possibly the last, is completely
# filled in a complete binary tree, and all nodes in the last level are as far
# left as possible. It can have between 1 and 2h nodes inclusive at the last level
# h.
# 
# Design an algorithm that runs in less than O(n) time complexity.
# 
# Example 1:
# 
# https://assets.leetcode.com/uploads/2021/01/14/complete.jpg
# 
# Input: root = [1,2,3,4,5,6]
# Output: 6
# 
# Example 2:
# 
# Input: root = []
# Output: 0
# 
# Example 3:
# 
# Input: root = [1]
# Output: 1
# 
# 
# Constraints:
#         The number of nodes in the tree is in the range [0, 5 * 10⁴].
#         0 <= Node.val <= 5 * 10⁴
#         The tree is guaranteed to be complete.

import sys
import os

# Add the parent directory to sys.path to import miscelaneus tools
current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)

from tree import get_tree


# Solution: https://leetcode.com/problems/count-complete-tree-nodes/solutions/693831/python-elegant-solution
def count_nodes(root):
    if not root:
        return 0
    
    def depthLeft(node):
        d = 0
        while node:
            d += 1
            node = node.left
        return d

    def depthRight(node):
        d = 0
        while node:
            d += 1
            node = node.right
        return d
    
    ld = depthLeft(root.left)
    rd = depthRight(root.right)
    
    if ld == rd:
        return 2**(ld + 1) - 1
    else:
        return 1 + count_nodes(root.left) + count_nodes(root.right)
    # Time: O(log²(n))
    # Space: O(h)
    # h = the height of the tree


def main():
    root = get_tree("[1,2,3,4,5,6]")
    result = count_nodes(root)
    print(result) # 6

    root = get_tree("[]")
    result = count_nodes(root)
    print(result) # 0

    root = get_tree("[1]")
    result = count_nodes(root)
    print(result) # 1

if __name__ == "__main__":
    main()
