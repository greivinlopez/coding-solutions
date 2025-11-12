# ------------------------------------
# 19. Remove Nth Node From End of List
# ------------------------------------

# Problem: https://leetcode.com/problems/remove-nth-node-from-end-of-list
#
# Given the head of a linked list, remove the n^th node from the end of the list
# and return its head.
# 
# Example 1:
# 
# https://assets.leetcode.com/uploads/2020/10/03/remove_ex1.jpg
# 
# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]
# 
# Example 2:
# 
# Input: head = [1], n = 1
# Output: []
# 
# Example 3:
# 
# Input: head = [1,2], n = 1
# Output: [1]
# 
# 
# Constraints:
#         The number of nodes in the list is sz.
#         1 <= sz <= 30
#         0 <= Node.val <= 100
#         1 <= n <= sz
# 
# Follow up: Could you do this in one pass?

import sys
import os

# Add the parent directory to sys.path to import miscelaneus tools
current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)

from linked import ListNode, from_list

# Solution: https://youtu.be/XVuQxVej6y8
# Credit: Navdeep Singh founder of NeetCode 
def remove_nth_from_end(head, n):
    dummy = ListNode(0, head)
    left = dummy
    right = head

    while n > 0:
        right = right.next
        n -= 1

    while right:
        left = left.next
        right = right.next

    # delete
    left.next = left.next.next
    return dummy.next
    # Time: O(n)
    # Space: O(1)

# Alternate Video Same Solution: https://youtu.be/fbi4UdayLSA

# Credit: Jeel Gajera -> https://github.com/JeelGajera
def remove_nth_from_end(head, n):
    cur = head
    length = 0
    while cur.next != None:
        length += 1
        cur = cur.next
    else:
        length += 1

    target = length - n
    prev = ListNode()
    cur = head

    if target == 0:
        head = cur.next
    else:
        for i in range(target):
            if i == target-1:
                prev = cur
            cur = cur.next
        prev.next = cur.next
    return head
    # Time: O(n)
    # Space: O(1)


def main():
    l = from_list([1,2,3,4,5])
    result = remove_nth_from_end(l, 2) 
    print(result) # [1,2,3,5]

    l = ListNode(1)
    result = remove_nth_from_end(l, 1) 
    print(result) # []

    l = from_list([1,2])
    result = remove_nth_from_end(l, 1) 
    print(result) # [1]

if __name__ == "__main__":
    main()