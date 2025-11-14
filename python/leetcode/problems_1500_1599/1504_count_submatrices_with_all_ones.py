# -------------------------------------
# 1504. Count Submatrices With All Ones
# -------------------------------------

# Problem: https://leetcode.com/problems/count-submatrices-with-all-ones
#
# Given an m x n binary matrix mat, return the number of submatrices that have all
# ones.
# 
# Example 1:
# 
# https://assets.leetcode.com/uploads/2021/10/27/ones1-grid.jpg
# 
# Input: mat = [[1,0,1],[1,1,0],[1,1,0]]
# Output: 13
# 
# Explanation:
# There are 6 rectangles of side 1x1.
# There are 2 rectangles of side 1x2.
# There are 3 rectangles of side 2x1.
# There is 1 rectangle of side 2x2.
# There is 1 rectangle of side 3x1.
# Total number of rectangles = 6 + 2 + 3 + 1 + 1 = 13.
# 
# Example 2:
# 
# https://assets.leetcode.com/uploads/2021/10/27/ones2-grid.jpg
# 
# Input: mat = [[0,1,1,0],[0,1,1,1],[1,1,1,0]]
# Output: 24
# 
# Explanation:
# There are 8 rectangles of side 1x1.
# There are 5 rectangles of side 1x2.
# There are 2 rectangles of side 1x3.
# There are 4 rectangles of side 2x1.
# There are 2 rectangles of side 2x2.
# There are 2 rectangles of side 3x1.
# There is 1 rectangle of side 3x2.
# Total number of rectangles = 8 + 5 + 2 + 4 + 2 + 2 + 1 = 24.
# 
# 
# Constraints:
#         1 <= m, n <= 150
#         mat[i][j] is either 0 or 1.


# Solution: https://algo.monster/liteproblems/1504
# Credit: AlgoMonster
def num_submat(mat):
    # Get matrix dimensions
    rows, cols = len(mat), len(mat[0])
    
    # Create a helper matrix to store consecutive 1s count ending at each position
    # consecutive_ones[i][j] = number of consecutive 1s ending at position (i, j) in row i
    consecutive_ones = [[0] * cols for _ in range(rows)]
    
    # Build the consecutive ones matrix
    # For each position, count how many consecutive 1s there are to its left (including itself)
    for i in range(rows):
        for j in range(cols):
            if mat[i][j] == 1:
                # If it's a 1, either start counting (j=0) or add to previous count
                consecutive_ones[i][j] = 1 if j == 0 else consecutive_ones[i][j - 1] + 1
            # If it's a 0, the value remains 0 (already initialized)
    
    # Count all possible submatrices
    total_submatrices = 0
    
    # For each position (i, j) as the bottom-right corner of potential submatrices
    for i in range(rows):
        for j in range(cols):
            # Track the minimum width available as we go up rows
            min_width = float('inf')
            
            # Try all possible top-left corners with same column j or less
            # k represents the top row of the submatrix
            for k in range(i, -1, -1):
                # Update minimum width (bottleneck for valid submatrix width)
                min_width = min(min_width, consecutive_ones[k][j])
                
                # Add count of all submatrices with bottom-right at (i,j) 
                # and top row at k, with width up to min_width
                total_submatrices += min_width
    
    return total_submatrices
    # Time: O(m² * n)
    # Space: O(m * n)


def main():
    result = num_submat(mat = [[1,0,1],[1,1,0],[1,1,0]])
    print(result) # 13

    result = num_submat(mat = [[0,1,1,0],[0,1,1,1],[1,1,1,0]])
    print(result) # 24

if __name__ == "__main__":
    main()
