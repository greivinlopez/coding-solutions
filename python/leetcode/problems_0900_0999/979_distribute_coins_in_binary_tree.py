# ------------------------------------
# 979. Distribute Coins in Binary Tree
# ------------------------------------

# Problem: https://leetcode.com/problems/distribute-coins-in-binary-tree
#
# You are given the root of a binary tree with n nodes where each node in the tree
# has node.val coins. There are n coins in total throughout the whole tree.
# 
# In one move, we may choose two adjacent nodes and move one coin from one node to
# another. A move may be from parent to child, or from child to parent.
# 
# Return the minimum number of moves required to make every node have exactly one
# coin.
# 
# Example 1:
# 
# Input: root = [3,0,0]
# Output: 2
# 
# Explanation: From the root of the tree, we move one coin to its left child, and
# one coin to its right child.
# 
# Example 2:
# 
# Input: root = [0,3,0]
# Output: 3
# 
# Explanation: From the left child of the root, we move two coins to the root
# [taking two moves]. Then, we move one coin from the root of the tree to the
# right child.
# 
# 
# Constraints:
#         The number of nodes in the tree is n.
#         1 <= n <= 100
#         0 <= Node.val <= n
#         The sum of all Node.val is n.

import sys
import os

# Add the parent directory to sys.path to import miscelaneus tools
current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)

# Import code needed for solutions
from tree import get_tree

# Solution: https://youtu.be/YfdfIOeV_RU
# Credit: Navdeep Singh founder of NeetCode
def distribute_coins(root):
    res = 0

    def dfs(cur):
        nonlocal res
        if not cur:
            return 0 # extra_coins
        
        l_extra = dfs(cur.left)
        r_extra = dfs(cur.right)
        
        extra_coins = cur.val - 1 + l_extra + r_extra
        res += abs(extra_coins)
        return extra_coins
    
    dfs(root)
    return res
    # Time: O(n)    n = number of nodes, h = height of the tree
    # Space: O(h)


def main():
    r = get_tree("[3,0,0]")
    result = distribute_coins(r)
    print(result) # 2

    r = get_tree("[0,3,0]")
    result = distribute_coins(r)
    print(result) # 3

if __name__ == "__main__":
    main()
