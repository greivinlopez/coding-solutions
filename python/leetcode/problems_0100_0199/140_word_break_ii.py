# -------------------
# 140. Word Break II
# -------------------

# Problem: https://leetcode.com/problems/word-break-ii/
# 
# Given a string s and a dictionary of strings wordDict, add spaces in s to 
# construct a sentence where each word is a valid dictionary word. Return 
# all such possible sentences in any order.
# 
# Note that the same word in the dictionary may be reused multiple times in 
# the segmentation.

# Solution: https://youtu.be/QgLKdluDo08
# Credit: Navdeep Singh founder of NeetCode
def word_break(s, wordDict):
    wordDict = set(wordDict)
    cache = {}

    def backtrack(i):
        if i == len(s):
            return ['']
        if i in cache:
            return cache[i]
        
        res = []
        for j in range(i, len(s)):
            w = s[i:j+1]
            if w not in wordDict:
                continue
            strings = backtrack(j + 1)
            if not strings:
                continue
            for substr in strings:
                sentence = w
                if substr:
                    sentence += ' ' + substr
                res.append(sentence)
        cache[i] = res
        return res
    return backtrack(0)

def main():
    result = word_break(s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"])
    print(result) # ["cats and dog","cat sand dog"]

    result = word_break(s = "pineapplepenapple", wordDict = ["apple","pen","applepen","pine","pineapple"])
    print(result) # ["pine apple pen apple","pineapple pen apple","pine applepen apple"]

    result = word_break(s = "catsandog", wordDict = ["cats","dog","sand","and","cat"])
    print(result) # []

if __name__ == "__main__":
    main()