# ---------------------------------------------------------
# 1347. Minimum Number of Steps to Make Two Strings Anagram
# ---------------------------------------------------------

# Problem: https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram
#
# You are given two strings of the same length s and t. In one step you can choose
# any character of t and replace it with another character.
# 
# Return the minimum number of steps to make t an anagram of s.
# 
# An Anagram of a string is a string that contains the same characters with a
# different (or the same) ordering.
# 
# Example 1:
# 
# Input: s = "bab", t = "aba"
# Output: 1
# 
# Explanation: Replace the first 'a' in t with b, t = "bba" which is anagram of s.
# 
# Example 2:
# 
# Input: s = "leetcode", t = "practice"
# Output: 5
# 
# Explanation: Replace 'p', 'r', 'a', 'i' and 'c' from t with proper characters to
# make t anagram of s.
# 
# Example 3:
# 
# Input: s = "anagram", t = "mangaar"
# Output: 0
# 
# Explanation: "anagram" and "mangaar" are anagrams.
# 
# 
# Constraints:
#         1 <= s.length <= 5 * 10⁴
#         s.length == t.length
#         s and t consist of lowercase English letters only.

from collections import Counter, defaultdict

# Credit: Jeel Gajera -> https://github.com/JeelGajera
def min_steps(s, t):
    f1 = defaultdict(int)
    f2 = defaultdict(int)
    res = 0
    n = len(s)

    for i in range(n):
        f1[s[i]] += 1
        f2[t[i]] += 1

    for i in set(t):
        diff = f2[i] - f1.get(i, 0)
        if diff > 0:
            res += diff

    return res
    # Time: O(n)
    # Space: O(1)

# Credit: Jaweria Batool -> https://github.com/Jaweria-B
def min_steps_alt(s, t):
    return sum((Counter(s) - Counter(t)).values())
    # Time: O(n)
    # Space: O(1)


def main():
    result = min_steps(s = "bab", t = "aba")
    print(result) # 1

    result = min_steps(s = "leetcode", t = "practice")
    print(result) # 5

    result = min_steps(s = "anagram", t = "mangaar")
    print(result) # 0

if __name__ == "__main__":
    main()
