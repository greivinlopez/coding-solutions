# --------------------------
# 965. Univalued Binary Tree
# --------------------------

# Problem: https://leetcode.com/problems/univalued-binary-tree
#
# A binary tree is uni-valued if every node in the tree has the same value.
# 
# Given the root of a binary tree, return true if the given tree is uni-valued, or
# false otherwise.
# 
# Example 1:
# 
# https://assets.leetcode.com/uploads/2018/12/28/unival_bst_1.png
# 
# Input: root = [1,1,1,1,1,null,1]
# Output: true
# 
# Example 2:
# 
# https://assets.leetcode.com/uploads/2018/12/28/unival_bst_2.png
# 
# Input: root = [2,2,2,5,2]
# Output: false
# 
# 
# Constraints:
#         The number of nodes in the tree is in the range [1, 100].
#         0 <= Node.val < 100

import sys
import os

# Add the parent directory to sys.path to import miscelaneus tools
current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)

from tree import get_tree

# Solution: https://algo.monster/liteproblems/965
# Credit: AlgoMonster
def is_unival_tree(root):
    # Store the value that all nodes should match (the root's value)
    target_value = root.val
    
    def dfs(node):
        # Base case: empty node is considered valid
        if node is None:
            return True
        
        # Check if current node matches target value
        # and recursively check both left and right subtrees
        return (node.val == target_value and 
                dfs(node.left) and 
                dfs(node.right))
    
    # Start DFS traversal from the root
    return dfs(root)
    # Time: O(n)
    # Space: O(n)


def main():
    root = get_tree("[1,1,1,1,1,null,1]")
    result = is_unival_tree(root)
    print(result) # True

    root = get_tree("[2,2,2,5,2]")
    result = is_unival_tree(root)
    print(result) # False

if __name__ == "__main__":
    main()
