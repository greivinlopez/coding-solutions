# ---------------------
# 563. Binary Tree Tilt
# ---------------------

# Problem: https://leetcode.com/problems/binary-tree-tilt
#
# Given the root of a binary tree, return the sum of every tree node's tilt.
# 
# The tilt of a tree node is the absolute difference between the sum of all left
# subtree node values and all right subtree node values. If a node does not have a
# left child, then the sum of the left subtree node values is treated as 0. The
# rule is similar if the node does not have a right child.
# 
# Example 1:
# 
# https://assets.leetcode.com/uploads/2020/10/20/tilt1.jpg
# 
# Input: root = [1,2,3]
# Output: 1
# 
# Explanation:
# Tilt of node 2 : |0-0| = 0 (no children)
# Tilt of node 3 : |0-0| = 0 (no children)
# Tilt of node 1 : |2-3| = 1 (left subtree is just left child, so sum is 2; right
# subtree is just right child, so sum is 3)
# Sum of every tilt : 0 + 0 + 1 = 1
# 
# Example 2:
# 
# https://assets.leetcode.com/uploads/2020/10/20/tilt2.jpg
# 
# Input: root = [4,2,9,3,5,null,7]
# Output: 15
# 
# Explanation:
# Tilt of node 3 : |0-0| = 0 (no children)
# Tilt of node 5 : |0-0| = 0 (no children)
# Tilt of node 7 : |0-0| = 0 (no children)
# Tilt of node 2 : |3-5| = 2 (left subtree is just left child, so sum is 3; right
# subtree is just right child, so sum is 5)
# Tilt of node 9 : |0-7| = 7 (no left child, so sum is 0; right subtree is just
# right child, so sum is 7)
# Tilt of node 4 : |(3+5+2)-(9+7)| = |10-16| = 6 (left subtree values are 3, 5,
# and 2, which sums to 10; right subtree values are 9 and 7, which sums to 16)
# Sum of every tilt : 0 + 0 + 0 + 2 + 7 + 6 = 15
# 
# Example 3:
# 
# https://assets.leetcode.com/uploads/2020/10/20/tilt3.jpg
# 
# Input: root = [21,7,14,1,1,2,2,3,3]
# Output: 9
# 
# 
# Constraints:
#         The number of nodes in the tree is in the range [0, 10⁴].
#         -1000 <= Node.val <= 1000

import sys
import os

# Add the parent directory to sys.path to import miscelaneus tools
current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)

from tree import get_tree

# Solution: https://algo.monster/liteproblems/563
# Credit: AlgoMonster
def find_tilt(root):
    # Initialize total tilt sum
    total_tilt = 0
    
    def calculate_sum_and_tilt(node):
        nonlocal total_tilt

        # Base case: empty node contributes 0 to sum
        if node is None:
            return 0
        
        # Recursively calculate left and right subtree sums
        left_sum = calculate_sum_and_tilt(node.left)
        right_sum = calculate_sum_and_tilt(node.right)
        
        # Calculate tilt for current node and add to total
        current_tilt = abs(left_sum - right_sum)
        total_tilt += current_tilt
        
        # Return sum of current subtree (left + right + current node value)
        return left_sum + right_sum + node.val
    
    # Start the traversal from root
    calculate_sum_and_tilt(root)
    
    return total_tilt
    # Time: O(n)
    # Space: O(h)
    # h = the height (or maximum depth) of the binary tree


def main():
    root = get_tree("[1,2,3]")
    result = find_tilt(root)
    print(result) # 1

    root = get_tree("[4,2,9,3,5,null,7]")
    result = find_tilt(root)
    print(result) # 15

    root = get_tree("[21,7,14,1,1,2,2,3,3]")
    result = find_tilt(root)
    print(result) # 9

if __name__ == "__main__":
    main()
