# --------------------------
# 1397. Find All Good Strings
# --------------------------

# Problem: https://leetcode.com/problems/find-all-good-strings
#
# Given the strings s1 and s2 of size n and the string evil, return the number of
# good strings.
# A good string has size n, it is alphabetically greater than or equal to s1, it
# is alphabetically smaller than or equal to s2, and it does not contain the
# string evil as a substring. Since the answer can be a huge number, return this
# modulo 109 + 7.
# Example 1:
# Input: n = 2, s1 = "aa", s2 = "da", evil = "b"
# Output: 51
# Explanation: There are 25 good strings starting with 'a':
# "aa","ac","ad",...,"az". Then there are 25 good strings starting with 'c':
# "ca","cc","cd",...,"cz" and finally there is one good string starting with 'd':
# "da". 
# Example 2:
# Input: n = 8, s1 = "leetcode", s2 = "leetgoes", evil = "leet"
# Output: 0
# Explanation: All strings greater than or equal to s1 and smaller than or equal
# to s2 start with the prefix "leet", therefore, there is not any good string.
# Example 3:
# Input: n = 2, s1 = "gx", s2 = "gz", evil = "x"
# Output: 2
# Constraints:
#         s1.length == n
#         s2.length == n
#         s1 <= s2
#         1 <= n <= 500
#         1 <= evil.length <= 50
#         All strings consist of lowercase English letters.

from functools import cache

# Solution: 
# Credit: Navdeep Singh founder of NeetCode
def find_good_strings(n, s1, s2, evil):
    a = ord('a')
    z = ord('z')
    
    arr_e = list(map(ord, evil))
    len_e = len(evil)
    next = [0] * len_e

    for i in range(1, len_e):
        j = next[i - 1]
        while j > 0 and evil[i] != evil[j]:
            j = next[j - 1]
        if evil[i] == evil[j]:
            next[i] = j + 1

    def good(s):
        arr = list(map(ord, s))
        len_a = len(arr)

        @cache
        def f(i, skip, reach, e):
            if e == len_e:
                return 0
            if i == len_a:
                return 0 if skip else 1

            limit = arr[i] if reach else z
            ans = 0

            if skip:
                ans += f(i + 1, True, False, 0)

            for c in range(a, limit + 1):
                ee = e
                while ee > 0 and arr_e[ee] != c:
                    ee = next[ee - 1] 

                if arr_e[ee] == c:
                    ee += 1

                ans += f(i + 1, False, reach and c == limit, ee)

            return ans % int(1e9 + 7)

        return f(0, True, True, 0)

    return (good(s2) - good(s1) + int(evil not in s1)) % int(1e9 + 7)


def main():
    result = find_good_strings(n = 2, s1 = "aa", s2 = "da", evil = "b")
    print(result) # 51

    result = find_good_strings(n = 8, s1 = "leetcode", s2 = "leetgoes", evil = "leet")
    print(result) # 0

    result = find_good_strings(n = 2, s1 = "gx", s2 = "gz", evil = "x")
    print(result) # 2

if __name__ == "__main__":
    main()
