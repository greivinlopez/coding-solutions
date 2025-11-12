# ------------------
# 242. Valid Anagram
# ------------------

# Problem: https://leetcode.com/problems/valid-anagram/
# 
# Given two strings s and t, return true if t is an anagram of s, and false 
# otherwise.
# 
#  
# Example 1:
# 
# Input: s = "anagram", t = "nagaram"
# 
# Output: true
# 
# 
# Example 2:
# 
# Input: s = "rat", t = "car"
# 
# Output: false
# 
# 
# Constraints:
# 
# 	1 <= s.length, t.length <= 5 * 104
# 	s and t consist of lowercase English letters.
# 
# Follow up: What if the inputs contain Unicode characters? How would you adapt 
# your solution to such a case?


# Solution: https://youtu.be/9UtInBqnCgA
# Credit: Navdeep Singh founder of NeetCode
def is_anagram(s, t):
    if len(s) != len(t):
        return False

    countS, countT = {}, {}

    for i in range(len(s)):
        countS[s[i]] = 1 + countS.get(s[i], 0)
        countT[t[i]] = 1 + countT.get(t[i], 0)
    return countS == countT

# easier solution
#return True if sorted(s) == sorted(t) else False

# Solution: https://youtu.be/_cCTcPQik6A
# Credit: Greg Hogg
from collections import Counter
def is_anagram_alt(s, t):
    if len(s) != len(t):
        return False

    s_dict = Counter(s)
    t_dict = Counter(t)

    return s_dict == t_dict
    # Let n be the length of the longest word
    # Time complexity: O(n)
    # Space complexity: O(n)

def main():
    result = is_anagram(s = "anagram", t = "nagaram")
    print(result) # True

    result = is_anagram(s = "rat", t = "car")
    print(result) # False

if __name__ == "__main__":
    main()
