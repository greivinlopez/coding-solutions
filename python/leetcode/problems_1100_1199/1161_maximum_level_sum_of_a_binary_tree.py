# ----------------------------------------
# 1161. Maximum Level Sum of a Binary Tree
# ----------------------------------------

# Problem: https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree
#
# Given the root of a binary tree, the level of its root is 1, the level of its
# children is 2, and so on.
# 
# Return the smallest level x such that the sum of all the values of nodes at
# level x is maximal.
# 
# Example 1:
# 
# https://assets.leetcode.com/uploads/2019/05/03/capture.JPG
# 
# Input: root = [1,7,0,7,-8,null,null]
# Output: 2
# 
# Explanation:
# Level 1 sum = 1.
# Level 2 sum = 7 + 0 = 7.
# Level 3 sum = 7 + -8 = -1.
# So we return the level with the maximum sum which is level 2.
# 
# Example 2:
# 
# Input: root = [989,null,10250,98693,-89388,null,null,null,-32127]
# Output: 2
# 
# 
# Constraints:
#         The number of nodes in the tree is in the range [1, 10⁴].
#         -10⁵ <= Node.val <= 10⁵

import sys
import os

# Add the parent directory to sys.path to import miscelaneus tools
current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)

from tree import get_tree
from collections import deque
from math import inf

# Solution: https://algo.monster/liteproblems/1161
# Credit: AlgoMonster
def max_level_sum(root):
    # Initialize queue for BFS with root node
    queue = deque([root])
    
    # Track maximum sum found so far
    max_sum = -inf
    
    # Current level number (1-indexed)
    current_level = 0
    
    # Result level with maximum sum
    result_level = 0
    
    # Process each level of the tree
    while queue:
        current_level += 1
        
        # Calculate sum for current level
        level_sum = 0
        
        # Process all nodes at current level
        level_size = len(queue)
        for _ in range(level_size):
            node = queue.popleft()
            level_sum += node.val
            
            # Add children to queue for next level
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        # Update maximum sum and corresponding level if needed
        if max_sum < level_sum:
            max_sum = level_sum
            result_level = current_level
    
    return result_level
    # Time: O(n)
    # Space: O(n)


def main():
    root = get_tree("[1,7,0,7,-8,null,null]")
    result = max_level_sum(root)
    print(result) # 2

    root = get_tree("[989,null,10250,98693,-89388,null,null,null,-32127]")
    result = max_level_sum(root)
    print(result) # 2

if __name__ == "__main__":
    main()
