# ---------------------------------------------
# 1372. Longest ZigZag Path in a Binary Tree 🌲
# ---------------------------------------------

# Problem: https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree
#
# You are given the root of a binary tree.
# 
# A ZigZag path for a binary tree is defined as follow:
#         
#   * Choose any node in the binary tree and a direction (right or left).
#   * If the current direction is right, move to the right child of the current 
#     node; otherwise, move to the left child.
#   * Change the direction from right to left or from left to right.
#   * Repeat the second and third steps until you can't move in the tree.
# 
# Zigzag length is defined as the number of nodes visited - 1. (A single node has
# a length of 0).
# 
# Return the longest ZigZag path contained in that tree.
# 
# Example 1:
# 
# https://assets.leetcode.com/uploads/2020/01/22/sample_1_1702.png
# 
# Input: root = [1,null,1,1,1,null,null,1,1,null,1,null,null,null,1]
# Output: 3
# 
# Explanation: Longest ZigZag path in blue nodes (right -> left -> right).
# 
# Example 2:
# 
# https://assets.leetcode.com/uploads/2020/01/22/sample_2_1702.png
# 
# Input: root = [1,1,1,null,1,null,null,1,1,null,1]
# Output: 4
# 
# Explanation: Longest ZigZag path in blue nodes (left -> right -> left -> right).
# 
# Example 3:
# 
# Input: root = [1]
# Output: 0
# 
# 
# Constraints:
#         The number of nodes in the tree is in the range [1, 5 * 10⁴].
#         1 <= Node.val <= 100

import sys
import os

# Add the parent directory to sys.path to import miscelaneus tools
current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)

from tree import get_tree

# Solution: https://algo.monster/liteproblems/1372
# Credit: AlgoMonster
def longest_zig_zag(root):
    
    def dfs(node, left_length, right_length):
        # Base case: if node is None, return
        if node is None:
            return
        
        # Update the maximum zigzag length found so far
        nonlocal max_length
        max_length = max(max_length, left_length, right_length)
        
        # Move to left child: 
        # - If we came from left (right_length), we continue the zigzag
        # - Reset the other direction to 0
        dfs(node.left, right_length + 1, 0)
        
        # Move to right child:
        # - If we came from right (left_length), we continue the zigzag  
        # - Reset the other direction to 0
        dfs(node.right, 0, left_length + 1)
    
    # Initialize the maximum zigzag length
    max_length = 0
    
    # Start DFS from root with both directions at 0
    dfs(root, 0, 0)
    
    return max_length
    # Time: O(n)
    # Space: O(h)
    # n = the number of nodes in the binary tree
    # h = the height of the binary tree. 


def main():
    root = get_tree("[1,null,1,1,1,null,null,1,1,null,1,null,null,null,1]")
    result = longest_zig_zag(root)
    print(result) # 3

    root = get_tree("[1,1,1,null,1,null,null,1,1,null,1]")
    result = longest_zig_zag(root)
    print(result) # 4

    root = get_tree("[1]")
    result = longest_zig_zag(root)
    print(result) # 0

if __name__ == "__main__":
    main()
