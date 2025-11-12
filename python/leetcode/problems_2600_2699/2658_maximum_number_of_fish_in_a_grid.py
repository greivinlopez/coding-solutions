# -----------------------------------------
# 2658. Maximum Number of Fish in a Grid 🐟
# -----------------------------------------

# Problem: https://leetcode.com/problems/maximum-number-of-fish-in-a-grid
#
# You are given a 0-indexed 2D matrix grid of size m x n, where (r, c) represents:
#         
#   * A land cell if grid[r][c] = 0, or
#   * A water cell containing grid[r][c] fish, if grid[r][c] > 0.
# 
# A fisher can start at any water cell (r, c) and can do the following operations
# any number of times:
#         
#   * Catch all the fish at cell (r, c), or
#   * Move to any adjacent water cell.
# 
# Return the maximum number of fish the fisher can catch if he chooses his
# starting cell optimally, or 0 if no water cell exists.
# 
# An adjacent cell of the cell (r, c), is one of the cells (r, c + 1), (r, c - 1),
# (r + 1, c) or (r - 1, c) if it exists.
# 
# Example 1:
# 
# Input: grid = [[0,2,1,0],[4,0,0,3],[1,0,0,4],[0,3,2,0]]
# Output: 7
# 
# Explanation: The fisher can start at cell (1,3) and collect 3 fish, then move to
# cell (2,3) and collect 4 fish.
# 
# Example 2:
# 
# Input: grid = [[1,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,1]]
# Output: 1
# 
# Explanation: The fisher can start at cells (0,0) or (3,3) and collect a single
# fish.
# 
# 
# Constraints:
#         m == grid.length
#         n == grid[i].length
#         1 <= m, n <= 10
#         0 <= grid[i][j] <= 10


# Solution: https://youtu.be/JhAz6CkRGHI
# Credit: Navdeep Singh founder of NeetCode
def find_max_fish(grid):
    ROWS, COLS = len(grid), len(grid[0])
    res = 0
    visit = [[False] * COLS for _ in range(ROWS)]

    def dfs(r, c):
        if (
            r < 0 or c < 0 or
            r == ROWS or c == COLS or
            grid[r][c] == 0 or visit[r][c]
        ):
            return 0

        visit[r][c] = True
        current_fish = grid[r][c]
        
        # Sum up fish from neighboring cells
        current_fish += dfs(r + 1, c)
        current_fish += dfs(r - 1, c)
        current_fish += dfs(r, c + 1)
        current_fish += dfs(r, c - 1)
        
        return current_fish

    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] > 0 and not visit[r][c]:
                res = max(res, dfs(r, c))

    return res
    # Time: O(r * c) 
    # Space: O(r * c)


def main():
    grid = [[0,2,1,0],[4,0,0,3],[1,0,0,4],[0,3,2,0]]
    result = find_max_fish(grid)
    print(result) # 7

    grid = [[1,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,1]]
    result = find_max_fish(grid)
    print(result) # 1

if __name__ == "__main__":
    main()
