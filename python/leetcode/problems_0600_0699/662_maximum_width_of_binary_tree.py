# ---------------------------------
# 662. Maximum Width Of Binary Tree
# ---------------------------------

# Problem: https://leetcode.com/problems/maximum-width-of-binary-tree/
# 
# Given the root of a binary tree, return the maximum width of the given tree.
# 
# The maximum width of a tree is the maximum width among all levels.
# 
# The width of one level is defined as the length between the end-nodes 
# (the leftmost and rightmost non-null nodes), where the null nodes between the 
# end-nodes that would be present in a complete binary tree extending down to 
# that level are also counted into the length calculation.
# 
# It is guaranteed that the answer will in the range of a 32-bit signed integer.
# 
#  
# Example 1:
# 
# Input: root = [1,3,2,5,3,null,9]
# Output: 4
# Explanation: The maximum width exists in the third level with 
# length 4 (5,3,null,9).
# 
# 
# Example 2:
# 
# Input: root = [1,3,2,5,null,null,9,6,null,7]
# Output: 7
# Explanation: The maximum width exists in the fourth level with 
# length 7 (6,null,null,null,null,null,7).
# 
# 
# Example 3:
# 
# Input: root = [1,3,2,5]
# Output: 2
# Explanation: The maximum width exists in the second level with 
# length 2 (3,2).
# 
# 
# Constraints:
# 
# 	The number of nodes in the tree is in the range [1, 3000].
# 	-100 <= Node.val <= 100

import sys
import os

# Add the parent directory to sys.path to import miscelaneus tools
current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)

# Import code needed for solutions
from tree import get_tree, TreeNode

# Solution: https://youtu.be/FPzLE2L7uHs
# Credit: Navdeep Singh founder of NeetCode
def width_of_binary_tree(root):
    if root is None:
        return 0

    q = [(root, 0)]
    width = 0
    while q:
        leftIndex = q[0][1]
        rightIndex = q[-1][1]
        width = max(width, rightIndex - leftIndex + 1)

        for _ in range(len(q)):
            node, index = q.pop(0)
            if node.left:
                q.append((node.left, index * 2))
            if node.right:
                q.append((node.right, index * 2 + 1))
    return width


def main():
    root = get_tree("[1,3,2,5,3,null,9]")
    result = width_of_binary_tree(root)
    print(result) # 4

    root = get_tree("[1,3,2,5,null,null,9,6,null,7]")
    result = width_of_binary_tree(root)
    print(result) # 7

    root = get_tree("[1,3,2,5]")
    result = width_of_binary_tree(root)
    print(result) # 2

if __name__ == "__main__":
    main()
