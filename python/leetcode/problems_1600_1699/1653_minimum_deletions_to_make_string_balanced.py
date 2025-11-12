# ----------------------------------------------
# 1653. Minimum Deletions to Make String Balanced
# ----------------------------------------------

# Problem: https://leetcode.com/problems/minimum-deletions-to-make-string-balanced
#
# You are given a string s consisting only of characters 'a' and 'b'​​​​.
# You can delete any number of characters in s to make s balanced. s is balanced
# if there is no pair of indices (i,j) such that i < j and s[i] = 'b' and s[j]=
# 'a'.
# Return the minimum number of deletions needed to make s balanced.
# Example 1:
# Input: s = "aababbab"
# Output: 2
# Explanation: You can either:
# Delete the characters at 0-indexed positions 2 and 6 ("aababbab" -> "aaabbb"),
# or
# Delete the characters at 0-indexed positions 3 and 6 ("aababbab" -> "aabbbb").
# Example 2:
# Input: s = "bbaaaaabb"
# Output: 2
# Explanation: The only solution is to delete the first two characters.
# Constraints:
#         1 <= s.length <= 105
#         s[i] is 'a' or 'b'​​.


# Solution: https://youtu.be/WDStNufBUQ8
# Credit: Navdeep Singh founder of NeetCode
def minimum_deletions_alt(s):
    a_count_right = [0] * len(s)
    for i in range(len(s) - 2, -1, -1):
        a_count_right[i] = a_count_right[i + 1]
        a_count_right[i] += 1 if s[i + 1] == "a" else 0

    b_count_left = 0
    res = len(s)
    for i, c in enumerate(s):
        res = min(res, b_count_left + a_count_right[i])
        if c == "b":
            b_count_left += 1
    return res
    # Time: O(n) 
    # Credit: O(n)

# Improved solution
def minimum_deletions(s):
    a_count_right = 0
    for c in s:
        a_count_right += 1 if c == "a" else 0

    b_count_left = 0
    res = len(s)
    for i, c in enumerate(s):
        if c == "a":
            a_count_right -= 1
        res = min(res, b_count_left + a_count_right)
        if c == "b":
            b_count_left += 1
    return res
    # Time: O(n) 
    # Credit: O(1)


def main():
    result = minimum_deletions("aababbab")
    print(result) # True

    result = minimum_deletions("bbaaaaabb")
    print(result) # True

if __name__ == "__main__":
    main()
