# ------------------
# 1609. Even Odd Tree
# ------------------

# Problem: https://leetcode.com/problems/even-odd-tree
#
# A binary tree is named Even-Odd if it meets the following conditions:
# 
#    - The root of the binary tree is at level index 0, its children are at
#      level index 1, their children are at level index 2, etc.
# 
#    - For every even-indexed level, all nodes at the level have odd integer
#      values in strictly increasing order (from left to right).
# 
#    - For every odd-indexed level, all nodes at the level have even integer
#      values in strictly decreasing order (from left to right).
# 
# Given the root of a binary tree, return true if the binary tree is Even-Odd,
# otherwise return false.
# 
# Example 1:
# 
# Input: root = [1,10,4,3,null,7,9,12,8,6,null,null,2]
# Output: true
# Explanation: The node values on each level are:
# Level 0: [1]
# Level 1: [10,4]
# Level 2: [3,7,9]
# Level 3: [12,8,6,2]
# Since levels 0 and 2 are all odd and increasing and levels 1 and 3 are all even
# and decreasing, the tree is Even-Odd.
# 
# Example 2:
# 
# Input: root = [5,4,2,3,3,7]
# Output: false
# Explanation: The node values on each level are:
# Level 0: [5]
# Level 1: [4,2]
# Level 2: [3,3,7]
# Node values in level 2 must be in strictly increasing order, so the tree is not
# Even-Odd.
# 
# Example 3:
# 
# Input: root = [5,9,1,3,5,7]
# Output: false
# Explanation: Node values in the level 1 should be even integers.
# 
# 
# Constraints:
#         The number of nodes in the tree is in the range [1, 10^5].
#         1 <= Node.val <= 10^6

import sys
import os

# Add the parent directory to sys.path to import miscelaneus tools
current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)

# Import code needed for solutions
from tree import get_tree
from collections import deque

# Solution: https://youtu.be/FkNWN1Fj_TY
# Credit: Navdeep Singh founder of NeetCode
def is_even_odd_tree(root):
    even = True
    q = deque([root])

    while q:
        prev = float("-inf") if even else float("inf")
        for _ in range(len(q)):
            node = q.popleft()

            if even and (node.val % 2 == 0 or node.val <= prev):
                return False
            elif not even and (node.val % 2 == 1 or node.val >= prev):
                return False
            
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
            prev = node.val
        even = not even
    return True


def main():
    root = get_tree("[1,10,4,3,null,7,9,12,8,6,null,null,2]")
    result = is_even_odd_tree(root)
    print(result) # True

    root = get_tree("[5,4,2,3,3,7]")
    result = is_even_odd_tree(root)
    print(result) # False

    root = get_tree("[5,9,1,3,5,7]")
    result = is_even_odd_tree(root)
    print(result) # False

if __name__ == "__main__":
    main()
