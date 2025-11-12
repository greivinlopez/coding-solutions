# ----------------
# 51. N-Queens ♟️
# ----------------

# Problem: https://leetcode.com/problems/n-queens/
# The n-queens puzzle is the problem of placing n queens on an n x n chessboard 
# such that no two queens attack each other.
# 
# Given an integer n, return all distinct solutions to the n-queens puzzle. 
# You may return the answer in any order.
# 
# Each solution contains a distinct board configuration of the n-queens' placement, 
# where 'Q' and '.' both indicate a queen and an empty space, respectively.

# Solution: https://youtu.be/Ph95IHmRp5M
# Credit: Navdeep Singh founder of NeetCode 
def solve_n_queens(n):
    col = set()
    posDiag = set()  # (r + c)
    negDiag = set()  # (r - c)

    res = []
    board = [["."] * n for i in range(n)]

    def backtrack(r):
        if r == n:
            copy = ["".join(row) for row in board]
            res.append(copy)
            return

        for c in range(n):
            if c in col or (r + c) in posDiag or (r - c) in negDiag:
                continue

            col.add(c)
            posDiag.add(r + c)
            negDiag.add(r - c)
            board[r][c] = "Q"

            backtrack(r + 1)

            col.remove(c)
            posDiag.remove(r + c)
            negDiag.remove(r - c)
            board[r][c] = "."

    backtrack(0)
    return res

def main():
    result = solve_n_queens(4)
    # Expected Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
    print(result)
    result = solve_n_queens(1)
    # Expected Output: [["Q"]]
    print(result)

if __name__ == "__main__":
    main()