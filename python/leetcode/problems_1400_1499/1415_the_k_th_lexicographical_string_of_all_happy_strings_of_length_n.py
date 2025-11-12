# ----------------------------------------------------------------------
# 1415. The k-th Lexicographical String of All Happy Strings of Length n
# ----------------------------------------------------------------------

# Problem: https://leetcode.com/problems/the-k-th-lexicographical-string-of-all-happy-strings-of-length-n
#
# A happy string is a string that:
# 
#   * consists only of letters of the set ['a', 'b', 'c'].
#   * s[i] != s[i + 1] for all values of i from 1 to s.length - 1 (string is
#     1-indexed).
# 
# For example, strings "abc", "ac", "b" and "abcbabcbcb" are all happy strings and
# strings "aa", "baa" and "ababbc" are not happy strings.
# 
# Given two integers n and k, consider a list of all happy strings of length n
# sorted in lexicographical order.
# 
# Return the kth string of this list or return an empty string if there are less
# than k happy strings of length n.
# 
# Example 1:
# 
# Input: n = 1, k = 3
# Output: "c"
# 
# Explanation: The list ["a", "b", "c"] contains all happy strings of length 1.
# The third string is "c".
# 
# Example 2:
# 
# Input: n = 1, k = 4
# Output: ""
# 
# Explanation: There are only 3 happy strings of length 1.
# 
# Example 3:
# 
# Input: n = 3, k = 9
# Output: "cab"
# 
# Explanation: There are 12 different happy string of length 3 ["aba", "abc",
# "aca", "acb", "bab", "bac", "bca", "bcb", "cab", "cac", "cba", "cbc"]. You will
# find the 9th string = "cab"
# 
# 
# Constraints:
#         1 <= n <= 10
#         1 <= k <= 100


# Solution: https://youtu.be/tRwXzsXJArI
# Credit: Navdeep Singh founder of NeetCode
def get_happy_string(n, k):
    total_happy = 3 * (2**(n - 1))
    
    if k > total_happy:
        return ""

    res = []
    choices = "abc"
    left, right = 1, total_happy

    for i in range(n):
        cur = left
        partition_size = (right - left + 1) // len(choices)

        for c in choices:
            if k in range(cur, cur + partition_size):
                res.append(c)
                left = cur
                right = cur + partition_size - 1
                choices = choices.replace(c, "")
                break
            cur += partition_size

    return "".join(res)


def main():
    result = get_happy_string(n = 1, k = 3)
    print(result) # "c"

    result = get_happy_string(n = 1, k = 4)
    print(result) # ""

    result = get_happy_string(n = 3, k = 9)
    print(result) # "cab"

if __name__ == "__main__":
    main()
