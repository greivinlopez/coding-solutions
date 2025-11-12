# -------------------------------------------------
# 3. Longest Substring Without Repeating Characters
# -------------------------------------------------

# Problem: https://leetcode.com/problems/longest-substring-without-repeating-characters
#
# Given a string s, find the length of the longest substring without duplicate
# characters.
# 
# Example 1:
# 
# Input: s = "abcabcbb"
# Output: 3
# 
# Explanation: The answer is "abc", with the length of 3.
# 
# Example 2:
# 
# Input: s = "bbbbb"
# Output: 1
# 
# Explanation: The answer is "b", with the length of 1.
# 
# Example 3:
# 
# Input: s = "pwwkew"
# Output: 3
# 
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a
# substring.
# 
# 
# Constraints:
#       0 <= s.length <= 5 * 10⁴
#       s consists of English letters, digits, symbols and spaces.

from collections import deque

# Solution: https://youtu.be/wiGpQwVHdE0
# Credit: Navdeep Singh founder of NeetCode 
def length_of_longest_substring(s):
    charSet = set()
    l = 0
    res = 0

    for r in range(len(s)):
        while s[r] in charSet:
            charSet.remove(s[l])
            l += 1
        charSet.add(s[r])
        res = max(res, r - l + 1)
    return res
    # Time: O(n)
    # Space: O(1)

# Solution: https://youtu.be/FCbOzdHKW18
# Credit: Greg Hogg
def length_of_longest_substring_alt(s):
    l = 0
    longest = 0
    sett = set()
    n = len(s)

    for r in range(n):
        while s[r] in sett:
            sett.remove(s[l])
            l += 1

        w = (r - l) + 1
        longest = max(longest, w)
        sett.add(s[r])

    return longest
    # Time: O(n)
    # Space: O(1)

# Credit: Jeel Gajera -> https://github.com/JeelGajera
def length_of_longest_substring_alt_2(s):
    res = 0
    q = deque()
    for c in s:
        if c in q:
            while q.popleft() != c:
                pass
        q.append(c)
        res = max(res, len(q))
    return res
    # Time: O(n)
    # Space: O(1)


def main():
    result = length_of_longest_substring("abcabcbb") # 3
    print(result)
    result = length_of_longest_substring("bbbbb") # 1
    print(result)
    result = length_of_longest_substring("pwwkew") # 3
    print(result)

if __name__ == "__main__":
    main()