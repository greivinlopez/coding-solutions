# -----------------
# 36. Valid Sudoku
# -----------------

# Problem: https://leetcode.com/problems/valid-sudoku/
# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells 
# need to be validated according to the following rules:
# 
# - Each row must contain the digits 1-9 without repetition.
# - Each column must contain the digits 1-9 without repetition.
# - Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
# 
# Note:
# - A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# - Only the filled cells need to be validated according to the mentioned rules.

# Solution: https://youtu.be/TjFXEUCMqI8
# Credit: Navdeep Singh founder of NeetCode 
import collections
def is_valid_sudoku(board):
    cols = collections.defaultdict(set)
    rows = collections.defaultdict(set)
    squares = collections.defaultdict(set)  # key = (r /3, c /3)

    for r in range(9):
        for c in range(9):
            if board[r][c] == ".":
                continue
            if (
                board[r][c] in rows[r]
                or board[r][c] in cols[c]
                or board[r][c] in squares[(r // 3, c // 3)]
            ):
                return False
            cols[c].add(board[r][c])
            rows[r].add(board[r][c])
            squares[(r // 3, c // 3)].add(board[r][c])

    return True

# Solution: https://youtu.be/HyiAKwasi3M
# Credit: Greg Hogg
def is_valid_sudoku_alt(board):
    # Time: O(n^2)
    # Space: O(n)

    # Validate Rows
    for i in range(9):
        s = set()
        for j in range(9):
            item = board[i][j]
            if item in s:
                return False
            elif item != '.':
                s.add(item)
    
    # Validate Cols
    for i in range(9):
        s = set()
        for j in range(9):
            item = board[j][i]
            if item in s:
                return False
            elif item != '.':
                s.add(item)
        
    # Validate Boxes
    starts = [(0, 0), (0, 3), (0, 6),
                (3, 0), (3, 3), (3, 6),
                (6, 0), (6, 3), (6, 6)]
    
    for i, j in starts:
        s = set()
        for row in range(i, i+3):
            for col in range(j, j+3):
                item = board[row][col]
                if item in s:
                    return False
                elif item != '.':
                    s.add(item)
    return True

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
    result = is_valid_sudoku(board) # True
    print(result)

    board = [["8","3",".",".","7",".",".",".","."],
             ["6",".",".","1","9","5",".",".","."],
             [".","9","8",".",".",".",".","6","."],
             ["8",".",".",".","6",".",".",".","3"],
             ["4",".",".","8",".","3",".",".","1"],
             ["7",".",".",".","2",".",".",".","6"],
             [".","6",".",".",".",".","2","8","."],
             [".",".",".","4","1","9",".",".","5"],
             [".",".",".",".","8",".",".","7","9"]]
    result = is_valid_sudoku(board) # False
    print(result)

if __name__ == "__main__":
    main()