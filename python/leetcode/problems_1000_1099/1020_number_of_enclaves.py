# -----------------------
# 1020. Number Of Enclaves
# -----------------------

# Problem: https://leetcode.com/problems/number-of-enclaves
#
# You are given an m x n binary matrix grid, where 0 represents a sea cell and 1
# represents a land cell.
# 
# A move consists of walking from one land cell to another adjacent
# (4-directionally) land cell or walking off the boundary of the grid.
# 
# Return the number of land cells in grid for which we cannot walk off the
# boundary of the grid in any number of moves.
# 
# Example 1:
# 
# https://assets.leetcode.com/uploads/2021/08/05/linkedlistnext1.jpg
# 
# Input: grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
# Output: 3
# Explanation: There are three 1s that are enclosed by 0s, and one 1 that is not
# enclosed because its on the boundary.
# 
# Example 2:
# 
# https://assets.leetcode.com/uploads/2021/08/05/linkedlistnext2.jpg
# 
# Input: grid = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
# Output: 0
# 
# Explanation: All 1s are either on the boundary or can reach the boundary.
# 
# 
# Constraints:
#         m == grid.length
#         n == grid[i].length
#         1 <= m, n <= 500
#         grid[i][j] is either 0 or 1.


# Solution: https://youtu.be/gf0zsh1FIgE
# Credit: Navdeep Singh founder of NeetCode
def num_enclaves(grid):
    ROWS, COLS = len(grid), len(grid[0])

    def dfs(grid, row, col):
        if 0 <= row < ROWS and 0 <= col < COLS:
            if grid[row][col] == 1:
                grid[row][col] = 0
                dfs(grid, row + 1, col)
                dfs(grid, row - 1, col)
                dfs(grid, row, col + 1)
                dfs(grid, row, col - 1)
            
    for row in range(ROWS):
        dfs(grid, row, 0)
        dfs(grid, row, COLS - 1)

    for col in range(COLS):
        dfs(grid, 0, col)
        dfs(grid, ROWS - 1, col)

    return sum(grid[row][col] == 1 for row in range(ROWS) for col in range(COLS))


def main():
    result = num_enclaves([[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]])
    print(result) # 3

    result = num_enclaves([[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]])
    print(result) # 0

if __name__ == "__main__":
    main()
