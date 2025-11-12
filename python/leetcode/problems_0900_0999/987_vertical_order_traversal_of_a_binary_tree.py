# ----------------------------------------------
# 987. Vertical Order Traversal of a Binary Tree
# ----------------------------------------------

# Problem: https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree
#
# Given the root of a binary tree, calculate the vertical order traversal of the
# binary tree.
# 
# For each node at position (row, col), its left and right children will be at
# positions (row + 1, col - 1) and (row + 1, col + 1) respectively. The root of
# the tree is at (0, 0).
# 
# The vertical order traversal of a binary tree is a list of top-to-bottom
# orderings for each column index starting from the leftmost column and ending on
# the rightmost column. There may be multiple nodes in the same row and same
# column. In such a case, sort these nodes by their values.
# 
# Return the vertical order traversal of the binary tree.
# 
# Example 1:
# 
# https://assets.leetcode.com/uploads/2021/01/29/vtree1.jpg
# 
# Input: root = [3,9,20,null,null,15,7]
# Output: [[9],[3,15],[20],[7]]
# 
# Explanation:
# Column -1: Only node 9 is in this column.
# Column 0: Nodes 3 and 15 are in this column in that order from top to bottom.
# Column 1: Only node 20 is in this column.
# Column 2: Only node 7 is in this column.
# 
# Example 2:
# 
# https://assets.leetcode.com/uploads/2021/01/29/vtree2.jpg
# 
# Input: root = [1,2,3,4,5,6,7]
# Output: [[4],[2],[1,5,6],[3],[7]]
# 
# Explanation:
# Column -2: Only node 4 is in this column.
# Column -1: Only node 2 is in this column.
# Column 0: Nodes 1, 5, and 6 are in this column.
#           1 is at the top, so it comes first.
#           5 and 6 are at the same position (2, 0), so we order them by their
# value, 5 before 6.
# Column 1: Only node 3 is in this column.
# Column 2: Only node 7 is in this column.
# 
# Example 3:
# 
# https://assets.leetcode.com/uploads/2021/01/29/vtree3.jpg
# 
# Input: root = [1,2,3,4,6,5,7]
# Output: [[4],[2],[1,5,6],[3],[7]]
# 
# Explanation:
# This case is the exact same as example 2, but with nodes 5 and 6 swapped.
# Note that the solution remains the same since 5 and 6 are in the same location
# and should be ordered by their values.
# 
# 
# Constraints:
#         The number of nodes in the tree is in the range [1, 1000].
#         0 <= Node.val <= 1000

import sys
import os

# Add the parent directory to sys.path to import miscelaneus tools
current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)

from tree import get_tree

# Solution: https://algo.monster/liteproblems/987
# Credit: AlgoMonster
def vertical_traversal(root):   
    def dfs(node, row, col):
        if node is None:
            return
        
        # Store node information as (column, row, value) for proper sorting
        node_positions.append((col, row, node.val))
        
        # Traverse left subtree (row increases, column decreases)
        dfs(node.left, row + 1, col - 1)
        
        # Traverse right subtree (row increases, column increases)
        dfs(node.right, row + 1, col + 1)
    
    # Collect all nodes with their positions
    node_positions = []
    dfs(root, 0, 0)
    
    # Sort by column first, then row, then value
    node_positions.sort()
    
    # Group nodes by column
    result = []
    previous_col = -2000  # Initialize with value outside possible column range
    
    for col, _, val in node_positions:
        # Start a new column group if column changed
        if previous_col != col:
            result.append([])
            previous_col = col
        
        # Add node value to current column group
        result[-1].append(val)
    
    return result
    # Time: O(n * log(n))
    # Space: O(n)


def main():
    root = get_tree("[3,9,20,null,null,15,7]")
    result = vertical_traversal(root)
    print(result) # [[9],[3,15],[20],[7]]

    root = get_tree("[1,2,3,4,5,6,7]")
    result = vertical_traversal(root)
    print(result) # [[4],[2],[1,5,6],[3],[7]]

    root = get_tree("[1,2,3,4,6,5,7]")
    result = vertical_traversal(root)
    print(result) # [[4],[2],[1,5,6],[3],[7]]

if __name__ == "__main__":
    main()
