# ---------------------------
# 691. Stickers to Spell Word
# ---------------------------

# Problem: https://leetcode.com/problems/stickers-to-spell-word
#
# We are given n different types of stickers. Each sticker has a lowercase English
# word on it.
# 
# You would like to spell out the given string target by cutting individual
# letters from your collection of stickers and rearranging them. You can use each
# sticker more than once if you want, and you have infinite quantities of each
# sticker.
# 
# Return the minimum number of stickers that you need to spell out target. If the
# task is impossible, return -1.
# 
# Note: In all test cases, all words were chosen randomly from the 1000 most
# common US English words, and target was chosen as a concatenation of two random
# words.
# 
# Example 1:
# 
# Input: stickers = ["with","example","science"], target = "thehat"
# Output: 3
# 
# Explanation:
# We can use 2 "with" stickers, and 1 "example" sticker.
# After cutting and rearrange the letters of those stickers, we can form the
# target "thehat".
# Also, this is the minimum number of stickers necessary to form the target
# string.
# 
# Example 2:
# 
# Input: stickers = ["notice","possible"], target = "basicbasic"
# Output: -1
# 
# Explanation:
# We cannot form the target "basicbasic" from cutting letters from the given
# stickers.
# 
# 
# Constraints:
#         n == stickers.length
#         1 <= n <= 50
#         1 <= stickers[i].length <= 10
#         1 <= target.length <= 15
#         stickers[i] and target consist of lowercase English letters.


# Solution: https://youtu.be/hsomLb6mUdI
# Credit: Navdeep Singh founder of NeetCode
def min_stickers(stickers, target):
    stickCount = []
    for i, s in enumerate(stickers):
        stickCount.append({})
        for c in s:
            stickCount[i][c] = 1 + stickCount[i].get(c, 0)
    
    dp = {}  # key = subseq of target | val = min num of stickers
    def dfs(t, stick):
        if t in dp:
            return dp[t]
        
        res = 1 if stick else 0
        remainT = ""
        for c in t:
            if c in stick and stick[c] > 0:
                stick[c] -= 1
            else:
                remainT += c
        
        if remainT:
            used = float("inf")
            
            for s in stickCount:
                if remainT[0] not in s:
                    continue
                used = min(used, dfs(remainT, s.copy()))
            dp[remainT] = used
            res += used
        return res
    
    res = dfs(target, {})
    return res if res != float("inf") else -1
    # Time: O(2^n * s * c)
    # Space: O(2^n * n + s * a)
    # n = length of the target string
    # s = number of stickers
    # c = number of unique characters in the target string
    # a = 26 = total number of lowercase English letters


def main():
    result = min_stickers(stickers = ["with","example","science"], target = "thehat")
    print(result) # 3

    result = min_stickers(stickers = ["notice","possible"], target = "basicbasic")
    print(result) # -1

if __name__ == "__main__":
    main()
