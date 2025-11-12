# -------------------
# 2. Add Two Numbers
# -------------------

# Problem: https://leetcode.com/problems/add-two-numbers
#
# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order, and each of their nodes contains a
# single digit. Add the two numbers and return the sum as a linked list.
# 
# You may assume the two numbers do not contain any leading zero, except the
# number 0 itself.
# 
# Example 1:
# 
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# 
# Explanation: 342 + 465 = 807.
# 
# Example 2:
# 
# Input: l1 = [0], l2 = [0]
# Output: [0]
# 
# Example 3:
# 
# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]
# 
# 
# Constraints:
#         The number of nodes in each linked list is in the range [1, 100].
#         0 <= Node.val <= 9
#         It is guaranteed that the list represents a number that does not have
# leading zeros.

import sys
import os

# Add the parent directory to sys.path to import miscelaneus tools
current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)

from linked import ListNode, from_list

# Solution: https://youtu.be/wgFPrzTjm7s
# Credit: Navdeep Singh founder of NeetCode 
def add_two_numbers_alt(l1, l2):
    dummy = ListNode()
    cur = dummy

    carry = 0
    while l1 or l2 or carry:
        v1 = l1.val if l1 else 0
        v2 = l2.val if l2 else 0

        # new digit
        val = v1 + v2 + carry
        carry = val // 10
        val = val % 10
        cur.next = ListNode(val)

        # update ptrs
        cur = cur.next
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None

    return dummy.next
    # Time: O(max(n, m))
    # Space: O(max(n, m))


# Credit: Jeel Gajera -> https://github.com/JeelGajera
def add_two_numbers(l1, l2):
    num1 = ""
    num2 = ""
    i = l1
    while i:
        num1 += str(i.val)
        i = i.next
    num1 = num1[::-1]

    j = l2
    while j:
        num2 += str(j.val)
        j = j.next
    num2 = num2[::-1]

    res = str(int(num1) + int(num2))
    res = res[::-1]
    l_sum = ListNode(0,None)
    current = l_sum
    for char in res:
        val = int(char)
        node = ListNode(val, None)
        current.next = node
        current = current.next
    l_sum = l_sum.next
    return l_sum
    # Time: O(n + m)
    # Space: O(n + m)


def main():
    l1 = from_list([2,4,3])
    l2 = from_list([5,6,4])
    result = add_two_numbers(l1,l2) 
    print(result) # [7,0,8]

    l1 = from_list([0])
    l2 = from_list([0])
    result = add_two_numbers(l1,l2) 
    print(result) # [0]

    l1 = from_list([9,9,9,9,9,9,9])
    l2 = from_list([9,9,9,9])
    result = add_two_numbers(l1,l2) 
    print(result) # [8,9,9,9,0,0,0,1]

if __name__ == "__main__":
    main()