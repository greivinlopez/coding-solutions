# -------------------------------------------------
# 971. Flip Binary Tree To Match Preorder Traversal
# -------------------------------------------------

# Problem: https://leetcode.com/problems/flip-binary-tree-to-match-preorder-traversal
#
# You are given the root of a binary tree with n nodes, where each node is
# uniquely assigned a value from 1 to n. You are also given a sequence of n values
# voyage, which is the desired pre-order traversal of the binary tree.
# 
# Any node in the binary tree can be flipped by swapping its left and right
# subtrees. For example, flipping node 1 will have the following effect:
# 
# https://assets.leetcode.com/uploads/2021/02/15/fliptree.jpg
# 
# Flip the smallest number of nodes so that the pre-order traversal of the tree
# matches voyage.
# 
# Return a list of the values of all flipped nodes. You may return the answer in
# any order. If it is impossible to flip the nodes in the tree to make the pre-
# order traversal match voyage, return the list [-1].
# 
# Example 1:
# 
# https://assets.leetcode.com/uploads/2019/01/02/1219-01.png
# 
# Input: root = [1,2], voyage = [2,1]
# Output: [-1]
# 
# Explanation: It is impossible to flip the nodes such that the pre-order
# traversal matches voyage.
# 
# Example 2:
# 
# https://assets.leetcode.com/uploads/2019/01/02/1219-02.png
# 
# Input: root = [1,2,3], voyage = [1,3,2]
# Output: [1]
# 
# Explanation: Flipping node 1 swaps nodes 2 and 3, so the pre-order traversal
# matches voyage.
# 
# Example 3:
# 
# https://assets.leetcode.com/uploads/2019/01/02/1219-02.png
# 
# Input: root = [1,2,3], voyage = [1,2,3]
# Output: []
# 
# Explanation: The tree's pre-order traversal already matches voyage, so no nodes
# need to be flipped.
# 
# 
# Constraints:
#         The number of nodes in the tree is n.
#         n == voyage.length
#         1 <= n <= 100
#         1 <= Node.val, voyage[i] <= n
#         All the values in the tree are unique.
#         All the values in voyage are unique.

import sys
import os

# Add the parent directory to sys.path to import miscelaneus tools
current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)

from tree import get_tree

# Solution: https://algo.monster/liteproblems/971
# Credit: AlgoMonster
def flip_match_voyage(root, voyage):
  
    def dfs(node):
        nonlocal voyage_index, is_valid
        
        # Base case: null node or already found invalid
        if node is None or not is_valid:
            return
        
        # Check if current node matches expected value in voyage
        if node.val != voyage[voyage_index]:
            is_valid = False
            return
        
        # Move to next position in voyage
        voyage_index += 1
        
        # Check if we need to flip children
        # If left child is None or matches next expected value, traverse normally
        if node.left is None or node.left.val == voyage[voyage_index]:
            # Normal traversal: left then right
            dfs(node.left)
            dfs(node.right)
        else:
            # Need to flip: traverse right then left
            flipped_nodes.append(node.val)
            dfs(node.right)
            dfs(node.left)
    
    # Initialize variables
    flipped_nodes = []  # List to store nodes that need flipping
    voyage_index = 0    # Current index in voyage array
    is_valid = True     # Flag to track if matching is possible
    
    # Start DFS traversal
    dfs(root)
    
    # Return result based on validity
    return flipped_nodes if is_valid else [-1]
    # Time: O(n)
    # Space: O(n)


def main():
    root = get_tree("[1,2]")
    result = flip_match_voyage(root, [2, 1])
    print(result) # [-1]

    root = get_tree("[1,2,3]")
    result = flip_match_voyage(root, [1, 3, 2])
    print(result) # [1]

    root = get_tree("[1,2,3]")
    result = flip_match_voyage(root, [1, 2, 3])
    print(result) # []

if __name__ == "__main__":
    main()
