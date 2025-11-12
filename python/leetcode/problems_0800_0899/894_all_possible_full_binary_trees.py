# -----------------------------------
# 894. All Possible Full Binary Trees
# -----------------------------------

# Problem: https://leetcode.com/problems/all-possible-full-binary-trees/
# 
# Given an integer n, return a list of all possible full binary trees with n 
# nodes. Each node of each tree in the answer must have Node.val == 0.
# 
# Each element of the answer is the root node of one possible tree. You may 
# return the final list of trees in any order.
# 
# A full binary tree is a binary tree where each node has exactly 0 or 2 
# children.
# 
# 
# Example 1:
# 
# Input: n = 7
# Output: [[0,0,0,null,null,0,0,null,null,0,0],[0,0,0,null,null,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,null,null,null,null,0,0],[0,0,0,0,0,null,null,0,0]]
# 
# Example 2:
# 
# Input: n = 3
# Output: [[0,0,0]]
#  
# 
# Constraints:
# 
#   1 <= n <= 20

import sys
import os

# Add the parent directory to sys.path to import miscelaneus tools
current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)

# Import code needed for solutions
from tree import TreeNode

# Solution: https://youtu.be/nZtrZPTTCAo
# Credit: Navdeep Singh founder of NeetCode
def all_possible_FBT(n):
    dp = { 0 : [], 1 : [ TreeNode() ] }

    def backtrack(n):
        if n in dp:
            return dp[n]
        
        res = []
        for l in range(n):
            r = n - 1 - l
            leftTrees, rightTrees = backtrack(l), backtrack(r)

            for t1 in leftTrees:
                for t2 in rightTrees:
                    res.append(TreeNode(0, t1, t2))
        dp[n] = res
        return res
    
    return backtrack(n)


def main():
    trees = all_possible_FBT(7)
    for t in trees:
        print(t)
    # [0, 0, 0, None, None, 0, 0, None, None, 0, 0]
    # [0, 0, 0, None, None, 0, 0, 0, 0]
    # [0, 0, 0, 0, 0, 0, 0]
    # [0, 0, 0, 0, 0, None, None, None, None, 0, 0]
    # [0, 0, 0, 0, 0, None, None, 0, 0]

if __name__ == "__main__":
    main()
