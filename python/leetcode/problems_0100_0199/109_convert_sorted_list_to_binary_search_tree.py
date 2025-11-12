# ----------------------------------------------
# 109. Convert Sorted List to Binary Search Tree
# ----------------------------------------------

# Problem: https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree
#
# Given the head of a singly linked list where elements are sorted in ascending
# order, convert it to a height-balanced binary search tree.
# 
# Example 1:
# 
# https://assets.leetcode.com/uploads/2020/08/17/linked.jpg
# 
# Input: head = [-10,-3,0,5,9]
# Output: [0,-3,9,-10,null,5]
# 
# Explanation: One possible answer is [0,-3,9,-10,null,5], which represents the
# shown height balanced BST.
# 
# Example 2:
# 
# Input: head = []
# Output: []
# 
# 
# Constraints:
#         The number of nodes in head is in the range [0, 2 * 10⁴].
#         -10⁵ <= Node.val <= 10⁵

import sys
import os

# Add the parent directory to sys.path to import miscelaneus tools
current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)

from linked import from_list
from tree import TreeNode


# Credit: Jeel Gajera -> https://github.com/JeelGajera
def sorted_list_to_BST(head):
    if not head: return None
    if head.next == None: return TreeNode(head.val)

    slow = head
    fast = head
    mid = slow

    while fast != None and fast.next != None:
        mid = slow
        slow = slow.next
        fast = fast.next.next

    node = TreeNode(slow.val)
    mid.next = None
    node.left = sorted_list_to_BST(head)
    node.right = sorted_list_to_BST(slow.next)

    return node


def main():
    result = sorted_list_to_BST(from_list([-10,-3,0,5,9]))
    print(result) # [0, -3, 9, -10, None, 5]

    result = sorted_list_to_BST(from_list([]))
    print(result) # None

if __name__ == "__main__":
    main()
