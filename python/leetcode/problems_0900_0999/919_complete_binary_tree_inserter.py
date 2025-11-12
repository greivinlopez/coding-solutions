# ----------------------------------
# 919. Complete Binary Tree Inserter
# ----------------------------------

# Problem: https://leetcode.com/problems/complete-binary-tree-inserter
#
# A complete binary tree is a binary tree in which every level, except possibly
# the last, is completely filled, and all nodes are as far left as possible.
# 
# Design an algorithm to insert a new node to a complete binary tree keeping it
# complete after the insertion.
# 
# Implement the CBTInserter class:
#         
#   * CBTInserter(TreeNode root) Initializes the data structure with the root
#     of the complete binary tree.
#   * int insert(int v) Inserts a TreeNode into the tree with value Node.val == val 
#     so that the tree remains complete, and returns the value of the parent of
#     the inserted TreeNode.
#   * TreeNode get_root() Returns the root node of the tree.
# 
# Example 1:
# 
# Input
# ["CBTInserter", "insert", "insert", "get_root"]
# [[[1, 2]], [3], [4], []]
# Output
# [null, 1, 2, [1, 2, 3, 4]]
# 
# Explanation
# CBTInserter cBTInserter = new CBTInserter([1, 2]);
# cBTInserter.insert(3);  // return 1
# cBTInserter.insert(4);  // return 2
# cBTInserter.get_root(); // return [1, 2, 3, 4]
# 
# 
# Constraints:
#         The number of nodes in the tree will be in the range [1, 1000].
#         0 <= Node.val <= 5000
#         root is a complete binary tree.
#         0 <= val <= 5000
#         At most 10⁴ calls will be made to insert and get_root.

import sys
import os

# Add the parent directory to sys.path to import miscelaneus tools
current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)

from tree import TreeNode
from collections import deque
from typing import Optional

# Solution: https://algo.monster/liteproblems/919
# Credit: AlgoMonster
class CBTInserter:
    """
    A class to handle insertions in a Complete Binary Tree (CBT).
    Maintains the tree nodes in level-order traversal for efficient insertion.
    """
  
    def __init__(self, root: Optional[TreeNode]):
        """
        Initialize the CBT inserter with an existing complete binary tree.
        Stores all nodes in a list following level-order traversal.
      
        Args:
            root: The root node of the existing complete binary tree
        """
        # Store all tree nodes in level-order (breadth-first) sequence
        self.tree_nodes = []
      
        # Use BFS to traverse the tree and store nodes in order
        queue = deque([root])
        while queue:
            # Process all nodes at current level
            level_size = len(queue)
            for _ in range(level_size):
                current_node = queue.popleft()
                self.tree_nodes.append(current_node)
              
                # Add children to queue for next level processing
                if current_node.left:
                    queue.append(current_node.left)
                if current_node.right:
                    queue.append(current_node.right)

    def insert(self, val: int) -> int:
        """
        Insert a new node with given value into the complete binary tree.
      
        Args:
            val: The value for the new node to be inserted
          
        Returns:
            The value of the parent node where the new node was inserted
        """
        # Calculate parent index using complete binary tree property
        # For 0-indexed array: parent of node at index i is at (i-1)//2
        parent_index = (len(self.tree_nodes) - 1) // 2
        parent_node = self.tree_nodes[parent_index]
      
        # Create the new node
        new_node = TreeNode(val)
        self.tree_nodes.append(new_node)
      
        # Attach new node to parent's left or right based on availability
        if parent_node.left is None:
            parent_node.left = new_node
        else:
            parent_node.right = new_node
          
        return parent_node.val

    def get_root(self) -> Optional[TreeNode]:
        """
        Get the root node of the complete binary tree.
      
        Returns:
            The root node of the tree
        """
        return self.tree_nodes[0] if self.tree_nodes else None


def main():
    print("TO DO")

if __name__ == "__main__":
    main()
