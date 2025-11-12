# -----------------------------------------------------------------
# 2471. Minimum Number of Operations to Sort a Binary Tree by Level
# -----------------------------------------------------------------

# Problem: https://leetcode.com/problems/minimum-number-of-operations-to-sort-a-binary-tree-by-level
#
# You are given the root of a binary tree with unique values.
# 
# In one operation, you can choose any two nodes at the same level and swap their values.
# 
# Return the minimum number of operations needed to make the values at each level
# sorted in a strictly increasing order.
# 
# The level of a node is the number of edges along the path between it and the
# root node.
# 
# Example 1:
# 
# Input: root = [1,4,3,7,6,8,5,null,null,null,null,9,null,10]
# Output: 3
# 
# Explanation:
# - Swap 4 and 3. The 2nd level becomes [3,4].
# - Swap 7 and 5. The 3rd level becomes [5,6,8,7].
# - Swap 8 and 7. The 3rd level becomes [5,6,7,8].
# We used 3 operations so return 3.
# It can be proven that 3 is the minimum number of operations needed.
# 
# Example 2:
# 
# Input: root = [1,3,2,7,6,5,4]
# Output: 3
# 
# Explanation:
# - Swap 3 and 2. The 2nd level becomes [2,3].
# - Swap 7 and 4. The 3rd level becomes [4,6,5,7].
# - Swap 6 and 5. The 3rd level becomes [4,5,6,7].
# We used 3 operations so return 3.
# It can be proven that 3 is the minimum number of operations needed.
# 
# Example 3:
# 
# Input: root = [1,2,3,4,5,6]
# Output: 0
# 
# Explanation: Each level is already sorted in increasing order so return 0.
# 
# 
# Constraints:
#         The number of nodes in the tree is in the range [1, 10⁵].
#         1 <= Node.val <= 10⁵
#         All the values of the tree are unique.

import sys
import os

# Add the parent directory to sys.path to import miscelaneus tools
current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)

from tree import get_tree
from collections import deque

# Solution: https://youtu.be/6mONZ_54rZg
# Credit: Navdeep Singh founder of NeetCode
def minimum_operations(root):
    def count_swaps(nums):
        swaps = 0
        sorted_nums = sorted(nums)
        idx_map = {n:i for i, n in enumerate(nums)}
        for i in range(len(nums)):
            if nums[i] != sorted_nums[i]:
                swaps += 1

                j = idx_map[sorted_nums[i]]
                nums[i], nums[j] = nums[j], nums[i]
                idx_map[nums[j]] = j
        
        return swaps
    
    q = deque([root])
    res = 0
    while q:
        level = []

        for _ in range(len(q)):
            node = q.popleft()
            level.append(node.val)

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        res += count_swaps(level)

    return res
    # Time: O(n * log(n))
    # Space: O(n)
    # n = total number of nodes in the binary tree


def main():
    root = get_tree("[1,4,3,7,6,8,5,null,null,null,null,9,null,10]")
    result = minimum_operations(root)
    print(result) # 3

    root2 = get_tree("[1,3,2,7,6,5,4]")
    result = minimum_operations(root2)
    print(result) # 3

    root3 = get_tree("[1,2,3,4,5,6]")
    result = minimum_operations(root3)
    print(result) # 0

if __name__ == "__main__":
    main()
