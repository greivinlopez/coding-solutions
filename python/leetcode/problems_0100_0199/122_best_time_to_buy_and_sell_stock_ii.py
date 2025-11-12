# ------------------------------------------
# 122. Best Time to Buy and Sell Stock II 📈
# ------------------------------------------

# Problem: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
# 
# You are given an integer array prices where prices[i] is the price of a given 
# stock on the ith day.
# 
# On each day, you may decide to buy and/or sell the stock. You can only hold at 
# most one share of the stock at any time. However, you can buy it then 
# immediately sell it on the same day.
# 
# Find and return the maximum profit you can achieve.

# Solution: https://youtu.be/3SJ3pUkPQMc
# Credit: Navdeep Singh founder of NeetCode
def max_profit(prices):
    # Time: O(n)
    # Space: O(1)
    max_profit = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i-1]:
            max_profit += prices[i] - prices[i-1]
    return max_profit

# Solution: https://youtu.be/TSpBHe5vInA
# Credit: Greg Hogg
def max_profit_alt(prices):
    # Time: O(n)
    # Space: O(1)
    i = 0
    lo = prices[0]
    hi = prices[0]
    profit = 0
    n = len(prices)

    while i < n-1:
        # look where to buy
        while i < n-1 and prices[i] >= prices[i+1]:
            i += 1
        lo = prices[i]

        # look where to sell
        while i < n-1 and prices[i] <= prices[i+1]:
            i += 1
        hi = prices[i]
        
        profit += hi - lo
    
    return profit

def main():
    result = max_profit([7,1,5,3,6,4])
    print(result) # 7

    result = max_profit([1,2,3,4,5])
    print(result) # 4

    result = max_profit([7,6,4,3,1])
    print(result) # 0

if __name__ == "__main__":
    main()