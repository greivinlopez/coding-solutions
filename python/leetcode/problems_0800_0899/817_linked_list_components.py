# ---------------------------
# 817. Linked List Components
# ---------------------------

# Problem: https://leetcode.com/problems/linked-list-components
#
# You are given the head of a linked list containing unique integer values and an
# integer array nums that is a subset of the linked list values.
# 
# Return the number of connected components in nums where two values are connected
# if they appear consecutively in the linked list.
# 
# Example 1:
# 
# https://assets.leetcode.com/uploads/2021/07/22/lc-linkedlistcom1.jpg
# 
# Input: head = [0,1,2,3], nums = [0,1,3]
# Output: 2
# 
# Explanation: 0 and 1 are connected, so [0, 1] and [3] are the two connected
# components.
# 
# Example 2:
# 
# https://assets.leetcode.com/uploads/2021/07/22/lc-linkedlistcom2.jpg
# 
# Input: head = [0,1,2,3,4], nums = [0,3,1,4]
# Output: 2
# 
# Explanation: 0 and 1 are connected, 3 and 4 are connected, so [0, 1] and [3, 4]
# are the two connected components.
# 
# 
# Constraints:
#         The number of nodes in the linked list is n.
#         1 <= n <= 10⁴
#         0 <= Node.val < n
#         All the values Node.val are unique.
#         1 <= nums.length <= n
#         0 <= nums[i] < n
#         All the values of nums are unique.

import sys
import os

# Add the parent directory to sys.path to import miscelaneus tools
current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)

from linked import from_list

# Solution: https://algo.monster/liteproblems/817
# Credit: AlgoMonster
def num_components(head, nums):
    component_count = 0
    # Convert nums to set for O(1) lookup
    nums_set = set(nums)
    
    current = head
    
    while current:
        # Skip nodes that are not part of any component
        while current and current.val not in nums_set:
            current = current.next
        
        # If we found a node in nums_set, we've found a new component
        if current is not None:
            component_count += 1
        
        # Traverse through all consecutive nodes in the current component
        while current and current.val in nums_set:
            current = current.next
    
    return component_count
    # Time: O(n)
    # Space: O(m)
    # n = the number of nodes in the linked list
    # m = the length of the nums array.


def main():
    result = num_components(from_list([0,1,2,3]), [0,1,3])
    print(result) # 2

    result = num_components(from_list([0,1,2,3,4]), [0,3,1,4])
    print(result) # 2

if __name__ == "__main__":
    main()
