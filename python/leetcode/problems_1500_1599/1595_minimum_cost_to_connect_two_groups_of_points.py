# --------------------------------------------------
# 1595. Minimum Cost to Connect Two Groups of Points
# --------------------------------------------------

# Problem: https://leetcode.com/problems/minimum-cost-to-connect-two-groups-of-points
#
# You are given two groups of points where the first group has size₁ points, the
# second group has size₂ points, and size₁ >= size₂.
# 
# The cost of the connection between any two points are given in an size₁ x size₂
# matrix where cost[i][j] is the cost of connecting point i of the first group and
# point j of the second group. The groups are connected if each point in both
# groups is connected to one or more points in the opposite group. In other words,
# each point in the first group must be connected to at least one point in the
# second group, and each point in the second group must be connected to at least
# one point in the first group.
# 
# Return the minimum cost it takes to connect the two groups.
# 
# Example 1:
# 
# https://assets.leetcode.com/uploads/2020/09/03/ex1.jpg
# 
# Input: cost = [[15, 96], [36, 2]]
# Output: 17
# 
# Explanation: The optimal way of connecting the groups is:
# 1--A
# 2--B
# This results in a total cost of 17.
# 
# Example 2:
# 
# https://assets.leetcode.com/uploads/2020/09/03/ex2.jpg
# 
# Input: cost = [[1, 3, 5], [4, 1, 1], [1, 5, 3]]
# Output: 4
# 
# Explanation: The optimal way of connecting the groups is:
# 1--A
# 2--B
# 2--C
# 3--A
# This results in a total cost of 4.
# Note that there are multiple points connected to point 2 in the first group and
# point A in the second group. This does not matter as there is no limit to the
# number of points that can be connected. We only care about the minimum total
# cost.
# 
# Example 3:
# 
# Input: cost = [[2, 5, 1], [3, 4, 7], [8, 1, 2], [6, 2, 4], [3, 8, 8]]
# Output: 10
# 
# 
# Constraints:
#         size₁ == cost.length
#         size₂ == cost[i].length
#         1 <= size₁, size₂ <= 12
#         size₁ >= size₂
#         0 <= cost[i][j] <= 100


# Solution: https://algo.monster/liteproblems/1595
# Credit: AlgoMonster
def connect_two_groups(cost):
    # Get dimensions of the cost matrix
    group1_size, group2_size = len(cost), len(cost[0])
    
    # Initialize DP table
    # dp[i][mask] = minimum cost to connect first i points from group1
    # with points from group2 represented by mask
    dp = [[float('inf')] * (1 << group2_size) for _ in range(group1_size + 1)]
    
    # Base case: no points from group1 connected to empty set costs 0
    dp[0][0] = 0
    
    # Iterate through each point in group1
    for i in range(1, group1_size + 1):
        # Iterate through all possible subsets of group2 (represented as bitmask)
        for mask in range(1 << group2_size):
            # Try connecting current point from group1 to each point in group2
            for j in range(group2_size):
                # Check if j-th point of group2 is in the current mask
                if (mask >> j & 1) == 0:
                    continue
                
                # Cost of connecting (i-1)th point of group1 to j-th point of group2
                connection_cost = cost[i - 1][j]
                
                # Calculate minimum cost from three possible transitions:
                # 1. Current point reuses existing connection (dp[i][mask ^ (1 << j)])
                # 2. Previous points already covered this mask (dp[i - 1][mask])
                # 3. Add new connection from previous state (dp[i - 1][mask ^ (1 << j)])
                min_previous_cost = min(
                    dp[i][mask ^ (1 << j)],  # Remove j from mask for current row
                    dp[i - 1][mask],          # All connections already made by previous points
                    dp[i - 1][mask ^ (1 << j)]  # Add connection from previous row
                )
                
                # Update minimum cost for current state
                dp[i][mask] = min(dp[i][mask], min_previous_cost + connection_cost)
    
    # Return minimum cost when all points from both groups are connected
    # (all bits set in the mask)
    return dp[group1_size][(1 << group2_size) - 1]
    # Time: O(m * n * 2ⁿ)
    # Space: O(m * 2ⁿ)


def main():
    result = connect_two_groups(cost = [[15, 96], [36, 2]])
    print(result) # 17

    result = connect_two_groups(cost = [[1, 3, 5], [4, 1, 1], [1, 5, 3]])
    print(result) # 4

    result = connect_two_groups(cost = [[2, 5, 1], [3, 4, 7], [8, 1, 2], [6, 2, 4], [3, 8, 8]])
    print(result) # 10

if __name__ == "__main__":
    main()
