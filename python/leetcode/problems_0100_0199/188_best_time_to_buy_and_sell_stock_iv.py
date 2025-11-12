# ---------------------------------------
# 188. Best Time to Buy and Sell Stock IV
# ---------------------------------------

# Problem: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv
#
# You are given an integer array prices where prices[i] is the price of a given
# stock on the ith day, and an integer k.
# 
# Find the maximum profit you can achieve. You may complete at most k
# transactions: i.e. you may buy at most k times and sell at most k times.
# 
# Note: You may not engage in multiple transactions simultaneously (i.e., you must
# sell the stock before you buy again).
# 
# Example 1:
# 
# Input: k = 2, prices = [2,4,1]
# Output: 2
# 
# Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit =
# 4-2 = 2.
# 
# Example 2:
# 
# Input: k = 2, prices = [3,2,6,5,0,3]
# Output: 7
# 
# Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit =
# 6-2 = 4. Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit =
# 3-0 = 3.
# 
# 
# Constraints:
#         1 <= k <= 100
#         1 <= prices.length <= 1000
#         0 <= prices[i] <= 1000


# Solution: https://leetcodethehardway.com/solutions/0100-0199/best-time-to-buy-and-sell-stock-iv-hard
# Credit: LeetCode the Hard Way -> https://leetcodethehardway.com/
def max_profit(k, prices):
    # no transaction, no profit
    if k == 0: return 0
    # dp[k][0] = min cost you need to spend at most k transactions
    # dp[k][1] = max profit you can achieve at most k transactions
    dp = [[1000, 0] for _ in range(k + 1)]
    for price in prices:
        for i in range(1, k + 1):
            # price - dp[i - 1][1] is how much you need to spend
            # i.e use the profit you earned from previous transaction to buy the stock
            # we want to minimize it
            dp[i][0] = min(dp[i][0], price - dp[i - 1][1])
            # price - dp[i][0] is how much you can achieve from previous min cost
            # we want to maximize it
            dp[i][1] = max(dp[i][1], price - dp[i][0])
    # return max profit at most k transactions
    # or you can write `return dp[-1][1]`
    return dp[k][1]


def main():
    result = max_profit(k = 2, prices = [2,4,1])
    print(result) # 2

    result = max_profit(k = 2, prices = [3,2,6,5,0,3])
    print(result) # 7

if __name__ == "__main__":
    main()
