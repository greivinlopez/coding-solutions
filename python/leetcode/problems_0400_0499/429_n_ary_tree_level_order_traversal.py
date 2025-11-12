# -------------------------------------
# 429. N-ary Tree Level Order Traversal
# -------------------------------------

# Problem: https://leetcode.com/problems/n-ary-tree-level-order-traversal/description/
# 
# Given an n-ary tree, return the level order traversal of its nodes' values.
# 
# Nary-Tree input serialization is represented in their level order traversal, 
# each group of children is separated by the null value (See examples).
# 
#  
# Example 1:
# 
# Input: root = [1,null,3,2,4,null,5,6]
# Output: [[1],[3,2,4],[5,6]]
# 
# Example 2:
# 
# Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
# Output: [[1],[2,3,4,5],[6,7,8,9,10],[11,12,13],[14]]
#  
# 
# Constraints:
# 
#   The height of the n-ary tree is less than or equal to 1000
#   The total number of nodes is between [0, 10^4]

from collections import deque

# Solution: No Video Found
# Credit: Greg Hogg
def level_order(root):
    if not root:
        return []
    output = []
    q = deque()
    q.append(root)

    while q:
        n = len(q)
        level = []
        for _ in range(n):
            node = q.popleft()
            level.append(node.val)
            for child in node.children:
                q.append(child)
        output.append(level)
    
    return output
    # Time: O(n)
    # Space: O(n)
    # n is number of nodes in the tree

def main():
    print("TO DO")

if __name__ == "__main__":
    main()
