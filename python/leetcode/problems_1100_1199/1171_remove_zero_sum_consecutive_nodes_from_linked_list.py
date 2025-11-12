# --------------------------------------------------------
# 1171. Remove Zero Sum Consecutive Nodes from Linked List
# --------------------------------------------------------

# Problem: https://leetcode.com/problems/remove-zero-sum-consecutive-nodes-from-linked-list
#
# Given the head of a linked list, we repeatedly delete consecutive sequences of
# nodes that sum to 0 until there are no such sequences.
# 
# After doing so, return the head of the final linked list.  You may return any
# such answer.
# 
# (Note that in the examples below, all sequences are serializations of ListNode
# objects.)
# 
# Example 1:
# 
# Input: head = [1,2,-3,3,1]
# Output: [3,1]
# 
# Note: The answer [1,2,1] would also be accepted.
# 
# Example 2:
# 
# Input: head = [1,2,3,-3,4]
# Output: [1,2,4]
# 
# Example 3:
# 
# Input: head = [1,2,3,-3,-2]
# Output: [1]
# 
# 
# Constraints:
#         The given linked list will contain between 1 and 1000 nodes.
#         Each node in the linked list has -1000 <= node.val <= 1000.

import sys
import os

# Add the parent directory to sys.path to import miscelaneus tools
current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)

from linked import ListNode, from_list

# Credit: Jaweria Batool -> https://github.com/Jaweria-B
def remove_zero_sum_sublists(head):
    front = ListNode(0, head)
    start = front
    
    while start is not None:
        prefix_sum = 0
        end = start.next
        
        while end is not None:
            prefix_sum += end.val
            
            if prefix_sum == 0:
                start.next = end.next
            
            end = end.next
        
        start = start.next
    
    return front.next
    # Time: O(n²)
    # Space: O(1)


def main():
    result = remove_zero_sum_sublists(head = from_list([1,2,-3,3,1]))
    print(result) # [3,1]

    result = remove_zero_sum_sublists(head = from_list([1,2,3,-3,4]))
    print(result) # [1,2,4]

    result = remove_zero_sum_sublists(head = from_list([1,2,3,-3,-2]))
    print(result) # [1]

if __name__ == "__main__":
    main()
