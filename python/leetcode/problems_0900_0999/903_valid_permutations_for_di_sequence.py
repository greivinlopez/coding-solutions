# ---------------------------------------
# 903. Valid Permutations for DI Sequence
# ---------------------------------------

# Problem: https://leetcode.com/problems/valid-permutations-for-di-sequence
#
# You are given a string s of length n where s[i] is either:
#         
#   * 'D' means decreasing, or
#   * 'I' means increasing.
# 
# A permutation perm of n + 1 integers of all the integers in the range [0, n] is
# called a valid permutation if for all valid i:
#         
#   * If s[i] == 'D', then perm[i] > perm[i + 1], and
#   * If s[i] == 'I', then perm[i] < perm[i + 1].
# 
# Return the number of valid permutations perm. Since the answer may be large,
# return it modulo 10⁹ + 7.
# 
# Example 1:
# 
# Input: s = "DID"
# Output: 5
# 
# Explanation: The 5 valid permutations of (0, 1, 2, 3) are:
# (1, 0, 3, 2)
# (2, 0, 3, 1)
# (2, 1, 3, 0)
# (3, 0, 2, 1)
# (3, 1, 2, 0)
# 
# Example 2:
# 
# Input: s = "D"
# Output: 1
# 
# 
# Constraints:
#         n == s.length
#         1 <= n <= 200
#         s[i] is either 'I' or 'D'.


# Solution: https://algo.monster/liteproblems/903
# Credit: AlgoMonster
def num_perms_di_sequence(s):
    MOD = 10**9 + 7
    n = len(s)
    
    # dp[i][j] represents the number of valid permutations of length i+1
    # where the last element has rank j among all i+1 elements
    # (rank 0 means smallest, rank i means largest)
    dp = [[0] * (n + 2) for _ in range(n + 2)]
    
    # Base case: one way to have a single element with rank 0
    dp[0][0] = 1
    
    # Process each character in the DI sequence
    for i, char in enumerate(s, start=1):
        if char == "D":
            # For 'D' (decrease): current element must be smaller than previous
            # If previous had rank k among i elements, and current has rank j among i+1 elements,
            # then we need j <= k (since adding current element shifts ranks)
            for j in range(i + 1):
                for k in range(j, i):
                    dp[i][j] = (dp[i][j] + dp[i - 1][k]) % MOD
        else:  # char == "I"
            # For 'I' (increase): current element must be larger than previous
            # If previous had rank k among i elements, and current has rank j among i+1 elements,
            # then we need j > k
            for j in range(i + 1):
                for k in range(j):
                    dp[i][j] = (dp[i][j] + dp[i - 1][k]) % MOD
    
    # Sum all valid permutations of length n+1 regardless of the last element's rank
    total = sum(dp[n][j] for j in range(n + 1)) % MOD
    return total
    # Time: O(n³)
    # Space: O(n²)


def main():
    result = num_perms_di_sequence(s = "DID")
    print(result) # 5

    result = num_perms_di_sequence(s = "D")
    print(result) # 1

if __name__ == "__main__":
    main()
