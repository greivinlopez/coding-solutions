# -------------------------------
# 1143. Longest Common Subsequence
# -------------------------------

# Problem: https://leetcode.com/problems/longest-common-subsequence
#
# Given two strings text1 and text2, return the length of their longest common
# subsequence. If there is no common subsequence, return 0.
# 
# A subsequence of a string is a new string generated from the original string
# with some characters (can be none) deleted without changing the relative order
# of the remaining characters.
# 
#         For example, "ace" is a subsequence of "abcde".
# 
# A common subsequence of two strings is a subsequence that is common to both
# strings.
# 
# Example 1:
# 
# Input: text1 = "abcde", text2 = "ace"
# Output: 3
# Explanation: The longest common subsequence is "ace" and its length is 3.
# 
# Example 2:
# 
# Input: text1 = "abc", text2 = "abc"
# 
# Output: 3
# 
# Explanation: The longest common subsequence is "abc" and its length is 3.
# Example 3:
# Input: text1 = "abc", text2 = "def"
# Output: 0
# Explanation: There is no such common subsequence, so the result is 0.
# 
# 
# Constraints:
#         1 <= text1.length, text2.length <= 1000
#         text1 and text2 consist of only lowercase English characters.


# Solution: https://youtu.be/Ua0GhsJSlWM
# Credit: Navdeep Singh founder of NeetCode
def longest_common_subsequence(text1, text2):
    dp = [[0 for j in range(len(text2) + 1)] for i in range(len(text1) + 1)]

    for i in range(len(text1) - 1, -1, -1):
        for j in range(len(text2) - 1, -1, -1):
            if text1[i] == text2[j]:
                dp[i][j] = 1 + dp[i + 1][j + 1]
            else:
                dp[i][j] = max(dp[i][j + 1], dp[i + 1][j])

    return dp[0][0]
    # Time: O(m*n)
    # Space: O(m*n)


# Solution: https://youtu.be/MNykgz1_ONQ
# Credit: Greg Hogg
from functools import cache
def longest_common_subsequence_memo(text1, text2):
    # Top Down DP (Memoization)
    m, n = len(text1), len(text2)

    @cache
    def longest(i, j):
        if i == m or j == n:
            return 0
        elif text1[i] == text2[j]:
            return 1 + longest(i+1, j+1)
        else:
            return max(longest(i, j+1), longest(i+1, j))
    
    return longest(0, 0)
    # Time: O(m*n)
    # Space: O(m*n)
    
# Same as Navdeep's
def longest_common_subsequence_dp(text1, text2):
    # Bottom Up DP (Tabulation)
    m, n = len(text1), len(text2)
    dp = [[0] * (n+1) for _ in range(m + 1)]

    for i in range(1, m+1):
        for j in range(1, n+1):
            if text1[i-1] == text2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    return dp[m][n]
    # Time: O(m*n)
    # Space: O(m*n)

def main():
    result = longest_common_subsequence(text1 = "abcde", text2 = "ace")
    print(result) # 3

    result = longest_common_subsequence(text1 = "abc", text2 = "abc")
    print(result) # 3

    result = longest_common_subsequence(text1 = "abc", text2 = "def")
    print(result) # 0

if __name__ == "__main__":
    main()
