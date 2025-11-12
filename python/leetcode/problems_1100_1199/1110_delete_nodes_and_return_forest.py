# ------------------------------------
# 1110. Delete Nodes And Return Forest
# ------------------------------------

# Problem: https://leetcode.com/problems/delete-nodes-and-return-forest
#
# Given the root of a binary tree, each node in the tree has a distinct value.
# 
# After deleting all nodes with a value in to_delete, we are left with a forest (a
# disjoint union of trees).
# 
# Return the roots of the trees in the remaining forest. You may return the result
# in any order.
# 
# Example 1:
# 
# https://assets.leetcode.com/uploads/2019/07/01/screen-shot-2019-07-01-at-53836-pm.png
# 
# Input: root = [1,2,3,4,5,6,7], to_delete = [3,5]
# Output: [[1,2,null,4],[6],[7]]
# 
# Example 2:
# 
# Input: root = [1,2,4,null,3], to_delete = [3]
# Output: [[1,2,4]]
# 
# 
# Constraints:
#         The number of nodes in the given tree is at most 1000.
#         Each node has a distinct value between 1 and 1000.
#         to_delete.length <= 1000
#         to_delete contains distinct values between 1 and 1000.

import sys
import os

# Add the parent directory to sys.path to import miscelaneus tools
current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)

from tree import get_tree

# Solution: https://youtu.be/UhKu0q1yXHY
# Credit: Navdeep Singh founder of NeetCode
def del_nodes(root, to_delete):
    to_delete = set(to_delete)
    res_set = set([root])
    
    def dfs(node):
        if not node:
            return None
        
        res = node
        if node.val in to_delete:
            res = None
            res_set.discard(node)
            if node.left: res_set.add(node.left)
            if node.right: res_set.add(node.right)
        
        node.left = dfs(node.left)
        node.right = dfs(node.right)
        
        return res
    
    dfs(root)
    return list(res_set)
    # Time: O(n)
    # Space: O(n)


def main():
    root = get_tree("[1,2,3,4,5,6,7]")
    result = del_nodes(root, [3,5])
    # [[1,2,null,4],[6],[7]]
    for t in result:
        print(t)

    root = get_tree("[1,2,4,null,3]")
    result = del_nodes(root, [3])
    # [[1,2,4]]
    for t in result:
        print(t)

if __name__ == "__main__":
    main()
