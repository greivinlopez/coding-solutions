# ------------------------------
# 99. Recover Binary Search Tree
# ------------------------------

# Problem: https://leetcode.com/problems/recover-binary-search-tree
#
# You are given the root of a binary search tree (BST), where the values of
# exactly two nodes of the tree were swapped by mistake. Recover the tree without
# changing its structure.
# 
# Example 1:
# 
# https://assets.leetcode.com/uploads/2020/10/28/recover1.jpg
# 
# Input: root = [1,3,null,null,2]
# Output: [3,1,null,null,2]
# 
# Explanation: 3 cannot be a left child of 1 because 3 > 1. Swapping 1 and 3 makes
# the BST valid.
# 
# Example 2:
# 
# https://assets.leetcode.com/uploads/2020/10/28/recover2.jpg
# 
# Input: root = [3,1,4,null,null,2]
# Output: [2,1,4,null,null,3]
# 
# Explanation: 2 cannot be in the right subtree of 3 because 2 < 3. Swapping 2 and
# 3 makes the BST valid.
# 
# 
# Constraints:
#         The number of nodes in the tree is in the range [2, 1000].
#         -2³¹ <= Node.val <= 2³¹ - 1
# 
# Follow up: A solution using O(n) space is pretty straight-forward. Could you
# devise a constant O(1) space solution?

import sys
import os

# Add the parent directory to sys.path to import miscelaneus tools
current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)

from tree import get_tree


# Solution: https://leetcode.com/problems/recover-binary-search-tree/solutions/7021623/beats-100-beginner-friendly-explanation-and-code-java-python-c-javascript
# Credit: Pradhuman Gupta -> https://leetcode.com/u/PradhumanGupta/
def recover_tree(root):
    first = second = prev = None

    def inorder(node):
        nonlocal first, second, prev
        if not node:
            return
        inorder(node.left)
        if prev and prev.val > node.val:
            if not first:
                first = prev
            second = node
        prev = node
        inorder(node.right)

    inorder(root)

    # Swap the values
    first.val, second.val = second.val, first.val
    # Time: O(n)
    # Space: O(h)


def main():
    root = get_tree("[1,3,null,null,2]")
    recover_tree(root)
    print(root) # [3, 1, None, None, 2]

    root1 = get_tree("[3,1,4,null,null,2]")
    recover_tree(root1)
    print(root1) # [2, 1, 4, None, None, 3]

if __name__ == "__main__":
    main()
