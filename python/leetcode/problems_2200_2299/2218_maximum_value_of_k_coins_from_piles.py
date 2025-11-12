# --------------------------------------------
# 2218. Maximum Value of K Coins From Piles 👛
# --------------------------------------------

# Problem: https://leetcode.com/problems/maximum-value-of-k-coins-from-piles
#
# There are n piles of coins on a table. Each pile consists of a positive number
# of coins of assorted denominations.
# 
# In one move, you can choose any coin on top of any pile, remove it, and add it
# to your wallet.
# 
# Given a list piles, where piles[i] is a list of integers denoting the
# composition of the ith pile from top to bottom, and a positive integer k, return
# the maximum total value of coins you can have in your wallet if you choose
# exactly k coins optimally.
# 
# Example 1:
# 
# Input: piles = [[1,100,3],[7,8,9]], k = 2
# Output: 101
# 
# Explanation:
# The above diagram shows the different ways we can choose k coins.
# The maximum total we can obtain is 101.
# 
# Example 2:
# 
# Input: piles = [[100],[100],[100],[100],[100],[100],[1,1,1,1,1,1,700]], k = 7
# Output: 706
# 
# Explanation:
# The maximum total can be obtained if we choose all coins from the last pile.
# 
# Constraints:
#         n == piles.length
#         1 <= n <= 1000
#         1 <= piles[i][j] <= 10^5
#         1 <= k <= sum(piles[i].length) <= 2000


# Solution: https://youtu.be/ZRdEd_eun8g
# Credit: Navdeep Singh founder of NeetCode
def max_value_of_coins(piles, k):
    n = len(piles)
    dp = [[-1] * (k + 1) for _ in range(n)]

    def dfs(i, coins):
        if i == n:
            return 0
        
        if dp[i][coins] != -1:
            return dp[i][coins]
        
        dp[i][coins] = dfs(i + 1, coins)
        curPile = 0
        for j in range(min(coins, len(piles[i]))):
            curPile += piles[i][j]
            dp[i][coins] = max(dp[i][coins], curPile + dfs(i + 1, coins - j - 1))
        
        return dp[i][coins]

    return dfs(0, k)
    # Time: O(n * k * M), M is the maximum length of any pile
    # Space: O(n * k)


def main():
    result = max_value_of_coins(piles = [[1,100,3],[7,8,9]], k = 2)
    print(result) # 101

    result = max_value_of_coins(piles = [[100],[100],[100],[100],[100],[100],[1,1,1,1,1,1,700]], k = 7)
    print(result) # 706

if __name__ == "__main__":
    main()
