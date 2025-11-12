# ------------------------------------
# 1721. Swapping Nodes In A Linked List
# ------------------------------------

# Problem: https://leetcode.com/problems/swapping-nodes-in-a-linked-list
#
# You are given the head of a linked list, and an integer k.
# 
# Return the head of the linked list after swapping the values of the kth node
# from the beginning and the kth node from the end (the list is 1-indexed).
# 
# Example 1:
# 
# Input: head = [1,2,3,4,5], k = 2
# Output: [1,4,3,2,5]
# 
# Example 2:
# 
# Input: head = [7,9,6,6,7,8,3,0,9,5], k = 5
# Output: [7,9,6,6,8,7,3,0,9,5]
# 
# 
# Constraints:
#         The number of nodes in the list is n.
#         1 <= k <= n <= 10^5
#         0 <= Node.val <= 100

import sys
import os

# Add the parent directory to sys.path to import miscelaneus tools
current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)

from linked import from_list

# Solution: https://youtu.be/4LsrgMyQIjQ
# Credit: Navdeep Singh founder of NeetCode
def swap_nodes(head, k):
    right_pointer = head
    for _ in range(1, k):
        right_pointer = right_pointer.next
    left_kth_node = right_pointer

    left_pointer = head
    while right_pointer is not None:
        right_kth_node = left_pointer
        right_pointer = right_pointer.next
        left_pointer = left_pointer.next

    left_kth_node.val, right_kth_node.val = right_kth_node.val, left_kth_node.val
    return head


def main():
    head = from_list([1,2,3,4,5])
    result = swap_nodes(head, 2)
    print(result) # [1, 4, 3, 2, 5]

    head = from_list([7,9,6,6,7,8,3,0,9,5])
    result = swap_nodes(head, 5)
    print(result) # [7, 9, 6, 6, 8, 7, 3, 0, 9, 5]

if __name__ == "__main__":
    main()
