# -------------------------------
# 652. Find Duplicate Subtrees 🌲
# -------------------------------

# Problem: https://leetcode.com/problems/find-duplicate-subtrees
#
# Given the root of a binary tree, return all duplicate subtrees.
# 
# For each kind of duplicate subtrees, you only need to return the root node of
# any one of them.
# 
# Two trees are duplicate if they have the same structure with the same node
# values.
# 
# Example 1:
# 
# Input: root = [1,2,3,4,null,2,4,null,null,4]
# Output: [[2,4],[4]]
# 
# Example 2:
# 
# Input: root = [2,1,1]
# Output: [[1]]
# 
# Example 3:
# 
# Input: root = [2,2,2,3,null,3,null]
# Output: [[2,3],[3]]
# 
# 
# Constraints:
#         The number of the nodes in the tree will be in the range [1, 5000]
#         -200 <= Node.val <= 200

import sys
import os

# Add the parent directory to sys.path to import miscelaneus tools
current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)

# Import code needed for solutions
from tree import get_tree
from collections import defaultdict

# Solution: https://youtu.be/kn0Z5_qPPzY
# Credit: Navdeep Singh founder of NeetCode
def find_duplicate_subtrees(root):
    subtrees = defaultdict(list)
    res = []

    def dfs(node):
        if not node:
            return "null"

        s = ",".join([
            str(node.val),
            dfs(node.left),
            dfs(node.right)
        ])
        
        if len(subtrees[s]) == 1:
            res.append(node)
        
        subtrees[s].append(node)
        
        return s
        
    dfs(root)
    return res
    # Time: O(n)
    # Space: O(n)


def main():
    root = get_tree("[1,2,3,4,null,2,4,null,null,4]")
    result = find_duplicate_subtrees(root)
    for t in result:
        print(t)
    print("--------")

    root = get_tree("[2,1,1]")
    result = find_duplicate_subtrees(root)
    for t in result:
        print(t)
    print("--------")

    root = get_tree("[2,2,2,3,null,3,null]")
    result = find_duplicate_subtrees(root)
    for t in result:
        print(t)
    print("--------")

if __name__ == "__main__":
    main()
