# --------------------------------
# 1367. Linked List in Binary Tree
# --------------------------------

# Problem: https://leetcode.com/problems/linked-list-in-binary-tree
#
# Given a binary tree root and a linked list with head as the first node. 
# 
# Return True if all the elements in the linked list starting from the head
# correspond to some downward path connected in the binary tree otherwise return
# False.
# 
# In this context downward path means a path that starts at some node and goes
# downwards.
# 
# Example 1:
# 
# Input: head = [4,2,8], root =
# [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
# Output: true
# 
# Explanation: Nodes in blue form a subpath in the binary Tree.
# 
# Example 2:
# 
# Input: head = [1,4,2,6], root =
# [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
# Output: true
# 
# Example 3:
# 
# Input: head = [1,4,2,6,8], root =
# [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
# Output: false
# 
# Explanation: There is no path in the binary tree that contains all the elements
# of the linked list from head.
# 
# 
# Constraints:
#         The number of nodes in the tree will be in the range [1, 2500].
#         The number of nodes in the list will be in the range [1, 100].
#         1 <= Node.val <= 100 for each node in the linked list and binary tree.

import sys
import os

# Add the parent directory to sys.path to import miscelaneus tools
current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)

# Import code needed for solutions
from tree import get_tree
from linked import from_list

# Solution: https://youtu.be/OaA9MgG00AE
# Credit: Navdeep Singh founder of NeetCode
def is_sub_path(head, root):
    
    def helper(list_node, tree_node):
        if not list_node:
            return True
        if not tree_node or list_node.val != tree_node.val:
            return False
        return (
            helper(list_node.next, tree_node.left) or
            helper(list_node.next, tree_node.right)
        )
    
    if helper(head, root):
        return True
    if not root:
        return False
    return (
        is_sub_path(head, root.left) or
        is_sub_path(head, root.right)
    )
    # Time: O(n * m * min(l, h))
    # Space: O(h + l)
    # n = number of nodes in the binary tree
    # m = numner of times of the matching process (potentially for each node)
    # l = length of the linked list
    # h = height of the binary tree


def main():
    root = get_tree("[1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]")
    head = from_list([4,2,8])
    result = is_sub_path(head, root)
    print(result) # True

    root = get_tree("[1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]")
    head = from_list([1,4,2,6])
    result = is_sub_path(head, root)
    print(result) # True

    root = get_tree("[1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]")
    head = from_list([1,4,2,6,8])
    result = is_sub_path(head, root)
    print(result) # False

if __name__ == "__main__":
    main()
