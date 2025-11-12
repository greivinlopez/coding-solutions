# ------------------------------------
# 145. Binary Tree Postorder Traversal
# ------------------------------------

# Given the root of a binary tree, return the postorder traversal of its nodes' values.
#  
# Example 1:
# 
# Input: root = [1,null,2,3]
# 
# Output: [3,2,1]
# 
# Explanation:
# 
# 
# Example 2:
# 
# Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]
# 
# Output: [4,6,7,5,2,9,8,3,1]
# 
# Explanation:
# 
# 
# Example 3:
# 
# Input: root = []
# 
# Output: []
# 
# Example 4:
# 
# Input: root = [1]
# 
# Output: [1]
# 
# 
# Constraints:
# 
# 	The number of the nodes in the tree is in the range [0, 100].
# 	-100 <= Node.val <= 100
# 
# Follow up: Recursive solution is trivial, could you do it iteratively?

import sys
import os

# Add the parent directory to sys.path to import miscelaneus tools
current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)

from tree import get_tree, TreeNode

# Solution: https://youtu.be/QhszUQhGGlA
# Credit: Navdeep Singh founder of NeetCode
def postorder_traversal(root):
    stack = [root]
    visit = [False]
    res = []

    while stack:
        cur, v = stack.pop(), visit.pop()
        if cur:
            if v:
                res.append(cur.val)
            else:
                stack.append(cur)
                visit.append(True)
                stack.append(cur.right)
                visit.append(False)
                stack.append(cur.left)
                visit.append(False)
    return res


def main():
    root = get_tree("[1,null,2,3]")
    result = postorder_traversal(root)
    print(result) # [3,2,1]

    root = get_tree("[1,2,3,4,5,null,8,null,null,6,7,9]")
    result = postorder_traversal(root)
    print(result) # [4,6,7,5,2,9,8,3,1]

    result = postorder_traversal(None)
    print(result) # []

    result = postorder_traversal(TreeNode(1))
    print(result) # [1]

if __name__ == "__main__":
    main()
