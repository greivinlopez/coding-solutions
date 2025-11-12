# ----------------------------------------
# 637. Average of Levels in Binary Tree 🌲
# ----------------------------------------

# Problem: https://leetcode.com/problems/average-of-levels-in-binary-tree
#
# Given the root of a binary tree, return the average value of the nodes on each
# level in the form of an array. Answers within 10-5 of the actual answer will be
# accepted.
# 
# Example 1:
# 
# Input: root = [3,9,20,null,null,15,7]
# Output: [3.00000,14.50000,11.00000]
# 
# Explanation: The average value of nodes on level 0 is 3, on level 1 is 14.5, and
# on level 2 is 11.
# Hence return [3, 14.5, 11].
# 
# Example 2:
# 
# Input: root = [3,9,20,15,7]
# Output: [3.00000,14.50000,11.00000]
# 
# 
# Constraints:
#         The number of nodes in the tree is in the range [1, 10⁴].
#         -2³¹ <= Node.val <= 2³¹ - 1

import sys
import os

# Add the parent directory to sys.path to import miscelaneus tools
current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)

from tree import get_tree
from collections import deque

# Solution: https://youtu.be/92zdLCeiumk
# Credit: Greg Hogg
def average_of_levels(root):
    avgs = []
    q = deque()
    q.append(root)

    while q:
        summ = 0
        n = len(q)
        for _ in range(n):
            node = q.popleft()
            summ += node.val

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        avgs.append(summ / n)
    
    return avgs
    # Time: O(n)
    # Space: O(n)


def main():
    root = get_tree("[3,9,20,null,null,15,7]")
    result = average_of_levels(root)
    print(result) # [3.0, 14.5, 11.0]

    root = get_tree("[3,9,20,15,7]")
    result = average_of_levels(root)
    print(result) # [3.0, 14.5, 11.0]

if __name__ == "__main__":
    main()
