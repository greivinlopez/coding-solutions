# -----------------------------
# 940. Distinct Subsequences II
# -----------------------------

# Problem: https://leetcode.com/problems/distinct-subsequences-ii
#
# Given a string s, return the number of distinct non-empty subsequences of s.
# Since the answer may be very large, return it modulo 10⁹ + 7.
# 
# A subsequence of a string is a new string that is formed from the original
# string by deleting some (can be none) of the characters without disturbing the
# relative positions of the remaining characters. (i.e., "ace" is a subsequence of
# "abcde" while "aec" is not.
# 
# Example 1:
# 
# Input: s = "abc"
# Output: 7
# 
# Explanation: The 7 distinct subsequences are "a", "b", "c", "ab", "ac", "bc",
# and "abc".
# 
# Example 2:
# 
# Input: s = "aba"
# Output: 6
# 
# Explanation: The 6 distinct subsequences are "a", "b", "ab", "aa", "ba", and
# "aba".
# 
# Example 3:
# Input: s = "aaa"
# Output: 3
# 
# Explanation: The 3 distinct subsequences are "a", "aa" and "aaa".
# 
# 
# Constraints:
#         1 <= s.length <= 2000
#         s consists of lowercase English letters.


# Solution: https://algo.monster/liteproblems/940
# Credit: AlgoMonster
def distinct_subseq_ii(s):
    MOD = 10**9 + 7
    n = len(s)
    
    # dp[i][j] represents the count of distinct subsequences ending with character 'a'+j
    # up to position i in the string
    dp = [[0] * 26 for _ in range(n + 1)]
    
    # Process each character in the string
    for i, char in enumerate(s, 1):
        # Convert character to index (0-25 for 'a'-'z')
        char_index = ord(char) - ord('a')
        
        # Update dp values for all 26 possible ending characters
        for j in range(26):
            if j == char_index:
                # If current character matches, we can:
                # 1. Append it to all previous subsequences (sum of dp[i-1])
                # 2. Create a new single-character subsequence (+1)
                dp[i][j] = (sum(dp[i - 1]) % MOD + 1) % MOD
            else:
                # If character doesn't match, carry forward the previous count
                dp[i][j] = dp[i - 1][j]
    
    # Return total count of distinct subsequences (sum of all ending possibilities)
    return sum(dp[-1]) % MOD
    # Time: O(n)
    # Space: O(n)


def main():
    result = distinct_subseq_ii(s = "abc")
    print(result) # 7

    result = distinct_subseq_ii(s = "aba")
    print(result) # 6

    result = distinct_subseq_ii(s = "aaa")
    print(result) # 3

if __name__ == "__main__":
    main()
