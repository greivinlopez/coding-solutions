# --------------------------------
# 559. Maximum Depth of N-ary Tree
# --------------------------------

# Problem: https://leetcode.com/problems/maximum-depth-of-n-ary-tree
#
# Given a n-ary tree, find its maximum depth.
# 
# The maximum depth is the number of nodes along the longest path from the root
# node down to the farthest leaf node.
# 
# Nary-Tree input serialization is represented in their level order traversal,
# each group of children is separated by the null value (See examples).
# 
# Example 1:
# 
# https://assets.leetcode.com/uploads/2018/10/12/narytreeexample.png
# 
# Input: root = [1,null,3,2,4,null,5,6]
# Output: 3
# 
# Example 2:
# 
# https://assets.leetcode.com/uploads/2019/11/08/sample_4_964.png
# 
# Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,1
# 2,null,13,null,null,14]
# Output: 5
# 
# 
# Constraints:
#         The total number of nodes is in the range [0, 10⁴].
#         The depth of the n-ary tree is less than or equal to 1000.

class Node:
    def __init__(self, val = None, children = None):
        self.val = val
        self.children = children

# Solution: https://algo.monster/liteproblems/559
# Credit: AlgoMonster
def max_depth(root):
    # Base case: if the tree is empty, depth is 0
    if root is None:
        return 0
    
    # If the node has no children, it's a leaf node with depth 1
    if not root.children:
        return 1
    
    # Initialize variable to track maximum depth among all children
    max_child_depth = 0
    
    # Recursively find the maximum depth among all children
    for child in root.children:
        child_depth = max_depth(child)
        max_child_depth = max(max_child_depth, child_depth)
    
    # Return current node's depth (1) plus the maximum child depth
    return 1 + max_child_depth
    # Time: O(n)
    # Space: O(h)
    # n = the total number of nodes in the N-ary tree
    # h = the height (or maximum depth) of the N-ary tree


def main():
    print("TO DO")

if __name__ == "__main__":
    main()
