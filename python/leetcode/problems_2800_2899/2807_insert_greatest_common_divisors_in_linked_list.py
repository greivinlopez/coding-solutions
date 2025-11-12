# ----------------------------------------------------
# 2807. Insert Greatest Common Divisors in Linked List
# ----------------------------------------------------


# Problem: https://leetcode.com/problems/insert-greatest-common-divisors-in-linked-list
#
# Given the head of a linked list head, in which each node contains an integer 
# value.
# 
# Between every pair of adjacent nodes, insert a new node with a value equal to 
# the greatest common divisor of them.
# 
# Return the linked list after insertion.
# 
# The greatest common divisor of two numbers is the largest positive integer that 
# evenly divides both numbers.
# 
#  
# Example 1:
# 
# Input: head = [18,6,10,3]
# Output: [18,6,6,2,10,1,3]
# Explanation: The 1st diagram denotes the initial linked list and the 2nd diagram denotes the linked list after inserting the new nodes (nodes in blue are the inserted nodes).
# - We insert the greatest common divisor of 18 and 6 = 6 between the 1st and the 2nd nodes.
# - We insert the greatest common divisor of 6 and 10 = 2 between the 2nd and the 3rd nodes.
# - We insert the greatest common divisor of 10 and 3 = 1 between the 3rd and the 4th nodes.
# There are no more adjacent nodes, so we return the linked list.
# 
# Example 2:
# 
# Input: head = [7]
# Output: [7]
# Explanation: The 1st diagram denotes the initial linked list and the 2nd diagram denotes the linked list after inserting the new nodes.
# There are no pairs of adjacent nodes, so we return the initial linked list.
#  
# 
# Constraints:
# 
#   The number of nodes in the list is in the range [1, 5000].
#   1 <= Node.val <= 1000

import sys
import os

# Add the parent directory to sys.path to import miscelaneus tools
current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)

from linked import from_list, ListNode
import math

# Solution: https://youtu.be/SS_IlBrocYQ
# Credit: Navdeep Singh founder of NeetCode
def insert_greatest_common_divisors(head):
    def gcd(a, b):
        while b > 0:
            a, b = b, a % b
        return a
    
    cur = head
    while cur.next:
        n1, n2 = cur.val, cur.next.val
        cur.next = ListNode(gcd(n1, n2), cur.next)
        cur = cur.next.next
    return head

# Solution: https://youtu.be/SVnSiD95r-0
# Credit: Greg Hogg
def insert_greatest_common_divisors_alt(head):
    prev = head
    cur = head.next
    
    while cur:
        gcd = math.gcd(cur.val, prev.val) # A
        g = ListNode(gcd)
        prev.next = g
        g.next = cur
        prev = cur
        cur = cur.next

    return head
    # Time: O(n * A)
    # Space: O(1)

def main():
    result = insert_greatest_common_divisors(from_list([18,6,10,3]))
    print(result) # [18,6,6,2,10,1,3]

    result = insert_greatest_common_divisors(from_list([7]))
    print(result) # [7]

if __name__ == "__main__":
    main()
