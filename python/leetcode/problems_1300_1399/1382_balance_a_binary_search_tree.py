# -------------------------------------
# 1382. Balance a Binary Search Tree 🌲
# -------------------------------------

# Problem: https://leetcode.com/problems/balance-a-binary-search-tree
#
# Given the root of a binary search tree, return a balanced binary search tree
# with the same node values. If there is more than one answer, return any of them.
# 
# A binary search tree is balanced if the depth of the two subtrees of every node
# never differs by more than 1.
# 
# Example 1:
# 
# https://assets.leetcode.com/uploads/2021/08/10/balance1-tree.jpg
# 
# Input: root = [1,null,2,null,3,null,4,null,null]
# Output: [2,1,3,null,null,null,4]
# 
# Explanation: This is not the only correct answer, [3,1,4,null,2] is also
# correct.
# 
# Example 2:
# 
# https://assets.leetcode.com/uploads/2021/08/10/balanced2-tree.jpg
# 
# Input: root = [2,1,3]
# Output: [2,1,3]
# 
# 
# Constraints:
#         The number of nodes in the tree is in the range [1, 10⁴].
#         1 <= Node.val <= 10⁵

import sys
import os

# Add the parent directory to sys.path to import miscelaneus tools
current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)

from tree import get_tree, TreeNode

# Solution: https://algo.monster/liteproblems/1382
# Credit: AlgoMonster
def balance_bst(root):

    def inorder_traversal(node):
        if node is None:
            return
        
        # Traverse left subtree
        inorder_traversal(node.left)
        
        # Process current node - add value to sorted list
        sorted_values.append(node.val)
        
        # Traverse right subtree
        inorder_traversal(node.right)
    
    def build_balanced_bst(left_idx, right_idx):
        # Base case: invalid range
        if left_idx > right_idx:
            return None
        
        # Choose middle element as root to ensure balance
        mid_idx = (left_idx + right_idx) // 2
        
        # Recursively build left subtree from left half
        left_subtree = build_balanced_bst(left_idx, mid_idx - 1)
        
        # Recursively build right subtree from right half
        right_subtree = build_balanced_bst(mid_idx + 1, right_idx)
        
        # Create new node with middle value and attach subtrees
        return TreeNode(sorted_values[mid_idx], left_subtree, right_subtree)
    
    # Step 1: Extract all values from BST in sorted order
    sorted_values = []
    inorder_traversal(root)
    
    # Step 2: Build balanced BST from sorted values
    return build_balanced_bst(0, len(sorted_values) - 1)
    # Time: O(n)
    # Space: O(n)


def main():
    root = get_tree("[1,null,2,null,3,null,4,null,null]")
    result = balance_bst(root)
    print(result) # [2, 1, 3, None, None, None, 4]

    root = get_tree("[2,1,3]")
    result = balance_bst(root)
    print(result) # [2, 1, 3]

if __name__ == "__main__":
    main()
