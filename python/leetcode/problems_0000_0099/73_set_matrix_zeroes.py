# -----------------------
# 73. Set Matrix Zeroes
# -----------------------

# Problem: https://leetcode.com/problems/set-matrix-zeroes/
# 
# Given an m x n integer matrix matrix, if an element is 0, set its entire 
# row and column to 0's.
# 
# You must do it in place.

# Solution: https://youtu.be/T41rL0L3Pnw
# Credit: Navdeep Singh founder of NeetCode 
def set_zeroes(matrix):
    # O(1)
    ROWS, COLS = len(matrix), len(matrix[0])
    rowZero = False

    # determine which rows/cols need to be zero
    for r in range(ROWS):
        for c in range(COLS):
            if matrix[r][c] == 0:
                matrix[0][c] = 0
                if r > 0:
                    matrix[r][0] = 0
                else:
                    rowZero = True

    for r in range(1, ROWS):
        for c in range(1, COLS):
            if matrix[0][c] == 0 or matrix[r][0] == 0:
                matrix[r][c] = 0

    if matrix[0][0] == 0:
        for r in range(ROWS):
            matrix[r][0] = 0

    if rowZero:
        for c in range(COLS):
            matrix[0][c] = 0


def main():
    matrix = [[1,1,1],[1,0,1],[1,1,1]]
    set_zeroes(matrix) 
    # Expected Output: [[1,0,1],[0,0,0],[1,0,1]]
    print(matrix)
    matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    set_zeroes(matrix)
    # Expected Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
    print(matrix)

if __name__ == "__main__":
    main()