# ------------------------
# 147. Insertion Sort List
# ------------------------

# Problem: https://leetcode.com/problems/insertion-sort-list/
# 
# Given the head of a singly linked list, sort the list using insertion sort, and return the sorted list's head.
# 
# The steps of the insertion sort algorithm:
# 
# 	Insertion sort iterates, consuming one input element each repetition and growing a sorted output list.
# 	At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list and inserts it there.
# 	It repeats until no input elements remain.
# 
# The following is a graphical example of the insertion sort algorithm. The partially sorted list (black) initially contains only the first element in the list. One element (red) is removed from the input data and inserted in-place into the sorted list with each iteration.
# 
# Example 1:
# 
# Input: head = [4,2,1,3]
# Output: [1,2,3,4]
# 
# Example 2:
# 
# Input: head = [-1,5,3,4,0]
# Output: [-1,0,3,4,5]
# 
#  
# Constraints:
# 
# 	The number of nodes in the list is in the range [1, 5000].
# 	-5000 <= Node.val <= 5000

import sys
import os

# Add the parent directory to sys.path to import miscelaneus tools
current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)

from linked import ListNode, from_list

# Solution: https://youtu.be/Kk6mXAzqX3Y
# Credit: Navdeep Singh founder of NeetCode
def insertion_sort_list(head):
    if not head or not head.next:
        return head

    sentinel = ListNode()
    curr = head
    while curr:
        prev = sentinel
        while prev.next and curr.val >= prev.next.val:
            prev = prev.next

        curr.next, prev.next, curr = prev.next, curr, curr.next

    return sentinel.next


def main():
    l = from_list([4,2,1,3])
    result = insertion_sort_list(l)
    print(result) # [1,2,3,4]

    l = from_list([-1,5,3,4,0])
    result = insertion_sort_list(l)
    print(result) # [-1,0,3,4,5]

if __name__ == "__main__":
    main()
