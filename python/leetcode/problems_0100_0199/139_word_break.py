# ----------------
# 139. Word Break
# ----------------

# Problem: https://leetcode.com/problems/word-break/
# 
# Given a string s and a dictionary of strings wordDict, return true if s can 
# be segmented into a space-separated sequence of one or more dictionary words.
# 
# Note that the same word in the dictionary may be reused multiple times in 
# the segmentation.

# Solution: https://youtu.be/Sx9NNgInc3A
# Credit: Navdeep Singh founder of NeetCode
def word_break(s, wordDict):
    dp = [False] * (len(s) + 1)
    dp[len(s)] = True

    for i in range(len(s) - 1, -1, -1):
        for w in wordDict:
            if (i + len(w)) <= len(s) and s[i : i + len(w)] == w:
                dp[i] = dp[i + len(w)]
            if dp[i]:
                break

    return dp[0]

def main():
    result = word_break(s = "leetcode", wordDict = ["leet","code"])
    print(result) # True

    result = word_break(s = "applepenapple", wordDict = ["apple","pen"])
    print(result) # True

    result = word_break(s = "catsandog", wordDict = ["cats","dog","sand","and","cat"])
    print(result) # False

if __name__ == "__main__":
    main()