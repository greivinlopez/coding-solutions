# ---------------------------------------
# 121. Best Time to Buy and Sell Stock 📈
# ---------------------------------------

# Problem: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# 
# You are given an array prices where prices[i] is the price of a given stock on 
# the ith day.
# 
# You want to maximize your profit by choosing a single day to buy one stock and 
# choosing a different day in the future to sell that stock.
# 
# Return the maximum profit you can achieve from this transaction. If you cannot 
# achieve any profit, return 0.

# Solution: https://www.youtube.com/watch?v=1pkOgXD63yU
# Credit: Navdeep Singh founder of NeetCode
def max_profit(prices):
    # Time: O(n)
    # Space: O(1)
    res = 0    
    lowest = prices[0]
    for price in prices:
        if price < lowest:
            lowest = price
        res = max(res, price - lowest)
    return res

# Solution: https://youtu.be/kJZrMGpyWpk
# Credit: Greg Hogg
def max_profit_alt(prices):
    # Time: O(n)
    # Space: O(1)
    min_price = float('inf')
    max_profit = 0        
    
    for price in prices:
        profit = price - min_price
        
        min_price = min(price, min_price)
        max_profit = max(profit, max_profit)
            
    return max_profit

def main():
    result = max_profit([7,1,5,3,6,4])
    print(result) # 5

    result = max_profit([7,6,4,3,1])
    print(result) # 0

if __name__ == "__main__":
    main()