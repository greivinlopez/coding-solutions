# --------------------------------------------
# 1536. Minimum Swaps to Arrange a Binary Grid
# --------------------------------------------

# Problem: https://leetcode.com/problems/minimum-swaps-to-arrange-a-binary-grid
#
# Given an n x n binary grid, in one step you can choose two adjacent rows of the
# grid and swap them.
# 
# A grid is said to be valid if all the cells above the main diagonal are zeros.
# 
# Return the minimum number of steps needed to make the grid valid, or -1 if the
# grid cannot be valid.
# 
# The main diagonal of a grid is the diagonal that starts at cell (1, 1) and ends
# at cell (n, n).
# 
# Example 1:
# 
# https://assets.leetcode.com/uploads/2020/07/28/fw.jpg
# 
# Input: grid = [[0,0,1],[1,1,0],[1,0,0]]
# Output: 3
# 
# Example 2:
# 
# https://assets.leetcode.com/uploads/2020/07/16/e2.jpg
# 
# Input: grid = [[0,1,1,0],[0,1,1,0],[0,1,1,0],[0,1,1,0]]
# Output: -1
# 
# Explanation: All rows are similar, swaps have no effect on the grid.
# 
# Example 3:
# 
# https://assets.leetcode.com/uploads/2020/07/16/e3.jpg
# 
# Input: grid = [[1,0,0],[1,1,0],[1,1,1]]
# Output: 0
# 
# 
# Constraints:
#         n == grid.length == grid[i].length
#         1 <= n <= 200
#         grid[i][j] is either 0 or 1


# Solution: https://algo.monster/liteproblems/1536
# Credit: AlgoMonster
def min_swaps(grid):
    n = len(grid)
    
    # Find the rightmost 1 position in each row
    # This tells us how many trailing zeros each row has
    rightmost_one_positions = [-1] * n
    
    for row_idx in range(n):
        for col_idx in range(n - 1, -1, -1):
            if grid[row_idx][col_idx] == 1:
                rightmost_one_positions[row_idx] = col_idx
                break
    
    total_swaps = 0
    
    # For each row position, find a suitable row that can be placed there
    for target_row in range(n):
        # Find the first row from current position onwards that can fit
        # A row can fit at position i if its rightmost 1 is at position <= i
        suitable_row_idx = -1
        
        for candidate_row in range(target_row, n):
            if rightmost_one_positions[candidate_row] <= target_row:
                # Found a suitable row
                total_swaps += candidate_row - target_row
                suitable_row_idx = candidate_row
                break
        
        # If no suitable row found, it's impossible to form upper triangular matrix
        if suitable_row_idx == -1:
            return -1
        
        # Bubble the suitable row up to the target position
        # This simulates the actual row swaps
        while suitable_row_idx > target_row:
            rightmost_one_positions[suitable_row_idx], rightmost_one_positions[suitable_row_idx - 1] = \
                rightmost_one_positions[suitable_row_idx - 1], rightmost_one_positions[suitable_row_idx]
            suitable_row_idx -= 1
    
    return total_swaps
    # Time: O(n²)
    # Space: O(n)


def main():
    result = min_swaps(grid = [[0,0,1],[1,1,0],[1,0,0]])
    print(result) # 3

    result = min_swaps(grid = [[0,1,1,0],[0,1,1,0],[0,1,1,0],[0,1,1,0]])
    print(result) # -1

    result = min_swaps(grid = [[1,0,0],[1,1,0],[1,1,1]])
    print(result) # 0

if __name__ == "__main__":
    main()
