# ------------------
# 72. Edit Distance
# ------------------

# Problem: https://leetcode.com/problems/edit-distance/
# 
# Given two strings word1 and word2, return the minimum number of operations 
# required to convert word1 to word2.
# 
# You have the following three operations permitted on a word:
# 
# - Insert a character
# - Delete a character
# - Replace a character

# Solution: https://youtu.be/XYi2-LPrwm4
# Credit: Navdeep Singh founder of NeetCode 
def min_distance(word1, word2):
    dp = [[float("inf")] * (len(word2) + 1) for i in range(len(word1) + 1)]

    for j in range(len(word2) + 1):
        dp[len(word1)][j] = len(word2) - j
    for i in range(len(word1) + 1):
        dp[i][len(word2)] = len(word1) - i

    for i in range(len(word1) - 1, -1, -1):
        for j in range(len(word2) - 1, -1, -1):
            if word1[i] == word2[j]:
                dp[i][j] = dp[i + 1][j + 1]
            else:
                dp[i][j] = 1 + min(dp[i + 1][j], dp[i][j + 1], dp[i + 1][j + 1])
    return dp[0][0]


def main():
    result = min_distance(word1 = "horse", word2 = "ros") 
    # Expected Output: 3
    print(result)
    result = min_distance(word1 = "intention", word2 = "execution")
    # Expected Output: 5
    print(result)

if __name__ == "__main__":
    main()