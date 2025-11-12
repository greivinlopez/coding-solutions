# ---------------------------------------------
# 730. Count Different Palindromic Subsequences
# ---------------------------------------------

# Problem: https://leetcode.com/problems/count-different-palindromic-subsequences
#
# Given a string s, return the number of different non-empty palindromic
# subsequences in s. Since the answer may be very large, return it modulo 10⁹ + 7.
# 
# A subsequence of a string is obtained by deleting zero or more characters from
# the string.
# 
# A sequence is palindromic if it is equal to the sequence reversed.
# 
# Two sequences a1, a2, ... and b1, b2, ... are different if there is some i for
# which aᵢ != bᵢ.
# 
# Example 1:
# 
# Input: s = "bccb"
# Output: 6
# 
# Explanation: The 6 different non-empty palindromic subsequences are 'b', 'c',
# 'bb', 'cc', 'bcb', 'bccb'.
# Note that 'bcb' is counted only once, even though it occurs twice.
# 
# Example 2:
# 
# Input: s = "abcdabcdabcdabcdabcdabcdabcdabcddcbadcbadcbadcbadcbadcbadcbadcba"
# Output: 104860361
# 
# Explanation: There are 3104860382 different non-empty palindromic subsequences,
# which is 104860361 modulo 10⁹ + 7.
# 
# 
# Constraints:
#         1 <= s.length <= 1000
#         s[i] is either 'a', 'b', 'c', or 'd'.


# Solution: https://algo.monster/liteproblems/730
# Credit: AlgoMonster
def count_palindromic_subsequences(s):
    MOD = 10**9 + 7
    n = len(s)
    
    # dp[i][j][char_idx] = number of distinct palindromic subsequences 
    # in s[i:j+1] that start and end with character at index char_idx
    # where char_idx: 0='a', 1='b', 2='c', 3='d'
    dp = [[[0] * 4 for _ in range(n)] for _ in range(n)]
    
    # Base case: single characters are palindromes
    for i, char in enumerate(s):
        char_index = ord(char) - ord('a')
        dp[i][i][char_index] = 1
    
    # Process substrings of increasing length
    for length in range(2, n + 1):
        for start in range(n - length + 1):
            end = start + length - 1
            
            # Try each possible character as start/end of palindrome
            for char in 'abcd':
                char_index = ord(char) - ord('a')
                
                if s[start] == s[end] == char:
                    # Both ends match the current character
                    # Count: empty string + single char + all palindromes from inner substring
                    dp[start][end][char_index] = 2 + sum(dp[start + 1][end - 1])
                elif s[start] == char:
                    # Only start matches - exclude the end character
                    dp[start][end][char_index] = dp[start][end - 1][char_index]
                elif s[end] == char:
                    # Only end matches - exclude the start character
                    dp[start][end][char_index] = dp[start + 1][end][char_index]
                else:
                    # Neither end matches - look at inner substring
                    dp[start][end][char_index] = dp[start + 1][end - 1][char_index]
    
    # Return total count of distinct palindromic subsequences
    return sum(dp[0][n - 1]) % MOD
    # Time: O(n²)
    # Space: O(n²)


def main():
    result = count_palindromic_subsequences(s = "bccb")
    print(result) # 6

    result = count_palindromic_subsequences(s = "abcdabcdabcdabcdabcdabcdabcdabcddcbadcbadcbadcbadcbadcbadcbadcba")
    print(result) # 104860361

if __name__ == "__main__":
    main()
