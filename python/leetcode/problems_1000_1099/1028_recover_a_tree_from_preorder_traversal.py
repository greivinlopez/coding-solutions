# --------------------------------------------
# 1028. Recover a Tree From Preorder Traversal
# --------------------------------------------

# Problem: https://leetcode.com/problems/recover-a-tree-from-preorder-traversal
#
# We run a preorder depth-first search (DFS) on the root of a binary tree.
# 
# At each node in this traversal, we output D dashes (where D is the depth of this
# node), then we output the value of this node.  If the depth of a node is D, the
# depth of its immediate child is D + 1.  The depth of the root node is 0.
# 
# If a node has only one child, that child is guaranteed to be the left child.
# 
# Given the output traversal of this traversal, recover the tree and return its
# root.
# 
# Example 1:
# 
# Input: traversal = "1-2--3--4-5--6--7"
# Output: [1,2,5,3,4,6,7]
# 
# Example 2:
# 
# Input: traversal = "1-2--3---4-5--6---7"
# Output: [1,2,5,3,null,6,null,4,null,7]
# 
# Example 3:
# 
# Input: traversal = "1-401--349---90--88"
# Output: [1,401,null,349,88,90]
# 
# 
# Constraints:
#         The number of nodes in the original tree is in the range [1, 1000].
#         1 <= Node.val <= 10^9

import sys
import os

# Add the parent directory to sys.path to import miscelaneus tools
current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)

# Import code needed for solutions
from tree import TreeNode

# Solution: https://youtu.be/VroH6J47kIE
# Credit: Navdeep Singh founder of NeetCode
def recover_from_preorder(traversal):
    dashes = 0 # depth
    stack = []
    i = 0

    while i < len(traversal):
        if traversal[i] == "-":
            dashes += 1
            i += 1
        else:
            j = i
            while j < len(traversal) and traversal[j] != "-":
                j += 1
            val = int(traversal[i:j])
            node = TreeNode(val)

            while len(stack) > dashes:
                stack.pop()
            
            if stack and not stack[-1].left:
                stack[-1].left = node
            elif stack:
                stack[-1].right = node
            stack.append(node)
            i = j
            dashes = 0

    return stack[0]
    # Time: O(n)
    # Space: O(h)  h = height of the tree

def main():
    result = recover_from_preorder(traversal = "1-2--3--4-5--6--7")
    print(result) # [1, 2, 5, 3, 4, 6, 7]

    result = recover_from_preorder(traversal = "1-2--3---4-5--6---7")
    print(result) # [1, 2, 5, 3, None, 6, None, 4, None, 7]

    result = recover_from_preorder(traversal = "1-401--349---90--88")
    print(result) # [1, 401, None, 349, 88, 90]

if __name__ == "__main__":
    main()
