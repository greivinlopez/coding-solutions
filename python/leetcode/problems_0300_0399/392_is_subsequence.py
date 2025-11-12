# -------------------
# 392. Is Subsequence
# -------------------

# Problem: https://leetcode.com/problems/is-subsequence/
# 
# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
# 
# A subsequence of a string is a new string that is formed from the original string by 
# deleting some (can be none) of the characters without disturbing the relative 
# positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while 
# "aec" is not).
# 
#  
# Example 1:
# Input: s = "abc", t = "ahbgdc"
# Output: true
# Example 2:
# Input: s = "axc", t = "ahbgdc"
# Output: false
# 
#  
# Constraints:
# 
# 	0 <= s.length <= 100
# 	0 <= t.length <= 104
# 	s and t consist only of lowercase English letters.
# 
# Follow up: Suppose there are lots of incoming s, say s1, s2, ..., sk where k >= 109, 
# and you want to check one by one to see if t has its subsequence. In this scenario, 
# how would you change your code?


# Solution: https://youtu.be/99RVfqklbCE
# Credit: Navdeep Singh founder of NeetCode
def is_subsequence(s, t):
    i, j = 0, 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
        j += 1
    return i == len(s)

# Solution: https://youtu.be/M_OB20n4hfo
# Credit: Greg Hogg
def is_subsequence_alt(s, t):
    S = len(s)
    T = len(t)
    if s == '': return True
    if S > T: return False

    j = 0
    for i in range(T):
        if t[i] == s[j]:
            if j == S-1:
                return True
            j += 1
    
    return False
    # Time: O(T)
    # Space: O(1)

def main():
    result = is_subsequence(s = "abc", t = "ahbgdc")
    print(result) # True

    result = is_subsequence(s = "axc", t = "ahbgdc")
    print(result) # False

if __name__ == "__main__":
    main()
