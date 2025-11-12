# ------------------------------------------
# 2196. Create Binary Tree From Descriptions
# ------------------------------------------

# Problem: https://leetcode.com/problems/create-binary-tree-from-descriptions
#
# You are given a 2D integer array descriptions where descriptions[i] = [parenti,
# childi, isLefti] indicates that parenti is the parent of childi in a binary tree
# of unique values. Furthermore,
#         
#   * If isLefti == 1, then childi is the left child of parenti.
#   * If isLefti == 0, then childi is the right child of parenti.
# 
# Construct the binary tree described by descriptions and return its root.
# 
# The test cases will be generated such that the binary tree is valid.
# 
# Example 1:
# 
# Input: descriptions = [[20,15,1],[20,17,0],[50,20,1],[50,80,0],[80,19,1]]
# Output: [50,20,80,15,17,19]
# 
# Explanation: The root node is the node with value 50 since it has no parent.
# The resulting binary tree is shown in the diagram.
# 
# Example 2:
# 
# Input: descriptions = [[1,2,1],[2,3,0],[3,4,1]]
# Output: [1,2,null,null,3,4]
# 
# Explanation: The root node is the node with value 1 since it has no parent.
# The resulting binary tree is shown in the diagram.
# 
# 
# Constraints:
#         1 <= descriptions.length <= 10^4
#         descriptions[i].length == 3
#         1 <= parenti, childi <= 10^5
#         0 <= isLefti <= 1
#         The binary tree described by descriptions is valid.

import sys
import os

# Add the parent directory to sys.path to import miscelaneus tools
current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)

# Import code needed for solutions
from tree import TreeNode

# Solution: https://youtu.be/yWkrFfqO7NA
# Credit: Navdeep Singh founder of NeetCode
def create_binary_tree(descriptions):
    nodes = {}
    children = set()

    for par, child, is_left in descriptions:
        children.add(child)
        if par not in nodes:
            nodes[par] = TreeNode(par)
        if child not in nodes:
            nodes[child] = TreeNode(child)
        
        if is_left:
            nodes[par].left = nodes[child]
        else:
            nodes[par].right = nodes[child]
    
    for p, c, l in descriptions:
        if p not in children:
            return nodes[p]
    # Time: O(n) 
    # Space: O(n)


def main():
    result = create_binary_tree([[20,15,1],[20,17,0],[50,20,1],[50,80,0],[80,19,1]])
    print(result) # [50, 20, 80, 15, 17, 19]

    result = create_binary_tree([[1,2,1],[2,3,0],[3,4,1]])
    print(result) # [1, 2, None, None, 3, 4]

if __name__ == "__main__":
    main()
