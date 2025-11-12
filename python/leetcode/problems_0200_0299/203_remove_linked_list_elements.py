# --------------------------------
# 203. Remove Linked List Elements
# --------------------------------

# Problem: https://leetcode.com/problems/remove-linked-list-elements/
# 
# Given the head of a linked list and an integer val, remove all the nodes of 
# the linked list that has Node.val == val, and return the new head.
# 
#  
# Example 1:
# 
# Input: head = [1,2,6,3,4,5,6], val = 6
# Output: [1,2,3,4,5]
# 
# 
# Example 2:
# 
# Input: head = [], val = 1
# Output: []
# 
# 
# Example 3:
# 
# Input: head = [7,7,7,7], val = 7
# Output: []
# 
#  
# Constraints:
# 
# 	The number of nodes in the list is in the range [0, 10^4].
# 	1 <= Node.val <= 50
# 	0 <= val <= 50

import sys
import os

# Add the parent directory to sys.path to import miscelaneus tools
current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)

from linked import ListNode, from_list


# Solution: https://youtu.be/JI71sxtHTng
# Credit: Navdeep Singh founder of NeetCode
def remove_elements(head, val):
    dummy = ListNode(next=head)
    prev, curr = dummy, head
    
    while curr:
        nxt = curr.next
        
        if curr.val == val:
            prev.next = nxt
        else:
            prev = curr
        
        curr = nxt
    return dummy.next


def main():
    l = from_list([1,2,6,3,4,5,6])
    result = remove_elements(l, 6)
    print(result) # [1,2,3,4,5]

    l = from_list([7,7,7,7])
    result = remove_elements(l, 7)
    print(result) # []

if __name__ == "__main__":
    main()
