# ----------------------------------------
# 1022. Sum of Root To Leaf Binary Numbers
# ----------------------------------------

# Problem: https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers
#
# You are given the root of a binary tree where each node has a value 0 or 1. Each
# root-to-leaf path represents a binary number starting with the most significant
# bit.
#         
#   * For example, if the path is 0 -> 1 -> 1 -> 0 -> 1, then this could
#     represent 01101 in binary, which is 13.
# 
# For all leaves in the tree, consider the numbers represented by the path from
# the root to that leaf. Return the sum of these numbers.
# 
# The test cases are generated so that the answer fits in a 32-bits integer.
# 
# Example 1:
# 
# https://assets.leetcode.com/uploads/2019/04/04/sum-of-root-to-leaf-binary-numbers.png
# 
# Input: root = [1,0,1,0,1,0,1]
# Output: 22
# 
# Explanation: (100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22
# 
# Example 2:
# 
# Input: root = [0]
# Output: 0
# 
# 
# Constraints:
#         The number of nodes in the tree is in the range [1, 1000].
#         Node.val is 0 or 1.

import sys
import os

# Add the parent directory to sys.path to import miscelaneus tools
current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)

from tree import get_tree

# Solution: https://algo.monster/liteproblems/1022
# Credit: AlgoMonster
def sum_root_to_leaf(root):
 
    def dfs(node, current_value):
        # Base case: if node is None, contribute 0 to the sum
        if node is None:
            return 0
        
        # Shift current value left by 1 bit and add current node's value
        # This effectively appends the current bit to the binary number
        current_value = (current_value << 1) | node.val
        
        # If this is a leaf node, return the accumulated binary value
        if node.left is None and node.right is None:
            return current_value
        
        # Recursively calculate sum for left and right subtrees
        left_sum = dfs(node.left, current_value)
        right_sum = dfs(node.right, current_value)
        
        return left_sum + right_sum
    
    # Start DFS from root with initial binary value of 0
    return dfs(root, 0)
    # Time: O(n)
    # Space: O(n)


def main():
    root = get_tree("[1,0,1,0,1,0,1]")
    result = sum_root_to_leaf(root)
    print(result) # 22

    root = get_tree("[0]")
    result = sum_root_to_leaf(root)
    print(result) # 0

if __name__ == "__main__":
    main()
