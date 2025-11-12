# -----------------------------------------------------------
# 395. Longest Substring with At Least K Repeating Characters
# -----------------------------------------------------------

# Problem: https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters
#
# Given a string s and an integer k, return the length of the longest substring of
# s such that the frequency of each character in this substring is greater than or
# equal to k.
# 
# if no such substring exists, return 0.
# 
# Example 1:
# 
# Input: s = "aaabb", k = 3
# Output: 3
# 
# Explanation: The longest substring is "aaa", as 'a' is repeated 3 times.
# 
# Example 2:
# 
# Input: s = "ababbc", k = 2
# Output: 5
# 
# Explanation: The longest substring is "ababb", as 'a' is repeated 2 times and
# 'b' is repeated 3 times.
# 
# 
# Constraints:
#         1 <= s.length <= 10⁴
#         s consists of only lowercase English letters.
#         1 <= k <= 10⁵

from collections import Counter

# Solution: https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/solutions/949688/python-short-simple-recursive-solution
# Credit: Navdeep Singh founder of NeetCode
def longest_substring(s, k):
    if len(s) == 0 or k > len(s):
        return 0
    c = Counter(s)
    sub1, sub2 = "", ""
    for i, letter in enumerate(s):
        if c[letter] < k:
            sub1 = longest_substring(s[:i], k)
            sub2 = longest_substring(s[i+1:], k)
            break
    else:
        return len(s)
    return max(sub1, sub2)
    # Time: O(n²)
    # Space: O(n²)


def main():
    result = longest_substring(s = "aaabb", k = 3)
    print(result) # 3

    result = longest_substring(s = "ababbc", k = 2)
    print(result) # 5

if __name__ == "__main__":
    main()
