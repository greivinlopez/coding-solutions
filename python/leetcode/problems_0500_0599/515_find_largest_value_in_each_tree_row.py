# -------------------------------------------
# 515. Find Largest Value in Each Tree Row 🌲
# -------------------------------------------

# Problem: https://leetcode.com/problems/find-largest-value-in-each-tree-row
#
# Given the root of a binary tree, return an array of the largest value in each
# row of the tree (0-indexed).
# 
# Example 1:
# 
# Input: root = [1,3,2,5,3,null,9]
# Output: [1,3,9]
# 
# Example 2:
# 
# Input: root = [1,2,3]
# Output: [1,3]
# 
# Constraints:
#         The number of nodes in the tree will be in the range [0, 10^4].
#         -2^31 <= Node.val <= 2^31 - 1

import sys
import os

# Add the parent directory to sys.path to import miscelaneus tools
current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)

# Import code needed for solutions
from tree import get_tree
from collections import deque

# Solution: https://youtu.be/wB9JOh7Z_cY
# Credit: Navdeep Singh founder of NeetCode
def largest_values(root):
    if not root:
        return []
    
    res = []
    q = deque([root])
    while q:
        row_max = q[0].val
        length = len(q)
        for _ in range(length):
            node = q.popleft()
            row_max = max(row_max, node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        res.append(row_max)
    return res
    # Time: O(n)
    # Space: O(w) w = maximum width of the tree (maximum number of nodes at any level)


def main():
    root = get_tree("[1,3,2,5,3,null,9]")
    result = largest_values(root)
    print(result) # [1,3,9]

    root = get_tree("[1,2,3]")
    result = largest_values(root)
    print(result) # [1,3]

if __name__ == "__main__":
    main()
