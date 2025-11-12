# --------------------------------------------------
# 2816. Double a Number Represented as a Linked List
# --------------------------------------------------

# Problem: https://leetcode.com/problems/double-a-number-represented-as-a-linked-list
#
# You are given the head of a non-empty linked list representing a non-negative
# integer without leading zeroes.
# 
# Return the head of the linked list after doubling it.
# 
# Example 1:
# 
# https://assets.leetcode.com/uploads/2023/05/28/example.png
# 
# Input: head = [1,8,9]
# Output: [3,7,8]
# 
# Explanation: The figure above corresponds to the given linked list which
# represents the number 189. Hence, the returned linked list represents the number
# 189 * 2 = 378.
# 
# Example 2:
# 
# https://assets.leetcode.com/uploads/2023/05/28/example2.png
# 
# Input: head = [9,9,9]
# Output: [1,9,9,8]
# 
# Explanation: The figure above corresponds to the given linked list which
# represents the number 999. Hence, the returned linked list reprersents the
# number 999 * 2 = 1998.
# 
# 
# Constraints:
#         The number of nodes in the list is in the range [1, 10⁴]
#         0 <= Node.val <= 9
#         The input is generated such that the list represents a number that does
# not have leading zeros, except the number 0 itself.

import sys
import os

# Add the parent directory to sys.path to import miscelaneus tools
current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)

from linked import ListNode, from_list


# Credit: Jaweria Batool -> https://github.com/Jaweria-B
def double_it(head):
    # Reverse the linked list
    reversed_list = reverse_list(head)
    # Initialize variables to track carry and previous node
    carry = 0
    current, previous = reversed_list, None

    # Traverse the reversed linked list
    while current:
        # Calculate the new value for the current node
        new_value = current.val * 2 + carry
        # Update the current node's value
        current.val = new_value % 10
        # Update carry for the next iteration
        carry = 1 if new_value > 9 else 0
        # Move to the next node
        previous, current = current, current.next

    # If there's a carry after the loop, add an extra node
    if carry:
        previous.next = ListNode(carry)

    # Reverse the list again to get the original order
    result = reverse_list(reversed_list)

    return result
    # Time: O(n)
    # Space: O(1)

# Method to reverse the linked list
def reverse_list(node):
    previous, current = None, node

    # Traverse the original linked list
    while current:
        # Store the next node
        next_node = current.next
        # Reverse the link
        current.next = previous
        # Move to the next nodes
        previous, current = current, next_node

    # Previous becomes the new head of the reversed list
    return previous

def main():
    result = double_it(head = from_list([1,8,9]))
    print(result) # [3,7,8]

    result = double_it(head = from_list([9,9,9]))
    print(result) # [1,9,9,8]

if __name__ == "__main__":
    main()
