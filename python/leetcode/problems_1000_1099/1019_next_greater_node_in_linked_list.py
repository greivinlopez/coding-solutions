# --------------------------------------
# 1019. Next Greater Node In Linked List
# --------------------------------------

# Problem: https://leetcode.com/problems/next-greater-node-in-linked-list
#
# You are given the head of a linked list with n nodes.
# 
# For each node in the list, find the value of the next greater node. That is, for
# each node, find the value of the first node that is next to it and has a
# strictly larger value than it.
# 
# Return an integer array answer where answer[i] is the value of the next greater
# node of the ith node (1-indexed). If the ith node does not have a next greater
# node, set answer[i] = 0.
# 
# Example 1:
# 
# Input: head = [2,1,5]
# Output: [5,5,0]
# 
# Example 2:
# 
# Input: head = [2,7,4,3,5]
# Output: [7,0,5,5,0]
# 
# 
# Constraints:
#         The number of nodes in the list is n.
#         1 <= n <= 10⁴
#         1 <= Node.val <= 10⁹

import sys
import os

# Add the parent directory to sys.path to import miscelaneus tools
current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)

from linked import from_list

# Solution: https://algo.monster/liteproblems/1019
# Credit: AlgoMonster
def next_larger_nodes(head):
    # Convert linked list to array for easier processing
    values = []
    current = head
    while current:
        values.append(current.val)
        current = current.next
    
    # Initialize monotonic stack and result array
    stack = []  # Monotonic decreasing stack to track potential next larger elements
    n = len(values)
    result = [0] * n  # Initialize result array with zeros (default when no larger element exists)
    
    # Traverse the array from right to left
    for i in range(n - 1, -1, -1):
        # Pop elements from stack that are smaller or equal to current element
        # They cannot be the next larger element for any future elements
        while stack and stack[-1] <= values[i]:
            stack.pop()
        
        # If stack is not empty, top element is the next larger element
        if stack:
            result[i] = stack[-1]
        
        # Add current element to stack for future comparisons
        stack.append(values[i])
    
    return result
    # Time: O(n)
    # Space: O(n)


def main():
    result = next_larger_nodes(from_list([2,1,5]))
    print(result) # [5,5,0]

    result = next_larger_nodes(from_list([2,7,4,3,5]))
    print(result) # [7,0,5,5,0]

if __name__ == "__main__":
    main()
