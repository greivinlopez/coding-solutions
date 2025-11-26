# ---------------------------------------------------
# 1638. Count Substrings That Differ by One Character
# ---------------------------------------------------

# Problem: https://leetcode.com/problems/count-substrings-that-differ-by-one-character
#
# Given two strings s and t, find the number of ways you can choose a non-empty
# substring of s and replace a single character by a different character such that
# the resulting substring is a substring of t. In other words, find the number of
# substrings in s that differ from some substring in t by exactly one character.
# 
# For example, the underlined substrings in "computer" and "computation" only
# differ by the 'e'/'a', so this is a valid way.
# 
# Return the number of substrings that satisfy the condition above.
# 
# A substring is a contiguous sequence of characters within a string.
# 
# Example 1:
# 
# Input: s = "aba", t = "baba"
# Output: 6
# 
# Explanation: The following are the pairs of substrings from s and t that differ
# by exactly 1 character:
# ("aba", "baba")
# ("aba", "baba")
# ("aba", "baba")
# ("aba", "baba")
# ("aba", "baba")
# ("aba", "baba")
# The underlined portions are the substrings that are chosen from s and t.
# 
# ​​Example 2:
# 
# Input: s = "ab", t = "bb"
# Output: 3
# 
# Explanation: The following are the pairs of substrings from s and t that differ
# by 1 character:
# ("ab", "bb")
# ("ab", "bb")
# ("ab", "bb")
# ​​​​The underlined portions are the substrings that are chosen from s and t.
# 
# 
# Constraints:
#         1 <= s.length, t.length <= 100
#         s and t consist of lowercase English letters only.


# Solution: https://algo.monster/liteproblems/1638
# Credit: AlgoMonster
def count_substrings(s, t):
    total_count = 0
    len_s, len_t = len(s), len(t)
    
    # Iterate through all character pairs from both strings
    for i in range(len_s):
        for j in range(len_t):
            # Check if characters at current positions differ
            if s[i] != t[j]:
                # Count matching characters to the left of mismatch
                left_matches = 0
                while (i - left_matches - 1 >= 0 and 
                        j - left_matches - 1 >= 0 and 
                        s[i - left_matches - 1] == t[j - left_matches - 1]):
                    left_matches += 1
                
                # Count matching characters to the right of mismatch
                right_matches = 0
                while (i + right_matches + 1 < len_s and 
                        j + right_matches + 1 < len_t and 
                        s[i + right_matches + 1] == t[j + right_matches + 1]):
                    right_matches += 1
                
                # Calculate total substrings with this mismatch point
                # (left_matches + 1) possible starting positions
                # (right_matches + 1) possible ending positions
                total_count += (left_matches + 1) * (right_matches + 1)
    
    return total_count
    # Time: O(m * n * min(m, n))
    # Space: O(1)


def main():
    result = count_substrings(s = "aba", t = "baba")
    print(result) # 6

    result = count_substrings(s = "ab", t = "bb")
    print(result) # 3

if __name__ == "__main__":
    main()
