# --------------------------
# 21. Merge Two Sorted Lists
# --------------------------

# Problem: https://leetcode.com/problems/merge-two-sorted-lists
#
# You are given the heads of two sorted linked lists list1 and list2.
# 
# Merge the two lists into one sorted list. The list should be made by splicing
# together the nodes of the first two lists.
# 
# Return the head of the merged linked list.
# 
# Example 1:
# 
# https://assets.leetcode.com/uploads/2020/10/03/merge_ex1.jpg
# 
# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]
# 
# Example 2:
# 
# Input: list1 = [], list2 = []
# Output: []
# 
# Example 3:
# 
# Input: list1 = [], list2 = [0]
# Output: [0]
# 
# 
# Constraints:
#         The number of nodes in both lists is in the range [0, 50].
#         -100 <= Node.val <= 100
#         Both list1 and list2 are sorted in non-decreasing order.

import sys
import os

# Add the parent directory to sys.path to import miscelaneus tools
current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)

from linked import ListNode, from_list

# Solution: https://youtu.be/XIdigk956u0
# Credit: Navdeep Singh founder of NeetCode 
def merge_two_lists(list1, list2):
    # Iterative Solution
    dummy = node = ListNode()

    while list1 and list2:
        if list1.val < list2.val:
            node.next = list1
            list1 = list1.next
        else:
            node.next = list2
            list2 = list2.next
        node = node.next

    node.next = list1 or list2

    return dummy.next
    # Time: O(n)
    # Space: O(1)

# Same Solution: https://youtu.be/5Rec4JS9H5o
# Credit: Greg Hogg
    
# Recursive Solution
# Credit: Navdeep Singh founder of NeetCode
def merge_two_lists_recursive(list1, list2):
    if not list1:
        return list2
    if not list2:
        return list1
    lil, big = (list1, list2) if list1.val < list2.val else (list2, list1)
    lil.next = merge_two_lists_recursive(lil.next, big)
    return lil
    # Time: O(n + m)
    # Space: O(n + m)


def main():
    l1 = from_list([1,2,4])
    l2 = from_list([1,3,4])
    result = merge_two_lists(l1,l2) 
    print(result) # [1,1,2,3,4,4]

    l1 = from_list([])
    l2 = from_list([])
    result = merge_two_lists(l1,l2) 
    print(result) # []

    l1 = from_list([])
    l2 = from_list([0])
    result = merge_two_lists(l1,l2) 
    print(result) # [0]

if __name__ == "__main__":
    main()