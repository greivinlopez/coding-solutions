# -----------------------------
# 687. Longest Univalue Path 🌲
# -----------------------------

# Problem: https://leetcode.com/problems/longest-univalue-path
#
# Given the root of a binary tree, return the length of the longest path, where
# each node in the path has the same value. This path may or may not pass through
# the root.
# 
# The length of the path between two nodes is represented by the number of edges
# between them.
# 
# Example 1:
# 
# https://assets.leetcode.com/uploads/2020/10/13/ex1.jpg
# 
# Input: root = [5,4,5,1,1,null,5]
# Output: 2
# 
# Explanation: The shown image shows that the longest path of the same value (i.e.
# 5).
# 
# Example 2:
# 
# https://assets.leetcode.com/uploads/2020/10/13/ex2.jpg
# 
# Input: root = [1,4,5,4,4,null,5]
# Output: 2
# 
# Explanation: The shown image shows that the longest path of the same value (i.e.
# 4).
# 
# 
# Constraints:
#         The number of nodes in the tree is in the range [0, 10⁴].
#         -1000 <= Node.val <= 1000
#         The depth of the tree will not exceed 1000.

import sys
import os

# Add the parent directory to sys.path to import miscelaneus tools
current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)

from tree import get_tree

# Solution: https://algo.monster/liteproblems/687
# Credit: AlgoMonster
def longest_univalue_path(root):
    max_path_length = 0
    
    def calculate_univalue_length(node) -> int:
        nonlocal max_path_length

        # Base case: if node is None, return 0
        if node is None:
            return 0
        
        # Recursively calculate the univalue length for left and right subtrees
        left_length = calculate_univalue_length(node.left)
        right_length = calculate_univalue_length(node.right)
        
        # If left child exists and has the same value, extend the left path
        # Otherwise, reset to 0
        left_arrow_length = left_length + 1 if node.left and node.left.val == node.val else 0
        
        # If right child exists and has the same value, extend the right path
        # Otherwise, reset to 0
        right_arrow_length = right_length + 1 if node.right and node.right.val == node.val else 0
        
        # Update the global maximum with the path passing through current node
        # (connecting left and right paths)
        max_path_length = max(max_path_length, left_arrow_length + right_arrow_length)
        
        # Return the longer single direction path for parent node to use
        return max(left_arrow_length, right_arrow_length)
    
    # Start the DFS traversal from root
    calculate_univalue_length(root)
    
    # Return the maximum path length found
    return max_path_length
    # Time: O(n)
    # Space: O(n)


def main():
    root = get_tree("[5,4,5,1,1,null,5]")
    result = longest_univalue_path(root)
    print(result) # 2

    root = get_tree("[1,4,5,4,4,null,5]")
    result = longest_univalue_path(root)
    print(result) # 2

if __name__ == "__main__":
    main()
