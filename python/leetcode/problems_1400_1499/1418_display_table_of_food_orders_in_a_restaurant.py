# -----------------------------------------------------
# 1418. Display Table of Food Orders in a Restaurant 🍜
# -----------------------------------------------------

# Problem: https://leetcode.com/problems/display-table-of-food-orders-in-a-restaurant
#
# Given the array orders, which represents the orders that customers have done in
# a restaurant. More specifically orders[i]=[customerNameᵢ, tableNumberᵢ, foodItemᵢ]
# where customerNameᵢ is the name of the customer, tableNumberᵢ is the table
# customer sit at, and foodItemᵢ is the item customer orders.
# 
# Return the restaurant's “display table”. The “display table” is a table whose
# row entries denote how many of each food item each table ordered. The first
# column is the table number and the remaining columns correspond to each food
# item in alphabetical order. The first row should be a header whose first column
# is “Table”, followed by the names of the food items. Note that the customer
# names are not part of the table. Additionally, the rows should be sorted in
# numerically increasing order.
# 
# Example 1:
# 
# Input: orders = [["David","3","Ceviche"],["Corina","10","Beef
# Burrito"],["David","3","Fried
# Chicken"],["Carla","5","Water"],["Carla","5","Ceviche"],["Rous","3","Ceviche"]]
# Output: [["Table","Beef Burrito","Ceviche","Fried Chicken","Water"],["3","0","2"
# ,"1","0"],["5","0","1","0","1"],["10","1","0","0","0"]]
# 
# Explanation:
# The displaying table looks like:
# Table,Beef Burrito,Ceviche,Fried Chicken,Water
# 3    ,0           ,2      ,1            ,0
# 5    ,0           ,1      ,0            ,1
# 10   ,1           ,0      ,0            ,0
# For the table 3: David orders "Ceviche" and "Fried Chicken", and Rous orders
# "Ceviche".
# For the table 5: Carla orders "Water" and "Ceviche".
# For the table 10: Corina orders "Beef Burrito".
# 
# Example 2:
# 
# Input: orders = [["James","12","Fried Chicken"],["Ratesh","12","Fried
# Chicken"],["Amadeus","12","Fried Chicken"],["Adam","1","Canadian
# Waffles"],["Brianna","1","Canadian Waffles"]]
# Output: [["Table","Canadian Waffles","Fried
# Chicken"],["1","2","0"],["12","0","3"]]
# 
# Explanation:
# For the table 1: Adam and Brianna order "Canadian Waffles".
# For the table 12: James, Ratesh and Amadeus order "Fried Chicken".
# 
# Example 3:
# 
# Input: orders = [["Laura","2","Bean Burrito"],["Jhon","2","Beef
# Burrito"],["Melissa","2","Soda"]]
# Output: [["Table","Bean Burrito","Beef Burrito","Soda"],["2","1","1","1"]]
# 
# 
# Constraints:
#   * 1 <= orders.length <= 5 * 10^4
#   * orders[i].length == 3
#   * 1 <= customerNameᵢ.length, foodItemᵢ.length <= 20
#   * customerNameᵢ and foodItemᵢ consist of lowercase and uppercase English
#     letters and the space character.
#   * tableNumberᵢ is a valid integer between 1 and 500.

from collections import defaultdict, Counter

# Solution: https://algo.monster/liteproblems/1418
# Credit: AlgoMonster
def display_table(orders):
    # Dictionary to store food items for each table
    # Key: table number (int), Value: list of food items
    table_orders = defaultdict(list)
    
    # Set to store all unique food items
    food_items = set()
    
    # Process each order to populate table_orders and food_items
    for customer_name, table_number, food_item in orders:
        table_orders[int(table_number)].append(food_item)
        food_items.add(food_item)
    
    # Sort food items alphabetically for column headers
    sorted_food_items = sorted(food_items)
    
    # Initialize result with header row
    result = [["Table"] + sorted_food_items]
    
    # Process each table in ascending order
    for table_number in sorted(table_orders):
        # Count occurrences of each food item for current table
        food_count = Counter(table_orders[table_number])
        
        # Build row: table number followed by count for each food item
        row = [str(table_number)] + [str(food_count[food_item]) for food_item in sorted_food_items]
        result.append(row)
    
    return result
    # Time: O(n + m × log m + k × log k + m × k)
    # Space: O(n + m + k)
    # m = the number of unique food items
    # k = the number of unique tables


def main():
    orders = [["David","3","Ceviche"],
              ["Corina","10","Beef Burrito"],
              ["David","3","Fried Chicken"],
              ["Carla","5","Water"],
              ["Carla","5","Ceviche"],
              ["Rous","3","Ceviche"]]
    result = display_table(orders)
    print(result) 
    # [['Table', 'Beef Burrito', 'Ceviche', 'Fried Chicken', 'Water'], 
    #  ['3', '0', '2', '1', '0'], 
    #  ['5', '0', '1', '0', '1'], 
    #  ['10', '1', '0', '0', '0']]

    orders = [["James","12","Fried Chicken"],
              ["Ratesh","12","Fried Chicken"],
              ["Amadeus","12","Fried Chicken"],
              ["Adam","1","Canadian Waffles"],
              ["Brianna","1","Canadian Waffles"]]
    result = display_table(orders)
    print(result) 
    # [['Table', 'Canadian Waffles', 'Fried Chicken'], 
    #  ['1', '2', '0'], 
    #  ['12', '0', '3']]

    orders = [["Laura","2","Bean Burrito"],
              ["Jhon","2","Beef Burrito"],
              ["Melissa","2","Soda"]]
    result = display_table(orders)
    print(result) 
    # [['Table', 'Bean Burrito', 'Beef Burrito', 'Soda'], 
    #  ['2', '1', '1', '1']]

if __name__ == "__main__":
    main()
