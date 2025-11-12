# -----------------------------
# 131. Palindrome Partitioning
# -----------------------------

# Problem: https://leetcode.com/problems/palindrome-partitioning
# 
# Given a string s, partition s such that every substring of the partition is a 
# palindrome. Return all possible palindrome partitioning of s.

# Solution: https://youtu.be/3jvWodd7ht0
# Credit: Navdeep Singh founder of NeetCode
def partition(s):
    res, part = [], []

    def dfs(i):
        if i >= len(s):
            res.append(part.copy())
            return
        for j in range(i, len(s)):
            if is_pali(s, i, j):
                part.append(s[i : j + 1])
                dfs(j + 1)
                part.pop()

    dfs(0)
    return res

def is_pali(s, l, r):
    while l < r:
        if s[l] != s[r]:
            return False
        l, r = l + 1, r - 1
    return True


def main():
    result = partition("aab")
    print(result) # [["a","a","b"],["aa","b"]]

    result = partition("a")
    print(result) # [["a"]]

if __name__ == "__main__":
    main()