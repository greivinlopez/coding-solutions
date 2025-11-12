# ------------------------------------
# 1915. Number of Wonderful Substrings
# ------------------------------------

# Problem: https://leetcode.com/problems/number-of-wonderful-substrings
#
# A wonderful string is a string where at most one letter appears an odd number of
# times.
#         
#   * For example, "ccjjc" and "abab" are wonderful, but "ab" is not.
# 
# Given a string word that consists of the first ten lowercase English letters
# ('a' through 'j'), return the number of wonderful non-empty substrings in word.
# If the same substring appears multiple times in word, then count each occurrence
# separately.
# 
# A substring is a contiguous sequence of characters in a string.
# 
# Example 1:
# 
# Input: word = "aba"
# Output: 4
# 
# Explanation: The four wonderful substrings are underlined below:
# - "aba" -> "a"
# - "aba" -> "b"
# - "aba" -> "a"
# - "aba" -> "aba"
# 
# Example 2:
# 
# Input: word = "aabb"
# Output: 9
# 
# Explanation: The nine wonderful substrings are underlined below:
# - "aabb" -> "a"
# - "aabb" -> "aa"
# - "aabb" -> "aab"
# - "aabb" -> "aabb"
# - "aabb" -> "a"
# - "aabb" -> "abb"
# - "aabb" -> "b"
# - "aabb" -> "bb"
# - "aabb" -> "b"
# 
# Example 3:
# 
# Input: word = "he"
# Output: 2
# 
# Explanation: The two wonderful substrings are underlined below:
# - "he" -> "h"
# - "he" -> "e"
# 
# 
# Constraints:
#         1 <= word.length <= 10⁵
#         word consists of lowercase English letters from 'a' to 'j'.


# Credit: Jaweria Batool -> https://github.com/Jaweria-B
def wonderful_substrings(word):
    # Create the frequency map
    # Key = bitmask, Value = frequency of bitmask key
    freq = {}

    # The empty prefix can be the smaller prefix, which is handled like this
    freq[0] = 1

    mask = 0
    res = 0
    for c in word:
        bit = ord(c) - 97

        # Flip the parity of the c-th bit in the running prefix mask
        mask ^= (1 << bit)

        # Count smaller prefixes that create substrings with no odd occurring letters
        if mask in freq:
            res += freq[mask]
            freq[mask] += 1
        else:
            freq[mask] = 1

        # Loop through every possible letter that can appear an odd number of times in a substring
        for odd_c in range(0, 10):
            if (mask ^ (1 << odd_c)) in freq:
                res += freq[mask ^ (1 << odd_c)]

    return res
    # Time: O(n)
    # Space: O(1)
    # ∣Σ∣ is the size of the character set (alphabet) used, which is fixed at 10
    # Time complexity is O(n * ∣Σ∣) and space complexity is O(2^∣Σ∣) = 1024.


def main():
    result = wonderful_substrings("aba")
    print(result) # 4

    result = wonderful_substrings("aabb")
    print(result) # 9

    result = wonderful_substrings("he")
    print(result) # 2

if __name__ == "__main__":
    main()
