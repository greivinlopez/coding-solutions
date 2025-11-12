# ---------------------------
# 234. Palindrome Linked List
# ---------------------------

# Problem: https://leetcode.com/problems/palindrome-linked-list/
# 
# Given the head of a singly linked list, return true if it is a palindrome 
# or false otherwise.
# 
#  
# Example 1:
# 
# Input: head = [1,2,2,1]
# Output: true
# 
# 
# Example 2:
# 
# Input: head = [1,2]
# Output: false
# 
# 
# Constraints:
# 
# 	The number of nodes in the list is in the range [1, 105].
# 	0 <= Node.val <= 9
# 
# Follow up: Could you do it in O(n) time and O(1) space?

import sys
import os

# Add the parent directory to sys.path to import miscelaneus tools
current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)

from linked import ListNode, from_list

# Solution: https://youtu.be/yOzXms1J6Nk
# Credit: Navdeep Singh founder of NeetCode
def is_palindrome(head):
    fast = head
    slow = head
    
    # find the middle (slow)
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        
    # reverse second half
    prev = None
    while slow:
        tmp = slow.next
        slow.next = prev
        prev = slow
        slow = tmp
    
    # check palindrome
    left, right = head, prev
    while right:
        if left.val != right.val:
            return False
        left = left.next
        right = right.next
    return True


def main():
    l = from_list([1,2,2,1])
    result = is_palindrome(l)
    print(result) # True

    l2 = from_list([1,2])
    result = is_palindrome(l2)
    print(result) # False

if __name__ == "__main__":
    main()
