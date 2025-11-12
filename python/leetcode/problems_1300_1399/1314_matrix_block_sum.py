# ----------------------
# 1314. Matrix Block Sum
# ----------------------

# Problem: https://leetcode.com/problems/matrix-block-sum
#
# Given a m x n matrix mat and an integer k, return a matrix answer where each
# answer[i][j] is the sum of all elements mat[r][c] for:
# 
#         i - k <= r <= i + k,
#         j - k <= c <= j + k, and
#         (r, c) is a valid position in the matrix.
#
# Example 1:
# 
# Input: mat = [[1,2,3],[4,5,6],[7,8,9]], k = 1
# Output: [[12,21,16],[27,45,33],[24,39,28]]
# 
# Example 2:
# 
# Input: mat = [[1,2,3],[4,5,6],[7,8,9]], k = 2
# Output: [[45,45,45],[45,45,45],[45,45,45]]
# 
# 
# Constraints:
#         m == mat.length
#         n == mat[i].length
#         1 <= m, n, k <= 100
#         1 <= mat[i][j] <= 100


# Solution: https://algo.monster/liteproblems/1314
# Credit: AlgoMonster
def matrix_block_sum(mat, k):
    # Get dimensions of the input matrix
    rows, cols = len(mat), len(mat[0])
    
    # Create prefix sum matrix with padding (one extra row and column of zeros)
    # This helps avoid boundary checks when calculating sums
    prefix_sum = [[0] * (cols + 1) for _ in range(rows + 1)]
    
    # Build the 2D prefix sum matrix
    # prefix_sum[i][j] represents sum of all elements from mat[0][0] to mat[i-1][j-1]
    for i, row in enumerate(mat, start=1):
        for j, value in enumerate(row, start=1):
            # Current prefix sum = sum above + sum to left - overlap + current value
            prefix_sum[i][j] = (prefix_sum[i - 1][j] + 
                                prefix_sum[i][j - 1] - 
                                prefix_sum[i - 1][j - 1] + 
                                value)
    
    # Initialize result matrix with same dimensions as input
    result = [[0] * cols for _ in range(rows)]
    
    # Calculate block sum for each position
    for i in range(rows):
        for j in range(cols):
            # Determine block boundaries, ensuring they stay within matrix bounds
            top_row = max(i - k, 0)
            left_col = max(j - k, 0)
            bottom_row = min(rows - 1, i + k)
            right_col = min(cols - 1, j + k)
            
            # Use prefix sum to calculate sum of the block in O(1) time
            # Formula: sum(bottom_right) - sum(top_right) - sum(bottom_left) + sum(top_left)
            result[i][j] = (prefix_sum[bottom_row + 1][right_col + 1] - 
                            prefix_sum[top_row][right_col + 1] - 
                            prefix_sum[bottom_row + 1][left_col] + 
                            prefix_sum[top_row][left_col])
    
    return result
    # Time: O(m * n)
    # Space: O(m * n)


def main():
    result = matrix_block_sum(mat = [[1,2,3],[4,5,6],[7,8,9]], k = 1)
    print(result) # [[12, 21, 16], [27, 45, 33], [24, 39, 28]]

    result = matrix_block_sum(mat = [[1,2,3],[4,5,6],[7,8,9]], k = 2)
    print(result) # [[45, 45, 45], [45, 45, 45], [45, 45, 45]]

if __name__ == "__main__":
    main()
