# -------------------------------
# 725. Split Linked List in Parts
# -------------------------------

# Problem: https://leetcode.com/problems/split-linked-list-in-parts
#
# Given the head of a singly linked list and an integer k, split the linked list
# into k consecutive linked list parts.
# 
# The length of each part should be as equal as possible: no two parts should have
# a size differing by more than one. This may lead to some parts being null.
# 
# The parts should be in the order of occurrence in the input list, and parts
# occurring earlier should always have a size greater than or equal to parts
# occurring later.
# 
# Return an array of the k parts.
# 
# Example 1:
# 
# https://assets.leetcode.com/uploads/2021/06/13/split1-lc.jpg
# 
# Input: head = [1,2,3], k = 5
# Output: [[1],[2],[3],[],[]]
# 
# Explanation:
# The first element output[0] has output[0].val = 1, output[0].next = null.
# The last element output[4] is null, but its string representation as a ListNode
# is [].
# 
# Example 2:
# 
# https://assets.leetcode.com/uploads/2021/06/13/split2-lc.jpg
# 
# Input: head = [1,2,3,4,5,6,7,8,9,10], k = 3
# Output: [[1,2,3,4],[5,6,7],[8,9,10]]
# 
# Explanation:
# The input has been split into consecutive parts with size difference at most 1,
# and earlier parts are a larger size than the later parts.
# 
# 
# Constraints:
#         The number of nodes in the list is in the range [0, 1000].
#         0 <= Node.val <= 1000
#         1 <= k <= 50

import sys
import os

# Add the parent directory to sys.path to import miscelaneus tools
current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)

from linked import from_list 

# Solution: https://youtu.be/-OTlqdrxrVI
# Credit: Navdeep Singh founder of NeetCode
def split_list_to_parts(head, k):
    length, curr = 0, head
    while curr:
        curr = curr.next
        length += 1
    base_len, remainder = length // k, length % k
    curr = head
    res = []
    for i in range(k):
        res.append(curr)
        for j in range(base_len - 1 + (1 if remainder else 0)):
            if not curr:
                break
            curr = curr.next
        remainder -= (1 if remainder else 0)
        if curr:
            curr.next, curr = None, curr.next
    return res
    # Time: O(n)
    # Space: O(k)


def main():
    result = split_list_to_parts(head = from_list([1,2,3]), k = 5)
    for l in result:
        print(l)

    result = split_list_to_parts(head = from_list([1,2,3,4,5,6,7,8,9,10]), k = 3)
    for l in result:
        print(l)

if __name__ == "__main__":
    main()
