# ----------------------
# 141. Linked List Cycle
# ----------------------

# Problem: https://leetcode.com/problems/linked-list-cycle/
# 
# Given head, the head of a linked list, determine if the linked list has a 
# cycle in it.
# 
# There is a cycle in a linked list if there is some node in the list that 
# can be reached again by continuously following the next pointer. 
# Internally, pos is used to denote the index of the node that tail's next 
# pointer is connected to. Note that pos is not passed as a parameter.
# 
# Return true if there is a cycle in the linked list. Otherwise, return false.
#  
# Example 1:
# 
# Input: head = [3,2,0,-4], pos = 1
# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
# 
# Example 2:
# 
# Input: head = [1,2], pos = 0
# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.
# 
# Example 3:
# 
# Input: head = [1], pos = -1
# Output: false
# Explanation: There is no cycle in the linked list.
# 
#  
# Constraints:
# 
# 	The number of the nodes in the list is in the range [0, 10^4].
# 	-10^5 <= Node.val <= 10^5
# 	pos is -1 or a valid index in the linked-list.
# 
#  
# Follow up: Can you solve it using O(1) (i.e. constant) memory?

import sys
import os

# Add the parent directory to sys.path to import miscelaneus tools
current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)

from linked import ListNode

# Solution: https://youtu.be/gBTe7lFR3vc
# Credit: Navdeep Singh founder of NeetCode
def has_cycle(head: ListNode) -> bool:
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    slow, fast = head, head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

# Same Solution: https://youtu.be/y-ckZ2hpC8Y
# Credit: Greg Hogg


def example_1():
    a = ListNode(3)
    b = ListNode(2)
    c = ListNode(0)
    d = ListNode(4)
    
    a.next = b
    b.next = c
    c.next = d
    d.next = b
    return a

def example_2():
    a = ListNode(1)
    b = ListNode(2)
    
    a.next = b
    b.next = a
    return a

def main():
    head = example_1()
    result = has_cycle(head)
    print(result) # True

    head = example_2()
    result = has_cycle(head)
    print(result) # True

    head = ListNode(1)
    result = has_cycle(head)
    print(result) # False

if __name__ == "__main__":
    main()
