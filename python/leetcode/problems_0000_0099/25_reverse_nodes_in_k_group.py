# ----------------------------
# 25. Reverse Nodes in k-Group
# ----------------------------

# Problem: https://leetcode.com/problems/reverse-nodes-in-k-group
#
# Given the head of a linked list, reverse the nodes of the list k at a time, and
# return the modified list.
# 
# k is a positive integer and is less than or equal to the length of the linked
# list. If the number of nodes is not a multiple of k then left-out nodes, in the
# end, should remain as it is.
# 
# You may not alter the values in the list's nodes, only nodes themselves may be
# changed.
# 
# Example 1:
# 
# https://assets.leetcode.com/uploads/2020/10/03/reverse_ex1.jpg
# 
# Input: head = [1,2,3,4,5], k = 2
# Output: [2,1,4,3,5]
# 
# Example 2:
# 
# https://assets.leetcode.com/uploads/2020/10/03/reverse_ex2.jpg
# 
# Input: head = [1,2,3,4,5], k = 3
# Output: [3,2,1,4,5]
# 
# 
# Constraints:
#         The number of nodes in the list is n.
#         1 <= k <= n <= 5000
#         0 <= Node.val <= 1000
# 
# 
# Follow-up: Can you solve the problem in O(1) extra memory space?

import sys
import os

# Add the parent directory to sys.path to import miscelaneus tools
current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)

from linked import ListNode, from_list

# Solution: https://youtu.be/1UOPsfP85V4
# Credit: Navdeep Singh founder of NeetCode
def reverse_k_group(head, k):
    dummy = ListNode(0, head)
    groupPrev = dummy

    def get_kth(curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr

    while True:
        kth = get_kth(groupPrev, k)
        if not kth:
            break
        groupNext = kth.next

        # reverse group
        prev, curr = kth.next, groupPrev.next
        while curr != groupNext:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        tmp = groupPrev.next
        groupPrev.next = kth
        groupPrev = tmp
    return dummy.next
    # Time: O(n)
    # Space: O(1)


def main():
    l = from_list([1,2,3,4,5])
    result = reverse_k_group(l, 2) # [2,1,4,3,5]
    print(result)

    l = from_list([1,2,3,4,5])
    result = reverse_k_group(l, 3) # [3,2,1,4,5]
    print(result)

if __name__ == "__main__":
    main()