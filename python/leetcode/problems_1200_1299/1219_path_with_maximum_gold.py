# ----------------------------
# 1219. Path with Maximum Gold
# ----------------------------

# Problem: https://leetcode.com/problems/path-with-maximum-gold
#
# In a gold mine grid of size m x n, each cell in this mine has an integer
# representing the amount of gold in that cell, 0 if it is empty.
# 
# Return the maximum amount of gold you can collect under the conditions:
#         
#   * Every time you are located in a cell you will collect all the gold in
#     that cell.
#   * From your position, you can walk one step to the left, right, up, or down.
#   * You can't visit the same cell more than once.
#   * Never visit a cell with 0 gold.
#   * You can start and stop collecting gold from any position in the grid
#     that has some gold.
# 
# Example 1:
# 
# Input: grid = [[0,6,0],[5,8,7],[0,9,0]]
# Output: 24
# 
# Explanation:
# [[0,6,0],
#  [5,8,7],
#  [0,9,0]]
# Path to get the maximum gold, 9 -> 8 -> 7.
# 
# Example 2:
# 
# Input: grid = [[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]
# Output: 28
# 
# Explanation:
# [[1,0,7],
#  [2,0,6],
#  [3,4,5],
#  [0,3,0],
#  [9,0,20]]
# Path to get the maximum gold, 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7.
# 
# 
# Constraints:
#         m == grid.length
#         n == grid[i].length
#         1 <= m, n <= 15
#         0 <= grid[i][j] <= 100
#         There are at most 25 cells containing gold.

# Solution: https://youtu.be/I1wllM_pozY
# Credit: Navdeep Singh founder of NeetCode
def get_maximum_gold(grid):
    ROWS, COLS = len(grid), len(grid[0])
    
    def dfs(r, c):
        if (
            min(r, c) < 0 or r == ROWS or c == COLS or
            grid[r][c] == 0
        ):
            return 0
        tmp = grid[r][c]
        grid[r][c] = 0
        res = 0
        neighbors = [[r + 1, c], [r - 1, c], [r, c + 1], [r, c - 1]]
        for r2, c2 in neighbors:
            res = max(res, tmp + dfs(r2, c2))
        grid[r][c] = tmp
        return res
    
    res = 0
    for r in range(ROWS):
        for c in range(COLS):
            res = max(res, dfs(r, c))
    
    return res
    # Time: O(rows * cols * 4^(rows * cols))
    # Space:O(rows * cols)


def main():
    grid = [[0,6,0],[5,8,7],[0,9,0]]
    result = get_maximum_gold(grid)
    print(result) # 24

    grid = [[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]
    result = get_maximum_gold(grid)
    print(result) # 28

if __name__ == "__main__":
    main()
