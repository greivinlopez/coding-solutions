# ------------------------------
# 876. Middle Of The Linked List
# ------------------------------

# Problem: https://leetcode.com/problems/middle-of-the-linked-list/
# 
# Given the head of a singly linked list, return the middle node of the linked 
# list.
# 
# If there are two middle nodes, return the second middle node.
# 
#  
# Example 1:
# 
# Input: head = [1,2,3,4,5]
# Output: [3,4,5]
# Explanation: The middle node of the list is node 3.
# 
# Example 2:
# 
# Input: head = [1,2,3,4,5,6]
# Output: [4,5,6]
# Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.
#  
# 
# Constraints:
# 
#   The number of nodes in the list is in the range [1, 100].
#   1 <= Node.val <= 100

import sys
import os

# Add the parent directory to sys.path to import miscelaneus tools
current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)

from linked import from_list

# Solution: https://youtu.be/A2_ldqM4QcY
# Credit: Navdeep Singh founder of NeetCode
def middle_node(head):
    if not head or not head.next:
        return head

    slow = fast = head
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next

    return slow

# Solution: https://youtu.be/OKq-WEwHDPQ
# Credit: Greg Hogg
# Pretty Same Solution
def middle_node_alt(head):
    slow = head
    fast = head

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

    return slow
    # Time: O(n)
    # Space: O(1)

def main():
    l = from_list([1,2,3,4,5])
    result = middle_node(l)
    print(result) # [3,4,5]

    l2 = from_list([1,2,3,4,5,6])
    result = middle_node(l2)
    print(result) # [4,5,6]

if __name__ == "__main__":
    main()
