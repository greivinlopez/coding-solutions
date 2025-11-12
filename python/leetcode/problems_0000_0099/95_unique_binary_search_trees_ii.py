# ----------------------------------
# 95. Unique Binary Search Trees II
# ----------------------------------

# Problem: https://leetcode.com/problems/unique-binary-search-trees-ii
#
# Given an integer n, return all the structurally unique BST's (binary search
# trees), which has exactly n nodes of unique values from 1 to n. Return the
# answer in any order.
# 
# Example 1:
# 
# Input: n = 3
# Output: [[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]]
# 
# Example 2:
# 
# Input: n = 1
# Output: [[1]]
# 
# 
# Constraints:
#         1 <= n <= 8

import sys
import os

# Add the parent directory to sys.path to import miscelaneus tools
current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)

from tree import TreeNode, serialize_binary_tree

# Solution: https://youtu.be/m907FlQa2Yc
# Credit: Navdeep Singh founder of NeetCode
def generate_trees(n):
    dp = {}
    def generate(left, right):
        if left > right:
            return [None]
        if (left, right) in dp:
            return dp[(left, right)]

        res = []
        for val in range(left, right + 1):
            for leftTree in generate(left, val - 1):
                for rightTree in generate(val + 1, right):
                    root = TreeNode(val, leftTree, rightTree)
                    res.append(root)

        dp[(left, right)] = res
        return res

    return generate(1, n)


def main():
    result = generate_trees(3)
    print( [ serialize_binary_tree(t) for t in result ] )

    result = generate_trees(1)
    print( [ serialize_binary_tree(t) for t in result ] )

if __name__ == "__main__":
    main()
