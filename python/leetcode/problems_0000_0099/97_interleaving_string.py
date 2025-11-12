# ----------------------------
# 97. Interleaving String
# ----------------------------

# Problem: https://leetcode.com/problems/interleaving-string/
# 
# Given strings s1, s2, and s3, find whether s3 is formed by an interleaving 
# of s1 and s2.
# 
# An interleaving of two strings s and t is a configuration where s and t are 
# divided into n and m substrings respectively, such that:
# 
# s = s1 + s2 + ... + sn
# t = t1 + t2 + ... + tm
# |n - m| <= 1
# The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 + t3 + s3 + ...
# 
# Note: a + b is the concatenation of strings a and b.

# Solution: https://youtu.be/RF_M9tX4Eag
# Credit: Navdeep Singh founder of NeetCode
def is_interleave(s1, s2, s3):
    # Time: O(n * m)
    if len(s1) + len(s2) != len(s3):
        return False

    dp = [[False] * (len(s2) + 1) for i in range(len(s1) + 1)]
    dp[len(s1)][len(s2)] = True

    for i in range(len(s1), -1, -1):
        for j in range(len(s2), -1, -1):
            if i < len(s1) and s1[i] == s3[i + j] and dp[i + 1][j]:
                dp[i][j] = True
            if j < len(s2) and s2[j] == s3[i + j] and dp[i][j + 1]:
                dp[i][j] = True
    return dp[0][0]


def main():
    result = is_interleave(s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac")
    print(result) # True

    result = is_interleave(s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc")
    print(result) # False

    result = is_interleave(s1 = "", s2 = "", s3 = "")
    print(result) # True

if __name__ == "__main__":
    main()