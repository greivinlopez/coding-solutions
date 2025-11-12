# ---------------------------
# 654. Maximum Binary Tree 🌲
# ---------------------------

# Problem: https://leetcode.com/problems/maximum-binary-tree
#
# You are given an integer array nums with no duplicates. A maximum binary tree
# can be built recursively from nums using the following algorithm:
#         
#   * Create a root node whose value is the maximum value in nums.
#   * Recursively build the left subtree on the subarray prefix to the left of
#     the maximum value.
#   * Recursively build the right subtree on the subarray suffix to the right
#     of the maximum value.
# 
# Return the maximum binary tree built from nums.
# 
# Example 1:
# 
# Input: nums = [3,2,1,6,0,5]
# Output: [6,3,5,null,2,0,null,null,1]
# 
# Explanation: The recursive calls are as follow:
# - The largest value in [3,2,1,6,0,5] is 6. Left prefix is [3,2,1] and right
# suffix is [0,5].
#     - The largest value in [3,2,1] is 3. Left prefix is [] and right suffix is
# [2,1].
#         - Empty array, so no child.
#         - The largest value in [2,1] is 2. Left prefix is [] and right suffix is
# [1].
#             - Empty array, so no child.
#             - Only one element, so child is a node with value 1.
#     - The largest value in [0,5] is 5. Left prefix is [0] and right suffix is
# [].
#         - Only one element, so child is a node with value 0.
#         - Empty array, so no child.
# 
# Example 2:
# 
# Input: nums = [3,2,1]
# Output: [3,null,2,null,1]
# 
# Constraints:
#         1 <= nums.length <= 1000
#         0 <= nums[i] <= 1000
#         All integers in nums are unique.

import sys
import os

# Add the parent directory to sys.path to import miscelaneus tools
current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)

from tree import TreeNode

# Solution: 
# Credit: Navdeep Singh founder of NeetCode
def construct_maximum_binary_tree(nums):
    def build_tree(arr):
        # Base case: empty array returns None
        if not arr:
            return None
        
        # Find the maximum value and its index
        max_value = max(arr)
        max_index = arr.index(max_value)
        
        # Create root node with maximum value
        root = TreeNode(max_value)
        
        # Recursively build left subtree from elements before max
        root.left = build_tree(arr[:max_index])
        
        # Recursively build right subtree from elements after max
        root.right = build_tree(arr[max_index + 1:])
        
        return root
    
    # Start the recursive construction
    return build_tree(nums)
    # Time: O(n²) in the worst case, O(n log n) in the average case
    # Space: O(n²) in the worst case, O(n log n) in the average case


def main():
    result = construct_maximum_binary_tree([3,2,1,6,0,5])
    print(result) # [6, 3, 5, None, 2, 0, None, None, 1]

    result = construct_maximum_binary_tree([3,2,1])
    print(result) # [3, None, 2, None, 1]

if __name__ == "__main__":
    main()
