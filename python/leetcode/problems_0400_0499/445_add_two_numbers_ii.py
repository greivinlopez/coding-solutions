# -----------------------
# 445. Add Two Numbers II
# -----------------------

# Problem: https://leetcode.com/problems/add-two-numbers-ii
#
# You are given two non-empty linked lists representing two non-negative integers.
# The most significant digit comes first and each of their nodes contains a single
# digit. Add the two numbers and return the sum as a linked list.
# 
# You may assume the two numbers do not contain any leading zero, except the
# number 0 itself.
# 
# Example 1:
# 
# https://assets.leetcode.com/uploads/2021/04/09/sumii-linked-list.jpg
# 
# Input: l1 = [7,2,4,3], l2 = [5,6,4]
# Output: [7,8,0,7]
# 
# Example 2:
# 
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [8,0,7]
# 
# Example 3:
# 
# Input: l1 = [0], l2 = [0]
# Output: [0]
# 
# 
# Constraints:
#       The number of nodes in each linked list is in the range [1, 100].
#       0 <= Node.val <= 9
#       It is guaranteed that the list represents a number that does not have
#       leading zeros.
# 
# 
# Follow up: Could you solve it without reversing the input lists?

import sys
import os

# Add the parent directory to sys.path to import miscelaneus tools
current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)

from linked import from_list, ListNode

# Solution: https://algo.monster/liteproblems/445
# Credit: AlgoMonster
def add_two_numbers(l1, l2):
    # Use stacks to store digits from both linked lists
    stack1, stack2 = [], []
    
    # Traverse first linked list and push all digits to stack1
    while l1:
        stack1.append(l1.val)
        l1 = l1.next
    
    # Traverse second linked list and push all digits to stack2
    while l2:
        stack2.append(l2.val)
        l2 = l2.next
    
    # Create dummy head for result linked list
    dummy_head = ListNode()
    carry = 0
    
    # Process digits from least significant to most significant (pop from stacks)
    while stack1 or stack2 or carry:
        # Get digits from stacks, use 0 if stack is empty
        digit1 = stack1.pop() if stack1 else 0
        digit2 = stack2.pop() if stack2 else 0
        
        # Calculate sum of current digits plus carry
        current_sum = digit1 + digit2 + carry
        
        # Calculate new carry and current digit value
        carry, digit_value = divmod(current_sum, 10)
        
        # Insert new node at the beginning of result list (after dummy)
        # This builds the result from least significant to most significant digit
        dummy_head.next = ListNode(digit_value, dummy_head.next)
    
    # Return the actual result list (skip dummy head)
    return dummy_head.next


def main():
    result = add_two_numbers(l1 = from_list([7,2,4,3]), l2 = from_list([5,6,4]))
    print(result) # [7, 8, 0, 7]

    result = add_two_numbers(l1 = from_list([2,4,3]), l2 = from_list([5,6,4]))
    print(result) # [8, 0, 7]

    result = add_two_numbers(l1 = from_list([0]), l2 = from_list([0]))
    print(result) # [0]

if __name__ == "__main__":
    main()
