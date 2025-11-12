# ------------------------------------------------------------------------------
# 1292. Maximum Side Length of a Square with Sum Less than or Equal to Threshold
# ------------------------------------------------------------------------------

# Problem: https://leetcode.com/problems/maximum-side-length-of-a-square-with-sum-less-than-or-equal-to-threshold
#
# Given a m x n matrix mat and an integer threshold, return the maximum side-
# length of a square with a sum less than or equal to threshold or return 0 if
# there is no such square.
# 
# Example 1:
# 
# https://assets.leetcode.com/uploads/2019/12/05/e1.png
# 
# Input: mat = [[1,1,3,2,4,3,2],[1,1,3,2,4,3,2],[1,1,3,2,4,3,2]], threshold = 4
# Output: 2
# 
# Explanation: The maximum side length of square with sum less than 4 is 2 as
# shown.
# 
# Example 2:
# 
# Input: mat = [[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2]],
# threshold = 1
# Output: 0
# 
# 
# Constraints:
#         m == mat.length
#         n == mat[i].length
#         1 <= m, n <= 300
#         0 <= mat[i][j] <= 10⁴
#         0 <= threshold <= 10⁵


# Solution: https://algo.monster/liteproblems/1292
# Credit: AlgoMonster
def max_side_length(mat, threshold):
    
    def can_form_square_with_side(side_length: int) -> bool:
        # Try all possible top-left corners for a square of given side length
        for row in range(rows - side_length + 1):
            for col in range(cols - side_length + 1):
                # Calculate sum using prefix sum array
                # Sum of square from (row, col) to (row + side_length - 1, col + side_length - 1)
                square_sum = (prefix_sum[row + side_length][col + side_length] 
                                - prefix_sum[row][col + side_length] 
                                - prefix_sum[row + side_length][col] 
                                + prefix_sum[row][col])
                
                if square_sum <= threshold:
                    return True
        return False
    
    # Get matrix dimensions
    rows, cols = len(mat), len(mat[0])
    
    # Build prefix sum array with padding for easier calculation
    # prefix_sum[i][j] represents sum of rectangle from (0,0) to (i-1, j-1)
    prefix_sum = [[0] * (cols + 1) for _ in range(rows + 1)]
    
    # Populate prefix sum array
    for i, row in enumerate(mat, start=1):
        for j, value in enumerate(row, start=1):
            prefix_sum[i][j] = (prefix_sum[i - 1][j] 
                                + prefix_sum[i][j - 1] 
                                - prefix_sum[i - 1][j - 1] 
                                + value)
    
    # Binary search on the side length
    # Maximum possible side length is the minimum of rows and cols
    left, right = 0, min(rows, cols)
    
    while left < right:
        # Use ceiling division to avoid infinite loop
        mid = (left + right + 1) >> 1  # Equivalent to (left + right + 1) // 2
        
        if can_form_square_with_side(mid):
            # If we can form a square with side length mid, try larger
            left = mid
        else:
            # If we cannot form a square with side length mid, try smaller
            right = mid - 1
    
    return left
    # Time: O(m * n * min(m, n))
    # Space: O(m * n)


def main():
    result = max_side_length(mat = [[1,1,3,2,4,3,2],[1,1,3,2,4,3,2],[1,1,3,2,4,3,2]], threshold = 4)
    print(result) # 2

    result = max_side_length(mat = [[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2]], threshold = 1)
    print(result) # 0

if __name__ == "__main__":
    main()
