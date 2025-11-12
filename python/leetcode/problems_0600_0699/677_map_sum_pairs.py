# ------------------
# 677. Map Sum Pairs
# ------------------

# Problem: https://leetcode.com/problems/map-sum-pairs
#
# Design a map that allows you to do the following:
#         
#   * Maps a string key to a given value.
#   * Returns the sum of the values that have a key with a prefix equal to a
#     given string.
# 
# Implement the MapSum class:
#         
#   * MapSum() Initializes the MapSum object.
#   * void insert(String key, int val) Inserts the key-val pair into the map.
#     If the key already existed, the original key-value pair will be overridden to
#     the new one.
#   * int sum(string prefix) Returns the sum of all the pairs' value whose key starts 
#     with the prefix.
# 
# Example 1:
# 
# Input
# ["MapSum", "insert", "sum", "insert", "sum"]
# [[], ["apple", 3], ["ap"], ["app", 2], ["ap"]]
# Output
# [null, null, 3, null, 5]
# 
# Explanation
# MapSum mapSum = new MapSum();
# mapSum.insert("apple", 3);
# mapSum.sum("ap");           // return 3 (apple = 3)
# mapSum.insert("app", 2);
# mapSum.sum("ap");           // return 5 (apple + app = 3 + 2 = 5)
# 
# 
# Constraints:
#         1 <= key.length, prefix.length <= 50
#         key and prefix consist of only lowercase English letters.
#         1 <= val <= 1000
#         At most 50 calls will be made to insert and sum.

from collections import defaultdict
from typing import List, Optional

# Solution: https://algo.monster/liteproblems/677
# Credit: AlgoMonster
class Trie:
    """A Trie (prefix tree) data structure for efficient prefix-based operations."""
  
    def __init__(self):
        # Array to store 26 child nodes (one for each lowercase letter a-z)
        self.children: List[Optional['Trie']] = [None] * 26
        # Accumulated value at this node (sum of all values for words ending here or passing through)
        self.val: int = 0

    def insert(self, word: str, delta: int) -> None:
        """
        Insert a word into the trie and update values along the path.
      
        Args:
            word: The word to insert
            delta: The value difference to add to each node along the path
        """
        node = self
        for char in word:
            # Convert character to index (0-25)
            index = ord(char) - ord('a')
            # Create new node if path doesn't exist
            if node.children[index] is None:
                node.children[index] = Trie()
            # Move to child node
            node = node.children[index]
            # Update the accumulated value at this node
            node.val += delta

    def search(self, prefix: str) -> int:
        """
        Search for a prefix and return the sum of all values with this prefix.
      
        Args:
            prefix: The prefix to search for
          
        Returns:
            The sum of all values for words with the given prefix, or 0 if prefix doesn't exist
        """
        node = self
        for char in prefix:
            # Convert character to index (0-25)
            index = ord(char) - ord('a')
            # If path doesn't exist, prefix is not in trie
            if node.children[index] is None:
                return 0
            # Move to child node
            node = node.children[index]
        # Return the accumulated value at the prefix node
        return node.val

class MapSum:
    """
    A data structure that maps strings to values and supports sum queries for prefixes.
    If a key already exists, its value is overridden.
    """
  
    def __init__(self):
        # Dictionary to store current value for each key
        self.key_value_map = defaultdict(int)
        # Trie to efficiently compute prefix sums
        self.trie = Trie()

    def insert(self, key: str, val: int) -> None:
        """
        Insert or update a key-value pair.
      
        Args:
            key: The string key to insert or update
            val: The new value for the key
        """
        # Calculate the difference between new value and old value (0 if new key)
        delta = val - self.key_value_map[key]
        # Update the stored value for this key
        self.key_value_map[key] = val
        # Update the trie with the value difference
        self.trie.insert(key, delta)

    def sum(self, prefix: str) -> int:
        """
        Return the sum of all values for keys that start with the given prefix.
      
        Args:
            prefix: The prefix to search for
          
        Returns:
            The sum of values for all keys with the given prefix
        """
        return self.trie.search(prefix)


def main():
    print("TO DO")

if __name__ == "__main__":
    main()
