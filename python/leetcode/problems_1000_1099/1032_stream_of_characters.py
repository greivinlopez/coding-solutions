# -------------------------
# 1032. Stream of Characters
# -------------------------

# Problem: https://leetcode.com/problems/stream-of-characters
#
# Design an algorithm that accepts a stream of characters and checks if a suffix
# of these characters is a string of a given array of strings words.
# 
# For example, if words = ["abc", "xyz"] and the stream added the four characters
# (one by one) 'a', 'x', 'y', and 'z', your algorithm should detect that the
# suffix "xyz" of the characters "axyz" matches "xyz" from words.
# 
# Implement the StreamChecker class:
#         
#   * StreamChecker(String[] words) Initializes the object with the strings
#     array words.
#   * boolean query(char letter) Accepts a new character from the stream and
#     returns true if any non-empty suffix from the stream forms a word that is in
#     words.
# 
# Example 1:
# 
# Input
# ["StreamChecker", "query", "query", "query", "query", "query", "query", "query",
# "query", "query", "query", "query", "query"]
# [[["cd", "f", "kl"]], ["a"], ["b"], ["c"], ["d"], ["e"], ["f"], ["g"], ["h"],
# ["i"], ["j"], ["k"], ["l"]]
# Output
# [null, false, false, false, true, false, true, false, false, false, false,
# false, true]
# 
# Explanation
# StreamChecker streamChecker = new StreamChecker(["cd", "f", "kl"]);
# streamChecker.query("a"); // return False
# streamChecker.query("b"); // return False
# streamChecker.query("c"); // return False
# streamChecker.query("d"); // return True, because 'cd' is in the wordlist
# streamChecker.query("e"); // return False
# streamChecker.query("f"); // return True, because 'f' is in the wordlist
# streamChecker.query("g"); // return False
# streamChecker.query("h"); // return False
# streamChecker.query("i"); // return False
# streamChecker.query("j"); // return False
# streamChecker.query("k"); // return False
# streamChecker.query("l"); // return True, because 'kl' is in the wordlist
# 
# 
# Constraints:
#         1 <= words.length <= 2000
#         1 <= words[i].length <= 200
#         words[i] consists of lowercase English letters.
#         letter is a lowercase English letter.
#         At most 4 * 10⁴ calls will be made to query.


# Solution: https://algo.monster/liteproblems/1032
# Credit: AlgoMonster
from typing import List

class Trie:
    """A trie data structure that stores words in reverse order for suffix matching."""
  
    def __init__(self):
        # Array to store 26 possible children (one for each lowercase letter)
        self.children = [None] * 26
        # Flag to mark if this node represents the end of a word
        self.is_end = False
  
    def insert(self, word: str) -> None:
        """
        Insert a word into the trie in reverse order.
      
        Args:
            word: The word to insert into the trie
        """
        current_node = self
        # Traverse the word in reverse order
        for char in word[::-1]:
            # Calculate the index for this character (0-25)
            index = ord(char) - ord('a')
            # Create a new node if it doesn't exist
            if current_node.children[index] is None:
                current_node.children[index] = Trie()
            # Move to the child node
            current_node = current_node.children[index]
        # Mark the end of the word
        current_node.is_end = True
  
    def search(self, characters: List[str]) -> bool:
        """
        Search if any suffix of the character list matches a word in the trie.
      
        Args:
            characters: List of characters to search
          
        Returns:
            True if any suffix matches a word in the trie, False otherwise
        """
        current_node = self
        # Traverse the characters in reverse order (checking suffixes)
        for char in characters[::-1]:
            # Calculate the index for this character
            index = ord(char) - ord('a')
            # If no matching path exists, return False
            if current_node.children[index] is None:
                return False
            # Move to the child node
            current_node = current_node.children[index]
            # If we've found a complete word, return True
            if current_node.is_end:
                return True
        return False

class StreamChecker:
    """
    A class to check if any suffix of a character stream matches words from a dictionary.
    """
  
    def __init__(self, words: List[str]):
        """
        Initialize the StreamChecker with a list of words.
      
        Args:
            words: List of words to match against the stream
        """
        # Initialize the trie for storing words
        self.trie = Trie()
        # List to store the stream of characters
        self.character_stream = []
        # Maximum number of recent characters to keep (optimization)
        self.max_length = 201
      
        # Insert all words into the trie
        for word in words:
            self.trie.insert(word)
  
    def query(self, letter: str) -> bool:
        """
        Add a letter to the stream and check if any suffix matches a word.
      
        Args:
            letter: The new character to add to the stream
          
        Returns:
            True if any suffix of the stream matches a word, False otherwise
        """
        # Add the new letter to the stream
        self.character_stream.append(letter)
        # Search only the last max_length characters (optimization for memory)
        return self.trie.search(self.character_stream[-self.max_length:])


def main():
    print("TO DO")

if __name__ == "__main__":
    main()
