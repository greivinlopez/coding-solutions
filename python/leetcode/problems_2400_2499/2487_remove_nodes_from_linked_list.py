# -----------------------------------
# 2487. Remove Nodes From Linked List
# -----------------------------------

# Problem: https://leetcode.com/problems/remove-nodes-from-linked-list
#
# You are given the head of a linked list.
# 
# Remove every node which has a node with a greater value anywhere to the right
# side of it.
# 
# Return the head of the modified linked list.
# 
# Example 1:
# 
# https://assets.leetcode.com/uploads/2022/10/02/drawio.png
# 
# Input: head = [5,2,13,3,8]
# Output: [13,8]
# Explanation: The nodes that should be removed are 5, 2 and 3.
# - Node 13 is to the right of node 5.
# - Node 13 is to the right of node 2.
# - Node 8 is to the right of node 3.
# 
# Example 2:
# 
# Input: head = [1,1,1,1]
# Output: [1,1,1,1]
# 
# Explanation: Every node has value 1, so no nodes are removed.
# 
# 
# Constraints:
#         The number of the nodes in the given list is in the range [1, 10⁵].
#         1 <= Node.val <= 10⁵

import sys
import os

# Add the parent directory to sys.path to import miscelaneus tools
current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)

from linked import from_list, ListNode

# Solution: https://youtu.be/y783sRTezDg
# Credit: Navdeep Singh founder of NeetCode
def remove_nodes(head):
    stack = []
    cur = head
    while cur:
        while stack and cur.val > stack[-1]:
            stack.pop()
        stack.append(cur.val)
        cur = cur.next
    
    dummy = ListNode()
    cur = dummy
    for n in stack:
        cur.next = ListNode(n)
        cur = cur.next
    return dummy.next
    # Time: O(n) 
    # Space: O(n)

def remove_nodes_alt(head):
    # Space optimized solution
    def reverse(head):
        prev, cur = None, head
        while cur:
            tmp = cur.next
            cur.next = prev
            prev, cur = cur, tmp
        return prev
    
    head = reverse(head)
    cur = head
    cur_max = cur.val
    while cur.next:
        if cur.next.val < cur_max:
            cur.next = cur.next.next
        else:
            cur_max = cur.next.val
            cur = cur.next
    return reverse(head)
    # Time: O(n) 
    # Space: O(1)

def main():
    result = remove_nodes(from_list([5,2,13,3,8]))
    print(result) # [13, 8]

    result = remove_nodes(from_list([1,1,1,1]))
    print(result) # [1, 1, 1, 1]

if __name__ == "__main__":
    main()
