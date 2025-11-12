# ---------------------------------
# 111. Minimum Depth of Binary Tree
# ---------------------------------

# Problem: https://leetcode.com/problems/minimum-depth-of-binary-tree
#
# Given a binary tree, find its minimum depth.
# 
# The minimum depth is the number of nodes along the shortest path from the root
# node down to the nearest leaf node.
# 
# Note: A leaf is a node with no children.
# 
# Example 1:
# 
# https://assets.leetcode.com/uploads/2020/10/12/ex_depth.jpg
# 
# Input: root = [3,9,20,null,null,15,7]
# Output: 2
# 
# Example 2:
# 
# Input: root = [2,null,3,null,4,null,5,null,6]
# Output: 5
# 
# 
# Constraints:
#         The number of nodes in the tree is in the range [0, 10⁵].
#         -1000 <= Node.val <= 1000

import sys
import os

# Add the parent directory to sys.path to import miscelaneus tools
current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)

from tree import get_tree
from collections import deque

# Solution: https://leetcode.com/problems/minimum-depth-of-binary-tree/solutions/6108825/0-ms-runtime-beats-100-user-code-idea-algorithm-solving-step
# Credit: Ravaan -> https://leetcode.com/u/ChinaTrigger/
def min_depth(root):
    if not root:
        return 0  # If the tree is empty, return depth 0
    
    queue = deque([(root, 1)])  # Initialize the queue with the root node and depth 1
    
    while queue:
        node, depth = queue.popleft()
        
        # If it's a leaf node, return the current depth
        if not node.left and not node.right:
            return depth
        
        # Add left and right children to the queue, if they exist
        if node.left:
            queue.append((node.left, depth + 1))
        if node.right:
            queue.append((node.right, depth + 1))
    # Time: O(n)
    # Space: O(n)


def main():
    root = get_tree("[3,9,20,null,null,15,7]")
    result = min_depth(root)
    print(result) # 2

    root = get_tree("[2,null,3,null,4,null,5,null,6]")
    result = min_depth(root)
    print(result) # 5

if __name__ == "__main__":
    main()
