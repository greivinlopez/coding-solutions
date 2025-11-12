# ------------------------------------------------------
# 28. Find the Index of the First Occurrence in a String
# ------------------------------------------------------

# Problem: https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string
#
# Given two strings needle and haystack, return the index of the first occurrence
# of needle in haystack, or -1 if needle is not part of haystack.
# 
# Example 1:
# 
# Input: haystack = "sadbutsad", needle = "sad"
# Output: 0
# 
# Explanation: "sad" occurs at index 0 and 6.
# The first occurrence is at index 0, so we return 0.
# 
# Example 2:
# 
# Input: haystack = "leetcode", needle = "leeto"
# Output: -1
# 
# Explanation: "leeto" did not occur in "leetcode", so we return -1.
# 
# 
# Constraints:
#         1 <= haystack.length, needle.length <= 10⁴
#         haystack and needle consist of only lowercase English characters.


# Solution: https://youtu.be/Gjkhm1gYIMw
# Credit: Navdeep Singh founder of NeetCode 
def str_str(haystack, needle):
    if needle == "":
        return 0
    lps = [0] * len(needle)

    prevLPS, i = 0, 1
    while i < len(needle):
        if needle[i] == needle[prevLPS]:
            lps[i] = prevLPS + 1
            prevLPS += 1
            i += 1
        elif prevLPS == 0:
            lps[i] = 0
            i += 1
        else:
            prevLPS = lps[prevLPS - 1]

    i = 0  # ptr for haystack
    j = 0  # ptr for needle
    while i < len(haystack):
        if haystack[i] == needle[j]:
            i, j = i + 1, j + 1
        else:
            if j == 0:
                i += 1
            else:
                j = lps[j - 1]
        if j == len(needle):
            return i - len(needle)
    return -1
    # Time: O(n + m)
    # Space: O(m)
    # n = length of the haystack string
    # m = length of the needle string

# Alternative Solution
def str_str_alt(haystack, needle):
    if needle == '':
        return 0
    
    for i in range(len(haystack) + 1 - len(needle)):
        if haystack[i: i + len(needle)] == needle:
            return i
    return -1
    # Time: O(n * m)
    # Space: O(m)
    # n = length of the haystack string
    # m = length of the needle string


def main():
    result = str_str_alt(haystack = "sadbutsad", needle = "sad") # 0
    print(result)
    result = str_str_alt(haystack = "leetcode", needle = "leeto") # -1
    print(result)

if __name__ == "__main__":
    main()