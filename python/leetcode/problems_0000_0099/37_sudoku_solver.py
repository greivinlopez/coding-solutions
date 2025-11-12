# -----------------
# 37. Sudoku Solver
# -----------------

# Problem: https://leetcode.com/problems/sudoku-solver
#
# Write a program to solve a Sudoku puzzle by filling the empty cells.
# 
# A sudoku solution must satisfy all of the following rules:
# 
#   * Each of the digits 1-9 must occur exactly once in each row.
#   * Each of the digits 1-9 must occur exactly once in each column.
#   * Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-
#     boxes of the grid.
# 
# The '.' character indicates empty cells.
# 
# Example 1:
# 
# https://upload.wikimedia.org/wikipedia/commons/thumb/f/ff/Sudoku-by-L2G-20050714.svg/250px-Sudoku-by-L2G-20050714.svg.png
# 
# Input: board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5","
# .",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".","
# .","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","
# 6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],
# [".",".",".",".","8",".",".","7","9"]]
# Output: [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4",
# "8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"]
# ,["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9
# ","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4
# ","5","2","8","6","1","7","9"]]
# 
# Explanation: The input board is shown above and the only valid solution is shown
# below:
# https://upload.wikimedia.org/wikipedia/commons/thumb/3/31/Sudoku-by-L2G-20050714_solution.svg/250px-Sudoku-by-L2G-20050714_solution.svg.png
# 
# 
# Constraints:
#         board.length == 9
#         board[i].length == 9
#         board[i][j] is a digit or '.'.
#         It is guaranteed that the input board has only one solution.


# Credit: Jeel Gajera -> https://github.com/JeelGajera
def solve_sudoku(board):
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    grids = [set() for _ in range(9)]

    for r in range(9):
        for c in range(9):
            if board[r][c] != ".":
                num = int(board[r][c])
                rows[r].add(num)
                cols[c].add(num)
                grids[r//3 * 3 + c//3].add(num)

    def backtrack(r,c):
        nonlocal solved
        if r == 9:
            solved = True
            return

        new_r = r + (c+1)//9
        new_c = (c+1) % 9

        if board[r][c] != ".":
            backtrack(new_r, new_c)
        else:
            grid_idx = r//3 * 3 + c//3
            for num in range(1,10):
                if (num not in rows[r]) and (num not in cols[c]) and (num not in grids[grid_idx]):
                    rows[r].add(num)
                    cols[c].add(num)
                    grids[grid_idx].add(num)
                    board[r][c] = str(num)

                    backtrack(new_r, new_c)

                    if not solved:
                        rows[r].remove(num)
                        cols[c].remove(num)
                        grids[grid_idx].remove(num)
                        board[r][c] = "."

    solved = False
    backtrack(0,0)
    # Time: O(9ⁿ)
    # Space: O(1)
    # n = number of empty cells 


def main():
    board = [["5","3",".",".","7",".",".",".","."],
             ["6",".",".","1","9","5",".",".","."],
             [".","9","8",".",".",".",".","6","."],
             ["8",".",".",".","6",".",".",".","3"],
             ["4",".",".","8",".","3",".",".","1"],
             ["7",".",".",".","2",".",".",".","6"],
             [".","6",".",".",".",".","2","8","."],
             [".",".",".","4","1","9",".",".","5"],
             [".",".",".",".","8",".",".","7","9"]]
    solve_sudoku(board)
    print(board) # True
    # [['5', '3', '4', '6', '7', '8', '9', '1', '2'], 
    #  ['6', '7', '2', '1', '9', '5', '3', '4', '8'], 
    #  ['1', '9', '8', '3', '4', '2', '5', '6', '7'], 
    #  ['8', '5', '9', '7', '6', '1', '4', '2', '3'], 
    #  ['4', '2', '6', '8', '5', '3', '7', '9', '1'], 
    #  ['7', '1', '3', '9', '2', '4', '8', '5', '6'], 
    #  ['9', '6', '1', '5', '3', '7', '2', '8', '4'], 
    #  ['2', '8', '7', '4', '1', '9', '6', '3', '5'], 
    #  ['3', '4', '5', '2', '8', '6', '1', '7', '9']]

if __name__ == "__main__":
    main()
