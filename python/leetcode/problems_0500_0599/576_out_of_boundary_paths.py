# -----------------------------
# 576. Out of Boundary Paths ⚽
# -----------------------------

# Problem: https://leetcode.com/problems/out-of-boundary-paths
#
# There is an m x n grid with a ball. The ball is initially at the position
# [startRow, startColumn]. You are allowed to move the ball to one of the four
# adjacent cells in the grid (possibly out of the grid crossing the grid
# boundary). You can apply at most maxMove moves to the ball.
# 
# Given the five integers m, n, maxMove, startRow, startColumn, return the number
# of paths to move the ball out of the grid boundary. Since the answer can be very
# large, return it modulo 10⁹ + 7.
# 
# Example 1:
# 
# Input: m = 2, n = 2, maxMove = 2, startRow = 0, startColumn = 0
# Output: 6
# 
# Example 2:
# 
# Input: m = 1, n = 3, maxMove = 3, startRow = 0, startColumn = 1
# Output: 12
# 
# 
# Constraints:
#         1 <= m, n <= 50
#         0 <= maxMove <= 50
#         0 <= startRow < m
#         0 <= startColumn < n


# Solution: https://youtu.be/Bg5CLRqtNmk
# Credit: Navdeep Singh founder of NeetCode
def find_paths(m, n, max_move, start_row, start_column):
    ROWS, COLS = m, n
    MOD = 10**9 + 7
    cache = {}

    def dfs(r, c, moves):
        if r < 0 or r == ROWS or c < 0 or c == COLS:
            return 1
        if moves == 0:
            return 0
        if (r, c, moves) in cache:
            return cache[(r, c, moves)]

        cache[(r, c, moves)] = (
            dfs(r + 1, c, moves - 1) +
            dfs(r - 1, c, moves - 1) +
            dfs(r, c + 1, moves - 1) +
            dfs(r, c - 1, moves - 1)
        ) % MOD
        return cache[(r, c, moves)]

    return dfs(start_row, start_column, max_move)
    # Time: O(m * n * max_move)
    # Space: O(m * n * max_move)

def find_paths_alt(m, n, max_move, start_row, start_column):
    # Dynamic programming solution
    ROWS, COLS = m, n
    MOD = 10**9 + 7
    grid = [[0] * COLS for r in range(ROWS)]

    for m in range(1, max_move + 1):
        tmp = [[0] * COLS for r in range(ROWS)]
        for r in range(ROWS):
            for c in range(COLS):
                if r + 1 == ROWS:
                    tmp[r][c] = (tmp[r][c] + 1) % MOD
                else:
                    tmp[r][c] = (tmp[r][c] + grid[r+1][c]) % MOD
                if r - 1 < 0:
                    tmp[r][c] = (tmp[r][c] + 1) % MOD
                else:
                    tmp[r][c] = (tmp[r][c] + grid[r-1][c]) % MOD
                if c + 1 == COLS:
                    tmp[r][c] = (tmp[r][c] + 1) % MOD
                else:
                    tmp[r][c] = (tmp[r][c] + grid[r][c+1]) % MOD
                if c - 1 < 0:
                    tmp[r][c] = (tmp[r][c] + 1) % MOD
                else:
                    tmp[r][c] = (tmp[r][c] + grid[r][c-1]) % MOD
        grid = tmp
    return grid[start_row][start_column]


def main():
    result = find_paths(m = 2, n = 2, max_move = 2, start_row = 0, start_column = 0)
    print(result) # 6

    result = find_paths(m = 1, n = 3, max_move = 3, start_row = 0, start_column = 1)
    print(result) # 12

if __name__ == "__main__":
    main()
