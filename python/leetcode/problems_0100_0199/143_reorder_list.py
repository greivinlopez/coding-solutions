# ------------------
# 143. Reorder List
# ------------------

# Problem: https://leetcode.com/problems/reorder-list/
# 
# You are given the head of a singly linked-list. The list can be represented as:
# 
# L0 → L1 → … → Ln - 1 → Ln
# 
# Reorder the list to be on the following form:
# 
# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
# 
# You may not modify the values in the list's nodes. Only nodes themselves may be changed.
#  
# Example 1:
# 
# Input: head = [1,2,3,4]
# Output: [1,4,2,3]
#  
# Example 2:
# 
# Input: head = [1,2,3,4,5]
# Output: [1,5,2,4,3]
#  
# Constraints:
# 
# 	The number of nodes in the list is in the range [1, 5 * 104].
# 	1 <= Node.val <= 1000

import sys
import os

# Add the parent directory to sys.path to import miscelaneus tools
current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)

from linked import ListNode, from_list, to_list

# Solution: https://youtu.be/S5bfdUTrKLM
# Credit: Navdeep Singh founder of NeetCode
def reorder_list(head: ListNode) -> None:
    # find middle
    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # reverse second half
    second = slow.next
    prev = slow.next = None
    while second:
        tmp = second.next
        second.next = prev
        prev = second
        second = tmp

    # merge two halfs
    first, second = head, prev
    while second:
        tmp1, tmp2 = first.next, second.next
        first.next = second
        second.next = tmp1
        first, second = tmp1, tmp2


def main():
    l = from_list([1,2,3,4])
    reorder_list(l)
    print(l) # [1,4,2,3]

    l = from_list([1,2,3,4,5])
    reorder_list(l)
    print(l) # [1,5,2,4,3]

if __name__ == "__main__":
    main()
