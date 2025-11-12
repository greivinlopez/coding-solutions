# -------------------------
# 655. Print Binary Tree 🌲
# -------------------------

# Problem: https://leetcode.com/problems/print-binary-tree
#
# Given the root of a binary tree, construct a 0-indexed m x n string matrix res
# that represents a formatted layout of the tree. The formatted layout matrix
# should be constructed using the following rules:
#         
#   * The height of the tree is height and the number of rows m should be
#     equal to height + 1.
#   * The number of columns n should be equal to 2ʰᵉᶦᵍʰᵗ⁻ʳ⁻¹.
#   * Place the root node in the middle of the top row (more formally, at
#     location res[0][(n-1)/2]).
#   * For each node that has been placed in the matrix at position res[r][c],
#     place its left child at res[r+1][c-2ʰᵉᶦᵍʰᵗ⁻ʳ⁻¹] and its right child at
#     res[r+1][c+2ʰᵉᶦᵍʰᵗ⁻ʳ⁻¹].
#   * Continue this process until all the nodes in the tree have been placed.
#   * Any empty cells should contain the empty string "".
# 
# Return the constructed matrix res.
# 
# Example 1:
# 
# Input: root = [1,2]
# Output:
# [["","1",""],
#  ["2","",""]]
# 
# Example 2:
# 
# Input: root = [1,2,3,null,4]
# Output:
# [["","","","1","","",""],
#  ["","2","","","","3",""],
#  ["","","4","","","",""]]
# 
# 
# Constraints:
#         The number of nodes in the tree is in the range [1, 2¹⁰].
#         -99 <= Node.val <= 99
#         The depth of the tree will be in the range [1, 10].

import sys
import os

# Add the parent directory to sys.path to import miscelaneus tools
current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)

from tree import get_tree

# Solution: https://algo.monster/liteproblems/655
# Credit: AlgoMonster
def print_tree(root):  
    def get_tree_height(node):
        if node is None:
            return -1
        
        left_height = get_tree_height(node.left)
        right_height = get_tree_height(node.right)
        
        return 1 + max(left_height, right_height)
    
    def fill_matrix(node, row, col):
        if node is None:
            return
        
        # Place current node value at the specified position
        result[row][col] = str(node.val)
        
        # Calculate offset for child nodes based on current depth
        # The offset decreases as we go deeper in the tree
        offset = 2 ** (tree_height - row - 1)
        
        # Recursively process left and right subtrees
        # Left child goes to the left (col - offset)
        fill_matrix(node.left, row + 1, col - offset)
        # Right child goes to the right (col + offset)
        fill_matrix(node.right, row + 1, col + offset)
    
    # Calculate tree dimensions
    tree_height = get_tree_height(root)
    
    # Matrix dimensions based on tree height
    # Rows: height + 1 (since height is 0-indexed)
    # Columns: 2^(height+1) - 1 (full binary tree width)
    num_rows = tree_height + 1
    num_cols = 2 ** (tree_height + 1) - 1
    
    # Initialize result matrix with empty strings
    result = [[""] * num_cols for _ in range(num_rows)]
    
    # Start filling from root at the center of the first row
    center_col = (num_cols - 1) // 2
    fill_matrix(root, 0, center_col)
    
    return result
    # Time: O(n * 2ʰ)
    # Space: O(h * 2ʰ)
    # n = the number of nodes in the tree
    # h = the height of the tree.


def main():
    root = get_tree("[1,2]")
    result = print_tree(root)
    print(result) 
    # [['', '1', ''], 
    #  ['2', '', '']]

    root = get_tree("[1,2,3,null,4]")
    result = print_tree(root)
    print(result)
    # [['', '', '', '1', '', '', ''], 
    #  ['', '2', '', '', '', '3', ''], 
    #  ['', '', '4', '', '', '', '']]

if __name__ == "__main__":
    main()
