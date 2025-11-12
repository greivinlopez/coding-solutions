# -----------------------------------------
# 82. Remove Duplicates from Sorted List II
# -----------------------------------------

# Problem: https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii
#
# Given the head of a sorted linked list, delete all nodes that have duplicate
# numbers, leaving only distinct numbers from the original list. Return the linked
# list sorted as well.
# 
# Example 1:
# https://assets.leetcode.com/uploads/2021/01/04/linkedlist1.jpg
# 
# Input: head = [1,2,3,3,4,4,5]
# Output: [1,2,5]
# 
# Example 2:
# https://assets.leetcode.com/uploads/2021/01/04/linkedlist2.jpg
#
# Input: head = [1,1,1,2,3]
# Output: [2,3]
# 
# 
# Constraints:
#         The number of nodes in the list is in the range [0, 300].
#         -100 <= Node.val <= 100
#         The list is guaranteed to be sorted in ascending order.

import sys
import os

# Add the parent directory to sys.path to import miscelaneus tools
current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)

from linked import ListNode, from_list

# Credit: Jeel Gajera -> https://github.com/JeelGajera
def delete_duplicates(head):
    dummy = prev = ListNode(0)
    dummy.next = head
    while head and head.next:
        if head.val == head.next.val:
            while head and head.next and head.val == head.next.val:
                head = head.next
            head = head.next
            prev.next = head
        else:
            prev = prev.next
            head = head.next

    return dummy.next
    # Time: O(n)
    # Space: O(1)


def main():
    result = delete_duplicates(head = from_list([1,2,3,3,4,4,5]))
    print(result) # [1,2,5]

    result = delete_duplicates(head = from_list([1,1,1,2,3]))
    print(result) # [2,3]

if __name__ == "__main__":
    main()
