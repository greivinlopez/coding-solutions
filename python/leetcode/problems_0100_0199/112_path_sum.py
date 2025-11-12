# -----------------
# 112. Path Sum 🌲
# -----------------

# Problem: https://leetcode.com/problems/path-sum/
# 
# Given the root of a binary tree and an integer targetSum, return true if the 
# tree has a root-to-leaf path such that adding up all the values along the 
# path equals targetSum.
# 
# A leaf is a node with no children.

import sys
import os

# Add the parent directory to sys.path to import miscelaneus tools
current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)

from tree import get_tree

# Solution: https://youtu.be/LSKQyOz_P8I
# Credit: Navdeep Singh founder of NeetCode
def has_path_sum(root, sum):
    # Recursive Solution
    # Time: O(n)
    # Space: O(h) or O(n)
    if not root:
        return False
    sum -= root.val
    if not root.left and not root.right:
        return sum == 0
    return has_path_sum(root.left, sum) or has_path_sum(root.right, sum)

def has_path_sum_iter(root, sum):
    # Iterative Solution
    de = [
        (root, sum - root.val),
    ]
    while de:
        node, curr_sum = de.pop()
        if not node.left and not node.right and curr_sum == 0:
            return True
        if node.right:
            de.append((node.right, curr_sum - node.right.val))
        if node.left:
            de.append((node.left, curr_sum - node.left.val))
    return False

# Same Solution: https://youtu.be/Txzs2maQ_D0
# Credit: Greg Hogg


def main():
    root = get_tree("[5,4,8,11,null,13,4,7,2,null,null,null,1]")
    result = has_path_sum(root, 22)
    print(result) # True

    root = get_tree("[1,2,3]")
    result = has_path_sum(root, 5)
    print(result) # False

    result = has_path_sum(None, 0)
    print(result) # False

if __name__ == "__main__":
    main()