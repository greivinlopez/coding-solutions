# ---------------------------------------
# 1208. Get Equal Substrings Within Budget
# ---------------------------------------

# Problem: https://leetcode.com/problems/get-equal-substrings-within-budget
#
# You are given two strings s and t of the same length and an integer maxCost.
# 
# You want to change s to t. Changing the ith character of s to ith character of t
# costs |s[i] - t[i]| (i.e., the absolute difference between the ASCII values of
# the characters).
# 
# Return the maximum length of a substring of s that can be changed to be the same
# as the corresponding substring of t with a cost less than or equal to maxCost.
# If there is no substring from s that can be changed to its corresponding
# substring from t, return 0.
# 
# Example 1:
# 
# Input: s = "abcd", t = "bcdf", maxCost = 3
# Output: 3
# 
# Explanation: "abc" of s can change to "bcd".
# That costs 3, so the maximum length is 3.
# 
# Example 2:
# 
# Input: s = "abcd", t = "cdef", maxCost = 3
# Output: 1
# 
# Explanation: Each character in s costs 2 to change to character in t,  so the
# maximum length is 1.
# 
# Example 3:
# 
# Input: s = "abcd", t = "acde", maxCost = 0
# Output: 1
# 
# Explanation: You cannot make any change, so the maximum length is 1.
# 
# Constraints:
#         1 <= s.length <= 10^5
#         t.length == s.length
#         0 <= maxCost <= 10^6
#         s and t consist of only lowercase English letters.


# Solution: https://youtu.be/3lsT1Le526U
# Credit: Navdeep Singh founder of NeetCode
def equal_substring(s, t, max_cost):
    cur_cost = 0
    l = 0
    res = 0

    for r in range(len(s)):
        cur_cost += abs(ord(s[r]) - ord(t[r]))

        while cur_cost > max_cost:
            cur_cost -= abs(ord(s[l]) - ord(t[l]))
            l += 1

        res = max(res, r - l + 1)

    return res
    # Time: O(n) 
    # Space: O(1)


def main():
    result = equal_substring(s = "abcd", t = "bcdf", max_cost = 3)
    print(result) # 3

    result = equal_substring(s = "abcd", t = "cdef", max_cost = 3)
    print(result) # 1

    result = equal_substring(s = "abcd", t = "acde", max_cost = 0)
    print(result) # 1

if __name__ == "__main__":
    main()
