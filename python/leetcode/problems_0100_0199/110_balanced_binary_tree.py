# ----------------------------
# 110. Balanced Binary Tree 🌲
# ----------------------------

# Problem: https://leetcode.com/problems/balanced-binary-tree/
# 
# Given a binary tree, determine if it is height-balanced.

import sys
import os

# Add the parent directory to sys.path to import miscelaneus tools
current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)

from tree import get_tree

# Solution: https://youtu.be/QfJsau0ItOY
# Credit: Navdeep Singh founder of NeetCode
def is_balanced(root):
    def dfs(root):
        if not root:
            return [True, 0]

        left, right = dfs(root.left), dfs(root.right)
        balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1
        return [balanced, 1 + max(left[1], right[1])]

    return dfs(root)[0]

# Solution: https://youtu.be/BrnZDIoScEA
# Credit: Greg Hogg
def is_balanced_alt(root):
    # Time: O(n)
    # Space: O(h) { here "h" is the height of the tree }
    balanced = [True]

    def height(root):
        if not root:
            return 0

        left_height = height(root.left)
        if balanced[0] is False:
            return 0

        right_height = height(root.right)
        if abs(left_height - right_height) > 1:
            balanced[0] = False
            return 0
        return 1 + max(left_height, right_height)

    height(root)
    return balanced[0]


def main():
    root = get_tree("[3,9,20,null,null,15,7]")
    result = is_balanced(root)
    print(result) # True

    root = get_tree("[1,2,2,3,3,null,null,4,4]")
    result = is_balanced(root)
    print(result) # False

    result = is_balanced(None)
    print(result) # True

if __name__ == "__main__":
    main()