# ---------------------
# 1473. Paint House III
# ---------------------

# Problem: https://leetcode.com/problems/paint-house-iii
#
# There is a row of m houses in a small city, each house must be painted with one
# of the n colors (labeled from 1 to n), some houses that have been painted last
# summer should not be painted again.
# 
# A neighborhood is a maximal group of continuous houses that are painted with the
# same color.
#         
#   * For example: houses = [1,2,2,3,3,2,1,1] contains 5 neighborhoods [{1},
#     {2,2}, {3,3}, {2}, {1,1}].
# 
# Given an array houses, an m x n matrix cost and an integer target where:
#         
#   * houses[i]: is the color of the house i, and 0 if the house is not painted yet.
#   * cost[i][j]: is the cost of paint the house i with the color j + 1.
# 
# Return the minimum cost of painting all the remaining houses in such a way that
# there are exactly target neighborhoods. If it is not possible, return -1.
# 
# Example 1:
# 
# Input: houses = [0,0,0,0,0], cost = [[1,10],[10,1],[10,1],[1,10],[5,1]], m = 5,
# n = 2, target = 3
# Output: 9
# 
# Explanation: Paint houses of this way [1,2,2,1,1]
# This array contains target = 3 neighborhoods, [{1}, {2,2}, {1,1}].
# Cost of paint all houses (1 + 1 + 1 + 1 + 5) = 9.
# 
# Example 2:
# 
# Input: houses = [0,2,1,2,0], cost = [[1,10],[10,1],[10,1],[1,10],[5,1]], m = 5,
# n = 2, target = 3
# Output: 11
# 
# Explanation: Some houses are already painted, Paint the houses of this way
# [2,2,1,2,2]
# This array contains target = 3 neighborhoods, [{2,2}, {1}, {2,2}].
# Cost of paint the first and last house (10 + 1) = 11.
# 
# Example 3:
# 
# Input: houses = [3,1,2,3], cost = [[1,1,1],[1,1,1],[1,1,1],[1,1,1]], m = 4, n =
# 3, target = 3
# Output: -1
# 
# Explanation: Houses are already painted with a total of 4 neighborhoods
# [{3},{1},{2},{3}] different of target = 3.
# 
# 
# Constraints:
#         m == houses.length == cost.length
#         n == cost[i].length
#         1 <= m <= 100
#         1 <= n <= 20
#         1 <= target <= m
#         0 <= houses[i] <= n
#         1 <= cost[i][j] <= 10⁴


# Solution: https://algo.monster/liteproblems/1473
# Credit: AlgoMonster
def min_cost(houses, cost, m, n, target):
    # Initialize DP table: dp[house_idx][color][num_neighborhoods]
    # dp[i][j][k] = minimum cost to paint houses 0..i where house i has color j 
    # and forms exactly k neighborhoods
    INF = float('inf')
    dp = [[[INF] * (target + 1) for _ in range(n + 1)] for _ in range(m)]
    
    # Base case: handle the first house
    if houses[0] == 0:
        # First house is unpainted, try all possible colors
        for color_idx, paint_cost in enumerate(cost[0], 1):
            dp[0][color_idx][1] = paint_cost
    else:
        # First house is already painted, no cost needed
        dp[0][houses[0]][1] = 0
    
    # Fill the DP table for remaining houses
    for house_idx in range(1, m):
        if houses[house_idx] == 0:
            # Current house is unpainted, try all possible colors
            for current_color in range(1, n + 1):
                # Try different numbers of neighborhoods (up to house_idx + 1)
                for num_neighborhoods in range(1, min(target + 1, house_idx + 2)):
                    # Consider all possible colors of the previous house
                    for prev_color in range(1, n + 1):
                        if current_color == prev_color:
                            # Same color as previous house, no new neighborhood
                            dp[house_idx][current_color][num_neighborhoods] = min(
                                dp[house_idx][current_color][num_neighborhoods],
                                dp[house_idx - 1][prev_color][num_neighborhoods] + cost[house_idx][current_color - 1]
                            )
                        else:
                            # Different color from previous house, creates new neighborhood
                            dp[house_idx][current_color][num_neighborhoods] = min(
                                dp[house_idx][current_color][num_neighborhoods],
                                dp[house_idx - 1][prev_color][num_neighborhoods - 1] + cost[house_idx][current_color - 1]
                            )
        else:
            # Current house is already painted with a specific color
            current_color = houses[house_idx]
            # Try different numbers of neighborhoods
            for num_neighborhoods in range(1, min(target + 1, house_idx + 2)):
                # Consider all possible colors of the previous house
                for prev_color in range(1, n + 1):
                    if current_color == prev_color:
                        # Same color as previous house, no new neighborhood
                        dp[house_idx][current_color][num_neighborhoods] = min(
                            dp[house_idx][current_color][num_neighborhoods],
                            dp[house_idx - 1][prev_color][num_neighborhoods]
                        )
                    else:
                        # Different color from previous house, creates new neighborhood
                        dp[house_idx][current_color][num_neighborhoods] = min(
                            dp[house_idx][current_color][num_neighborhoods],
                            dp[house_idx - 1][prev_color][num_neighborhoods - 1]
                        )
    
    # Find the minimum cost among all possible colors for the last house
    # with exactly target neighborhoods
    min_cost = min(dp[-1][color][target] for color in range(1, n + 1))
    
    # Return -1 if impossible, otherwise return the minimum cost
    return -1 if min_cost >= INF else min_cost
    # Time: O(m * n² * target)
    # Space: O(m * n * target)


def main():
    result = min_cost(houses = [0,0,0,0,0], cost = [[1,10],[10,1],[10,1],[1,10],[5,1]], m = 5, n = 2, target = 3)
    print(result) # 9

    result = min_cost(houses = [0,2,1,2,0], cost = [[1,10],[10,1],[10,1],[1,10],[5,1]], m = 5, n = 2, target = 3)
    print(result) # 11

    result = min_cost(houses = [3,1,2,3], cost = [[1,1,1],[1,1,1],[1,1,1],[1,1,1]], m = 4, n = 3, target = 3)
    print(result) # -1

if __name__ == "__main__":
    main()
