# ------------------------------------
# 501. Find Mode in Binary Search Tree
# ------------------------------------

# Problem: https://leetcode.com/problems/find-mode-in-binary-search-tree
#
# Given the root of a binary search tree (BST) with duplicates, return all the
# mode(s) (i.e., the most frequently occurred element) in it.
# 
# If the tree has more than one mode, return them in any order.
# 
# Assume a BST is defined as follows:
#         
#   * The left subtree of a node contains only nodes with keys less than or
#     equal to the node's key.
#   * The right subtree of a node contains only nodes with keys greater than
#     or equal to the node's key.
#   * Both the left and right subtrees must also be binary search trees.
# 
# Example 1:
# 
# Input: root = [1,null,2,2]
# Output: [2]
# 
# Example 2:
# 
# Input: root = [0]
# Output: [0]
# 
# 
# Constraints:
#         The number of nodes in the tree is in the range [1, 10⁴].
#         -10⁵ <= Node.val <= 10⁵
# 
# Follow up: Could you do that without using any extra space? (Assume that the
# implicit stack space incurred due to recursion does not count).

import sys
import os

# Add the parent directory to sys.path to import miscelaneus tools
current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)

from tree import get_tree
from collections import defaultdict

# Credit: Jaweria Batool -> https://github.com/Jaweria-B
def find_mode(root):
    
    def dfs(node, counter):
        if not node:
            return
        
        counter[node.val] += 1
        dfs(node.left, counter)
        dfs(node.right, counter)
        
    counter = defaultdict(int)
    dfs(root, counter)
    
    max_freq = max(counter.values())
    
    ans = []
    for key in counter:
        if counter[key] == max_freq:
            ans.append(key)
    return ans
    # Time: O(n)
    # Space: O(n)


def main():
    result = find_mode(get_tree("[1,null,2,2]"))
    print(result) # [2]

    result = find_mode(get_tree("[0]"))
    print(result) # [0]

if __name__ == "__main__":
    main()
