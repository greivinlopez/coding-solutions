# ----------------------------
# 543. Diameter Of Binary Tree
# ----------------------------

# Problem: https://leetcode.com/problems/diameter-of-binary-tree/
# 
# Given the root of a binary tree, return the length of the diameter of the 
# tree.
# 
# The diameter of a binary tree is the length of the longest path between any 
# two nodes in a tree. This path may or may not pass through the root.
# 
# The length of a path between two nodes is represented by the number of edges 
# between them.
#  
# 
# Example 1:
# 
# Input: root = [1,2,3,4,5]
# Output: 3
# Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].
# 
# 
# Example 2:
# 
# Input: root = [1,2]
# Output: 1
# 
#  
# Constraints:
# 
# 	The number of nodes in the tree is in the range [1, 10^4].
# 	-100 <= Node.val <= 100

import sys
import os

# Add the parent directory to sys.path to import miscelaneus tools
current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)

# Import code needed for solutions
from tree import get_tree

# Solution: https://youtu.be/K81C31ytOZE
# Credit: Navdeep Singh founder of NeetCode
def diameter_of_binary_tree(root) -> int:
    res = 0

    def dfs(root):
        nonlocal res

        if not root:
            return 0
        left = dfs(root.left)
        right = dfs(root.right)
        res = max(res, left + right)

        return 1 + max(left, right)

    dfs(root)
    return res

# Solution: https://youtu.be/6lJZ_xj1mEo
# Credit: Greg Hogg
# Same Solution
def diameter_of_binary_tree_alt(root) -> int:
    largest_diameter = [0]

    def height(root):
        if root is None:
            return 0

        left_height = height(root.left)
        right_height = height(root.right)
        diameter = left_height + right_height

        largest_diameter[0] = max(largest_diameter[0], diameter)
        
        return 1 + max(left_height, right_height)

    height(root)
    return largest_diameter[0]
    # Time: O(n)
    # Space: O(h) { here "h" is the height of the tree }


def main():
    root = get_tree("[1,2,3,4,5]")
    result = diameter_of_binary_tree(root)
    print(result) # 3

    root = get_tree("[1,2]")
    result = diameter_of_binary_tree(root)
    print(result) # 1

if __name__ == "__main__":
    main()
