# ----------------------------------------------
# 1594. Maximum Non Negative Product in a Matrix
# ----------------------------------------------

# Problem: https://leetcode.com/problems/maximum-non-negative-product-in-a-matrix
#
# You are given a m x n matrix grid. Initially, you are located at the top-left
# corner (0, 0), and in each step, you can only move right or down in the matrix.
# 
# Among all possible paths starting from the top-left corner (0, 0) and ending in
# the bottom-right corner (m - 1, n - 1), find the path with the maximum non-
# negative product. The product of a path is the product of all integers in the
# grid cells visited along the path.
# 
# Return the maximum non-negative product modulo 10⁹ + 7. If the maximum product
# is negative, return -1.
# 
# Notice that the modulo is performed after getting the maximum product.
# 
# Example 1:
# 
# https://assets.leetcode.com/uploads/2021/12/23/product1.jpg
# 
# Input: grid = [[-1,-2,-3],[-2,-3,-3],[-3,-3,-2]]
# Output: -1
# 
# Explanation: It is not possible to get non-negative product in the path from (0,
# 0) to (2, 2), so return -1.
# 
# Example 2:
# 
# https://assets.leetcode.com/uploads/2021/12/23/product2.jpg
# 
# Input: grid = [[1,-2,1],[1,-2,1],[3,-4,1]]
# Output: 8
# 
# Explanation: Maximum non-negative product is shown (1 * 1 * -2 * -4 * 1 = 8).
# 
# Example 3:
# 
# https://assets.leetcode.com/uploads/2021/12/23/product3.jpg
# 
# Input: grid = [[1,3],[0,-4]]
# Output: 0
# 
# Explanation: Maximum non-negative product is shown (1 * 0 * -4 = 0).
# 
# 
# Constraints:
#         m == grid.length
#         n == grid[i].length
#         1 <= m, n <= 15
#         -4 <= grid[i][j] <= 4


# Solution: https://algo.monster/liteproblems/1594
# Credit: AlgoMonster
def max_product_path(grid):
    # Get grid dimensions
    rows, cols = len(grid), len(grid[0])
    MOD = 10**9 + 7
    
    # Initialize DP table: dp[i][j] = [min_product, max_product] at cell (i, j)
    # Each cell stores both minimum and maximum products to handle negative numbers
    dp = [[[grid[0][0], grid[0][0]] for _ in range(cols)] for _ in range(rows)]
    
    # Initialize first column (can only come from above)
    for row in range(1, rows):
        prev_product = dp[row - 1][0][0]
        current_value = grid[row][0]
        dp[row][0][0] = prev_product * current_value  # min product
        dp[row][0][1] = prev_product * current_value  # max product
    
    # Initialize first row (can only come from left)
    for col in range(1, cols):
        prev_product = dp[0][col - 1][0]
        current_value = grid[0][col]
        dp[0][col][0] = prev_product * current_value  # min product
        dp[0][col][1] = prev_product * current_value  # max product
    
    # Fill the DP table for remaining cells
    for row in range(1, rows):
        for col in range(1, cols):
            current_value = grid[row][col]
            
            if current_value >= 0:
                # For non-negative values:
                # - Minimum comes from multiplying with previous minimum
                # - Maximum comes from multiplying with previous maximum
                min_from_above = dp[row - 1][col][0]
                min_from_left = dp[row][col - 1][0]
                dp[row][col][0] = min(min_from_above, min_from_left) * current_value
                
                max_from_above = dp[row - 1][col][1]
                max_from_left = dp[row][col - 1][1]
                dp[row][col][1] = max(max_from_above, max_from_left) * current_value
            else:
                # For negative values:
                # - Minimum comes from multiplying with previous maximum (sign flip)
                # - Maximum comes from multiplying with previous minimum (sign flip)
                max_from_above = dp[row - 1][col][1]
                max_from_left = dp[row][col - 1][1]
                dp[row][col][0] = max(max_from_above, max_from_left) * current_value
                
                min_from_above = dp[row - 1][col][0]
                min_from_left = dp[row][col - 1][0]
                dp[row][col][1] = min(min_from_above, min_from_left) * current_value
    
    # Get the maximum product at the bottom-right cell
    max_product = dp[-1][-1][1]
    
    # Return -1 if the maximum product is negative, otherwise return modulo result
    return -1 if max_product < 0 else max_product % MOD
    # Time: O(m * n)
    # Space: O(m * n)


def main():
    result = max_product_path(grid = [[-1,-2,-3],[-2,-3,-3],[-3,-3,-2]])
    print(result) # -1

    result = max_product_path(grid = [[1,-2,1],[1,-2,1],[3,-4,1]])
    print(result) # 8

    result = max_product_path(grid = [[1,3],[0,-4]])
    print(result) # 0

if __name__ == "__main__":
    main()
