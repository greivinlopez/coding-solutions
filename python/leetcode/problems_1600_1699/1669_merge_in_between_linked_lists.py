# ----------------------------------
# 1669. Merge In Between Linked Lists
# ----------------------------------

# Problem: https://leetcode.com/problems/merge-in-between-linked-lists
#
# You are given two linked lists: list1 and list2 of sizes n and m respectively.
# 
# Remove list1's nodes from the ath node to the bth node, and put list2 in their
# place.
# 
# The blue edges and nodes in the following figure indicate the result:
# Build the result list and return its head.
# 
# Example 1:
# 
# Input: list1 = [10,1,13,6,9,5], a = 3, b = 4, list2 = [1000000,1000001,1000002]
# Output: [10,1,13,1000000,1000001,1000002,5]
# Explanation: We remove the nodes 3 and 4 and put the entire list2 in their
# place. The blue edges and nodes in the above figure indicate the result.
# 
# Example 2:
# 
# Input: list1 = [0,1,2,3,4,5,6], a = 2, b = 5, list2 =
# [1000000,1000001,1000002,1000003,1000004]
# Output: [0,1,1000000,1000001,1000002,1000003,1000004,6]
# Explanation: The blue edges and nodes in the above figure indicate the result.
# 
# 
# Constraints:
#         3 <= list1.length <= 10^4
#         1 <= a <= b < list1.length - 1
#         1 <= list2.length <= 10^4

import sys
import os

# Add the parent directory to sys.path to import miscelaneus tools
current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)

from linked import from_list

# Solution: https://youtu.be/pI775VutBxg
# Credit: Navdeep Singh founder of NeetCode
def merge_in_between(list1, a, b, list2):
    curr = list1
    i = 0
    while i < a - 1:
        curr = curr.next
        i += 1

    head = curr
    while i <= b:
        curr = curr.next
        i += 1
    head.next = list2

    while list2.next:
        list2 = list2.next
    list2.next = curr
    return list1


def main():
    list1 = from_list([10,1,13,6,9,5])
    list2 = from_list([1000000,1000001,1000002])
    result = merge_in_between(list1, 3, 4, list2)
    print(result) # [10,1,13,1000000,1000001,1000002,5]

    list1 = from_list([0,1,2,3,4,5,6])
    list2 = from_list([1000000,1000001,1000002,1000003,1000004])
    result = merge_in_between(list1, 2, 5, list2)
    print(result) # [0,1,1000000,1000001,1000002,1000003,1000004,6]

if __name__ == "__main__":
    main()
