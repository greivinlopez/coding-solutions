# -------------------
# 1518. Water Bottles
# -------------------

# Problem: https://leetcode.com/problems/water-bottles
#
# There are numBottles water bottles that are initially full of water. You can
# exchange numExchange empty water bottles from the market with one full water
# bottle.
# 
# The operation of drinking a full water bottle turns it into an empty bottle.
# 
# Given the two integers numBottles and numExchange, return the maximum number of
# water bottles you can drink.
# 
# Example 1:
# 
# Input: numBottles = 9, numExchange = 3
# Output: 13
# 
# Explanation: You can exchange 3 empty bottles to get 1 full water bottle.
# Number of water bottles you can drink: 9 + 3 + 1 = 13.
# 
# Example 2:
# 
# Input: numBottles = 15, numExchange = 4
# Output: 19
# 
# Explanation: You can exchange 4 empty bottles to get 1 full water bottle.
# Number of water bottles you can drink: 15 + 3 + 1 = 19.
# 
# 
# Constraints:
#         1 <= numBottles <= 100
#         2 <= numExchange <= 100


# Solution: https://youtu.be/V4d6xym5efE
# Credit: Navdeep Singh founder of NeetCode
def num_water_bottles(numBottles, numExchange):
    res = 0
    empty = 0
    while numBottles > 0:
        res += numBottles
        empty += numBottles
        numBottles = empty // numExchange
        empty = empty % numExchange
    return res
    # Time: O(log(n))
    # Space: O(1)


def main():
    result = num_water_bottles(numBottles = 9, numExchange = 3)
    print(result) # 13

    result = num_water_bottles(numBottles = 15, numExchange = 4)
    print(result) # 19

if __name__ == "__main__":
    main()
