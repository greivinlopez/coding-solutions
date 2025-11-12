# -------------------------------------------
# 5. Longest Palindromic Substring 🅰 🅱 🅱 🅰
# -------------------------------------------

# Problem: https://leetcode.com/problems/longest-palindromic-substring
#
# Given a string s, return the longest palindromic substring in s.
# 
# Example 1:
# 
# Input: s = "babad"
# Output: "bab"
# 
# Explanation: "aba" is also a valid answer.
# 
# Example 2:
# 
# Input: s = "cbbd"
# Output: "bb"
# 
# Constraints:
#         1 <= s.length <= 1000
#         s consist of only digits and English letters.

# Solution: https://www.youtube.com/watch?v=XYQecbcd6_c
# Credit: Navdeep Singh founder of NeetCode 
def longest_palindrome_alt(s):
    result = ""
    longest = 0
    size = len(s)

    for i in range(size):
        # odd length
        l = r = i
        while l >= 0 and r < size and s[l] == s[r]:
            pal_size = r - l + 1
            if pal_size > longest:
                result = s[l:r+1]
                longest = pal_size
            l -= 1
            r += 1
        # even length
        l, r = i, i+1
        while l >= 0 and r < size and s[l] == s[r]:
            pal_size = r - l + 1
            if pal_size > longest:
                result = s[l:r+1]
                longest = pal_size
            l -= 1
            r += 1
    return result
    # Time: O(n²)
    # Space: O(1)

# Credit: Jeel Gajera -> https://github.com/JeelGajera
def longest_palindrome(s):
    res = ""
    def expand(s,i,j):
        while i >= 0 and  j < len(s) and s[i] == s[j]:
            i -= 1
            j += 1
        return s[i+1:j]

    for i in range(len(s)):
        res = max(res, expand(s,i,i), expand(s,i,i+1), key=len)
    return res
    # Time: O(n²)
    # Space: O(1)


def main():
    result = longest_palindrome("babad") # "bab"
    print(result)
    result = longest_palindrome("cbbd") # "bb"
    print(result)

if __name__ == "__main__":
    main()