# ----------------
# 113. Path Sum II
# ----------------

# Problem: https://leetcode.com/problems/path-sum-ii
#
# Given the root of a binary tree and an integer targetSum, return all root-to-
# leaf paths where the sum of the node values in the path equals targetSum. Each
# path should be returned as a list of the node values, not node references.
# 
# A root-to-leaf path is a path starting from the root and ending at any leaf
# node. A leaf is a node with no children.
# 
# Example 1:
# 
# https://assets.leetcode.com/uploads/2021/01/18/pathsumii1.jpg
# 
# Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
# Output: [[5,4,11,2],[5,8,4,5]]
# 
# Explanation: There are two paths whose sum equals targetSum:
# 5 + 4 + 11 + 2 = 22
# 5 + 8 + 4 + 5 = 22
# 
# Example 2:
# 
# https://assets.leetcode.com/uploads/2021/01/18/pathsum2.jpg
# 
# Input: root = [1,2,3], targetSum = 5
# Output: []
# 
# Example 3:
# 
# Input: root = [1,2], targetSum = 0
# Output: []
# 
# 
# Constraints:
#         The number of nodes in the tree is in the range [0, 5000].
#         -1000 <= Node.val <= 1000
#         -1000 <= targetSum <= 1000


import sys
import os

# Add the parent directory to sys.path to import miscelaneus tools
current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)

from tree import get_tree


# Solution: https://leetcode.com/problems/path-sum-ii/solutions/6933884/beats-99-82-very-easy-using-dfs-java-python-c-javascript
# Credit: Pradhuman Gupta -> https://leetcode.com/u/PradhumanGupta/
def path_sum(root, targetSum):
    res = []
    
    def dfs(node, path, curSum):
        if not node: return
        
        curSum += node.val
        path.append(node.val)
        
        if not node.left and not node.right and curSum == targetSum:
            res.append(path[:])
        
        dfs(node.left, path, curSum)
        dfs(node.right, path, curSum)
        path.pop()
    
    dfs(root, [], 0)
    return res
    # Time: O(n)
    # Space: O(h)


def main():
    root = get_tree("[5,4,8,11,null,13,4,7,2,null,null,5,1]")
    result = path_sum(root, 22)
    print(result) # [[5, 4, 11, 2], [5, 8, 4, 5]]

    root = get_tree("[1,2,3]")
    result = path_sum(root, 5)
    print(result) # []

    root = get_tree("[1,2]")
    result = path_sum(root, 0)
    print(result) # []

if __name__ == "__main__":
    main()
