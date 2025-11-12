# ----------------------------------------------------------------
# 2096. Step-By-Step Directions From a Binary Tree Node to Another
# ----------------------------------------------------------------

# Problem: https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another
#
# You are given the root of a binary tree with n nodes. Each node is uniquely
# assigned a value from 1 to n. You are also given an integer startValue
# representing the value of the start node s, and a different integer destValue
# representing the value of the destination node t.
# 
# Find the shortest path starting from node s and ending at node t. Generate step-
# by-step directions of such path as a string consisting of only the uppercase
# letters 'L', 'R', and 'U'. Each letter indicates a specific direction:
#         
#   'L' means to go from a node to its left child node.
#   'R' means to go from a node to its right child node.
#   'U' means to go from a node to its parent node.
# 
# Return the step-by-step directions of the shortest path from node s to node t.
# 
# Example 1:
# 
# Input: root = [5,1,2,3,null,6,4], startValue = 3, destValue = 6
# Output: "UURL"
# Explanation: The shortest path is: 3 → 1 → 5 → 2 → 6.
# 
# Example 2:
# 
# Input: root = [2,1], startValue = 2, destValue = 1
# Output: "L"
# 
# Explanation: The shortest path is: 2 → 1.
# 
# 
# Constraints:
#         The number of nodes in the tree is n.
#         2 <= n <= 10⁵
#         1 <= Node.val <= n
#         All the values in the tree are unique.
#         1 <= startValue, destValue <= n
#         startValue != destValue

import sys
import os

# Add the parent directory to sys.path to import miscelaneus tools
current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)

from tree import get_tree

# Solution: https://youtu.be/JegJNGcwtFg
# Credit: Navdeep Singh founder of NeetCode
def get_directions(root, startValue, destValue):
    def dfs(node, path, target):
        if not node:
            return ""
        if node.val == target:
            return path
        path.append("L")
        res = dfs(node.left, path, target)
        if res:
            return res
        path.pop()
        path.append("R")
        res = dfs(node.right, path, target)
        if res:
            return res
        path.pop()
        return ""
    start_path = dfs(root, [], startValue)
    dest_path = dfs(root, [], destValue)
    i = 0
    while i < len(start_path) and i < len(dest_path):
        if start_path[i] != dest_path[i]:
            break
        i += 1
    res = ["U"] * len(start_path[i:]) + dest_path[i:]
    return "".join(res)
    # Time: O(n)
    # Space: O(h)
    # n = number of nodes in the tree
    # h = height of the tree


def main():
    root = get_tree("[5,1,2,3,null,6,4]")
    result = get_directions(root, startValue = 3, destValue = 6)
    print(result) # "UURL"

    root = get_tree("[2,1]")
    result = get_directions(root, startValue = 2, destValue = 1)
    print(result) # "L"

if __name__ == "__main__":
    main()
