# ----------------------
# 518. Coin Change II 🟡
# ----------------------

# Problem: https://leetcode.com/problems/coin-change-ii/
# 
# You are given an integer array coins representing coins of different 
# denominations and an integer amount representing a total amount of money.
# 
# Return the number of combinations that make up that amount. If that amount 
# of money cannot be made up by any combination of the coins, return 0.
# 
# You may assume that you have an infinite number of each kind of coin.
# 
# The answer is guaranteed to fit into a signed 32-bit integer.
# 
#  
# Example 1:
# 
# Input: amount = 5, coins = [1,2,5]
# Output: 4
# Explanation: there are four ways to make up the amount:
# 5=5
# 5=2+2+1
# 5=2+1+1+1
# 5=1+1+1+1+1
# 
# 
# Example 2:
# 
# Input: amount = 3, coins = [2]
# Output: 0
# Explanation: the amount of 3 cannot be made up just with coins of 2.
# 
# 
# Example 3:
# 
# Input: amount = 10, coins = [10]
# Output: 1
# 
#  
# Constraints:
# 
# 	1 <= coins.length <= 300
# 	1 <= coins[i] <= 5000
# 	All the values of coins are unique.
# 	0 <= amount <= 5000


# Solution: https://youtu.be/Mjy4hd2xgrs
# Credit: Navdeep Singh founder of NeetCode
def change(amount, coins):
    # MEMOIZATION
    cache = {}

    def dfs(i, a):
        if a == amount:
            return 1
        if a > amount:
            return 0
        if i == len(coins):
            return 0
        if (i, a) in cache:
            return cache[(i, a)]

        cache[(i, a)] = dfs(i, a + coins[i]) + dfs(i + 1, a)
        return cache[(i, a)]

    return dfs(0, 0)
    # Time: O(n*m)
    # Space: O(n*m)

def change_dp(amount, coins):
    # DYNAMIC PROGRAMMING
    dp = [[0] * (len(coins) + 1) for i in range(amount + 1)]
    dp[0] = [1] * (len(coins) + 1)
    for a in range(1, amount + 1):
        for i in range(len(coins) - 1, -1, -1):
            dp[a][i] = dp[a][i + 1]
            if a - coins[i] >= 0:
                dp[a][i] += dp[a - coins[i]][i]
    return dp[amount][0]
    # Time: O(n*m)
    # Space: O(n*m)

def change_dp_2(amount, coins):
    # DYNAMIC PROGRAMMING
    dp = [0] * (amount + 1)
    dp[0] = 1
    for i in range(len(coins) - 1, -1, -1):
        nextDP = [0] * (amount + 1)
        nextDP[0] = 1

        for a in range(1, amount + 1):
            nextDP[a] = dp[a]
            if a - coins[i] >= 0:
                nextDP[a] += nextDP[a - coins[i]]
        dp = nextDP
    return dp[amount]
    # Time: O(n*m)
    # Space: O(n) where n = amount

def main():
    result = change(amount = 5, coins = [1,2,5])
    print(result) # 4

    result = change(amount = 3, coins = [2])
    print(result) # 0

    result = change(amount = 10, coins = [10])
    print(result) # 1

if __name__ == "__main__":
    main()
