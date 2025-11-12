# -----------------------
# 566. Reshape the Matrix
# -----------------------

# Problem: https://leetcode.com/problems/reshape-the-matrix
#
# In MATLAB, there is a handy function called reshape which can reshape an m x n
# matrix into a new one with a different size r x c keeping its original data.
# 
# You are given an m x n matrix mat and two integers r and c representing the
# number of rows and the number of columns of the wanted reshaped matrix.
# 
# The reshaped matrix should be filled with all the elements of the original
# matrix in the same row-traversing order as they were.
# 
# If the reshape operation with given parameters is possible and legal, output the
# new reshaped matrix; Otherwise, output the original matrix.
# 
# Example 1:
# 
# https://assets.leetcode.com/uploads/2021/04/24/reshape1-grid.jpg
# 
# Input: mat = [[1,2],[3,4]], r = 1, c = 4
# Output: [[1,2,3,4]]
# 
# Example 2:
# 
# https://assets.leetcode.com/uploads/2021/04/24/reshape2-grid.jpg
# 
# Input: mat = [[1,2],[3,4]], r = 2, c = 4
# Output: [[1,2],[3,4]]
# 
# 
# Constraints:
#         m == mat.length
#         n == mat[i].length
#         1 <= m, n <= 100
#         -1000 <= mat[i][j] <= 1000
#         1 <= r, c <= 300


# Solution: https://algo.monster/liteproblems/566
# Credit: AlgoMonster
def matrix_reshape(mat, r, c):
    # Get dimensions of the original matrix
    rows, cols = len(mat), len(mat[0])
    
    # Check if reshape is possible (total elements must match)
    if rows * cols != r * c:
        return mat
    
    # Initialize the reshaped matrix with zeros
    reshaped_matrix = [[0] * c for _ in range(r)]
    
    # Iterate through all elements using a single index
    for index in range(rows * cols):
        # Calculate source position in original matrix
        source_row = index // cols
        source_col = index % cols
        
        # Calculate target position in reshaped matrix
        target_row = index // c
        target_col = index % c
        
        # Copy element from source to target position
        reshaped_matrix[target_row][target_col] = mat[source_row][source_col]
    
    return reshaped_matrix
    # Time: O(m * n)
    # Space: O(r * c)
    # m = the number of rows in the original matrix
    # n = the number of columns in the original matrix


def main():
    result = matrix_reshape(mat = [[1,2],[3,4]], r = 1, c = 4)
    print(result) # [[1,2,3,4]]

    result = matrix_reshape(mat = [[1,2],[3,4]], r = 2, c = 4)
    print(result) # [[1,2],[3,4]]

if __name__ == "__main__":
    main()
