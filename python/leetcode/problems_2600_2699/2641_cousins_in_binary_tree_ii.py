# -------------------------------
# 2641. Cousins in Binary Tree II
# -------------------------------

# Problem: https://leetcode.com/problems/cousins-in-binary-tree-ii
#
# Given the root of a binary tree, replace the value of each node in the tree with
# the sum of all its cousins' values.
# 
# Two nodes of a binary tree are cousins if they have the same depth with
# different parents.
# 
# Return the root of the modified tree.
# 
# Note that the depth of a node is the number of edges in the path from the root
# node to it.
# 
# Example 1:
# 
# https://assets.leetcode.com/uploads/2023/01/11/example11.png
# 
# Input: root = [5,4,9,1,10,null,7]
# Output: [0,0,0,7,7,null,11]
# 
# Explanation: The diagram above shows the initial binary tree and the binary tree
# after changing the value of each node.
# - Node with value 5 does not have any cousins so its sum is 0.
# - Node with value 4 does not have any cousins so its sum is 0.
# - Node with value 9 does not have any cousins so its sum is 0.
# - Node with value 1 has a cousin with value 7 so its sum is 7.
# - Node with value 10 has a cousin with value 7 so its sum is 7.
# - Node with value 7 has cousins with values 1 and 10 so its sum is 11.
# 
# Example 2:
# 
# https://assets.leetcode.com/uploads/2023/01/11/diagram33.png
# 
# Input: root = [3,1,2]
# Output: [0,0,0]
# 
# Explanation: The diagram above shows the initial binary tree and the binary tree
# after changing the value of each node.
# - Node with value 3 does not have any cousins so its sum is 0.
# - Node with value 1 does not have any cousins so its sum is 0.
# - Node with value 2 does not have any cousins so its sum is 0.
# 
# 
# Constraints:
#         The number of nodes in the tree is in the range [1, 10⁵].
#         1 <= Node.val <= 10⁴

import sys
import os

# Add the parent directory to sys.path to import miscelaneus tools
current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)

# Import code needed for solutions
from tree import get_tree
from collections import deque

# Solution: https://youtu.be/xvwTd19SncE
# Credit: Navdeep Singh founder of NeetCode
def replace_value_in_tree(root):
    level_sum = []

    q = deque([root])
    while q:
        cur_sum = 0
        for i in range(len(q)):
            node = q.popleft()
            cur_sum += node.val
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        level_sum.append(cur_sum)

    q = deque([root])
    root.val = 0
    level = 0
    while q:
        for i in range(len(q)):
            node = q.popleft()
            
            child_sum = 0
            if node.left:
                child_sum += node.left.val
            if node.right:
                child_sum += node.right.val
            
            if node.left:
                node.left.val = level_sum[level+1] - child_sum
                q.append(node.left)
            
            if node.right:
                node.right.val = level_sum[level+1] - child_sum
                q.append(node.right)
        
        level += 1

    return root
    # Time: O(n)
    # Space: O(n)


def main():
    root = get_tree("[5,4,9,1,10,null,7]")
    result = replace_value_in_tree(root)
    print(result) # [0, 0, 0, 7, 7, None, 11]

    root = get_tree("[3,1,2]")
    result = replace_value_in_tree(root)
    print(result) # [0, 0, 0]

if __name__ == "__main__":
    main()
