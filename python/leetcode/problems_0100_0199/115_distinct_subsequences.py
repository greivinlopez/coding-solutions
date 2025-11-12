# --------------------------
# 115. Distinct Subsequences
# --------------------------

# Problem: https://leetcode.com/problems/merge-sorted-array/
# 
# Given two strings s and t, return the number of distinct subsequences of s
# which equals t.
# 
# The test cases are generated so that the answer fits on a 32-bit signed integer.

# Solution: https://youtu.be/-RDzMJ33nx8
# Credit: Navdeep Singh founder of NeetCode
def num_distinct(s, t):
    cache = {}

    for i in range(len(s) + 1):
        cache[(i, len(t))] = 1
    for j in range(len(t)):
        cache[(len(s), j)] = 0

    for i in range(len(s) - 1, -1, -1):
        for j in range(len(t) - 1, -1, -1):
            if s[i] == t[j]:
                cache[(i, j)] = cache[(i + 1, j + 1)] + cache[(i + 1, j)]
            else:
                cache[(i, j)] = cache[(i + 1, j)]
    return cache[(0, 0)]


def main():
    result = num_distinct(s = "rabbbit", t = "rabbit")
    print(result) # 3

    result = num_distinct(s = "babgbag", t = "bag")
    print(result) # 5

if __name__ == "__main__":
    main()