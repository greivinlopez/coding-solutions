# -------------------------------
# 1145. Binary Tree Coloring Game
# -------------------------------

# Problem: https://leetcode.com/problems/binary-tree-coloring-game
#
# Two players play a turn based game on a binary tree. We are given the root of
# this binary tree, and the number of nodes n in the tree. n is odd, and each node
# has a distinct value from 1 to n.
# 
# Initially, the first player names a value x with 1 <= x <= n, and the second
# player names a value y with 1 <= y <= n and y != x. The first player colors the
# node with value x red, and the second player colors the node with value y blue.
# 
# Then, the players take turns starting with the first player. In each turn, that
# player chooses a node of their color (red if player 1, blue if player 2) and
# colors an uncolored neighbor of the chosen node (either the left child, right
# child, or parent of the chosen node.)
# 
# If (and only if) a player cannot choose such a node in this way, they must pass
# their turn. If both players pass their turn, the game ends, and the winner is
# the player that colored more nodes.
# 
# You are the second player. If it is possible to choose such a y to ensure you
# win the game, return true. If it is not possible, return false.
# 
# Example 1:
# 
# https://assets.leetcode.com/uploads/2019/08/01/1480-binary-tree-coloring-game.png
# 
# Input: root = [1,2,3,4,5,6,7,8,9,10,11], n = 11, x = 3
# Output: true
# 
# Explanation: The second player can choose the node with value 2.
# 
# Example 2:
# 
# Input: root = [1,2,3], n = 3, x = 1
# Output: false
# 
# 
# Constraints:
#         The number of nodes in the tree is n.
#         1 <= x <= n <= 100
#         n is odd.
#         1 <= Node.val <= n
#         All the values of the tree are unique.

import sys
import os

# Add the parent directory to sys.path to import miscelaneus tools
current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)

from tree import get_tree

# Solution: https://algo.monster/liteproblems/1145
# Credit: AlgoMonster
def btree_game_winning_move(root, n, x):
   
    def find_node(current_node):
        # Base case: empty node or found the target node
        if current_node is None or current_node.val == x:
            return current_node
        
        # Search in left subtree first, then right subtree
        left_result = find_node(current_node.left)
        return left_result if left_result else find_node(current_node.right)
    
    def count_nodes(current_node):
        # Base case: empty node contributes 0
        if current_node is None:
            return 0
        
        # Count current node (1) plus all nodes in left and right subtrees
        return 1 + count_nodes(current_node.left) + count_nodes(current_node.right)
    
    # Find the node chosen by the first player
    target_node = find_node(root)
    
    # Count nodes in the left and right subtrees of the target node
    left_subtree_count = count_nodes(target_node.left)
    right_subtree_count = count_nodes(target_node.right)
    
    # Calculate nodes in the parent region (total minus target and its subtrees)
    parent_region_count = n - left_subtree_count - right_subtree_count - 1
    
    # The second player wins if they can control more than half the nodes
    # by choosing one of the three regions: left subtree, right subtree, or parent region
    max_controllable_nodes = max(left_subtree_count, right_subtree_count, parent_region_count)
    
    return max_controllable_nodes > n // 2
    # Time: O(n)
    # Space: O(n)


def main():
    root = get_tree("[1,2,3,4,5,6,7,8,9,10,11]")
    result = btree_game_winning_move(root, n = 11, x = 3)
    print(result) # True

    root = get_tree("[1,2,3]")
    result = btree_game_winning_move(root, n = 3, x = 1)
    print(result) # False

if __name__ == "__main__":
    main()
