# -------------------------------------------------
# 1123. Lowest Common Ancestor of Deepest Leaves 🍂
# -------------------------------------------------

# Problem: https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves
#
# Given the root of a binary tree, return the lowest common ancestor of its
# deepest leaves.
# 
# Recall that:
#         
#   * The node of a binary tree is a leaf if and only if it has no children         
#   * The depth of the root of the tree is 0. if the depth of a node is d, the
#     depth of each of its children is d + 1.
#   * The lowest common ancestor of a set S of nodes, is the node A with the
#     largest depth such that every node in S is in the subtree with root A.
# 
# Example 1:
# 
# https://s3-lc-upload.s3.amazonaws.com/uploads/2018/07/01/sketch1.png
# 
# Input: root = [3,5,1,6,2,0,8,null,null,7,4]
# Output: [2,7,4]
# 
# Explanation: We return the node with value 2, colored in yellow in the diagram.
# The nodes coloured in blue are the deepest leaf-nodes of the tree.
# Note that nodes 6, 0, and 8 are also leaf nodes, but the depth of them is 2, but
# the depth of nodes 7 and 4 is 3.
# 
# Example 2:
# 
# Input: root = [1]
# Output: [1]
# 
# Explanation: The root is the deepest node in the tree, and it's the lca of
# itself.
# 
# Example 3:
# 
# Input: root = [0,1,3,null,2]
# Output: [2]
# 
# Explanation: The deepest leaf node in the tree is 2, the lca of one node is
# itself.
# 
# 
# Constraints:
#         The number of nodes in the tree will be in the range [1, 1000].
#         0 <= Node.val <= 1000
#         The values of the nodes in the tree are unique.
# 
# Note: This question is the same as 865: https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/

import sys
import os

# Add the parent directory to sys.path to import miscelaneus tools
current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)

from tree import get_tree

# Solution: https://youtu.be/bMXHK-ASQV0
# Credit: Navdeep Singh founder of NeetCode
def lca_deepest_leaves(root):
    # Return (LCA, height)
    def dfs(node):
        if not node:
            return (None, 0)
        
        left_node, left_height = dfs(node.left)
        right_node, right_height = dfs(node.right)

        if left_height == right_height:
            return node, 1 + left_height
        elif left_height > right_height:
            return left_node, left_height + 1
        else:
            return right_node, right_height + 1

    node, _ = dfs(root)
    return node
    # Time: O(n)
    # Space: O(h)
    # n = number of nodes in the binary tree
    # h = height of the binary tree

def lca_deepest_leaves_alt(root):
    # Return (LCA, depth)
    def dfs(node, depth):
        if not node:
            return (None, depth + 1)
        
        left_node, left_depth = dfs(node.left, depth + 1)
        right_node, right_depth = dfs(node.right, depth + 1)

        if left_depth > right_depth:
            return left_node, left_depth
        elif left_depth < right_depth:
            return right_node, right_depth
        return node, left_depth

    node, _ = dfs(root, 0)
    return node
    # Time: O(n)
    # Space: O(h)
    # n = number of nodes in the binary tree
    # h = height of the binary tree


def main():
    root = get_tree("[3,5,1,6,2,0,8,null,null,7,4]")
    result = lca_deepest_leaves(root)
    print(result) # [2, 7, 4]

    root2 = get_tree("[1]")
    result = lca_deepest_leaves(root2)
    print(result) # [1]

    root3 = get_tree("[0,1,3,null,2]")
    result = lca_deepest_leaves(root3)
    print(result) # [2]

if __name__ == "__main__":
    main()
