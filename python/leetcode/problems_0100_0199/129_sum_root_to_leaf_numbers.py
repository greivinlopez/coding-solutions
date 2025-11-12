# -----------------------------
# 129. Sum Root to Leaf Numbers
# -----------------------------

# Problem: https://leetcode.com/problems/sum-root-to-leaf-numbers
#
# You are given the root of a binary tree containing digits from 0 to 9 only.
# 
# Each root-to-leaf path in the tree represents a number.
#  
#   * For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.
# 
# Return the total sum of all root-to-leaf numbers. Test cases are generated so
# that the answer will fit in a 32-bit integer.
# 
# A leaf node is a node with no children.
# 
# Example 1:
# 
# https://assets.leetcode.com/uploads/2021/02/19/num1tree.jpg
# 
# Input: root = [1,2,3]
# Output: 25
# 
# Explanation:
# The root-to-leaf path 1->2 represents the number 12.
# The root-to-leaf path 1->3 represents the number 13.
# Therefore, sum = 12 + 13 = 25.
# 
# Example 2:
# 
# https://assets.leetcode.com/uploads/2021/02/19/num2tree.jpg
# 
# Input: root = [4,9,0,5,1]
# Output: 1026
# 
# Explanation:
# The root-to-leaf path 4->9->5 represents the number 495.
# The root-to-leaf path 4->9->1 represents the number 491.
# The root-to-leaf path 4->0 represents the number 40.
# Therefore, sum = 495 + 491 + 40 = 1026.
# 
# 
# Constraints:
#         The number of nodes in the tree is in the range [1, 1000].
#         0 <= Node.val <= 9
#         The depth of the tree will not exceed 10.

import sys
import os

# Add the parent directory to sys.path to import miscelaneus tools
current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)

from tree import get_tree

# Solution: https://youtu.be/Jk16lZGFWxE
# Credit: Navdeep Singh founder of NeetCode
def sum_numbers(root):
    def dfs(cur, num):
        if not cur:
            return 0
        
        num = num * 10 + cur.val
        if not cur.left and not cur.right:
            return num
        
        return dfs(cur.left, num) + dfs(cur.right, num)

    return dfs(root, 0)
    # Time: O(n)
    # Space: O(h)
    # n = number of nodes in the binary tree
    # h = height of the binary tree


def main():
    root = get_tree("[1,2,3]")
    result = sum_numbers(root)
    print(result) # 25

    root = get_tree("[4,9,0,5,1]")
    result = sum_numbers(root)
    print(result) # 1026

if __name__ == "__main__":
    main()
