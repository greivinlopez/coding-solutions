# -----------------------
# 24. Swap Nodes in Pairs
# -----------------------

# Problem: https://leetcode.com/problems/swap-nodes-in-pairs
#
# Given a linked list, swap every two adjacent nodes and return its head. You must
# solve the problem without modifying the values in the list's nodes (i.e., only
# nodes themselves may be changed.)
# 
# Example 1:
# 
# Input: head = [1,2,3,4]
# Output: [2,1,4,3]
# 
# Explanation:
# https://assets.leetcode.com/uploads/2020/10/03/swap_ex1.jpg
# 
# Example 2:
# 
# Input: head = []
# Output: []
# 
# Example 3:
# 
# Input: head = [1]
# Output: [1]
# 
# Example 4:
# 
# Input: head = [1,2,3]
# Output: [2,1,3]
# 
# 
# Constraints:
#         The number of nodes in the list is in the range [0, 100].
#         0 <= Node.val <= 100

import sys
import os

# Add the parent directory to sys.path to import miscelaneus tools
current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)

from linked import ListNode, from_list

# Solution: https://youtu.be/o811TZLAWOo
# Credit: Navdeep Singh founder of NeetCode 
def swap_pairs(head):
    # Time: O(n)
    dummy = ListNode(0, head)
    prev, curr = dummy, head

    while curr and curr.next:
        # save ptrs
        nxtPair = curr.next.next
        second = curr.next

        # reverse this pair
        second.next = curr
        curr.next = nxtPair
        prev.next = second

        # update ptrs
        prev = curr
        curr = nxtPair

    return dummy.next


def main():
    l = from_list([1,2,3,4])
    result = swap_pairs(l) # [2,1,4,3]
    print(result)

    l = from_list([])
    result = swap_pairs(l) # None
    print(result)

    l = from_list([1])
    result = swap_pairs(l) # [1]
    print(result)

    l = from_list([1,2,3])
    result = swap_pairs(l) # [2,1,3]
    print(result)

if __name__ == "__main__":
    main()