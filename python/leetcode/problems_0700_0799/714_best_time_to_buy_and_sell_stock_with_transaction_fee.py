# ---------------------------------------------------------
# 714. Best Time to Buy and Sell Stock with Transaction Fee
# ---------------------------------------------------------

# Problem: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee
#
# You are given an array prices where prices[i] is the price of a given stock on
# the ith day, and an integer fee representing a transaction fee.
# 
# Find the maximum profit you can achieve. You may complete as many transactions
# as you like, but you need to pay the transaction fee for each transaction.
#
# Note:
#         
#   * You may not engage in multiple transactions simultaneously (i.e., you must 
#     sell the stock before you buy again).
#   * The transaction fee is only charged once for each stock purchase and sale.
# 
# Example 1:
# 
# Input: prices = [1,3,2,8,4,9], fee = 2
# Output: 8
# 
# Explanation: The maximum profit can be achieved by:
# - Buying at prices[0] = 1
# - Selling at prices[3] = 8
# - Buying at prices[4] = 4
# - Selling at prices[5] = 9
# The total profit is ((8 - 1) - 2) + ((9 - 4) - 2) = 8.
# 
# Example 2:
# 
# Input: prices = [1,3,7,5,10,3], fee = 3
# Output: 6
# 
# 
# Constraints:
#         1 <= prices.length <= 5 * 10⁴
#         1 <= prices[i] < 5 * 10⁴
#         0 <= fee < 5 * 10⁴

from functools import cache

# Solution: https://algo.monster/liteproblems/714
# Credit: AlgoMonster
def max_profit(prices, fee):
    @cache
    def dp(day, holding_stock):
        # Base case: no more days left
        if day >= len(prices):
            return 0
        
        # Option 1: Do nothing on this day
        max_profit = dp(day + 1, holding_stock)
        
        if holding_stock:
            # Currently holding stock - can sell
            # Selling: gain price minus fee, transition to not holding
            max_profit = max(max_profit, prices[day] - fee + dp(day + 1, 0))
        else:
            # Not holding stock - can buy
            # Buying: lose price, transition to holding
            max_profit = max(max_profit, -prices[day] + dp(day + 1, 1))
        
        return max_profit
    
    # Start from day 0 with no stock held
    return dp(0, 0)
    # Time: O(n)
    # Space: O(n)


def main():
    result = max_profit(prices = [1,3,2,8,4,9], fee = 2)
    print(result) # 8

    result = max_profit(prices = [1,3,7,5,10,3], fee = 3)
    print(result) # 6

if __name__ == "__main__":
    main()
