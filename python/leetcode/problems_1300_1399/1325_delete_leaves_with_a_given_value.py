# --------------------------------------
# 1325. Delete Leaves With a Given Value
# --------------------------------------

# Problem: https://leetcode.com/problems/delete-leaves-with-a-given-value
#
# Given a binary tree root and an integer target, delete all the leaf nodes with
# value target.
# 
# Note that once you delete a leaf node with value target, if its parent node
# becomes a leaf node and has the value target, it should also be deleted (you
# need to continue doing that until you cannot).
# 
# Example 1:
# 
# https://assets.leetcode.com/uploads/2020/01/09/sample_1_1684.png
# 
# Input: root = [1,2,3,2,null,2,4], target = 2
# Output: [1,null,3,null,4]
# 
# Explanation: Leaf nodes in green with value (target = 2) are removed (Picture in
# left).
# After removing, new nodes become leaf nodes with value (target = 2) (Picture in
# center).
# 
# Example 2:
# 
# https://assets.leetcode.com/uploads/2020/01/09/sample_2_1684.png
# 
# Input: root = [1,3,3,3,2], target = 3
# Output: [1,3,null,null,2]
# 
# Example 3:
# 
# https://assets.leetcode.com/uploads/2020/01/15/sample_3_1684.png
# 
# Input: root = [1,2,null,2,null,2], target = 2
# Output: [1]
# Explanation: Leaf nodes in green with value (target = 2) are removed at each
# step.
# 
# 
# Constraints:
#         The number of nodes in the tree is in the range [1, 3000].
#         1 <= Node.val, target <= 1000

import sys
import os

# Add the parent directory to sys.path to import miscelaneus tools
current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)

from tree import get_tree

# Solution: https://youtu.be/FqAoYAwbwV8
# Credit: Navdeep Singh founder of NeetCode
def remove_leaf_nodes_rec(root, target):
    if not root:
        return None
    
    root.left = remove_leaf_nodes_rec(root.left, target)
    root.right = remove_leaf_nodes_rec(root.right, target)
    
    if not root.left and not root.right and root.val == target:
        return None
        
    return root
    # Time: O(n)
    # Space: O(h)


def remove_leaf_nodes(root, target):
    # Iterative solution
    stack = [root]
    visit = set()
    parents = {root: None}

    while stack:
        node = stack.pop()
        if not node.left and not node.right:
            if node.val == target:
                p = parents[node]
                if not p:
                    return None
                if p.left == node:
                    p.left = None
                if p.right == node:
                    p.right = None
        elif node not in visit:
            visit.add(node)
            stack.append(node)
            if node.left:
                stack.append(node.left)
                parents[node.left] = node
            if node.right:
                stack.append(node.right)
                parents[node.right] = node
    return root
    # Time: O(n)
    # Space: O(n)


def main():
    root = get_tree("[1,2,3,2,null,2,4]")
    result = remove_leaf_nodes(root, 2)
    print(result) # [1, None, 3, None, 4]

    root = get_tree("[1,3,3,3,2]")
    result = remove_leaf_nodes(root, 3)
    print(result) # [1, 3, None, None, 2]

    root = get_tree("[1,2,null,2,null,2]")
    result = remove_leaf_nodes(root, 2)
    print(result) # [1]

if __name__ == "__main__":
    main()
