# -------------------------------
# 208. Implement Trie Prefix Tree
# -------------------------------

# Problem: https://leetcode.com/problems/implement-trie-prefix-tree/
# 
# A trie (pronounced as "try") or prefix tree is a tree data structure used to 
# efficiently store and retrieve keys in a dataset of strings. There are various 
# applications of this data structure, such as autocomplete and spellchecker.
# 
# Implement the Trie class:
# 
# 	Trie() Initializes the trie object.
# 	void insert(String word) Inserts the string word into the trie.
# 	boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
# 	boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.
# 
#  
# Example 1:
# 
# Input
# ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
# [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
# Output
# [null, null, true, false, true, null, true]
# 
# Explanation
# Trie trie = new Trie();
# trie.insert("apple");
# trie.search("apple");   // return True
# trie.search("app");     // return False
# trie.startsWith("app"); // return True
# trie.insert("app");
# trie.search("app");     // return True
# 
#  
# Constraints:
# 
# 
# 	1 <= word.length, prefix.length <= 2000
# 	word and prefix consist only of lowercase English letters.
# 	At most 3 * 104 calls in total will be made to insert, search, and startsWith.


# Solution: https://youtu.be/oobqoCJlHA0
# Credit: Navdeep Singh founder of NeetCode
class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.end = False

class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        curr = self.root
        for c in word:
            i = ord(c) - ord("a")
            if curr.children[i] is None:
                curr.children[i] = TrieNode()
            curr = curr.children[i]
        curr.end = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        curr = self.root
        for c in word:
            i = ord(c) - ord("a")
            if curr.children[i] is None:
                return False
            curr = curr.children[i]
        return curr.end

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        curr = self.root
        for c in prefix:
            i = ord(c) - ord("a")
            if curr.children[i] is None:
                return False
            curr = curr.children[i]
        return True

# Solution: https://youtu.be/8mhw5WT2x0U
# Credit: Greg Hogg
class Trie:
    def __init__(self):
        self.trie = {}

    def insert(self, word: str) -> None:
        d = self.trie

        for c in word:
            if c not in d:
                d[c] = {}
            d = d[c]

        d['.'] = '.'

    def search(self, word: str) -> bool:
        d = self.trie

        for c in word:
            if c not in d:
                return False
            d = d[c]

        return '.' in d

    def startsWith(self, prefix: str) -> bool:
        d = self.trie

        for c in prefix:
            if c not in d:
                return False
            d = d[c]

        return True

def main():
    print("TO DO")

if __name__ == "__main__":
    main()
