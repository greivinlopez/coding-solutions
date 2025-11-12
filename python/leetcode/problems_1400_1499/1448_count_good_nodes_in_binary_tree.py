# ------------------------------------
# 1448. Count Good Nodes In Binary Tree
# ------------------------------------

# Problem: https://leetcode.com/problems/count-good-nodes-in-binary-tree
#
# Given a binary tree root, a node X in the tree is named good if in the path from
# root to X there are no nodes with a value greater than X.
# Return the number of good nodes in the binary tree.
# 
# Example 1:
# 
# Input: root = [3,1,4,3,null,1,5]
# Output: 4
# Explanation: Nodes in blue are good.
# Root Node (3) is always a good node.
# Node 4 -> (3,4) is the maximum value in the path starting from the root.
# Node 5 -> (3,4,5) is the maximum value in the path
# Node 3 -> (3,1,3) is the maximum value in the path.
# 
# Example 2:
# 
# Input: root = [3,3,null,4,2]
# Output: 3
# Explanation: Node 2 -> (3, 3, 2) is not good, because "3" is higher than it.
# 
# Example 3:
# 
# Input: root = [1]
# Output: 1
# Explanation: Root is considered as good.
# 
# 
# Constraints:
#         The number of nodes in the binary tree is in the range [1, 10^5].
#         Each node's value is between [-10^4, 10^4].

import sys
import os

# Add the parent directory to sys.path to import miscelaneus tools
current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)

# Import code needed for solutions
from tree import get_tree

# Solution: https://youtu.be/7cp5imvDzl4
# Credit: Navdeep Singh founder of NeetCode
def good_nodes(root):
    def dfs(node, maxVal):
        if not node:
            return 0

        res = 1 if node.val >= maxVal else 0
        maxVal = max(maxVal, node.val)
        res += dfs(node.left, maxVal)
        res += dfs(node.right, maxVal)
        return res

    return dfs(root, root.val)

# Solution: https://youtu.be/2AdOBLcj2wk
# Credit: Greg Hogg
def good_nodes_alt(root):
    good_nodes = 0
    stk = [(root, float("-inf"))]

    while stk:
        node, largest = stk.pop()
        
        if largest <= node.val:
            good_nodes += 1

        largest = max(largest, node.val)
        if node.right: stk.append((node.right, largest))
        if node.left: stk.append((node.left, largest))

    return good_nodes
    # Time: O(n)
    # Space: O(n)


def main():
    root = get_tree("[3,1,4,3,null,1,5]")
    result = good_nodes(root)
    print(result) # 4

    root = get_tree("[3,3,null,4,2]")
    result = good_nodes(root)
    print(result) # 3

    root = get_tree("[1]")
    result = good_nodes(root)
    print(result) # 1

if __name__ == "__main__":
    main()
