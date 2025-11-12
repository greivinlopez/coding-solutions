# ---------------------------
# 92. Reverse Linked List II
# ---------------------------

# Problem: https://leetcode.com/problems/reverse-linked-list-ii/
# 
# Given the head of a singly linked list and two integers left and right where 
# left <= right, reverse the nodes of the list from position left to position 
# right, and return the reversed list.

import sys
import os

# Add the parent directory to sys.path to import miscelaneus tools
current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)

from linked import ListNode, from_list

# Solution: https://youtu.be/RF_M9tX4Eag
# Credit: Navdeep Singh founder of NeetCode 
def reverse_between(head, left, right):
    dummy = ListNode(0, head)

    # 1) reach node at position "left"
    leftPrev, cur = dummy, head
    for i in range(left - 1):
        leftPrev, cur = cur, cur.next

    # Now cur="left", leftPrev="node before left"
    # 2) reverse from left to right
    prev = None
    for i in range(right - left + 1):
        tmpNext = cur.next
        cur.next = prev
        prev, cur = cur, tmpNext

    # 3) Update pointers
    leftPrev.next.next = cur  # cur is node after "right"
    leftPrev.next = prev  # prev is "right"
    return dummy.next

def main():
    l = from_list([1,2,3,4,5])
    result = reverse_between(l, left = 2, right = 4) # [1,4,3,2,5]
    print(result)

    l = from_list([5])
    result = reverse_between(l, left = 1, right = 1) # [5]
    print(result)

if __name__ == "__main__":
    main()