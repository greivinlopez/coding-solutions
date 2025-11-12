# -----------------
# 437. Path Sum III
# -----------------

# Problem: https://leetcode.com/problems/path-sum-iii
#
# Given the root of a binary tree and an integer targetSum, return the number of
# paths where the sum of the values along the path equals targetSum.
# 
# The path does not need to start or end at the root or a leaf, but it must go
# downwards (i.e., traveling only from parent nodes to child nodes).
# 
# Example 1:
# 
# https://assets.leetcode.com/uploads/2021/04/09/pathsum3-1-tree.jpg
# 
# Input: root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
# Output: 3
# 
# Explanation: The paths that sum to 8 are shown.
# 
# Example 2:
# 
# Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
# Output: 3
# 
# 
# Constraints:
#         The number of nodes in the tree is in the range [0, 1000].
#         -10⁹ <= Node.val <= 10⁹
#         -1000 <= targetSum <= 1000

import sys
import os

# Add the parent directory to sys.path to import miscelaneus tools
current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)

from tree import get_tree
from collections import Counter

# Solution: https://algo.monster/liteproblems/437
# Credit: AlgoMonster
def path_sum(root, targetSum):
    
    def dfs(node, current_sum):
        # Base case: empty node contributes no paths
        if node is None:
            return 0
        
        # Update cumulative sum to include current node
        current_sum += node.val
        
        # Count paths ending at current node with sum equal to targetSum
        # We look for (current_sum - targetSum) in our prefix sum counter
        # If it exists, those occurrences represent valid starting points
        path_count = prefix_sum_count[current_sum - targetSum]
        
        # Add current prefix sum to counter for use by descendant nodes
        prefix_sum_count[current_sum] += 1
        
        # Recursively count paths in left and right subtrees
        path_count += dfs(node.left, current_sum)
        path_count += dfs(node.right, current_sum)
        
        # Backtrack: remove current sum from counter as we return up the tree
        # This ensures the counter only contains sums from the current path
        prefix_sum_count[current_sum] -= 1
        
        return path_count
    
    # Initialize prefix sum counter with 0:1 to handle paths starting from root
    prefix_sum_count = Counter({0: 1})
    
    # Start DFS from root with initial sum of 0
    return dfs(root, 0)


def main():
    root = get_tree("[10,5,-3,3,2,null,11,3,-2,null,1]")
    result = path_sum(root, 8)
    print(result) # 3

    root = get_tree("[5,4,8,11,null,13,4,7,2,null,null,5,1]")
    result = path_sum(root, 22)
    print(result) # 3

if __name__ == "__main__":
    main()
