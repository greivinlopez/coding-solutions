# -----------------------
# 404. Sum of Left Leaves
# -----------------------

# Problem: https://leetcode.com/problems/sum-of-left-leaves
#
# Given the root of a binary tree, return the sum of all left leaves.
# 
# A leaf is a node with no children. A left leaf is a leaf that is the left child
# of another node.
# 
# Example 1:
# 
# https://assets.leetcode.com/uploads/2021/04/08/leftsum-tree.jpg
# 
# Input: root = [3,9,20,null,null,15,7]
# Output: 24
# 
# Explanation: There are two left leaves in the binary tree, with values 9 and 15
# respectively.
# 
# Example 2:
# 
# Input: root = [1]
# Output: 0
# 
# 
# Constraints:
#         The number of nodes in the tree is in the range [1, 1000].
#         -1000 <= Node.val <= 1000

import sys
import os

# Add the parent directory to sys.path to import miscelaneus tools
current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)

from tree import get_tree

# Credit: Jaweria Batool -> https://github.com/Jaweria-B
def sum_of_left_leaves(root):
    def dfs(node, is_left):
        if not node:
            return 0
        if not node.left and not node.right:  # Leaf node
            if is_left:
                return node.val
            else:
                return 0
        left_sum = dfs(node.left, True)   # Traverse left child
        right_sum = dfs(node.right, False)  # Traverse right child
        return left_sum + right_sum
    
    return dfs(root, False)
    # Time: O(n) 
    # Space: O(h) 
    # n = the number of nodes in the binary tree 
    # h = the height of the tree.


def main():
    root = get_tree("[3,9,20,null,null,15,7]")
    result = sum_of_left_leaves(root)
    print(result) # 24

    root = get_tree("[1]")
    result = sum_of_left_leaves(root)
    print(result) # 0

if __name__ == "__main__":
    main()
