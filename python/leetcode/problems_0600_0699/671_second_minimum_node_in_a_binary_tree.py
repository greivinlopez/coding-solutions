# -----------------------------------------
# 671. Second Minimum Node In a Binary Tree
# -----------------------------------------

# Problem: https://leetcode.com/problems/second-minimum-node-in-a-binary-tree
#
# Given a non-empty special binary tree consisting of nodes with the non-negative
# value, where each node in this tree has exactly two or zero sub-node. If the
# node has two sub-nodes, then this node's value is the smaller value among its
# two sub-nodes. More formally, the property root.val = min(root.left.val,
# root.right.val) always holds.
# 
# Given such a binary tree, you need to output the second minimum value in the set
# made of all the nodes' value in the whole tree.
# 
# If no such second minimum value exists, output -1 instead.
# 
# Example 1:
# 
# https://assets.leetcode.com/uploads/2020/10/15/smbt1.jpg
# 
# Input: root = [2,2,5,null,null,5,7]
# Output: 5
# 
# Explanation: The smallest value is 2, the second smallest value is 5.
# 
# Example 2:
# 
# https://assets.leetcode.com/uploads/2020/10/15/smbt2.jpg
# 
# Input: root = [2,2,2]
# Output: -1
# 
# Explanation: The smallest value is 2, but there isn't any second smallest value.
# 
# 
# Constraints:
#   The number of nodes in the tree is in the range [1, 25].
#   1 <= Node.val <= 2³¹ - 1
#   root.val == min(root.left.val, root.right.val) for each internal node of the tree.

import sys
import os

# Add the parent directory to sys.path to import miscelaneus tools
current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)

from tree import get_tree

# Solution: https://algo.monster/liteproblems/671
# Credit: AlgoMonster
def find_second_minimum_value(root):   
    def dfs(node):
        # Base case: if node is None, return
        if not node:
            return
        
        # Recursively traverse left and right subtrees
        dfs(node.left)
        dfs(node.right)
        
        # Access outer scope variables
        nonlocal second_min, first_min
        
        # If current node value is greater than the minimum (root value),
        # it's a candidate for second minimum
        if node.val > first_min:
            # Update second_min: either set it for first time or take minimum
            if second_min == -1:
                second_min = node.val
            else:
                second_min = min(second_min, node.val)
    
    # Initialize variables
    # second_min: stores the second minimum value (-1 if not found)
    # first_min: stores the minimum value (which is always the root value)
    second_min = -1
    first_min = root.val
    
    # Start DFS traversal from root
    dfs(root)
    
    # Return the second minimum value
    return second_min
    # Time: O(n)
    # Space: O(h)
    # n = the number of nodes in the binary tree
    # h = the height of the binary tree.


def main():
    root = get_tree("[2,2,5,null,null,5,7]")
    result = find_second_minimum_value(root)
    print(result) # 5

    root = get_tree("[2,2,2]")
    result = find_second_minimum_value(root)
    print(result) # -1

if __name__ == "__main__":
    main()
