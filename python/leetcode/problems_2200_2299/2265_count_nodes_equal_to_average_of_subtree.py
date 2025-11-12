# ---------------------------------------------
# 2265. Count Nodes Equal to Average of Subtree
# ---------------------------------------------

# Problem: https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/
#
# Given the root of a binary tree, return the number of nodes where the value of 
# the node is equal to the average of the values in its subtree.
# 
# Note:
# 
#   The average of n elements is the sum of the n elements divided by n and rounded 
#   down to the nearest integer.
# 
#   A subtree of root is a tree consisting of root and all of its descendants.
#  
# 
# Example 1:
# 
# Input: root = [4,8,5,0,1,null,6]
# Output: 5
# Explanation: 
# For the node with value 4: The average of its subtree is (4 + 8 + 5 + 0 + 1 + 6) / 6 = 24 / 6 = 4.
# For the node with value 5: The average of its subtree is (5 + 6) / 2 = 11 / 2 = 5.
# For the node with value 0: The average of its subtree is 0 / 1 = 0.
# For the node with value 1: The average of its subtree is 1 / 1 = 1.
# For the node with value 6: The average of its subtree is 6 / 1 = 6.
# 
# Example 2:
# 
# Input: root = [1]
# Output: 1
# Explanation: For the node with value 1: The average of its subtree is 1 / 1 = 1.
#  
# 
# Constraints:
# 
#   The number of nodes in the tree is in the range [1, 1000].
#   0 <= Node.val <= 1000

import sys
import os

# Add the parent directory to sys.path to import miscelaneus tools
current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)

# Import code needed for solutions
from tree import get_tree

# Solution: https://www.youtube.com/shorts/8KEr7b_Ll14
# Credit: Greg Hogg
def average_of_subtree(root):
    num_nodes = [0]

    def dfs(root):
        if not root:
            return (0, 0)
        
        N_left, summ_left = dfs(root.left)
        N_right, summ_right = dfs(root.right)

        N = 1 + N_left + N_right
        summ = root.val + summ_left + summ_right
        avg = summ // N

        if root.val == avg:
            num_nodes[0] += 1

        return (N, summ)
    
    dfs(root)
    return num_nodes[0]
    # Time: O(N)
    # Space: O(N)


def main():
    root = get_tree("[4,8,5,0,1,null,6]")
    result = average_of_subtree(root)
    print(result) # 5

    root = get_tree("[1]")
    result = average_of_subtree(root)
    print(result) # 1

if __name__ == "__main__":
    main()
