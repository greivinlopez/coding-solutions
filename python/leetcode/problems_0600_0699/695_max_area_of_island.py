# --------------------------
# 695. Max Area Of Island 🏝️
# --------------------------

# Problem: https://leetcode.com/problems/max-area-of-island/
# 
# You are given an m x n binary matrix grid. An island is a group of 1's 
# (representing land) connected 4-directionally (horizontal or vertical.) 
# You may assume all four edges of the grid are surrounded by water.
# 
# The area of an island is the number of cells with a value 1 in the island.
# 
# Return the maximum area of an island in grid. If there is no island, 
# return 0.
# 
#  
# Example 1:
# 
# https://assets.leetcode.com/uploads/2021/05/01/maxarea1-grid.jpg
# 
# Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
# Output: 6
# Explanation: The answer is not 11, because the island must be connected 4-directionally.
# 
# 
# Example 2:
# 
# Input: grid = [[0,0,0,0,0,0,0,0]]
# Output: 0
# 
# 
# Constraints:
# 
# 	m == grid.length
# 	n == grid[i].length
# 	1 <= m, n <= 50
# 	grid[i][j] is either 0 or 1.


# Solution: https://youtu.be/iJGr1OtmH0c
# Credit: Navdeep Singh founder of NeetCode
def max_area_of_island(grid):
    ROWS, COLS = len(grid), len(grid[0])
    visit = set()

    def dfs(r, c):
        if (
            r < 0
            or r == ROWS
            or c < 0
            or c == COLS
            or grid[r][c] == 0
            or (r, c) in visit
        ):
            return 0
        visit.add((r, c))
        return 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)

    area = 0
    for r in range(ROWS):
        for c in range(COLS):
            area = max(area, dfs(r, c))
    return area
    # Time: O(r * c)
    # Space: O(r * c)


# Solution: https://youtu.be/rowp_Frq_eI
# Credit: Greg Hogg
def max_area_of_island(grid):
    m = len(grid)
    n = len(grid[0])

    def dfs(i, j):
        if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] != 1:
            return 0
        else:
            grid[i][j] = 0
            return 1 + dfs(i + 1, j) + dfs(i, j - 1) + dfs(i - 1, j) + dfs(i, j + 1)

    max_area = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                max_area = max(max_area, dfs(i, j))

    return max_area
    # Time: O(m * n)
    # Space: O(m * n)


def main():
    grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
            [0,0,0,0,0,0,0,1,1,1,0,0,0],
            [0,1,1,0,1,0,0,0,0,0,0,0,0],
            [0,1,0,0,1,1,0,0,1,0,1,0,0],
            [0,1,0,0,1,1,0,0,1,1,1,0,0],
            [0,0,0,0,0,0,0,0,0,0,1,0,0],
            [0,0,0,0,0,0,0,1,1,1,0,0,0],
            [0,0,0,0,0,0,0,1,1,0,0,0,0]]
    result = max_area_of_island(grid)
    print(result) # 6

    grid = [[0,0,0,0,0,0,0,0]]
    result = max_area_of_island(grid)
    print(result) # 0

if __name__ == "__main__":
    main()
