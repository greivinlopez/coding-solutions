# ---------------------------------------------
# 1080. Insufficient Nodes in Root to Leaf Paths
# ---------------------------------------------

# Problem: https://leetcode.com/problems/insufficient-nodes-in-root-to-leaf-paths
#
# Given the root of a binary tree and an integer limit, delete all insufficient
# nodes in the tree simultaneously, and return the root of the resulting binary
# tree.
# 
# A node is insufficient if every root to leaf path intersecting this node has a
# sum strictly less than limit.
# 
# A leaf is a node with no children.
# 
# Example 1:
# 
# https://assets.leetcode.com/uploads/2019/06/05/insufficient-11.png
# 
# Input: root = [1,2,3,4,-99,-99,7,8,9,-99,-99,12,13,-99,14], limit = 1
# Output: [1,2,3,4,null,null,7,8,9,null,14]
# 
# Example 2:
# 
# https://assets.leetcode.com/uploads/2019/06/05/insufficient-3.png
# 
# Input: root = [5,4,8,11,null,17,4,7,1,null,null,5,3], limit = 22
# Output: [5,4,8,11,null,17,4,7,null,null,null,5]
# 
# Example 3:
# 
# https://assets.leetcode.com/uploads/2019/06/11/screen-shot-2019-06-11-at-83301-pm.png
# 
# Input: root = [1,2,-3,-5,null,4,null], limit = -1
# Output: [1,null,-3,4]
# 
# 
# Constraints:
#         The number of nodes in the tree is in the range [1, 5000].
#         -10⁵ <= Node.val <= 10⁵
#         -10⁹ <= limit <= 10⁹

import sys
import os

# Add the parent directory to sys.path to import miscelaneus tools
current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)

from tree import get_tree

# Solution: https://algo.monster/liteproblems/1080
# Credit: AlgoMonster
def sufficient_subset(root, limit):
    # Base case: empty tree
    if root is None:
        return None
    
    # Subtract current node's value from limit for recursive calls
    # This tracks the remaining sum needed for paths below this node
    limit -= root.val
    
    # Leaf node case: check if the path sum meets the threshold
    if root.left is None and root.right is None:
        # If limit > 0, the path sum is insufficient (sum < original limit)
        # Return None to remove this leaf, otherwise keep it
        return None if limit > 0 else root
    
    # Recursively process left and right subtrees
    # Pass the updated limit to check sufficiency of child paths
    root.left = sufficient_subset(root.left, limit)
    root.right = sufficient_subset(root.right, limit)
    
    # After processing children, check if current node should be removed
    # If both children were removed (both are None), this node leads to no sufficient paths
    # Remove it by returning None, otherwise keep the node
    return None if root.left is None and root.right is None else root
    # Time: O(n)
    # Space: O(h)
    # n = the number of nodes in the binary tree
    # h = the height of the binary tree.


def main():
    root = get_tree("[1,2,3,4,-99,-99,7,8,9,-99,-99,12,13,-99,14]")
    result = sufficient_subset(root, 1)
    print(result) # [1, 2, 3, 4, None, None, 7, 8, 9, None, 14]

    root = get_tree("[5,4,8,11,null,17,4,7,1,null,null,5,3]")
    result = sufficient_subset(root, 22)
    print(result) # [5, 4, 8, 11, None, 17, 4, 7, None, None, None, 5]

    root = get_tree("[1,2,-3,-5,null,4,null]")
    result = sufficient_subset(root, -1)
    print(result) # [1, None, -3, 4]

if __name__ == "__main__":
    main()
