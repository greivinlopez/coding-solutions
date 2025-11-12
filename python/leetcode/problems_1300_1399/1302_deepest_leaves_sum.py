# ---------------------------
# 1302. Deepest Leaves Sum 🍃
# ---------------------------

# Problem: https://leetcode.com/problems/deepest-leaves-sum
#
# Given the root of a binary tree, return the sum of values of its deepest leaves.
# 
# Example 1:
# 
# https://assets.leetcode.com/uploads/2019/07/31/1483_ex1.png
# 
# Input: root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
# Output: 15
# 
# Example 2:
# 
# Input: root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
# Output: 19
# 
# 
# Constraints:
#         The number of nodes in the tree is in the range [1, 10⁴].
#         1 <= Node.val <= 100

import sys
import os

# Add the parent directory to sys.path to import miscelaneus tools
current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)

from tree import get_tree
from collections import deque

# Solution: https://algo.monster/liteproblems/1302
# Credit: AlgoMonster
def deepest_leaves_sum(root):
    # Initialize queue with root node for BFS traversal
    queue = deque([root])
    
    # Process each level of the tree
    while queue:
        # Reset sum for current level
        current_level_sum = 0
        # Get the number of nodes at current level
        level_size = len(queue)
        
        # Process all nodes at the current level
        for _ in range(level_size):
            # Get next node from queue
            current_node = queue.popleft()
            # Add node's value to current level sum
            current_level_sum += current_node.val
            
            # Add children to queue for next level processing
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
    
    # Return sum of the last (deepest) level processed
    return current_level_sum
    # Time: O(n)
    # Space: O(n)


def main():
    root = get_tree("[1,2,3,4,5,null,6,7,null,null,null,null,8]")
    result = deepest_leaves_sum(root)
    print(result) # 15

    root = get_tree("[6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]")
    result = deepest_leaves_sum(root)
    print(result) # 19

if __name__ == "__main__":
    main()
