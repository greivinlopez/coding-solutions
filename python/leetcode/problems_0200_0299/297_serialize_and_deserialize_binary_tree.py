# ------------------------------------------
# 297. Serialize And Deserialize Binary Tree
# ------------------------------------------


# Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.
# 
# Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.
# 
# Clarification: The input/output format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.
# 
#  
# Example 1:
# 
# 
# Input: root = [1,2,3,null,null,4,5]
# Output: [1,2,3,null,null,4,5]
# 
# 
# Example 2:
# 
# 
# Input: root = []
# Output: []
# 
# 
#  
# Constraints:
# 
# 
# 	The number of nodes in the tree is in the range [0, 104].
# 	-1000 <= Node.val <= 1000

import sys
import os

# Add the parent directory to sys.path to import miscelaneus tools
current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)

from tree import TreeNode

# Solution: https://youtu.be/u4JAi2JJhI8
# Credit: Navdeep Singh founder of NeetCode
class Codec:
    def serialize(self, root):
        res = []

        def dfs(node):
            if not node:
                res.append("N")
                return
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ",".join(res)

    def deserialize(self, data):
        vals = data.split(",")

        def dfs():
            val = vals.pop(0)
            if val == "N":
                return None
            node = TreeNode(val=int(val))
            node.left = dfs()
            node.right = dfs()
            return node

        return dfs()


def main():
    print("TO DO")

if __name__ == "__main__":
    main()
