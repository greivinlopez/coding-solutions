# ------------------------
# 206. Reverse Linked List
# ------------------------

# Problem: https://leetcode.com/problems/reverse-linked-list/
# 
# Given the head of a singly linked list, reverse the list, and return the 
# reversed list.
# 
#  
# Example 1:
# 
# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]
# 
# 
# Example 2:
# 
# Input: head = [1,2]
# Output: [2,1]
# 
# 
# Example 3:
# 
# Input: head = []
# Output: []
# 
# 
# Constraints:
# 
# 	The number of nodes in the list is the range [0, 5000].
# 	-5000 <= Node.val <= 5000
# 
# Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?

import sys
import os

# Add the parent directory to sys.path to import miscelaneus tools
current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)

from linked import ListNode, from_list

# Solution: https://youtu.be/G0_I-ZF0S38
# Credit: Navdeep Singh founder of NeetCode
def reverse_list(head):
    # Time: O(n)
    # Space: O(1)
    prev, curr = None, head

    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    return prev

# Solution: https://youtu.be/KRxeMng7fBU
# Credit: Greg Hogg
# Same Solution

def main():
    l = from_list([1,2,3,4,5])
    result = reverse_list(l)
    print(result) # [5,4,3,2,1]

    l2 = from_list([1,2])
    result = reverse_list(l2)
    print(result) # [2,1]

if __name__ == "__main__":
    main()
