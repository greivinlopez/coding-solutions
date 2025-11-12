# -----------------------------------------------------
# 2486. Append Characters to String to Make Subsequence
# -----------------------------------------------------

# Problem: https://leetcode.com/problems/append-characters-to-string-to-make-subsequence
#
# You are given two strings s and t consisting of only lowercase English letters.
# 
# Return the minimum number of characters that need to be appended to the end of s
# so that t becomes a subsequence of s.
# 
# A subsequence is a string that can be derived from another string by deleting
# some or no characters without changing the order of the remaining characters.
# 
# Example 1:
# 
# Input: s = "coaching", t = "coding"
# Output: 4
# 
# Explanation: Append the characters "ding" to the end of s so that s =
# "coachingding".
# Now, t is a subsequence of s ("coachingding").
# It can be shown that appending any 3 characters to the end of s will never make
# t a subsequence.
# 
# Example 2:
# 
# Input: s = "abcde", t = "a"
# Output: 0
# 
# Explanation: t is already a subsequence of s ("abcde").
# 
# Example 3:
# 
# Input: s = "z", t = "abcde"
# Output: 5
# 
# Explanation: Append the characters "abcde" to the end of s so that s = "zabcde".
# Now, t is a subsequence of s ("zabcde").
# It can be shown that appending any 4 characters to the end of s will never make
# t a subsequence.
# 
# 
# Constraints:
#         1 <= s.length, t.length <= 10⁵
#         s and t consist only of lowercase English letters.


# Solution: https://youtu.be/gKDmO8ZLRD8
# Credit: Navdeep Singh founder of NeetCode
def append_characters(s, t):
    i, j = 0, 0

    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i, j = i + 1, j + 1
        else:
            i += 1

    return len(t) - j
    # Time: O(n + m)
    # Space: O(1)


def main():
    result = append_characters(s = "coaching", t = "coding")
    print(result) # 4

    result = append_characters(s = "abcde", t = "a")
    print(result) # 0

    result = append_characters(s = "z", t = "abcde")
    print(result) # 5

if __name__ == "__main__":
    main()
