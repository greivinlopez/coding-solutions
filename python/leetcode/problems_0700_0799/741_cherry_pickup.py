# ---------------------
# 741. Cherry Pickup 🍒
# ---------------------

# Problem: https://leetcode.com/problems/cherry-pickup
#
# You are given an n x n grid representing a field of cherries, each cell is one
# of three possible integers.
#         
#   * 0 means the cell is empty, so you can pass through,
#   * 1 means the cell contains a cherry that you can pick up and pass through, or
#   * -1 means the cell contains a thorn that blocks your way.
# 
# Return the maximum number of cherries you can collect by following the rules
# below:
#         
#   * Starting at the position (0, 0) and reaching (n - 1, n - 1) by moving
#     right or down through valid path cells (cells with value 0 or 1).
#   * After reaching (n - 1, n - 1), returning to (0, 0) by moving left or up
#     through valid path cells.
#   * When passing through a path cell containing a cherry, you pick it up,
#     and the cell becomes an empty cell 0.
#   * If there is no valid path between (0, 0) and (n - 1, n - 1), then no
#     cherries can be collected.
# 
# Example 1:
# 
# https://assets.leetcode.com/uploads/2020/12/14/grid.jpg
# 
# Input: grid = [[0,1,-1],[1,0,-1],[1,1,1]]
# Output: 5
# 
# Explanation: The player started at (0, 0) and went down, down, right right to
# reach (2, 2).
# 4 cherries were picked up during this single trip, and the matrix becomes
# [[0,1,-1],[0,0,-1],[0,0,0]].
# Then, the player went left, up, up, left to return home, picking up one more
# cherry.
# The total number of cherries picked up is 5, and this is the maximum possible.
# 
# Example 2:
# 
# Input: grid = [[1,1,-1],[1,-1,1],[-1,1,1]]
# Output: 0
# 
# 
# Constraints:
#         n == grid.length
#         n == grid[i].length
#         1 <= n <= 50
#         grid[i][j] is -1, 0, or 1.
#         grid[0][0] != -1
#         grid[n - 1][n - 1] != -1


# Solution: https://algo.monster/liteproblems/741
# Credit: AlgoMonster
def cherry_pickup(grid):
    n = len(grid)
    
    # dp[k][i1][i2] represents the maximum cherries collected when:
    # - Person 1 is at position (i1, j1) where j1 = k - i1
    # - Person 2 is at position (i2, j2) where j2 = k - i2
    # - k represents the sum of coordinates (i + j), indicating the step number
    dp = [[[-float('inf')] * n for _ in range(n)] for _ in range(2 * n - 1)]
    
    # Initialize starting position - both persons start at (0, 0)
    dp[0][0][0] = grid[0][0]
    
    # Iterate through each step (k represents Manhattan distance from origin)
    for k in range(1, 2 * n - 1):
        for row1 in range(n):
            for row2 in range(n):
                # Calculate column positions based on current step and row
                col1 = k - row1
                col2 = k - row2
                
                # Check if positions are valid and not blocked by thorns
                if (not 0 <= col1 < n or 
                    not 0 <= col2 < n or 
                    grid[row1][col1] == -1 or 
                    grid[row2][col2] == -1):
                    continue
                
                # Calculate cherries to pick at current positions
                cherries_picked = grid[row1][col1]
                # Avoid double counting if both persons are at the same cell
                if row1 != row2:
                    cherries_picked += grid[row2][col2]
                
                # Check all possible previous positions for both persons
                # Each person could have come from either up or left
                for prev_row1 in range(row1 - 1, row1 + 1):
                    for prev_row2 in range(row2 - 1, row2 + 1):
                        # Ensure previous positions are within bounds
                        if prev_row1 >= 0 and prev_row2 >= 0:
                            dp[k][row1][row2] = max(
                                dp[k][row1][row2], 
                                dp[k - 1][prev_row1][prev_row2] + cherries_picked
                            )
    
    # Return the maximum cherries collected, or 0 if no valid path exists
    return max(0, dp[-1][-1][-1])
    # Time: O(n³)
    # Space: O(n³)


def main():
    result = cherry_pickup(grid = [[0,1,-1],[1,0,-1],[1,1,1]])
    print(result) # 5

    result = cherry_pickup([[1,1,-1],[1,-1,1],[-1,1,1]])
    print(result) # 0

if __name__ == "__main__":
    main()
