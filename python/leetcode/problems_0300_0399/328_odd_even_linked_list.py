# -------------------------
# 328. Odd Even Linked List
# -------------------------

# Problem: https://leetcode.com/problems/odd-even-linked-list
#
# Given the head of a singly linked list, group all the nodes with odd indices
# together followed by the nodes with even indices, and return the reordered list.
# 
# The first node is considered odd, and the second node is even, and so on.
# 
# Note that the relative order inside both the even and odd groups should remain
# as it was in the input.
# 
# You must solve the problem in O(1) extra space complexity and O(n) time
# complexity.
# 
# Example 1:
# 
# Input: head = [1,2,3,4,5]
# Output: [1,3,5,2,4]
# 
# Example 2:
# 
# Input: head = [2,1,3,5,6,4,7]
# Output: [2,3,6,7,1,5,4]
# 
# 
# Constraints:
#         The number of nodes in the linked list is in the range [0, 10⁴].
#         -10⁶ <= Node.val <= 10⁶

import sys
import os

# Add the parent directory to sys.path to import miscelaneus tools
current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)

from linked import from_list

# Solution: https://leetcode.com/problems/odd-even-linked-list/solutions/4761304/simple-beginner-friendly-dry-run-two-approach-full-explanation-time-o-n-space-o-1-gits
# Credit: Gitesh Suresh Ratnaparkhi -> https://leetcode.com/u/GiteshSK_12/
def odd_even_list(head):
    if head == None or head.next == None: 
        return head
    odd = head
    even = head.next
    ehead = even

    while even != None and even.next != None:
        odd.next = odd.next.next
        even.next = even.next.next
        odd=odd.next
        even= even.next
    odd.next = ehead

    return head
    # Time: O(n)
    # Space: O(1)


def main():
    result = odd_even_list(from_list([1,2,3,4,5]))
    print(result) # [1, 3, 5, 2, 4]

    result = odd_even_list(from_list([2,1,3,5,6,4,7]))
    print(result) # [2, 3, 6, 7, 1, 5, 4]

if __name__ == "__main__":
    main()
