# ---------------------
# 337. House Robber III
# ---------------------

# Problem: https://leetcode.com/problems/house-robber-iii
#
# The thief has found himself a new place for his thievery again. There is only
# one entrance to this area, called root.
# 
# Besides the root, each house has one and only one parent house. After a tour,
# the smart thief realized that all houses in this place form a binary tree. It
# will automatically contact the police if two directly-linked houses were broken
# into on the same night.
# 
# Given the root of the binary tree, return the maximum amount of money the thief
# can rob without alerting the police.
# 
# Example 1:
# 
# Input: root = [3,2,3,null,3,null,1]
# Output: 7
# 
# Explanation: Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.
# 
# Example 2:
# 
# Input: root = [3,4,5,1,3,null,1]
# Output: 9
# 
# Explanation: Maximum amount of money the thief can rob = 4 + 5 = 9.
# 
# 
# Constraints:
#         The number of nodes in the tree is in the range [1, 10^4].
#         0 <= Node.val <= 10^4

import sys
import os

# Add the parent directory to sys.path to import miscelaneus tools
current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)

# Import code needed for solutions
from tree import get_tree

# Solution: https://youtu.be/nHR8ytpzz7c
# Credit: Navdeep Singh founder of NeetCode
def rob(root):
    
    def dfs(root):
        if not root:
            return [0, 0]

        left_pair = dfs(root.left)
        right_pair = dfs(root.right)

        with_root = root.val + left_pair[1] + right_pair[1]
        without_root = max(left_pair) + max(right_pair)

        return [with_root, without_root]

    return max(dfs(root))
    # Time: O(n)
    # Space: O(h)  where h is the height of the binary tree


def main():
    root = get_tree("[3,2,3,null,3,null,1]")
    result = rob(root)
    print(result) # 7

    root = get_tree("[3,4,5,1,3,null,1]")
    result = rob(root)
    print(result) # 9

if __name__ == "__main__":
    main()
