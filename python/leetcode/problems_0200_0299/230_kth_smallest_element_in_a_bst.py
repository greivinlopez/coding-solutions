# ----------------------------------
# 230. Kth Smallest Element In A BST
# ----------------------------------

# Problem: https://leetcode.com/problems/kth-smallest-element-in-a-bst/
# 
# Given the root of a binary search tree, and an integer k, return the kth 
# smallest value (1-indexed) of all the values of the nodes in the tree.
# 
#  
# Example 1:
# 
# Input: root = [3,1,4,null,2], k = 1
# Output: 1
# 
# 
# Example 2:
# 
# Input: root = [5,3,6,2,4,null,null,1], k = 3
# Output: 3
# 
#  
# Constraints:
# 
# 	The number of nodes in the tree is n.
# 	1 <= k <= n <= 104
# 	0 <= Node.val <= 104
#  
# Follow up: If the BST is modified often (i.e., we can do insert and delete operations) and you need to find the kth smallest frequently, how would you optimize?

import sys
import os

# Add the parent directory to sys.path to import miscelaneus tools
current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)

from tree import get_tree

# Solution: https://youtu.be/5LUXSvjmGCw
# Credit: Navdeep Singh founder of NeetCode
def kth_smallest(root, k):
    stack = []
    curr = root

    while stack or curr:
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        k -= 1
        if k == 0:
            return curr.val
        curr = curr.right

# Solution: https://youtu.be/PwjF3RO9djY
# Credit: Greg Hogg
def kth_smallest_alt(root, k):
    count = [k]
    ans = [0]

    def dfs(node):
        if not node:
            return
        
        dfs(node.left)

        if count[0] == 1:
            ans[0] = node.val
        
        count[0] = count[0] - 1
        if count[0] > 0:
            dfs(node.right)
    
    dfs(root)
    return ans[0]
    # Time: O(n)
    # Space: O(n)


def main():
    root = get_tree("[3,1,4,null,2]")
    result = kth_smallest(root, 1)
    print(result) # 1

    root = get_tree("[5,3,6,2,4,null,null,1]")
    result = kth_smallest(root, 3)
    print(result) # 3

if __name__ == "__main__":
    main()
