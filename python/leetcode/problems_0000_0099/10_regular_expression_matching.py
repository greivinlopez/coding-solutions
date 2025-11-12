# -------------------------------
# 10. Regular Expression Matching
# -------------------------------

# Problem: https://leetcode.com/problems/regular-expression-matching
#
# Given an input string s and a pattern p, implement regular expression matching
# with support for '.' and '*' where:
#         
#   '.' Matches any single character.​​​​
#   '*' Matches zero or more of the preceding element.
# 
# The matching should cover the entire input string (not partial).
# 
# Example 1:
# 
# Input: s = "aa", p = "a"
# Output: false
# 
# Explanation: "a" does not match the entire string "aa".
# 
# Example 2:
# 
# Input: s = "aa", p = "a*"
# Output: true
# 
# Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by
# repeating 'a' once, it becomes "aa".
# 
# Example 3:
# 
# Input: s = "ab", p = ".*"
# Output: true
# 
# Explanation: ".*" means "zero or more (*) of any character (.)".
# 
# 
# Constraints:
#         1 <= s.length <= 20
#         1 <= p.length <= 20
#         s contains only lowercase English letters.
#         p contains only lowercase English letters, '.', and '*'.
#         It is guaranteed for each appearance of the character '*', there will be
# a previous valid character to match.


# Solution: https://youtu.be/HAA8mgxlov8
# Credit: Navdeep Singh founder of NeetCode 

# BOTTOM-UP Dynamic Programming
def is_match(s, p):
    cache = [[False] * (len(p) + 1) for i in range(len(s) + 1)]
    cache[len(s)][len(p)] = True

    for i in range(len(s), -1, -1):
        for j in range(len(p) - 1, -1, -1):
            match = i < len(s) and (s[i] == p[j] or p[j] == ".")

            if (j + 1) < len(p) and p[j + 1] == "*":
                cache[i][j] = cache[i][j + 2]
                if match:
                    cache[i][j] = cache[i + 1][j] or cache[i][j]
            elif match:
                cache[i][j] = cache[i + 1][j + 1]

    return cache[0][0]
    # Time: O(m * n)
    # Space: O(m * n)
    # m = length of string s
    # n = length of the pattern p

# TOP DOWN MEMOIZATION
def is_match_alt(s, p):
    cache = {}

    def dfs(i, j):
        if (i, j) in cache:
            return cache[(i, j)]
        if i >= len(s) and j >= len(p):
            return True
        if j >= len(p):
            return False

        match = i < len(s) and (s[i] == p[j] or p[j] == ".")
        if (j + 1) < len(p) and p[j + 1] == "*":
            cache[(i, j)] = dfs(i, j + 2) or (  # dont use *
                match and dfs(i + 1, j)
            )  # use *
            return cache[(i, j)]
        if match:
            cache[(i, j)] = dfs(i + 1, j + 1)
            return cache[(i, j)]
        cache[(i, j)] = False
        return False

    return dfs(0, 0)
    # Time: O(m * n)
    # Space: O(m * n)
    # m = length of string s
    # n = length of the pattern p


def main():
    result = is_match(s = "aa", p = "a") # False
    print(result)
    result = is_match(s = "aa", p = "a*") # True
    print(result)
    result = is_match(s = "ab", p = ".*") # True
    print(result)

if __name__ == "__main__":
    main()