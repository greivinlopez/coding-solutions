# ----------------------
# 44. Wildcard Matching
# ----------------------

# Problem: https://leetcode.com/problems/wildcard-matching/
# Given an input string (s) and a pattern (p), implement wildcard pattern 
# matching with support for '?' and '*' where:
# 
# - '?' Matches any single character.
# - '*' Matches any sequence of characters (including the empty sequence).
# 
# The matching should cover the entire input string (not partial).

# Solution: https://youtu.be/FJJavs1tyoQ
# Credit: "Professor Oakes"
def is_match(s, p):
    dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
    dp[-1][-1] = True
    for i in range(len(s), -1, -1):
        for j in range(len(p) - 1, -1, -1):
            if p[j] == '*':
                dp[i][j] = dp[i][j + 1] or (i < len(s) and dp[i + 1][j])
            else:
                dp[i][j] = i < len(s) and (p[j] == s[i] or p[j] == '?') and dp[i + 1][j + 1]
    return dp[0][0]

def main():
    result = is_match(s = "aa", p = "a") # False
    print(result)
    result = is_match(s = "aa", p = "*") # True
    print(result)
    result = is_match(s = "cb", p = "?a") # False
    print(result)

if __name__ == "__main__":
    main()