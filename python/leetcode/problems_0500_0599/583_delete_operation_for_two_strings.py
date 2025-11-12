# -------------------------------------
# 583. Delete Operation for Two Strings
# -------------------------------------

# Problem: https://leetcode.com/problems/delete-operation-for-two-strings
#
# Given two strings word1 and word2, return the minimum number of steps required
# to make word1 and word2 the same.
# 
# In one step, you can delete exactly one character in either string.
# 
# Example 1:
# 
# Input: word1 = "sea", word2 = "eat"
# Output: 2
# 
# Explanation: You need one step to make "sea" to "ea" and another step to make
# "eat" to "ea".
# 
# Example 2:
# 
# Input: word1 = "leetcode", word2 = "etco"
# Output: 4
# 
# 
# Constraints:
#         1 <= word1.length, word2.length <= 500
#         word1 and word2 consist of only lowercase English letters.


# Solution: https://algo.monster/liteproblems/583
# Credit: AlgoMonster
def min_distance(word1, word2):
    len1, len2 = len(word1), len(word2)
    
    # Create a 2D DP table where dp[i][j] represents the minimum deletions
    # needed to make word1[0:i] and word2[0:j] equal
    dp = [[0] * (len2 + 1) for _ in range(len1 + 1)]
    
    # Base case: If word2 is empty, delete all characters from word1
    for i in range(1, len1 + 1):
        dp[i][0] = i
        
    # Base case: If word1 is empty, delete all characters from word2
    for j in range(1, len2 + 1):
        dp[0][j] = j
        
    # Fill the DP table
    for i, char1 in enumerate(word1, 1):
        for j, char2 in enumerate(word2, 1):
            if char1 == char2:
                # Characters match, no deletion needed
                dp[i][j] = dp[i - 1][j - 1]
            else:
                # Characters don't match, delete from either string
                # Take minimum of:
                # 1. Delete from word1: dp[i-1][j] + 1
                # 2. Delete from word2: dp[i][j-1] + 1
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + 1
                
    return dp[len1][len2]


def main():
    result = min_distance(word1 = "sea", word2 = "eat")
    print(result) # 2

    result = min_distance(word1 = "leetcode", word2 = "etco")
    print(result) # 4

if __name__ == "__main__":
    main()
