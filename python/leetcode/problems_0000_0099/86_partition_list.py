# -------------------
# 86. Partition List
# -------------------

# Problem: https://leetcode.com/problems/partition-list/
# 
# Given the head of a linked list and a value x, partition it such that all 
# nodes less than x come before nodes greater than or equal to x.
# 
# You should preserve the original relative order of the nodes in each of the 
# two partitions.

import sys
import os

# Add the parent directory to sys.path to import miscelaneus tools
current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)

from linked import ListNode, from_list

# Solution: https://youtu.be/KT1iUciJr4g
# Credit: Navdeep Singh founder of NeetCode 
def partition(head, x):
    less_head, bigger_head = ListNode(-1), ListNode(-1)
    less_prev, bigger_prev = less_head, bigger_head
    while head:
        if head.val < x:
            less_prev.next = head
            less_prev = less_prev.next
        else:
            bigger_prev.next = head
            bigger_prev = bigger_prev.next

        head = head.next

    less_prev.next = bigger_prev.next = None
    less_prev.next = bigger_head.next

    return less_head.next

def main():
    l = from_list([1,4,3,2,5,2])
    result = partition(l, 3) # [1,2,2,4,3,5]
    print(result)

    l = from_list([2,1])
    result = partition(l, 2) # [1,2]
    print(result)

if __name__ == "__main__":
    main()