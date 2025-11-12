# ---------------------
# 867. Transpose Matrix
# ---------------------

# Problem: https://leetcode.com/problems/transpose-matrix
#
# Given a 2D integer array matrix, return the transpose of matrix.
# 
# The transpose of a matrix is the matrix flipped over its main diagonal,
# switching the matrix's row and column indices.
# 
# https://assets.leetcode.com/uploads/2021/02/10/hint_transpose.png
# 
# Example 1:
# 
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[1,4,7],[2,5,8],[3,6,9]]
# 
# Example 2:
# 
# Input: matrix = [[1,2,3],[4,5,6]]
# Output: [[1,4],[2,5],[3,6]]
# 
# 
# Constraints:
#         m == matrix.length
#         n == matrix[i].length
#         1 <= m, n <= 1000
#         1 <= m * n <= 10⁵
#         -10⁹ <= matrix[i][j] <= 10⁹


# Solution: https://youtu.be/DzMT3bDgVn0
# Credit: Navdeep Singh founder of NeetCode
def transpose_matrix(matrix):
    ROWS, COLS = len(matrix), len(matrix[0])
    res = [[0] * ROWS for _ in range(COLS)]
    
    for r in range(ROWS):
        for c in range(COLS):
            res[c][r] = matrix[r][c]
            
    return res
    # Time: O(r * c)
    # Space: O(r * c)


def main():
    result = transpose_matrix(matrix = [[1,2,3],[4,5,6],[7,8,9]])
    print(result) # [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

    result = transpose_matrix(matrix = [[1,2,3],[4,5,6]])
    print(result) # [[1, 4], [2, 5], [3, 6]]

if __name__ == "__main__":
    main()
