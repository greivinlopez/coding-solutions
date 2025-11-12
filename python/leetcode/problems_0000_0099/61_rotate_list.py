# -------------------
# 61. Rotate List 🔄
# -------------------

# Problem: https://leetcode.com/problems/rotate-list/
# 
# Given the head of a linked list, rotate the list to the right by k places.

import sys
import os

# Add the parent directory to sys.path to import miscelaneus tools
current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)

from linked import ListNode, from_list

# Solution: https://youtu.be/UcGtPs2LE_c
# Credit: Navdeep Singh founder of NeetCode 
def rotate_right(head, k):
    if not head or not head.next or k == 0:
        return head

    old_head = head

    curr, size = head, 0
    while curr:
        curr, size = curr.next, size + 1

    if k % size == 0:
        return head

    k %= size
    slow = fast = head
    while fast and fast.next:
        if k <= 0:
            slow = slow.next
        fast = fast.next
        k -= 1

    new_tail, new_head, old_tail = slow, slow.next, fast
    new_tail.next, old_tail.next = None, old_head

    return new_head

def main():
    l = from_list([1,2,3,4,5])
    result = rotate_right(l, 2) # [4,5,1,2,3]
    print(result)

    l = from_list([0,1,2])
    result = rotate_right(l, 4) # [2,0,1]
    print(result)

if __name__ == "__main__":
    main()