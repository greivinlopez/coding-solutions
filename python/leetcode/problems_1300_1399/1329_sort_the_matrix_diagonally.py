# --------------------------------
# 1329. Sort the Matrix Diagonally
# --------------------------------

# Problem: https://leetcode.com/problems/sort-the-matrix-diagonally
#
# A matrix diagonal is a diagonal line of cells starting from some cell in either
# the topmost row or leftmost column and going in the bottom-right direction until
# reaching the matrix's end. For example, the matrix diagonal starting from
# mat[2][0], where mat is a 6 x 3 matrix, includes cells mat[2][0], mat[3][1], and
# mat[4][2].
# 
# Given an m x n matrix mat of integers, sort each matrix diagonal in ascending
# order and return the resulting matrix.
# 
# Example 1:
# 
# https://assets.leetcode.com/uploads/2020/01/21/1482_example_1_2.png
# 
# Input: mat = [[3,3,1,1],[2,2,1,2],[1,1,1,2]]
# Output: [[1,1,1,1],[1,2,2,2],[1,2,3,3]]
# 
# Example 2:
# 
# Input: mat = [[11,25,66,1,69,7],[23,55,17,45,15,52],[75,31,36,44,58,8],[22,27,33
# ,25,68,4],[84,28,14,11,5,50]]
# Output: [[5,17,4,1,52,7],[11,11,25,45,8,69],[14,23,25,44,58,15],[22,27,31,36,50,
# 66],[84,28,75,33,55,68]]
# 
# 
# Constraints:
#         m == mat.length
#         n == mat[i].length
#         1 <= m, n <= 100
#         1 <= mat[i][j] <= 100


# Solution: https://algo.monster/liteproblems/1329
# Credit: AlgoMonster
def diagonal_sort(mat):
    # Get matrix dimensions
    rows, cols = len(mat), len(mat[0])
    
    # Create buckets to store elements from each diagonal
    # Each diagonal is identified by (row - col) value, but we offset by rows to avoid negative indices
    # Total possible diagonals: rows + cols - 1
    diagonal_buckets = [[] for _ in range(rows + cols)]
    
    # Collect all elements and group them by their diagonal
    # Elements on the same diagonal have the same (rows - row_idx + col_idx) value
    for row_idx, row in enumerate(mat):
        for col_idx, value in enumerate(row):
            diagonal_id = rows - row_idx + col_idx
            diagonal_buckets[diagonal_id].append(value)
    
    # Sort each diagonal in descending order for efficient pop() operation
    # pop() removes from the end, so we'll get smallest elements first
    for diagonal in diagonal_buckets:
        diagonal.sort(reverse=True)
    
    # Place sorted elements back into the matrix
    # Pop from each diagonal bucket to get elements in ascending order
    for row_idx in range(rows):
        for col_idx in range(cols):
            diagonal_id = rows - row_idx + col_idx
            mat[row_idx][col_idx] = diagonal_buckets[diagonal_id].pop()
    
    return mat
    # Time: O(m * n * log(min(m, n)))
    # Space: O(m * n)


def main():
    mat = [[3,3,1,1],
           [2,2,1,2],
           [1,1,1,2]]
    result = diagonal_sort(mat)
    print(result) # [[1, 1, 1, 1], [1, 2, 2, 2], [1, 2, 3, 3]]

    mat = mat = [[11,25,66,1,69,7],
                 [23,55,17,45,15,52],
                 [75,31,36,44,58,8],
                 [22,27,33,25,68,4],
                 [84,28,14,11,5,50]]
    result = diagonal_sort(mat)
    print(result) # [[5, 17, 4, 1, 52, 7], [11, 11, 25, 45, 8, 69], [14, 23, 25, 44, 58, 15], [22, 27, 31, 36, 50, 66], [84, 28, 75, 33, 55, 68]]

if __name__ == "__main__":
    main()
