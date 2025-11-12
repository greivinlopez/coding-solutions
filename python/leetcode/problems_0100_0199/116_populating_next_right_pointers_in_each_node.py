# ------------------------------------------------
# 116. Populating Next Right Pointers in Each Node
# ------------------------------------------------

# Problem: https://leetcode.com/problems/populating-next-right-pointers-in-each-node
#
# You are given a perfect binary tree where all leaves are on the same level, and
# every parent has two children. The binary tree has the following definition:
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
# https://assets.leetcode.com/uploads/2019/02/14/116_sample.png
# 
# Input: root = [1,2,3,4,5,6,7]
# Output: [1,#,2,3,#,4,5,6,7,#]
# 
# Explanation: Given the above perfect binary tree (Figure A), your function
# should populate each next pointer to point to its next right node, just like in
# Figure B. The serialized output is in level order as connected by the next
# pointers, with '#' signifying the end of each level.
# 
# Example 2:
# 
# Input: root = []
# Output: []
# 
# 
# Constraints:
#         The number of nodes in the tree is in the range [0, 2¹² - 1].
#         -1000 <= Node.val <= 1000
# 
# 
# Follow-up:
#         You may only use constant extra space.
#         The recursive approach is fine. You may assume implicit stack space does
# not count as extra space for this problem.

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
    
    def recursion(root):
        if not root:
            return
        
        if root.left:
            root.left.next = root.right
        
        if root.right and root.next:
            root.right.next = root.next.left
            
        recursion(root.left)
        recursion(root.right)
    
    recursion(root)
    
    return root
    # Time: O(n)
    # Space: (h)
    # n = the total number of nodes
    # h = the height of the binary tree


def main():
    print("TO DO")

if __name__ == "__main__":
    main()
