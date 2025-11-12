# ---------------------
# 938. Range Sum of BST
# ---------------------

# Problem: https://leetcode.com/problems/range-sum-of-bst
#
# Given the root node of a binary search tree and two integers low and high,
# return the sum of values of all nodes with a value in the inclusive range [low,
# high].
# 
# Example 1:
# 
# Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
# Output: 32
# 
# Explanation: Nodes 7, 10, and 15 are in the range [7, 15]. 7 + 10 + 15 = 32.
# 
# Example 2:
# 
# Input: root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10
# Output: 23
# 
# Explanation: Nodes 6, 7, and 10 are in the range [6, 10]. 6 + 7 + 10 = 23.
# 
# 
# Constraints:
#         The number of nodes in the tree is in the range [1, 2 * 10^4].
#         1 <= Node.val <= 10^5
#         1 <= low <= high <= 10^5
#         All Node.val are unique.

import sys
import os

# Add the parent directory to sys.path to import miscelaneus tools
current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)

# Import code needed for solutions
from tree import get_tree

# Solution: https://youtu.be/uLVG45n4Sbg
# Credit: Navdeep Singh founder of NeetCode
def range_sum_bst(root, low, high):
    if not root:
        return 0

    if root.val > high:
        return range_sum_bst(root.left, low, high)

    if root.val < low:
        return range_sum_bst(root.right, low, high)

    return (
        root.val +
        range_sum_bst(root.left, low, high) +
        range_sum_bst(root.right, low, high)
    )
    # Time: O(n)
    # Space: O(h)   h = is the height of the tree


def main():
    root = get_tree("[10,5,15,3,7,null,18]")
    result = range_sum_bst(root, 7, 15)
    print(result) # 32

    root = get_tree("[10,5,15,3,7,13,18,1,null,6]")
    result = range_sum_bst(root, 6, 10)
    print(result) # 23

if __name__ == "__main__":
    main()
