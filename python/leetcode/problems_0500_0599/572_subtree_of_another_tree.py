# ----------------------------
# 572. Subtree Of Another Tree
# ----------------------------

# Problem: https://leetcode.com/problems/subtree-of-another-tree/
# 
# Given the roots of two binary trees root and subRoot, return true if there is 
# a subtree of root with the same structure and node values of subRoot and false
# otherwise.
# 
# A subtree of a binary tree tree is a tree that consists of a node in tree and 
# all of this node's descendants. The tree tree could also be considered as a 
# subtree of itself.
# 
#  
# Example 1:
# 
# Input: root = [3,4,5,1,2], subRoot = [4,1,2]
# Output: true
# 
# 
# Example 2:
# 
# Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
# Output: false
# 
# 
# Constraints:
# 
# 	The number of nodes in the root tree is in the range [1, 2000].
# 	The number of nodes in the subRoot tree is in the range [1, 1000].
# 	-10^4 <= root.val <= 10^4
# 	-10^4 <= subRoot.val <= 10^4

import sys
import os

# Add the parent directory to sys.path to import miscelaneus tools
current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)

# Import code needed for solutions
from tree import get_tree

# Solution: https://youtu.be/E36O5SWp-LE
# Credit: Navdeep Singh founder of NeetCode
def is_subtree(root, subRoot):
    if not subRoot:
        return True
    if not root:
        return False

    if is_same_tree(root, subRoot):
        return True
    return is_subtree(root.left, subRoot) or is_subtree(root.right, subRoot)
    # Time: O(m * n)
    # Space: O(n)

def is_same_tree(p, q):
    if not p and not q:
        return True
    if p and q and p.val == q.val:
        return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)
    else:
        return False

# Solution: https://youtu.be/fvyqbtmor9U
# Credit: Greg Hogg
# Same Solution


def main():
    root = get_tree("[3,4,5,1,2]")
    subroot = get_tree("[4,1,2]")
    result = is_subtree(root, subroot)
    print(result) # True

    root = get_tree("[3,4,5,1,2,null,null,null,null,0]")
    subroot = get_tree("[4,1,2]")
    result = is_subtree(root, subroot)
    print(result) # False

if __name__ == "__main__":
    main()
