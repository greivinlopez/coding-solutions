# ----------------------------------------------------
# 3217. Delete Nodes From Linked List Present in Array
# ----------------------------------------------------

# Problem: https://leetcode.com/problems/delete-nodes-from-linked-list-present-in-array
#
# You are given an array of integers nums and the head of a linked list. Return
# the head of the modified linked list after removing all nodes from the linked
# list that have a value that exists in nums.
# 
# Example 1:
# 
# Input: nums = [1,2,3], head = [1,2,3,4,5]
# Output: [4,5]
# 
# Explanation:
# https://assets.leetcode.com/uploads/2024/06/11/linkedlistexample0.png
# 
# Remove the nodes with values 1, 2, and 3.
# 
# Example 2:
# 
# Input: nums = [1], head = [1,2,1,2,1,2]
# Output: [2,2,2]
# 
# Explanation:
# https://assets.leetcode.com/uploads/2024/06/11/linkedlistexample1.png
# 
# Remove the nodes with value 1.
# 
# Example 3:
# 
# Input: nums = [5], head = [1,2,3,4]
# Output: [1,2,3,4]
# 
# Explanation:
# https://assets.leetcode.com/uploads/2024/06/11/linkedlistexample2.png
# 
# No node has value 5.
# 
# 
# Constraints:
#         1 <= nums.length <= 10⁵
#         1 <= nums[i] <= 10⁵
#         All elements in nums are unique.
#         The number of nodes in the given list is in the range [1, 10⁵].
#         1 <= Node.val <= 10⁵
#         The input is generated such that there is at least one node in the
# linked list that has a value not present in nums.

import sys
import os

# Add the parent directory to sys.path to import miscelaneus tools
current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)

from linked import ListNode, from_list

# Solution: https://youtu.be/3xZuqYD3EYA
# Credit: Navdeep Singh founder of NeetCode
def modified_list(nums, head):
    nums = set(nums)
    dummy = ListNode(0, head)
    
    prev = dummy
    while prev.next:
        if prev.next.val in nums:
            prev.next = prev.next.next
        else:
            prev = prev.next
    
    return dummy.next
    # Time: O(n + m)
    # Space: O(n)
    # n = number of elements in num
    # m = number of nodes in the linked list


def main():
    result = modified_list([1,2,3], from_list([1,2,3,4,5]))
    print(result) # [4,5]

    result = modified_list([1], from_list([1,2,1,2,1,2]))
    print(result) # [2,2,2]

    result = modified_list([5], from_list([1,2,3,4]))
    print(result) # [1,2,3,4]

if __name__ == "__main__":
    main()
