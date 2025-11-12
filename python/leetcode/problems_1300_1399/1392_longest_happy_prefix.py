# --------------------------
# 1392. Longest Happy Prefix
# --------------------------

# Problem: https://leetcode.com/problems/longest-happy-prefix
#
# A string is called a happy prefix if is a non-empty prefix which is also a
# suffix (excluding itself).
# 
# Given a string s, return the longest happy prefix of s. Return an empty string
# "" if no such prefix exists.
# 
# Example 1:
# 
# Input: s = "level"
# Output: "l"
# 
# Explanation: s contains 4 prefix excluding itself ("l", "le", "lev", "leve"),
# and suffix ("l", "el", "vel", "evel"). The largest prefix which is also suffix
# is given by "l".
# 
# Example 2:
# 
# Input: s = "ababab"
# Output: "abab"
# 
# Explanation: "abab" is the largest prefix which is also suffix. They can overlap
# in the original string.
# 
# 
# Constraints:
#         1 <= s.length <= 10⁵
#         s contains only lowercase English letters.


# Solution: https://algo.monster/liteproblems/1392
# Credit: AlgoMonster
def longest_prefix(s):
    # Iterate through possible prefix/suffix lengths from longest to shortest
    # Start from 1 to exclude the entire string (len(s) - 1 characters max)
    for i in range(1, len(s)):
        # Check if prefix of length (len(s) - i) equals suffix of same length
        # s[:-i] gets all characters except last i characters (prefix)
        # s[i:] gets all characters from index i to end (suffix)
        if s[:-i] == s[i:]:
            # If they match, return this common prefix/suffix
            return s[i:]
    
    # No common proper prefix/suffix found
    return ''
    # Time: O(n²)
    # Space: O(n)


def main():
    result = longest_prefix(s = "level")
    print(result) # "l"

    result = longest_prefix(s = "ababab")
    print(result) # "abab"

if __name__ == "__main__":
    main()
