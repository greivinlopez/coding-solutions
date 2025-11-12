# -----------------------------------------------
# 1315. Sum of Nodes with Even-Valued Grandparent
# -----------------------------------------------

# Problem: https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent
#
# Given the root of a binary tree, return the sum of values of nodes with an even-
# valued grandparent. If there are no nodes with an even-valued grandparent,
# return 0.
# 
# A grandparent of a node is the parent of its parent if it exists.
# 
# Example 1:
# 
# https://assets.leetcode.com/uploads/2021/08/10/even1-tree.jpg
# 
# Input: root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
# Output: 18
# 
# Explanation: The red nodes are the nodes with even-value grandparent while the
# blue nodes are the even-value grandparents.
# 
# Example 2:
# 
# https://assets.leetcode.com/uploads/2021/08/10/even2-tree.jpg
# 
# Input: root = [1]
# Output: 0
# 
# 
# Constraints:
#         The number of nodes in the tree is in the range [1, 10⁴].
#         1 <= Node.val <= 100

import sys
import os

# Add the parent directory to sys.path to import miscelaneus tools
current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)

from tree import get_tree

# Solution: https://algo.monster/liteproblems/1315
# Credit: AlgoMonster
def sum_even_grandparent(root):

    def dfs(node, parent_val):
        # Base case: if node is None, return 0
        if node is None:
            return 0
        
        # Recursively calculate sum for left and right subtrees
        # Pass current node's value as the parent value for children
        total_sum = dfs(node.left, node.val) + dfs(node.right, node.val)
        
        # If parent value is even, current node's children have an even grandparent
        if parent_val % 2 == 0:
            # Add left child's value if it exists
            if node.left:
                total_sum += node.left.val
            # Add right child's value if it exists
            if node.right:
                total_sum += node.right.val
        
        return total_sum
    
    # Start DFS with root node and odd parent value (1) to avoid counting root's children
    return dfs(root, 1)
    # Time: O(n)
    # Space: O(n)


def main():
    root = get_tree("[6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]")
    result = sum_even_grandparent(root)
    print(result) # 18

    root = get_tree("[1]")
    result = sum_even_grandparent(root)
    print(result) # 0

if __name__ == "__main__":
    main()
