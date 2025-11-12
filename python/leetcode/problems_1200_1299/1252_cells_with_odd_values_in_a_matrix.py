# ---------------------------------------
# 1252. Cells with Odd Values in a Matrix
# ---------------------------------------

# Problem: https://leetcode.com/problems/cells-with-odd-values-in-a-matrix
#
# There is an m x n matrix that is initialized to all 0's. There is also a 2D
# array indices where each indices[i] = [rᵢ, cᵢ] represents a 0-indexed location
# to perform some increment operations on the matrix.
# 
# For each location indices[i], do both of the following:
#         
#   1. Increment all the cells on row rᵢ.
#   2. Increment all the cells on column cᵢ.
# 
# Given m, n, and indices, return the number of odd-valued cells in the matrix
# after applying the increment to all locations in indices.
# 
# Example 1:
# 
# https://assets.leetcode.com/uploads/2019/10/30/e1.png
# 
# Input: m = 2, n = 3, indices = [[0,1],[1,1]]
# Output: 6
# 
# Explanation: Initial matrix = [[0,0,0],[0,0,0]].
# After applying first increment it becomes [[1,2,1],[0,1,0]].
# The final matrix is [[1,3,1],[1,3,1]], which contains 6 odd numbers.
# 
# Example 2:
# 
# https://assets.leetcode.com/uploads/2019/10/30/e2.png
# 
# Input: m = 2, n = 2, indices = [[1,1],[0,0]]
# Output: 0
# 
# Explanation: Final matrix = [[2,2],[2,2]]. There are no odd numbers in the final
# matrix.
# 
# 
# Constraints:
#         1 <= m, n <= 50
#         1 <= indices.length <= 100
#         0 <= rᵢ < m
#         0 <= cᵢ < n
# 
# Follow up: Could you solve this in O(n + m + indices.length) time with only O(n
# + m) extra space?


# Solution: https://algo.monster/liteproblems/1252
# Credit: AlgoMonster
def odd_cells(m, n, indices):
    # Initialize m x n matrix with all zeros
    matrix = [[0] * n for _ in range(m)]
    
    # Process each increment operation
    for row_index, col_index in indices:
        # Increment all cells in the specified column
        for i in range(m):
            matrix[i][col_index] += 1
        
        # Increment all cells in the specified row
        for j in range(n):
            matrix[row_index][j] += 1
    
    # Count cells with odd values
    odd_count = sum(value % 2 for row in matrix for value in row)
    
    return odd_count
    # Time: O(k * (m + n) + m * n)
    # Space: O(m * n)


def main():
    result = odd_cells(m = 2, n = 3, indices = [[0,1],[1,1]])
    print(result) # 6

    result = odd_cells(m = 2, n = 2, indices = [[1,1],[0,0]])
    print(result) # 0

if __name__ == "__main__":
    main()
