# ---------------------------------------------------
# 117. Populating Next Right Pointers in Each Node II
# ---------------------------------------------------

# Problem: https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii
#
# Given a binary tree
# 
# struct Node {
#   int val;
#   Node *left;
#   Node *right;
#   Node *next;
# }
# 
# Populate each next pointer to point to its next right node. If there is no next
# right node, the next pointer should be set to NULL.
# 
# Initially, all next pointers are set to NULL.
# 
# Example 1:
# 
# https://assets.leetcode.com/uploads/2019/02/15/117_sample.png
# 
# Input: root = [1,2,3,4,5,null,7]
# Output: [1,#,2,3,#,4,5,7,#]
# 
# Explanation: Given the above binary tree (Figure A), your function should
# populate each next pointer to point to its next right node, just like in Figure
# B. The serialized output is in level order as connected by the next pointers,
# with '#' signifying the end of each level.
# 
# Example 2:
# 
# Input: root = []
# Output: []
# 
# 
# Constraints:
#         The number of nodes in the tree is in the range [0, 6000].
#         -100 <= Node.val <= 100
# 
# 
# Follow-up:
#       * You may only use constant extra space.
#       * The recursive approach is fine. You may assume implicit stack space does
#         not count as extra space for this problem.

import collections

class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

# Credit: Jaweria Batool -> https://github.com/Jaweria-B
def connect(root):
    if not root:
        return root
    
    queue = collections.deque()
    queue.append(root)
    
    while queue:
        
        size = len(queue)
        prev = None
        
        for i in range(size):
            cur = queue.popleft()
            
            if cur.left:
                queue.append(cur.left)
            
            if cur.right:
                queue.append(cur.right)
            
            if prev:
                prev.next = cur
                prev = cur
            else:
                prev = cur
                
    return root
    # Time: O(n)
    # Space: O(w)
    # n = the number of nodes 
    # w = the maximum width of the tree


def main():
    print("TO DO")

if __name__ == "__main__":
    main()
