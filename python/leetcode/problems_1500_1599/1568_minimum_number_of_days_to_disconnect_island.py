# ----------------------------------------------------
# 1568. Minimum Number of Days to Disconnect Island 🏝️
# ----------------------------------------------------

# Problem: https://leetcode.com/problems/minimum-number-of-days-to-disconnect-island
#
# You are given an m x n binary grid grid where 1 represents land and 0 represents
# water. An island is a maximal 4-directionally (horizontal or vertical) connected
# group of 1's.
# 
# The grid is said to be connected if we have exactly one island, otherwise is
# said disconnected.
# 
# In one day, we are allowed to change any single land cell (1) into a water cell
# (0).
# 
# Return the minimum number of days to disconnect the grid.
# 
# Example 1:
# 
# https://assets.leetcode.com/uploads/2021/12/24/land1.jpg
# 
# Input: grid = [[0,1,1,0],[0,1,1,0],[0,0,0,0]]
# Output: 2
# 
# Explanation: We need at least 2 days to get a disconnected grid.
# Change land grid[1][1] and grid[0][2] to water and get 2 disconnected island.
# 
# Example 2:
# 
# https://assets.leetcode.com/uploads/2021/12/24/land2.jpg
# 
# Input: grid = [[1,1]]
# Output: 2
# 
# Explanation: Grid of full water is also disconnected ([[1,1]] -> [[0,0]]), 0
# islands.
# 
# 
# Constraints:
#         m == grid.length
#         n == grid[i].length
#         1 <= m, n <= 30
#         grid[i][j] is either 0 or 1.


# Solution: https://youtu.be/aO-QbJ5eZwU
# Credit: Navdeep Singh founder of NeetCode
def min_days(grid):
    ROWS, COLS = len(grid), len(grid[0])

    def dfs(r, c, visit):
        if (r < 0 or c < 0 or r == ROWS or c == COLS
            or grid[r][c] == 0 or (r, c) in visit):
            return
        visit.add((r, c))
        neighbors = [[r+1, c], [r,c+1], [r-1,c], [r,c-1]]
        for nr, nc in neighbors:
            dfs(nr, nc, visit)

    visit = set()
    count = 0
    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] and (r, c) not in visit:
                dfs(r, c, visit)
                count += 1
                
    if count != 1:
        return 0
    
    land = list(visit)
    for r, c in land:
        grid[r][c] = 0

        visit = set()
        count = 0
        for r2 in range(ROWS):
            for c2 in range(COLS):
                if grid[r2][c2] and (r2, c2) not in visit:
                    dfs(r2, c2, visit)
                    count += 1
        if count != 1:
            return 1
        grid[r][c] = 1

    return 2
    # Time: O((r * c)^2)
    # Space: O(r * c)


def main():
    result = min_days([[0,1,1,0],[0,1,1,0],[0,0,0,0]])
    print(result) # 2

    result = min_days([[1,1]])
    print(result) # 2

if __name__ == "__main__":
    main()
