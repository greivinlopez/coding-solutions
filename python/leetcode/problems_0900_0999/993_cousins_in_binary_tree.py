# ---------------------------
# 993. Cousins in Binary Tree
# ---------------------------

# Problem: https://leetcode.com/problems/cousins-in-binary-tree
#
# Given the root of a binary tree with unique values and the values of two
# different nodes of the tree x and y, return true if the nodes corresponding to
# the values x and y in the tree are cousins, or false otherwise.
# 
# Two nodes of a binary tree are cousins if they have the same depth with
# different parents.
# 
# Note that in a binary tree, the root node is at the depth 0, and children of
# each depth k node are at the depth k + 1.
# 
# Example 1:
# 
# https://assets.leetcode.com/uploads/2019/02/12/q1248-01.png
# 
# Input: root = [1,2,3,4], x = 4, y = 3
# Output: false
# 
# Example 2:
# 
# https://assets.leetcode.com/uploads/2019/02/12/q1248-02.png
# 
# Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
# Output: true
# 
# Example 3:
# 
# https://assets.leetcode.com/uploads/2019/02/13/q1248-03.png
# 
# Input: root = [1,2,3,null,4], x = 2, y = 3
# Output: false
# 
# 
# Constraints:
#         The number of nodes in the tree is in the range [2, 100].
#         1 <= Node.val <= 100
#         Each node has a unique value.
#         x != y
#         x and y are exist in the tree.

import sys
import os

# Add the parent directory to sys.path to import miscelaneus tools
current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)

from tree import get_tree
from collections import deque

# Solution: https://algo.monster/liteproblems/993
# Credit: AlgoMonster
def is_cousins(root, x, y):
    # Initialize queue for BFS with (node, parent) tuples
    queue = deque([(root, None)])
    
    # Track current depth level
    current_depth = 0
    
    # Variables to store parent and depth information for x and y
    parent_x = parent_y = None
    depth_x = depth_y = None
    
    # Perform level-order traversal (BFS)
    while queue:
        # Process all nodes at the current depth level
        level_size = len(queue)
        
        for _ in range(level_size):
            node, parent = queue.popleft()
            
            # Check if current node matches x or y
            if node.val == x:
                parent_x = parent
                depth_x = current_depth
            elif node.val == y:
                parent_y = parent
                depth_y = current_depth
            
            # Add children to queue for next level
            if node.left:
                queue.append((node.left, node))
            if node.right:
                queue.append((node.right, node))
        
        # Move to next depth level
        current_depth += 1
    
    # Cousins must have different parents but same depth
    return parent_x != parent_y and depth_x == depth_y
    # Time: O(n)
    # Space: O(w)
    # w = maximum width of the tree.


def main():
    root = get_tree("[1,2,3,4]")
    result = is_cousins(root, 4, 3)
    print(result) # False

    root = get_tree("[1,2,3,null,4,null,5]")
    result = is_cousins(root, 5, 4)
    print(result) # True

    root = get_tree("[1,2,3,null,4]")
    result = is_cousins(root, 2, 3)
    print(result) # False

if __name__ == "__main__":
    main()
