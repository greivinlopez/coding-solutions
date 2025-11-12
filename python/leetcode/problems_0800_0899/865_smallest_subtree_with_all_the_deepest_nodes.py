# ------------------------------------------------
# 865. Smallest Subtree with all the Deepest Nodes
# ------------------------------------------------

# Problem: https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes
#
# Given the root of a binary tree, the depth of each node is the shortest distance
# to the root.
# 
# Return the smallest subtree such that it contains all the deepest nodes in the
# original tree.
# 
# A node is called the deepest if it has the largest depth possible among any node
# in the entire tree.
# 
# The subtree of a node is a tree consisting of that node, plus the set of all
# descendants of that node.
# 
# Example 1:
# 
# https://s3-lc-upload.s3.amazonaws.com/uploads/2018/07/01/sketch1.png
# 
# Input: root = [3,5,1,6,2,0,8,null,null,7,4]
# Output: [2,7,4]
# 
# Explanation: We return the node with value 2, colored in yellow in the diagram.
# The nodes coloured in blue are the deepest nodes of the tree.
# Notice that nodes 5, 3 and 2 contain the deepest nodes in the tree but node 2 is
# the smallest subtree among them, so we return it.
# 
# Example 2:
# 
# Input: root = [1]
# Output: [1]
# 
# Explanation: The root is the deepest node in the tree.
# 
# Example 3:
# 
# Input: root = [0,1,3,null,2]
# Output: [2]
# 
# Explanation: The deepest node in the tree is 2, the valid subtrees are the
# subtrees of nodes 2, 1 and 0 but the subtree of node 2 is the smallest.
# 
# 
# Constraints:
#         
#   The number of nodes in the tree will be in the range [1, 500].
#   0 <= Node.val <= 500
#   The values of the nodes in the tree are unique.
# 
# Note: This question is the same as 
# 1123: https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/

import sys
import os

# Add the parent directory to sys.path to import miscelaneus tools
current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)

from tree import get_tree


# Solution: https://algo.monster/liteproblems/865
# Credit: AlgoMonster
def subtree_with_all_deepest(root):

    def dfs(node):
        # Base case: if node is None, return None with depth 0
        if node is None:
            return None, 0
        
        # Recursively process left and right subtrees
        left_subtree, left_depth = dfs(node.left)
        right_subtree, right_depth = dfs(node.right)
        
        # If left subtree is deeper, all deepest nodes are in the left subtree
        if left_depth > right_depth:
            return left_subtree, left_depth + 1
        
        # If right subtree is deeper, all deepest nodes are in the right subtree
        if left_depth < right_depth:
            return right_subtree, right_depth + 1
        
        # If both subtrees have the same depth, current node is the LCA of all deepest nodes
        return node, left_depth + 1
    
    # Return only the node from the tuple (discard the depth)
    return dfs(root)[0]
    # Time: O(n)
    # Space: O(n)


def main():
    root = get_tree("[3,5,1,6,2,0,8,null,null,7,4]")
    result = subtree_with_all_deepest(root)
    print(result) # [2, 7, 4]

    root = get_tree("[1]")
    result = subtree_with_all_deepest(root)
    print(result) # [1]

    root = get_tree("[0,1,3,null,2]")
    result = subtree_with_all_deepest(root)
    print(result) # [2]

if __name__ == "__main__":
    main()
