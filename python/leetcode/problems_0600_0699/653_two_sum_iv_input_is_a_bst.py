# -----------------------------------
# 653. Two Sum IV - Input is a BST 🌲
# -----------------------------------

# Problem: https://leetcode.com/problems/two-sum-iv-input-is-a-bst
#
# Given the root of a binary search tree and an integer k, return true if there
# exist two elements in the BST such that their sum is equal to k, or false
# otherwise.
# 
# Example 1:
# 
# https://assets.leetcode.com/uploads/2020/09/21/sum_tree_1.jpg
# 
# Input: root = [5,3,6,2,4,null,7], k = 9
# Output: true
# 
# Example 2:
# 
# https://assets.leetcode.com/uploads/2020/09/21/sum_tree_2.jpg
# 
# Input: root = [5,3,6,2,4,null,7], k = 28
# Output: false
# 
# 
# Constraints:
#         The number of nodes in the tree is in the range [1, 10⁴].
#         -10⁴ <= Node.val <= 10⁴
#         root is guaranteed to be a valid binary search tree.
#         -10⁵ <= k <= 10⁵

import sys
import os

# Add the parent directory to sys.path to import miscelaneus tools
current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)

from tree import get_tree

# Solution: https://algo.monster/liteproblems/653
# Credit: AlgoMonster
def find_target(root, k):

    def dfs(node):
        # Base case: reached null node
        if node is None:
            return False
        
        # Check if complement of current value exists in visited set
        complement = k - node.val
        if complement in visited_values:
            return True
        
        # Add current node value to visited set
        visited_values.add(node.val)
        
        # Recursively search left and right subtrees
        return dfs(node.left) or dfs(node.right)
    
    # Initialize set to store visited node values
    visited_values = set()
    
    # Start DFS from root
    return dfs(root)
    # Time: O(n)
    # Space: O(n)


def main():
    root = get_tree("[5,3,6,2,4,null,7]")
    result = find_target(root, 9)
    print(result) # True

    root = get_tree("[5,3,6,2,4,null,7]")
    result = find_target(root, 28)
    print(result) # False

if __name__ == "__main__":
    main()
