# --------------------
# 87. Scramble String
# --------------------

# Problem: https://leetcode.com/problems/scramble-string
#
# We can scramble a string s to get a string t using the following algorithm:
#         
#   1. If the length of the string is 1, stop.
#   2. If the length of the string is > 1, do the following:
#       * Split the string into two non-empty substrings at a random
#         index, i.e., if the string is s, divide it to x and y where s = x + y.
#       * Randomly decide to swap the two substrings or to keep them in
#         the same order. i.e., after this step, s may become s = x + y or s = y + x.
#       * Apply step 1 recursively on each of the two substrings x and y.
# 
# Given two strings s1 and s2 of the same length, return true if s2 is a scrambled
# string of s1, otherwise, return false.
# 
# Example 1:
# 
# Input: s1 = "great", s2 = "rgeat"
# Output: true
# 
# Explanation: One possible scenario applied on s1 is:
# "great" --> "gr/eat" // divide at random index.
# "gr/eat" --> "gr/eat" // random decision is not to swap the two substrings and
# keep them in order.
# "gr/eat" --> "g/r / e/at" // apply the same algorithm recursively on both
# substrings. divide at random index each of them.
# "g/r / e/at" --> "r/g / e/at" // random decision was to swap the first substring
# and to keep the second substring in the same order.
# "r/g / e/at" --> "r/g / e/ a/t" // again apply the algorithm recursively, divide
# "at" to "a/t".
# "r/g / e/ a/t" --> "r/g / e/ a/t" // random decision is to keep both substrings
# in the same order.
# The algorithm stops now, and the result string is "rgeat" which is s2.
# As one possible scenario led s1 to be scrambled to s2, we return true.
# 
# Example 2:
# 
# Input: s1 = "abcde", s2 = "caebd"
# Output: false
# 
# Example 3:
# Input: s1 = "a", s2 = "a"
# Output: true
# 
# 
# Constraints:
#         s1.length == s2.length
#         1 <= s1.length <= 30
#         s1 and s2 consist of lowercase English letters.

from collections import Counter
from functools import cache

# Solution: https://leetcode.com/problems/scramble-string/solutions/3219393/scramble-string/comments/1848052/
# Credit: https://leetcode.com/u/vokasik/
def is_scramble(s, t):
    @cache
    def dfs(s1, s2):
        if s1 == s2:
            return True
        if Counter(s1) != Counter(s2):
            return False
        
        N = len(s1)
        for k in range(1, N):
            # gr|eat and rg|tea
            if (dfs(s1[:k], s2[:k]) and dfs(s1[k:], s2[k:]) or
                # gr|eat and tea|gr
                dfs(s1[:k], s2[N - k:]) and dfs(s1[k:], s2[:N - k])):
                return True
        return False       
    return dfs(s,t)
    # Time: O(n⁴)
    # Space: O(n⁴)


def main():
    result = is_scramble("great", "rgeat")
    print(result) # True

    result = is_scramble("abcde", "caebd")
    print(result) # False

    result = is_scramble("a", "a")
    print(result) # True

if __name__ == "__main__":
    main()
