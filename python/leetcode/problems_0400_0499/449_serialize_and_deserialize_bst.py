# ----------------------------------
# 449. Serialize and Deserialize BST
# ----------------------------------

# Problem: https://leetcode.com/problems/serialize-and-deserialize-bst
#
# Serialization is converting a data structure or object into a sequence of bits
# so that it can be stored in a file or memory buffer, or transmitted across a
# network connection link to be reconstructed later in the same or another
# computer environment.
# 
# Design an algorithm to serialize and deserialize a binary search tree. There is
# no restriction on how your serialization/deserialization algorithm should work.
# You need to ensure that a binary search tree can be serialized to a string, and
# this string can be deserialized to the original tree structure.
# 
# The encoded string should be as compact as possible.
# 
# Example 1:
# 
# Input: root = [2,1,3]
# Output: [2,1,3]
# 
# Example 2:
# 
# Input: root = []
# Output: []
# 
# 
# Constraints:
#         The number of nodes in the tree is in the range [0, 10⁴].
#         0 <= Node.val <= 10⁴
#         The input tree is guaranteed to be a binary search tree.

import sys
import os

# Add the parent directory to sys.path to import miscelaneus tools
current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)

from tree import get_tree, TreeNode
from math import inf

# Solution: 
# Credit: Navdeep Singh founder of NeetCode
class Codec:
    def serialize(self, root):

        def preorder_traversal(node):
            """Helper function to perform preorder traversal and collect values."""
            if node is None:
                return
          
            # Visit root first (preorder)
            values.append(node.val)
            # Then traverse left subtree
            preorder_traversal(node.left)
            # Finally traverse right subtree
            preorder_traversal(node.right)
      
        # List to store the node values in preorder
        values = []
        preorder_traversal(root)
      
        # Convert list of integers to space-separated string
        return " ".join(map(str, values))

    def deserialize(self, data):
     
        def build_bst(min_val, max_val):
            nonlocal current_index
          
            # Check if we've processed all values or current value doesn't fit constraints
            if current_index == len(values) or not (min_val <= values[current_index] <= max_val):
                return None
          
            # Current value becomes the root of this subtree
            root_value = values[current_index]
            root_node = TreeNode(root_value)
            current_index += 1
          
            # Build left subtree with values less than root_value
            root_node.left = build_bst(min_val, root_value)
            # Build right subtree with values greater than root_value
            root_node.right = build_bst(root_value, max_val)
          
            return root_node
      
        # Handle empty tree case
        if not data:
            return None
      
        # Convert string back to list of integers
        values = list(map(int, data.split()))
      
        # Index to track current position in values list
        current_index = 0
      
        # Start building BST with no constraints
        return build_bst(-inf, inf)


def main():
    ser = Codec()
    deser = Codec()
    tree = ser.serialize(get_tree("[2,1,3]"))
    ans = deser.deserialize(tree)
    print(ans) # [2, 1, 3]

if __name__ == "__main__":
    main()
