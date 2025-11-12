# ----------------------
# 498. Diagonal Traverse
# ----------------------

# Problem: https://leetcode.com/problems/diagonal-traverse
#
# Given an m x n matrix mat, return an array of all the elements of the array in a
# diagonal order.
# 
# Example 1:
# 
# https://assets.leetcode.com/uploads/2021/04/10/diag1-grid.jpg
# 
# Input: mat = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,4,7,5,3,6,8,9]
# 
# Example 2:
# 
# Input: mat = [[1,2],[3,4]]
# Output: [1,2,3,4]
# 
# 
# Constraints:
#         m == mat.length
#         n == mat[i].length
#         1 <= m, n <= 10⁴
#         1 <= m * n <= 10⁴
#         -10⁵ <= mat[i][j] <= 10⁵


# Solution: https://algo.monster/liteproblems/498
# Credit: AlgoMonster
def find_diagonal_order(mat):
    # Get matrix dimensions
    rows, cols = len(mat), len(mat[0])
    result = []
    
    # Iterate through all diagonals (total: rows + cols - 1)
    for diagonal_index in range(rows + cols - 1):
        diagonal_elements = []
        
        # Determine starting position for current diagonal
        # If diagonal_index < cols, start from first row
        # Otherwise, start from appropriate row below
        start_row = 0 if diagonal_index < cols else diagonal_index - cols + 1
        start_col = diagonal_index if diagonal_index < cols else cols - 1
        
        # Traverse current diagonal from top-right to bottom-left
        current_row = start_row
        current_col = start_col
        while current_row < rows and current_col >= 0:
            diagonal_elements.append(mat[current_row][current_col])
            current_row += 1
            current_col -= 1
        
        # For even-indexed diagonals, reverse the order (zigzag pattern)
        if diagonal_index % 2 == 0:
            diagonal_elements = diagonal_elements[::-1]
        
        # Add diagonal elements to final result
        result.extend(diagonal_elements)
    
    return result
    # Time: O(m * n)
    # Space: O(min(m, n))
    # m = number of rows
    # n = number of columns


def main():
    result = find_diagonal_order(mat = [[1,2,3],[4,5,6],[7,8,9]])
    print(result) # [1,2,4,7,5,3,6,8,9]

    result = find_diagonal_order(mat = [[1,2],[3,4]])
    print(result) # [1,2,3,4]

if __name__ == "__main__":
    main()
