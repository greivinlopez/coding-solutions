# ------------------------------------
# 1400. Construct K Palindrome Strings
# ------------------------------------

# Problem: https://leetcode.com/problems/construct-k-palindrome-strings
#
# Given a string s and an integer k, return true if you can use all the characters
# in s to construct non-empty k palindrome strings or false otherwise.
# 
# Example 1:
# 
# Input: s = "annabelle", k = 2
# Output: true
# 
# Explanation: You can construct two palindromes using all characters in s.
# Some possible constructions "anna" + "elble", "anbna" + "elle", "anellena" + "b"
# 
# Example 2:
# 
# Input: s = "leetcode", k = 3
# Output: false
# 
# Explanation: It is impossible to construct 3 palindromes using all the
# characters of s.
# 
# Example 3:
# 
# Input: s = "true", k = 4
# Output: true
# 
# Explanation: The only possible solution is to put each character in a separate
# string.
# 
# 
# Constraints:
#         1 <= s.length <= 10⁵
#         s consists of lowercase English letters.
#         1 <= k <= 10⁵

from collections import Counter

# Solution: https://youtu.be/D00qGvqmqN0
# Credit: Navdeep Singh founder of NeetCode
def can_construct(s, k):
    if k > len(s):
        return False
    
    count = Counter(s)
    odd = 0
    for cnt in count.values():
        odd += cnt % 2
        
    return odd <= k
    # Time: O(n)
    # Space: O(1)


def main():
    result = can_construct(s = "annabelle", k = 2)
    print(result) # True

    result = can_construct(s = "leetcode", k = 3)
    print(result) # False

    result = can_construct(s = "true", k = 4)
    print(result) # True

if __name__ == "__main__":
    main()
