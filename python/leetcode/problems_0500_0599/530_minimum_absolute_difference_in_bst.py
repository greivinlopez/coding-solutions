# ---------------------
# 525. Contiguous Array
# ---------------------

# Problem: https://leetcode.com/problems/contiguous-array/
# 
# Given a binary array nums, return the maximum length of a contiguous subarray 
# with an equal number of 0 and 1.
# 
#  
# Example 1:
# 
# Input: nums = [0,1]
# Output: 2
# Explanation: [0, 1] is the longest contiguous subarray with an equal number 
# of 0 and 1.
# 
# 
# Example 2:
# 
# Input: nums = [0,1,0]
# Output: 2
# Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal 
# number of 0 and 1.
# 
# 
# Example 3:
# 
# Input: nums = [0,1,1,1,1,1,0,0,0]
# Output: 6
# Explanation: [1,1,1,0,0,0] is the longest contiguous subarray with equal number 
# of 0 and 1.
# 
# 
# Constraints:
# 
# 	1 <= nums.length <= 10^5
# 	nums[i] is either 0 or 1.

import sys
import os

# Add the parent directory to sys.path to import miscelaneus tools
current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)

# Import code needed for solutions
from tree import get_tree

# Solution: https://youtu.be/NttA_NC_ZhI
# Credit: Greg Hogg
def get_minimum_difference(root):
    min_distance = [float('inf')]
    prev = [None]

    def dfs(node):
        if node is None:
            return
            
        dfs(node.left)

        if prev[0] is not None:
            min_distance[0] = min(min_distance[0], node.val - prev[0])

        prev[0] = node.val
        dfs(node.right)

    dfs(root)
    return min_distance[0]
    # Time: O(n)
    # Space: O(n)

# Solution: https://youtu.be/IFm_NtpwJD4
# Credit: marutaro -> https://github.com/marutaro
def get_minimum_difference_alt(root):
    def inorder(node):
        nonlocal min_diff, prev_val

        if node.left:
            inorder(node.left)
        
        if prev_val is not None:
            min_diff = min(min_diff, node.val - prev_val)
        prev_val = node.val

        if node.right:
            inorder(node.right)

    min_diff = float("inf")
    prev_val = None
    inorder(root)
    return min_diff


def main():
    root = get_tree("[4,2,6,1,3]")
    result = get_minimum_difference_alt(root)
    print(result) # 1

    root = get_tree("[1,0,48,null,null,12,49]")
    result = get_minimum_difference_alt(root)
    print(result) # 1

if __name__ == "__main__":
    main()
