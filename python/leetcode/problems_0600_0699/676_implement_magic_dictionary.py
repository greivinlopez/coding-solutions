# -------------------------------
# 676. Implement Magic Dictionary
# -------------------------------

# Problem: https://leetcode.com/problems/implement-magic-dictionary
#
# Design a data structure that is initialized with a list of different words.
# Provided a string, you should determine if you can change exactly one character
# in this string to match any word in the data structure.
# 
# Implement the MagicDictionary class:
#         
#   * MagicDictionary() Initializes the object.
#   * void buildDict(String[] dictionary) Sets the data structure with an array of 
#     distinct strings dictionary.
#   * bool search(String searchWord) Returns true if you can change exactly one 
#     character in searchWord to match any string in the data structure, otherwise
#     returns false.
# 
# Example 1:
# 
# Input
# ["MagicDictionary", "buildDict", "search", "search", "search", "search"]
# [[], [["hello", "leetcode"]], ["hello"], ["hhllo"], ["hell"], ["leetcoded"]]
# Output
# [null, null, false, true, false, false]
# 
# Explanation
# MagicDictionary magicDictionary = new MagicDictionary();
# magicDictionary.buildDict(["hello", "leetcode"]);
# magicDictionary.search("hello"); // return False
# magicDictionary.search("hhllo"); // We can change the second 'h' to 'e' to match
# "hello" so we return True
# magicDictionary.search("hell"); // return False
# magicDictionary.search("leetcoded"); // return False
# 
# 
# Constraints:
#         1 <= dictionary.length <= 100
#         1 <= dictionary[i].length <= 100
#         dictionary[i] consists of only lower-case English letters.
#         All the strings in dictionary are distinct.
#         1 <= searchWord.length <= 100
#         searchWord consists of only lower-case English letters.
#         buildDict will be called only once before search.
#         At most 100 calls will be made to search.


# Solution: https://algo.monster/liteproblems/676
# Credit: AlgoMonster
from typing import List, Dict

class Trie:
    """Trie (prefix tree) data structure with support for fuzzy search."""
  
    __slots__ = ["children", "is_end"]
  
    def __init__(self) -> None:
        """Initialize an empty trie node."""
        self.children: Dict[str, 'Trie'] = {}
        self.is_end: bool = False
  
    def insert(self, word: str) -> None:
        """
        Insert a word into the trie.
      
        Args:
            word: The word to insert into the trie
        """
        current_node = self
        for char in word:
            if char not in current_node.children:
                current_node.children[char] = Trie()
            current_node = current_node.children[char]
        current_node.is_end = True
  
    def search(self, word: str) -> bool:
        """
        Search for a word that differs by exactly one character.
      
        Args:
            word: The word to search for (with one character difference)
          
        Returns:
            True if a word exists that differs by exactly one character, False otherwise
        """
        def dfs(index: int, node: 'Trie', difference_count: int) -> bool:
            """
            Depth-first search to find a word with exactly one character difference.
          
            Args:
                index: Current position in the search word
                node: Current trie node
                difference_count: Number of character differences found so far
              
            Returns:
                True if a valid word with exactly one difference is found
            """
            # Base case: reached end of search word
            if index == len(word):
                return difference_count == 1 and node.is_end
          
            # Try to continue with the same character (no difference)
            if word[index] in node.children and dfs(index + 1, node.children[word[index]], difference_count):
                return True
          
            # Try to use a different character (add one difference)
            # Only allowed if we haven't used our one difference yet
            return difference_count == 0 and any(
                dfs(index + 1, node.children[char], 1) 
                for char in node.children 
                if char != word[index]
            )
      
        return dfs(0, self, 0)

class MagicDictionary:
    """
    A dictionary that supports searching for words with exactly one character modification.
    """
  
    def __init__(self) -> None:
        """Initialize an empty MagicDictionary."""
        self.trie = Trie()
  
    def buildDict(self, dictionary: List[str]) -> None:
        """
        Build the dictionary from a list of words.
      
        Args:
            dictionary: List of words to add to the dictionary
        """
        for word in dictionary:
            self.trie.insert(word)
  
    def search(self, searchWord: str) -> bool:
        """
        Search if there exists any word in the dictionary that differs 
        by exactly one character from the search word.
      
        Args:
            searchWord: The word to search for (with one character modification)
          
        Returns:
            True if such a word exists in the dictionary, False otherwise
        """
        return self.trie.search(searchWord)


def main():
    print("TO DO")

if __name__ == "__main__":
    main()
