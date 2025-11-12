# ---------------------------
# 617. Merge Two Binary Trees
# ---------------------------

# Problem: https://leetcode.com/problems/merge-two-binary-trees/
# 
# You are given two binary trees root1 and root2.
# 
# Imagine that when you put one of them to cover the other, some nodes of the 
# two trees are overlapped while the others are not. You need to merge the two 
# trees into a new binary tree. The merge rule is that if two nodes overlap, 
# then sum node values up as the new value of the merged node. Otherwise, the 
# NOT null node will be used as the node of the new tree.
# 
# Return the merged tree.
# 
# Note: The merging process must start from the root nodes of both trees.
# 
#  
# Example 1:
# 
# Input: root1 = [1,3,2,5], root2 = [2,1,3,null,4,null,7]
# Output: [3,4,5,5,4,null,7]
# 
# 
# Example 2:
# 
# Input: root1 = [1], root2 = [1,2]
# Output: [2,2]
# 
# 
# Constraints:
# 
# 	The number of nodes in both trees is in the range [0, 2000].
# 	-10^4 <= Node.val <= 10^4

import sys
import os

# Add the parent directory to sys.path to import miscelaneus tools
current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)

# Import code needed for solutions
from tree import get_tree, TreeNode

# Solution: https://youtu.be/QHH6rIK3dDQ
# Credit: Navdeep Singh founder of NeetCode
def merge_trees(t1, t2):
    if not t1 and not t2:
        return None

    v1 = t1.val if t1 else 0
    v2 = t2.val if t2 else 0
    root = TreeNode(v1 + v2)

    root.left = merge_trees(t1.left if t1 else None, t2.left if t2 else None)
    root.right = merge_trees(t1.right if t1 else None, t2.right if t2 else None)
    return root


def main():
    r1 = get_tree("[1,3,2,5]")
    r2 = get_tree("[2,1,3,null,4,null,7]")
    result = merge_trees(r1, r2)
    print(result) # [3, 4, 5, 5, 4, None, 7]

    r1 = get_tree("[1]")
    r2 = get_tree("[1,2]")
    result = merge_trees(r1, r2)
    print(result) # [2,2]

if __name__ == "__main__":
    main()
