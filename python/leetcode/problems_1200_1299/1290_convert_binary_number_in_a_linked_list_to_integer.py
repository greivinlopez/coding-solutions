# -------------------------------------------------------
# 1290. Convert Binary Number in a Linked List to Integer
# -------------------------------------------------------

# Problem: https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer
#
# Given head which is a reference node to a singly-linked list. The value of each
# node in the linked list is either 0 or 1. The linked list holds the binary
# representation of a number.
# 
# Return the decimal value of the number in the linked list.
# 
# The most significant bit is at the head of the linked list.
# 
# Example 1:
# 
# https://assets.leetcode.com/uploads/2019/12/05/graph-1.png
# 
# Input: head = [1,0,1]
# Output: 5
# 
# Explanation: (101) in base 2 = (5) in base 10
# 
# Example 2:
# 
# Input: head = [0]
# Output: 0
# 
# 
# Constraints:
#         The Linked List is not empty.
#         Number of nodes will not exceed 30.
#         Each node's value is either 0 or 1.

import sys
import os

# Add the parent directory to sys.path to import miscelaneus tools
current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)

from linked import from_list

# Solution: https://algo.monster/liteproblems/1290
# Credit: AlgoMonster
def get_decimal_value(head):
    # Initialize the result to store the decimal value
    decimal_value = 0
    
    # Traverse through the linked list
    while head:
        # Left shift the current value by 1 bit (multiply by 2)
        # and add the current node's value (0 or 1)
        # This is equivalent to: decimal_value = decimal_value * 2 + head.val
        decimal_value = (decimal_value << 1) | head.val
        
        # Move to the next node
        head = head.next
    
    # Return the final decimal value
    return decimal_value
    # Time: O(n)
    # Space: O(1)


def main():
    result = get_decimal_value(from_list([1,0,1]))
    print(result) # 5

    result = get_decimal_value(from_list([0]))
    print(result) # 0

if __name__ == "__main__":
    main()
