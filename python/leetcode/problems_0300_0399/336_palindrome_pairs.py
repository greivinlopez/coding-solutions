# ---------------------
# 336. Palindrome Pairs
# ---------------------

# Problem: https://leetcode.com/problems/palindrome-pairs
#
# You are given a 0-indexed array of unique strings words.
# 
# A palindrome pair is a pair of integers (i, j) such that:
#   * 0 <= i, j < words.length,
#   * i != j, and
#   * words[i] + words[j] (the concatenation of the two strings) is a palindrome.
# 
# Return an array of all the palindrome pairs of words.
# 
# You must write an algorithm with O(sum of words[i].length) runtime complexity.
# 
# Example 1:
# 
# Input: words = ["abcd","dcba","lls","s","sssll"]
# Output: [[0,1],[1,0],[3,2],[2,4]]
# 
# Explanation: The palindromes are ["abcddcba","dcbaabcd","slls","llssssll"]
# 
# Example 2:
# 
# Input: words = ["bat","tab","cat"]
# Output: [[0,1],[1,0]]
# 
# Explanation: The palindromes are ["battab","tabbat"]
# 
# Example 3:
# 
# Input: words = ["a",""]
# Output: [[0,1],[1,0]]
# 
# Explanation: The palindromes are ["a","a"]
# 
# 
# Constraints:
#         1 <= words.length <= 5000
#         0 <= words[i].length <= 300
#         words[i] consists of lowercase English letters.


# Solution: https://leetcode.com/problems/palindrome-pairs/solutions/1987826/python-trie-solution-explained
# Credit: Bucca Tini -> https://leetcode.com/u/buccatini/
class TrieNode:
    def __init__(self):
        self.children = dict()
        self.end = False
        self.idx = -1
        self.palindromeIdxs = list()

class Solution:
    def __init__(self):
        self.root = TrieNode()
        
    def palindromePairs(self, words):
        res = list()
        
        for i in range(len(words)):
            cur = self.root
            rWord = words[i][::-1]
            for j in range(len(rWord)):
                if self.isPalindrome(rWord[j:]):
                    cur.palindromeIdxs.append(i)
                    
                if rWord[j] not in cur.children:
                    cur.children[rWord[j]] = TrieNode()
                cur = cur.children[rWord[j]]
                
            cur.end = True
            cur.idx = i
            
        for i in range(len(words)):
            self.search(words[i], i, res)
            
        return res
        
    def search(self, word, idx, res):   
        cur = self.root
        for i in range(len(word)):
            if cur.end and self.isPalindrome(word[i:]):
                res.append([idx, cur.idx])
                
            if word[i] not in cur.children:
                return
            cur = cur.children[word[i]]        
        
        if cur.end and cur.idx != idx:
            res.append([cur.idx, idx])
        
        for pIdx in cur.palindromeIdxs:
            res.append([idx, pIdx])
                
        return
            
    def isPalindrome(self, s):
        return s == s[::-1]

# Solution: https://leetcode.com/problems/palindrome-pairs/solutions/2585442/intuitive-python3-hashmap-95-time-space-o-n-w-2
# Credit: Ryan Grayson -> https://leetcode.com/u/ryangrayson/
def palindrome_pairs_alt(words):
    backward, res = {}, []
    for i, word in enumerate(words):
        backward[word[::-1]] = i

    for i, word in enumerate(words):
        
        if word in backward and backward[word] != i:
            res.append([i, backward[word]])
            
        if word != "" and "" in backward and word == word[::-1]:
            res.append([i, backward[""]])
            res.append([backward[""], i])
            
        for j in range(len(word)):
            if word[j:] in backward and word[:j] == word[j-1::-1]:
                res.append([backward[word[j:]], i])
            if word[:j] in backward and word[j:] == word[:j-1:-1]:
                res.append([i, backward[word[:j]]])
                
    return res
    # Time: O(n * k²)
    # Space: O(n * k)
    # n = number of words
    # k = average word length


def main():
    result = palindrome_pairs_alt(words = ["abcd","dcba","lls","s","sssll"])
    print(result) # [[0,1],[1,0],[3,2],[2,4]]

    result = palindrome_pairs_alt(words = ["bat","tab","cat"])
    print(result) # [[0,1],[1,0]]

    result = palindrome_pairs_alt(words = ["a",""])
    print(result) # [[0,1],[1,0]]

if __name__ == "__main__":
    main()
