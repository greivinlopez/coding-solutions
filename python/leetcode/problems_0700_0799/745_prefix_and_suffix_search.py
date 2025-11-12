# -----------------------------
# 745. Prefix And Suffix Search
# -----------------------------

# Problem: https://leetcode.com/problems/prefix-and-suffix-search/
# 
# Design a special dictionary that searches the words in it by a prefix and 
# a suffix.
# 
# Implement the WordFilter class:
# 
#   * WordFilter(string[] words) Initializes the object with the words in the 
#   dictionary.
#   
#   * f(string pref, string suff) Returns the index of the word in the dictionary, 
#     which has the prefix pref and the suffix suff. If there is more than one valid 
#     index, return the largest of them. If there is no such word in the dictionary, 
#     return -1.
#  
# Example 1:
# 
# Input
# ["WordFilter", "f"]
# [[["apple"]], ["a", "e"]]
# Output
# [null, 0]
# Explanation
# WordFilter wordFilter = new WordFilter(["apple"]);
# wordFilter.f("a", "e"); // return 0, because the word at index 0 has prefix = "a" and suffix = "e".
#  
# 
# Constraints:
# 
# 1 <= words.length <= 10^4
# 1 <= words[i].length <= 7
# 1 <= pref.length, suff.length <= 7
# words[i], pref and suff consist of lowercase English letters only.
# At most 10^4 calls will be made to the function f.


# Solution: Not video found
# Credit: Navdeep Singh founder of NeetCode
class TrieNode:
    def __init__(self):
        self.children = {}  # Dictionary to store child nodes
        self.word = -1  # Store the index of the word at this node


class WordFilter:
    def __init__(self, words: List[str]):
        # Initialize root of the Trie
        self.root = TrieNode()

        # For each word, we create combined prefix-suffix keys
        for index, word in enumerate(words):
            # Insert all combinations of the form prefix{suffix into the Trie
            for i in range(len(word) + 1):
                for j in range(len(word) + 1):
                    # Create the key as suffix + '{' + prefix
                    key = word[i:] + '{' + word[:j]
                    cur = self.root
                    for c in key:
                        if c not in cur.children:
                            cur.children[c] = TrieNode()
                        cur = cur.children[c]
                    cur.word = index  # Store the index of the word at this node

    def f(self, pref: str, suff: str) -> int:
        # Combine suffix and prefix to search in Trie
        key = suff + '{' + pref
        cur = self.root
        for c in key:
            if c not in cur.children:
                return -1  # If combination doesn't exist, return -1
            cur = cur.children[c]
        return cur.word  # Return the largest index found for the valid combination


def main():
    print("TO DO")

if __name__ == "__main__":
    main()
