# -------------------------
# 450. Delete Node In A Bst
# -------------------------

# Problem: https://leetcode.com/problems/delete-node-in-a-bst/
# 
# Given a root node reference of a BST and a key, delete the node with the 
# given key in the BST. Return the root node reference (possibly updated) 
# of the BST.
# 
# Basically, the deletion can be divided into two stages:
# 
# 	Search for a node to remove.
# 	If the node is found, delete the node.
# 
#  
# Example 1:
# 
# Input: root = [5,3,6,2,4,null,7], key = 3
# Output: [5,4,6,2,null,null,7]
# 
# Explanation: Given key to delete is 3. So we find the node with value 3 and delete it.
# One valid answer is [5,4,6,2,null,null,7], shown in the above BST.
# Please notice that another valid answer is [5,2,6,null,4,null,7] and it's also accepted.
# 
# Example 2:
# 
# Input: root = [5,3,6,2,4,null,7], key = 0
# Output: [5,3,6,2,4,null,7]
# 
# Explanation: The tree does not contain a node with value = 0.
# 
# Example 3:
# 
# Input: root = [], key = 0
# Output: []
# 
# 
# Constraints:
# 
# 	The number of nodes in the tree is in the range [0, 104].
# 	-10^5 <= Node.val <= 10^5
# 	Each node has a unique value.
# 	root is a valid binary search tree.
# 	-10^5 <= key <= 10^5
# 
# Follow up: Could you solve it with time complexity O(height of tree)?

import sys
import os

# Add the parent directory to sys.path to import miscelaneus tools
current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)

from tree import get_tree

# Solution: https://youtu.be/LFzAoJJt92M
# Credit: Navdeep Singh founder of NeetCode
def delete_node(root, key):
    if not root:
        return root
    
    if key > root.val:
        root.right = delete_node(root.right, key)
    elif key < root.val:
        root.left = delete_node(root.left, key)
    else:
        if not root.left:
            return root.right
        elif not root.right:
            return root.left
        
        # Find the min from right subtree
        cur = root.right
        while cur.left:
            cur = cur.left 
        root.val = cur.val
        root.right = delete_node(root.right, root.val)
    return root


def main():
    root = get_tree("[5,3,6,2,4,null,7]")
    result = delete_node(root, 3)
    print(result) # [5, 4, 6, 2, None, None, 7]

    root = get_tree("[5,3,6,2,4,null,7]")
    result = delete_node(root, 0)
    print(result) # [5, 3, 6, 2, 4, None, 7]

if __name__ == "__main__":
    main()
