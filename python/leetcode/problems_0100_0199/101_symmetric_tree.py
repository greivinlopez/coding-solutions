# -----------------------
# 101. Symmetric Tree 🌲
# -----------------------

# Problem: https://leetcode.com/problems/symmetric-tree/
# 
# Given the root of a binary tree, check whether it is a mirror of itself 
# (i.e., symmetric around its center).

import sys
import os

# Add the parent directory to sys.path to import miscelaneus tools
current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)

# Import code needed for solutions
from tree import get_tree
from collections import deque

# Solution: https://youtu.be/Mao9uzxwvmc
# Credit: Navdeep Singh founder of NeetCode
def is_symmetric(root):
    if not root.left and not root.right:
        return True
    queueLeft = deque()
    queueRight = deque()

    queueLeft.appendleft(root.left)
    queueRight.appendleft(root.right)

    while queueLeft and queueRight:
        nodeLeft, nodeRight = queueLeft.pop(), queueRight.pop()
        if not nodeLeft and not nodeRight:
            continue
        # both node must exist
        # if exists thet must have the same value
        if not nodeLeft or not nodeRight or nodeLeft.val != nodeRight.val:
            return False

        queueLeft.appendleft(nodeLeft.left)
        queueLeft.appendleft(nodeLeft.right)

        queueRight.appendleft(nodeRight.right)
        queueRight.appendleft(nodeRight.left)
    return not (queueLeft or queueRight)
    
# Solution: https://youtu.be/BooilJIjNHc
# Credit: Greg Hogg
def is_symmetric_rec(root):
    # Time: O(n)
    # Space: O(height) or O(n)
    def same(root1, root2):
        if not root1 and not root2:
            return True

        if not root1 or not root2:
            return False
        
        if root1.val != root2.val:
            return False
        
        return same(root1.left, root2.right) and \
                same(root1.right, root2.left)

    return same(root, root)


def main():
    root = get_tree("[1,2,2,3,4,4,3]")
    result = is_symmetric(root)
    print(result) # True

    root = get_tree("[1,2,2,null,3,null,3]")
    result = is_symmetric(root)
    print(result) # False

if __name__ == "__main__":
    main()