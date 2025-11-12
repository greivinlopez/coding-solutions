# ---------------------------------------
# 83. Remove Duplicates from Sorted List
# ---------------------------------------

# Problem: https://leetcode.com/problems/remove-duplicates-from-sorted-list/
# 
# Given the head of a sorted linked list, delete all duplicates such that each 
# element appears only once. Return the linked list sorted as well.

import sys
import os

# Add the parent directory to sys.path to import miscelaneus tools
current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)

from linked import ListNode, from_list

# Solution: https://youtu.be/p10f-VpO4nE
# Credit: Navdeep Singh founder of NeetCode 
def delete_duplicates(head):
    # Time: O(n)
    # Space: O(1)
    cur = head
    while cur:
        while cur.next and cur.next.val == cur.val:
            cur.next = cur.next.next
        cur = cur.next
    return head

# Solution: https://youtu.be/Nvf9Yt1EElg
# Credit: Greg Hogg
# Almost identical
def delete_duplicates_alt(head):
    # Time: O(n)
    # Space: O(1)
    cur = head
    while cur and cur.next:
        if cur.val == cur.next.val:
            cur.next = cur.next.next
        else:
            cur = cur.next
    return head

def main():
    l = from_list([1,1,2])
    result = delete_duplicates(l) # [1,2]
    print(result)

    l = from_list([1,1,2,3,3])
    result = delete_duplicates(l) # [1,2,3]
    print(result)

if __name__ == "__main__":
    main()