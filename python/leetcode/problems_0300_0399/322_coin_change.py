# ----------------
# 322. Coin Change
# ----------------

# Problem: https://leetcode.com/problems/coin-change/
# 
# You are given an integer array coins representing coins of different denominations 
# and an integer amount representing a total amount of money.
# 
# Return the fewest number of coins that you need to make up that amount. If that 
# amount of money cannot be made up by any combination of the coins, return -1.
# 
# You may assume that you have an infinite number of each kind of coin.
# 
#  
# Example 1:
# 
# Input: coins = [1,2,5], amount = 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1
# 
# 
# Example 2:
# 
# Input: coins = [2], amount = 3
# Output: -1
# 
# 
# Example 3:
# 
# Input: coins = [1], amount = 0
# Output: 0
# 
# 
# Constraints:
# 
# 	1 <= coins.length <= 12
# 	1 <= coins[i] <= 231 - 1
# 	0 <= amount <= 104


# Solution: https://youtu.be/H9bfqozjoqs
# Credit: Navdeep Singh founder of NeetCode
def coin_change(coins, amount):
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0

    for a in range(1, amount + 1):
        for c in coins:
            if a - c >= 0:
                dp[a] = min(dp[a], 1 + dp[a - c])
    return dp[amount] if dp[amount] != amount + 1 else -1

# Solution: https://youtu.be/koE9ly1CFDc
# Credit: Greg Hogg
def coin_change_brute(coins, amount):
    # Brute force with simple recursion
    # Time: O(Coins ^ Amount)
    # Space: O(Amount)
    if amount == 0:
        return 0
    elif amount < 0:
        return -1

    min_cnt = -1
    for coin in coins:
        cnt = self.coinChange(coins, amount - coin)
        if cnt >= 0:
            min_cnt = cnt + 1 if min_cnt < 0 else min(min_cnt, cnt + 1)
    return min_cnt


def coin_change_memo(coins, amount):
    # Top Down DP (Memoization)
    # Time: O(Coins * Amount)
    # Space: O(Amount)
    coins.sort()
    memo = {0:0}

    def min_coins(amt):
        if amt in memo:
            return memo[amt]
        
        minn = float('inf')
        for coin in coins:
            diff = amt - coin
            if diff < 0:
                break
            minn = min(minn, 1 + min_coins(diff))
        
        memo[amt] = minn
        return minn

    result = min_coins(amount)
    if result < float('inf'):
        return result
    else:
        return -1

def coin_change_dp(coins, amount):
    # Bottom Up DP (Tabulation)
    # Time: O(Coins * Amount)
    # Space: O(Amount)
    dp = [0] * (amount + 1)
    coins.sort()

    for i in range(1, amount+1):
        minn = float('inf')
        
        for coin in coins:
            diff = i - coin
            if diff < 0:
                break
            minn = min(minn, dp[diff] + 1)
        
        dp[i] = minn
    
    if dp[amount] < float('inf'):
        return dp[amount]
    else:
        return -1

def main():
    result = coin_change(coins = [1,2,5], amount = 11)
    print(result) # 3

    result = coin_change(coins = [2], amount = 3)
    print(result) # -1

    result = coin_change(coins = [1], amount = 0)
    print(result) # 0

if __name__ == "__main__":
    main()
