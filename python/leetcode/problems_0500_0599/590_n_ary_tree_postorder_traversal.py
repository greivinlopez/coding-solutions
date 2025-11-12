# -----------------------------------
# 590. N-ary Tree Postorder Traversal
# -----------------------------------

# Problem: https://leetcode.com/problems/n-ary-tree-postorder-traversal
#
# Given the root of an n-ary tree, return the postorder traversal of its nodes'
# values.
# 
# Nary-Tree input serialization is represented in their level order traversal.
# Each group of children is separated by the null value (See examples)
# 
# Example 1:
# 
# https://assets.leetcode.com/uploads/2018/10/12/narytreeexample.png
# 
# Input: root = [1,null,3,2,4,null,5,6]
# Output: [5,6,3,2,4,1]
# 
# Example 2:
# 
# https://assets.leetcode.com/uploads/2019/11/08/sample_4_964.png
# 
# Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,1
# 2,null,13,null,null,14]
# Output: [2,6,14,11,7,3,12,8,4,13,9,10,5,1]
# 
# 
# Constraints:
#         The number of nodes in the tree is in the range [0, 104].
#         0 <= Node.val <= 104
#         The height of the n-ary tree is less than or equal to 1000.
# 
# Follow up: Recursive solution is trivial, could you do it iteratively?

# Definition for a Node.
class Node:
    def __init__(self, val = None, children = None):
        self.val = val
        self.children = children

# Solution: https://youtu.be/GMUI91_pDmM
# Credit: Navdeep Singh founder of NeetCode
def postorder(root):
    # Recursive solution
    res = []

    def helper(node):
        if not node:
            return
        for c in node.children:
            helper(c)
        res.append(node.val)

    helper(root)
    return res
    # Time: O(n)
    # Space: O(h)
    # n = number of nodes
    # h = height of the tree

def postorder(root):
    # Iterative solution
    res = []
    if not root:
        return []
    stack = [(root, False)]

    while stack:
        node, visited = stack.pop()
        if visited:
            res.append(node.val)
        else:
            stack.append((node, True))
            for c in node.children[::-1]:
                stack.append((c, False))

    return res
    # Time: O(n)
    # Space: O(h + n)
    # n = number of nodes
    # h = height of the tree


def main():
    print("TO DO")

if __name__ == "__main__":
    main()
