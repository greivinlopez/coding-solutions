# ---------------------
# 1206. Design Skiplist
# ---------------------

# Problem: https://leetcode.com/problems/design-skiplist
#
# Design a Skiplist without using any built-in libraries.
# 
# A skiplist is a data structure that takes O(log(n)) time to add, erase and
# search. Comparing with treap and red-black tree which has the same function and
# performance, the code length of Skiplist can be comparatively short and the idea
# behind Skiplists is just simple linked lists.
# 
# For example, we have a Skiplist containing [30,40,50,60,70,90] and we want to
# add 80 and 45 into it. The Skiplist works this way:
# 
# https://assets.leetcode.com/uploads/2019/09/27/1506_skiplist.gif
# 
# Artyom Kalinin [CC BY-SA 3.0], via Wikimedia Commons
# 
# You can see there are many layers in the Skiplist. Each layer is a sorted linked
# list. With the help of the top layers, add, erase and search can be faster than
# O(n). It can be proven that the average time complexity for each operation is
# O(log(n)) and space complexity is O(n).
# 
# See more about Skiplist: https://en.wikipedia.org/wiki/Skip_list
# 
# Implement the Skiplist class:
#         
#   * Skiplist() Initializes the object of the skiplist.
#   * bool search(int target) Returns true if the integer target exists in the
#     Skiplist or false otherwise.
#   * void add(int num) Inserts the value num into the SkipList.
#   * bool erase(int num) Removes the value num from the Skiplist and returns
#     true. If num does not exist in the Skiplist, do nothing and return false. If
#     there exist multiple num values, removing any one of them is fine.
# 
# Note that duplicates may exist in the Skiplist, your code needs to handle this
# situation.
# 
# Example 1:
# 
# Input
# ["Skiplist", "add", "add", "add", "search", "add", "search", "erase", "erase",
# "search"]
# [[], [1], [2], [3], [0], [4], [1], [0], [1], [1]]
# Output
# [null, null, null, null, false, null, true, false, true, false]
# 
# Explanation
# Skiplist skiplist = new Skiplist();
# skiplist.add(1);
# skiplist.add(2);
# skiplist.add(3);
# skiplist.search(0); // return False
# skiplist.add(4);
# skiplist.search(1); // return True
# skiplist.erase(0);  // return False, 0 is not in skiplist.
# skiplist.erase(1);  // return True
# skiplist.search(1); // return False, 1 has already been erased.
# 
# 
# Constraints:
#         0 <= num, target <= 2 * 10⁴
#         At most 5 * 10⁴ calls will be made to search, add, and erase.

import random
from typing import List, Optional

# Solution: https://algo.monster/liteproblems/1206
# Credit: AlgoMonster
class Node:
    """Node class for skip list implementation."""
    __slots__ = ['val', 'next']
  
    def __init__(self, val: int, level: int) -> None:
        """
        Initialize a node with a value and level.
      
        Args:
            val: The value stored in the node
            level: The number of forward pointers this node will have
        """
        self.val: int = val
        self.next: List[Optional['Node']] = [None] * level

class Skiplist:
    """
    Skip list data structure implementation.
  
    A probabilistic data structure that allows O(log n) search, insertion and deletion.
    Each node can have multiple forward pointers at different levels.
    """
  
    MAX_LEVEL: int = 32  # Maximum number of levels in the skip list
    PROBABILITY: float = 0.25  # Probability for determining node levels
  
    def __init__(self) -> None:
        """Initialize an empty skip list with a sentinel head node."""
        # Create head node with maximum possible level
        self.head: Node = Node(-1, self.MAX_LEVEL)
        # Current maximum level in use
        self.level: int = 0
  
    def search(self, target: int) -> bool:
        """
        Search for a target value in the skip list.
      
        Args:
            target: The value to search for
          
        Returns:
            True if the target exists, False otherwise
        """
        current: Node = self.head
      
        # Start from the highest level and move down
        for i in range(self.level - 1, -1, -1):
            # Find the node just before where target would be at this level
            current = self._find_closest_node(current, i, target)
            # Check if the next node at this level contains the target
            if current.next[i] and current.next[i].val == target:
                return True
      
        return False
  
    def add(self, num: int) -> None:
        """
        Add a number to the skip list.
      
        Args:
            num: The number to add
        """
        current: Node = self.head
        # Randomly determine the level for the new node
        node_level: int = self._generate_random_level()
        new_node: Node = Node(num, node_level)
      
        # Update the maximum level if necessary
        self.level = max(self.level, node_level)
      
        # Insert the node at all levels from top to bottom
        for i in range(self.level - 1, -1, -1):
            # Find the position to insert at this level
            current = self._find_closest_node(current, i, num)
          
            # Only update pointers for levels within the new node's range
            if i < node_level:
                new_node.next[i] = current.next[i]
                current.next[i] = new_node
  
    def erase(self, num: int) -> bool:
        """
        Remove the first occurrence of a number from the skip list.
      
        Args:
            num: The number to remove
          
        Returns:
            True if the number was found and removed, False otherwise
        """
        current: Node = self.head
        found: bool = False
      
        # Remove the node from all levels where it appears
        for i in range(self.level - 1, -1, -1):
            # Find the node just before the target at this level
            current = self._find_closest_node(current, i, num)
          
            # If the next node contains the target value, remove it
            if current.next[i] and current.next[i].val == num:
                current.next[i] = current.next[i].next[i]
                found = True
      
        # Decrease the maximum level if top levels are now empty
        while self.level > 1 and self.head.next[self.level - 1] is None:
            self.level -= 1
      
        return found
  
    def _find_closest_node(self, current: Node, level: int, target: int) -> Node:
        """
        Find the rightmost node whose value is less than the target at a given level.
      
        Args:
            current: The starting node
            level: The level to search at
            target: The target value
          
        Returns:
            The node just before where the target would be positioned
        """
        # Move forward at this level while the next value is less than target
        while current.next[level] and current.next[level].val < target:
            current = current.next[level]
      
        return current
  
    def _generate_random_level(self) -> int:
        """
        Generate a random level for a new node using geometric distribution.
      
        Returns:
            A random level between 1 and MAX_LEVEL
        """
        level: int = 1
      
        # Keep increasing level with probability PROBABILITY
        while level < self.MAX_LEVEL and random.random() < self.PROBABILITY:
            level += 1
      
        return level


def main():
    print("TO DO")

if __name__ == "__main__":
    main()
