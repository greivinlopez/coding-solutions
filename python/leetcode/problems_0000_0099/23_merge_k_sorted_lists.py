# ------------------------
# 23. Merge k Sorted Lists
# ------------------------

# Problem: https://leetcode.com/problems/merge-k-sorted-lists/
# 
# You are given an array of k linked-lists lists, each linked-list is sorted 
# in ascending order.
# 
# Merge all the linked-lists into one sorted linked-list and return it.
# 
# Example 1:
# 
# Input: lists = [[1,4,5],[1,3,4],[2,6]]
# Output: [1,1,2,3,4,4,5,6]
# Explanation: The linked-lists are:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# merging them into one sorted linked list:
# 1->1->2->3->4->4->5->6
# 
# 
# Example 2:
# 
# Input: lists = []
# Output: []
# 
# 
# Example 3:
# 
# Input: lists = [[]]
# Output: []
# 
# 
# Constraints:
# 
# 	k == lists.length
# 	0 <= k <= 10⁴
# 	0 <= lists[i].length <= 500
# 	-10⁴ <= lists[i][j] <= 10⁴
# 	lists[i] is sorted in ascending order.
# 	The sum of lists[i].length will not exceed 10⁴.

import sys
import os

# Add the parent directory to sys.path to import miscelaneus tools
current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)

from linked import ListNode, from_list


# Solution: https://youtu.be/q5a5OiGbT6Q
# Credit: Navdeep Singh founder of NeetCode 
def merge_k_lists(lists):
    if not lists or len(lists) == 0:
        return None

    while len(lists) > 1:
        mergedLists = []
        for i in range(0, len(lists), 2):
            l1 = lists[i]
            l2 = lists[i + 1] if (i + 1) < len(lists) else None
            mergedLists.append(merge_list(l1, l2))
        lists = mergedLists
    return lists[0]
    # Time: O(n log k)
    # Space: O(k)

def merge_list(l1, l2):
    dummy = ListNode()
    tail = dummy

    while l1 and l2:
        if l1.val < l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next
    if l1:
        tail.next = l1
    if l2:
        tail.next = l2
    return dummy.next
    # Time: O(n + m)
    # Space: O(1)

# Solution: https://youtu.be/RyrVWP76lVo
# Credit: Greg Hogg
import heapq
def merge_k_lists_alt(lists):
    heap = []
    for i, node in enumerate(lists):
        if node:
            heapq.heappush(heap, (node.val, i, node))
    
    D = ListNode()
    cur = D
    
    # n log k
    while heap:
        val, i, node = heapq.heappop(heap)
        cur.next = node
        cur = node
        node = node.next
        if node:
            heapq.heappush(heap, (node.val, i, node))
    
    return D.next
    # Time: O(n log k)
    # Space: O(k)


def main():
    l1 = from_list([1,4,5])
    l2 = from_list([1,3,4])
    l3 = from_list([2,6])
    result = merge_k_lists([l1,l2,l3]) 
    print(result) # [1,1,2,3,4,4,5,6]

if __name__ == "__main__":
    main()