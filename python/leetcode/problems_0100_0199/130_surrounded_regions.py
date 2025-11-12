# ------------------------
# 130. Surrounded Regions
# ------------------------

# Problem: https://leetcode.com/problems/surrounded-regions/
# 
# You are given an m x n matrix board containing letters 'X' and 'O', capture 
# regions that are surrounded:
# 
# - Connect: A cell is connected to adjacent cells horizontally or vertically.
# - Region: To form a region connect every 'O' cell.
# - Surround: The region is surrounded with 'X' cells if you can connect the 
# region with 'X' cells and none of the region cells are on the edge of the board.
# 
# To capture a surrounded region, replace all 'O's with 'X's in-place within 
# the original board. You do not need to return anything.

# Solution: https://youtu.be/9z2BunfoZ5Y
# Credit: Navdeep Singh founder of NeetCode
def solve(board):
    rows, cols = len(board), len(board[0])
    flag = set()

    def dfs(r, c):
        if not(r in range(rows) and c in range(cols)) or board[r][c] != 'O' or (r, c) in flag:
            return
        flag.add((r, c))
        return (dfs(r + 1, c), dfs(r - 1, c), dfs(r, c + 1), dfs(r, c - 1))

    # traverse through the board
    for r in range(rows):
        for c in range(cols):
            if( (r == 0 or c == 0 or r == rows - 1 or c == cols - 1) and board[r][c] == 'O'):
                dfs(r, c)

    # set all of the 'X's to 'O's
    for r in range(rows):
        for c in range(cols):
            if board[r][c] == 'O' and (r, c) not in flag:
                board[r][c] = 'X'


def main():
    board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
    solve(board)
    print(board) # [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]

    board = [["X"]]
    solve(board)
    print(board) # [["X"]]

if __name__ == "__main__":
    main()