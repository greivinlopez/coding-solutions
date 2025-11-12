# ------------------------------------------------------------------
# 106. Construct Binary Tree from Inorder and Postorder Traversal 🌲
# ------------------------------------------------------------------

# Problem: https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/
# 
# Given two integer arrays inorder and postorder where inorder is the inorder 
# traversal of a binary tree and postorder is the postorder traversal of the 
# same tree, construct and return the binary tree.

import sys
import os

# Add the parent directory to sys.path to import miscelaneus tools
current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)

from tree import TreeNode

# Solution: https://youtu.be/vm63HuIU7kw
# Credit: Navdeep Singh founder of NeetCode
def build_tree(inorder, postorder):
    def buildTreeHelper(left, right):
        if left > right:
            return None

        rootVal = postorder.pop()
        rootNode = TreeNode(rootVal)

        idx = inorderIndexMap[rootVal]
        rootNode.right = buildTreeHelper(idx + 1, right)
        rootNode.left = buildTreeHelper(left, idx - 1)
        return rootNode

    inorderIndexMap = {}
    for (i, val) in enumerate(inorder):
        inorderIndexMap[val] = i

    return buildTreeHelper(0, len(postorder) - 1)


def main():
    result = build_tree(inorder = [9,3,15,20,7], postorder = [9,15,7,20,3])
    print(result) # True

    result = build_tree(inorder = [-1], postorder = [-1])
    print(result) # True

if __name__ == "__main__":
    main()