# ---------------------------------
# 1483. Kth Ancestor of a Tree Node
# ---------------------------------

# Problem: https://leetcode.com/problems/kth-ancestor-of-a-tree-node
#
# You are given a tree with n nodes numbered from 0 to n - 1 in the form of a
# parent array parent where parent[i] is the parent of iᵗʰ node. The root of the
# tree is node 0. Find the kᵗʰ ancestor of a given node.
# 
# The kᵗʰ ancestor of a tree node is the kᵗʰ node in the path from that node to
# the root node.
# 
# Implement the TreeAncestor class:
#         
#   * TreeAncestor(int n, int[] parent) Initializes the object with the number
#     of nodes in the tree and the parent array.
#   * int getKthAncestor(int node, int k) return the kᵗʰ ancestor of the given
#     node node. If there is no such ancestor, return -1.
# 
# Example 1:
# 
# https://assets.leetcode.com/uploads/2019/08/28/1528_ex1.png
# 
# Input
# ["TreeAncestor", "getKthAncestor", "getKthAncestor", "getKthAncestor"]
# [[7, [-1, 0, 0, 1, 1, 2, 2]], [3, 1], [5, 2], [6, 3]]
# Output
# [null, 1, 0, -1]
# 
# Explanation
# TreeAncestor treeAncestor = new TreeAncestor(7, [-1, 0, 0, 1, 1, 2, 2]);
# treeAncestor.getKthAncestor(3, 1); // returns 1 which is the parent of 3
# treeAncestor.getKthAncestor(5, 2); // returns 0 which is the grandparent of 5
# treeAncestor.getKthAncestor(6, 3); // returns -1 because there is no such
# ancestor
# 
# 
# Constraints:
#         1 <= k <= n <= 5 * 10⁴
#         parent.length == n
#         parent[0] == -1
#         0 <= parent[i] < n for all 0 < i < n
#         0 <= node < n
#         There will be at most 5 * 10⁴ queries.


# Solution: https://algo.monster/liteproblems/1483
# Credit: AlgoMonster
from typing import List

class TreeAncestor:
    def __init__(self, n: int, parent: List[int]):
        """
        Initialize the TreeAncestor data structure.
      
        Args:
            n: Number of nodes in the tree (nodes are numbered from 0 to n-1)
            parent: List where parent[i] is the parent of node i (-1 for root)
        """
        # Maximum power of 2 we need (2^17 > 50000, which covers most tree sizes)
        max_power = 18
      
        # Binary lifting table: ancestors[i][j] = 2^j-th ancestor of node i
        # -1 means the ancestor doesn't exist (we've gone above the root)
        self.ancestors = [[-1] * max_power for _ in range(n)]
      
        # Initialize the first column: direct parent (2^0 = 1st ancestor)
        for node, parent_node in enumerate(parent):
            self.ancestors[node][0] = parent_node
      
        # Build the binary lifting table using dynamic programming
        # ancestors[i][j] = ancestors[ancestors[i][j-1]][j-1]
        # This means: 2^j-th ancestor = 2^(j-1)-th ancestor of 2^(j-1)-th ancestor
        for power in range(1, max_power):
            for node in range(n):
                # If the 2^(power-1)-th ancestor doesn't exist, skip
                if self.ancestors[node][power - 1] == -1:
                    continue
              
                # Find the 2^(power-1)-th ancestor of the 2^(power-1)-th ancestor
                intermediate_ancestor = self.ancestors[node][power - 1]
                self.ancestors[node][power] = self.ancestors[intermediate_ancestor][power - 1]

    def getKthAncestor(self, node: int, k: int) -> int:
        """
        Find the k-th ancestor of the given node.
      
        Args:
            node: The node whose ancestor we want to find
            k: The number of steps to go up in the tree
          
        Returns:
            The k-th ancestor of node, or -1 if it doesn't exist
        """
        # Decompose k into sum of powers of 2 and jump accordingly
        # We check bits from most significant to least significant
        for bit_position in range(17, -1, -1):
            # Check if the bit at position 'bit_position' is set in k
            if (k >> bit_position) & 1:
                # Jump 2^bit_position steps up
                node = self.ancestors[node][bit_position]
              
                # If we've gone above the root, stop early
                if node == -1:
                    break
      
        return node


def main():
    print("TO DO")

if __name__ == "__main__":
    main()
