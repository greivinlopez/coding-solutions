# ---------------------------------------------
# 712. Minimum ASCII Delete Sum for Two Strings
# ---------------------------------------------

# Problem: https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings
#
# Given two strings s1 and s2, return the lowest ASCII sum of deleted characters
# to make two strings equal.
# 
# Example 1:
# 
# Input: s1 = "sea", s2 = "eat"
# Output: 231
# 
# Explanation: Deleting "s" from "sea" adds the ASCII value of "s" (115) to the
# sum.
# Deleting "t" from "eat" adds 116 to the sum.
# At the end, both strings are equal, and 115 + 116 = 231 is the minimum sum
# possible to achieve this.
# 
# Example 2:
# 
# Input: s1 = "delete", s2 = "leet"
# Output: 403
# 
# Explanation: Deleting "dee" from "delete" to turn the string into "let",
# adds 100[d] + 101[e] + 101[e] to the sum.
# Deleting "e" from "leet" adds 101[e] to the sum.
# At the end, both strings are equal to "let", and the answer is 100+101+101+101 =
# 403.
# If instead we turned both strings into "lee" or "eet", we would get answers of
# 433 or 417, which are higher.
# 
# 
# Constraints:
#         1 <= s1.length, s2.length <= 1000
#         s1 and s2 consist of lowercase English letters.


# Solution: https://algo.monster/liteproblems/712
# Credit: AlgoMonster
def minimum_delete_sum(s1, s2):
    # Get lengths of both strings
    len_s1, len_s2 = len(s1), len(s2)
    
    # Create DP table where dp[i][j] represents the minimum delete sum
    # for s1[0:i] and s2[0:j] to make them equal
    dp = [[0] * (len_s2 + 1) for _ in range(len_s1 + 1)]
    
    # Initialize first column: delete all characters from s1[0:i]
    for i in range(1, len_s1 + 1):
        dp[i][0] = dp[i - 1][0] + ord(s1[i - 1])
    
    # Initialize first row: delete all characters from s2[0:j]
    for j in range(1, len_s2 + 1):
        dp[0][j] = dp[0][j - 1] + ord(s2[j - 1])
    
    # Fill the DP table
    for i in range(1, len_s1 + 1):
        for j in range(1, len_s2 + 1):
            if s1[i - 1] == s2[j - 1]:
                # Characters match: no deletion needed for these characters
                dp[i][j] = dp[i - 1][j - 1]
            else:
                # Characters don't match: delete from either s1 or s2
                # Choose the option with minimum ASCII sum
                dp[i][j] = min(
                    dp[i - 1][j] + ord(s1[i - 1]),  # Delete from s1
                    dp[i][j - 1] + ord(s2[j - 1])   # Delete from s2
                )
    
    # Return the minimum delete sum for entire strings
    return dp[len_s1][len_s2]
    # Time: O(m * n)
    # Space: O(m * n)


def main():
    result = minimum_delete_sum(s1 = "sea", s2 = "eat")
    print(result) # 231

    result = minimum_delete_sum(s1 = "delete", s2 = "leet")
    print(result) # 403

if __name__ == "__main__":
    main()
