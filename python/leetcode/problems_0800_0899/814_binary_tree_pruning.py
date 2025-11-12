# ------------------------
# 814. Binary Tree Pruning
# ------------------------

# Problem: https://leetcode.com/problems/binary-tree-pruning
#
# Given the root of a binary tree, return the same tree where every subtree (of
# the given tree) not containing a 1 has been removed.
# 
# A subtree of a node node is node plus every node that is a descendant of node.
# 
# Example 1:
# 
# https://s3-lc-upload.s3.amazonaws.com/uploads/2018/04/06/1028_2.png
# 
# Input: root = [1,null,0,0,1]
# Output: [1,null,0,null,1]
# 
# Explanation:
# Only the red nodes satisfy the property "every subtree not containing a 1".
# The diagram on the right represents the answer.
# 
# Example 2:
# 
# https://s3-lc-upload.s3.amazonaws.com/uploads/2018/04/06/1028_1.png
# 
# Input: root = [1,0,1,0,0,0,1]
# Output: [1,null,1,null,1]
# 
# Example 3:
# 
# https://s3-lc-upload.s3.amazonaws.com/uploads/2018/04/05/1028.png
# 
# Input: root = [1,1,0,1,1,0,1,0]
# Output: [1,1,0,1,1,null,1]
# 
# 
# Constraints:
#         The number of nodes in the tree is in the range [1, 200].
#         Node.val is either 0 or 1.

import sys
import os

# Add the parent directory to sys.path to import miscelaneus tools
current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)

from tree import get_tree

# Solution: https://algo.monster/liteproblems/814
# Credit: AlgoMonster
def prune_tree(root):
    # Base case: if the node is None, return None
    if root is None:
        return root
    
    # Recursively prune the left subtree
    root.left = prune_tree(root.left)
    
    # Recursively prune the right subtree
    root.right = prune_tree(root.right)
    
    # If current node has value 0 and both children are None (or pruned),
    # then this node should be pruned as well
    # Note: root.left == root.right checks if both are None
    if root.val == 0 and root.left == root.right:
        return None
    
    # Otherwise, keep this node in the tree
    return root
    # Time: O(n)
    # Space: O(n)


def main():
    root1 = get_tree("[1,null,0,0,1]")
    result = prune_tree(root1)
    print(result) # [1, None, 0, None, 1]

    root2 = get_tree("[1,0,1,0,0,0,1]")
    result = prune_tree(root2)
    print(result) # [1, None, 1, None, 1]

    root3 = get_tree("[1,1,0,1,1,0,1,0]")
    result = prune_tree(root3)
    print(result) # [1, 1, 0, 1, 1, None, 1]

if __name__ == "__main__":
    main()
