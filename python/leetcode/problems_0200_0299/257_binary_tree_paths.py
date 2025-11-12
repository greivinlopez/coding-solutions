# ----------------------
# 257. Binary Tree Paths
# ----------------------

# Problem: https://leetcode.com/problems/binary-tree-paths
#
# Given the root of a binary tree, return all root-to-leaf paths in any order.
# 
# A leaf is a node with no children.
# 
# Example 1:
# 
# https://assets.leetcode.com/uploads/2021/03/12/paths-tree.jpg
# 
# Input: root = [1,2,3,null,5]
# Output: ["1->2->5","1->3"]
# 
# Example 2:
# 
# Input: root = [1]
# Output: ["1"]
# 
# 
# Constraints:
#         The number of nodes in the tree is in the range [1, 100].
#         -100 <= Node.val <= 100

import sys
import os

# Add the parent directory to sys.path to import miscelaneus tools
current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)

from tree import get_tree

# Solution: https://leetcode.com/problems/binary-tree-paths/solutions/827629/python-o-n-2-by-dfs-w-comment
def binary_tree_paths(root):
    result = []
    
    def helper(node, cur):  
        if not node:
            # base case
            return
        
        copy_plus_insertion = cur + [str(node.val)]
        if not node.left and not node.right:
            result.append(copy_plus_insertion)
            
        else:
            # general case
            helper(node.left, copy_plus_insertion)
            helper(node.right, copy_plus_insertion)
    
    helper(node=root, cur=[])
    return list(map('->'.join, result))
    # Time: O(n²)
    # Space: O(n²)


def main():
    root = get_tree("[1,2,3,null,5]")
    result = binary_tree_paths(root)
    print(result) # ["1->2->5","1->3"]

    root = get_tree("[1]")
    result = binary_tree_paths(root)
    print(result) # ["1"]

if __name__ == "__main__":
    main()
