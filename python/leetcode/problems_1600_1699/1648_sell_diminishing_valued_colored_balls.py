# -------------------------------------------
# 1648. Sell Diminishing-Valued Colored Balls
# -------------------------------------------

# Problem: https://leetcode.com/problems/sell-diminishing-valued-colored-balls
#
# You have an inventory of different colored balls, and there is a customer that
# wants orders balls of any color.
# 
# The customer weirdly values the colored balls. Each colored ball's value is the
# number of balls of that color you currently have in your inventory. For example,
# if you own 6 yellow balls, the customer would pay 6 for the first yellow ball.
# After the transaction, there are only 5 yellow balls left, so the next yellow
# ball is then valued at 5 (i.e., the value of the balls decreases as you sell
# more to the customer).
# 
# You are given an integer array, inventory, where inventory[i] represents the
# number of balls of the iᵗʰ color that you initially own. You are also given an
# integer orders, which represents the total number of balls that the customer
# wants. You can sell the balls in any order.
# 
# Return the maximum total value that you can attain after selling orders colored
# balls. As the answer may be too large, return it modulo 10⁹ + 7.
# 
# Example 1:
# 
# https://assets.leetcode.com/uploads/2020/11/05/jj.gif
# 
# Input: inventory = [2,5], orders = 4
# Output: 14
# 
# Explanation: Sell the 1st color 1 time (2) and the 2nd color 3 times (5 + 4 +
# 3).
# The maximum total value is 2 + 5 + 4 + 3 = 14.
# 
# Example 2:
# 
# Input: inventory = [3,5], orders = 6
# Output: 19
# 
# Explanation: Sell the 1st color 2 times (3 + 2) and the 2nd color 4 times (5 + 4
# + 3 + 2).
# The maximum total value is 3 + 2 + 5 + 4 + 3 + 2 = 19.
# 
# 
# Constraints:
#         1 <= inventory.length <= 10⁵
#         1 <= inventory[i] <= 10⁹
#         1 <= orders <= min(sum(inventory[i]), 10⁹)


# Solution: https://algo.monster/liteproblems/1648
# Credit: AlgoMonster
def max_profit(inventory, orders):
    # Sort inventory in descending order to process highest value items first
    inventory.sort(reverse=True)
    MOD = 10**9 + 7
    total_profit = 0
    current_index = 0
    inventory_size = len(inventory)

    while orders > 0:
        # Find how many items have the same highest value
        while current_index < inventory_size and inventory[current_index] >= inventory[0]:
            current_index += 1

        # Determine the next lower price level
        next_price_level = 0
        if current_index < inventory_size:
            next_price_level = inventory[current_index]

        # Number of items at current highest price
        items_at_current_price = current_index

        # Calculate how many units we can sell from current price to next price level
        price_difference = inventory[0] - next_price_level
        total_units_available = items_at_current_price * price_difference

        if total_units_available > orders:
            # Can't sell all available units, need to partially fulfill orders
            full_levels_to_sell = orders // items_at_current_price

            # Calculate profit from selling complete levels
            # Using arithmetic sequence sum: (first + last) * count / 2
            first_price = inventory[0] - full_levels_to_sell + 1
            last_price = inventory[0]
            total_profit += (first_price + last_price) * full_levels_to_sell // 2 * items_at_current_price

            # Add profit from remaining partial level
            remaining_orders = orders % items_at_current_price
            total_profit += (inventory[0] - full_levels_to_sell) * remaining_orders

            orders = 0  # All orders fulfilled
        else:
            # Sell all units from current price down to next price level
            first_price = next_price_level + 1
            last_price = inventory[0]
            total_profit += (first_price + last_price) * price_difference // 2 * items_at_current_price

            # Update the highest price to the next level
            inventory[0] = next_price_level
            orders -= total_units_available

        # Apply modulo to prevent integer overflow
        total_profit %= MOD

    return total_profit
    # Time: O(n log n + n * k)
    # Space: O(1)


def main():
    result = max_profit(inventory = [2,5], orders = 4)
    print(result) # 14

    result = max_profit(inventory = [3,5], orders = 6)
    print(result) # 19

if __name__ == "__main__":
    main()
