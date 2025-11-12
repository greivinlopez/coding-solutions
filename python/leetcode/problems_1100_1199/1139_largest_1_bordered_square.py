# -------------------------------
# 1139. Largest 1-Bordered Square
# -------------------------------

# Problem: https://leetcode.com/problems/largest-1-bordered-square
#
# Given a 2D grid of 0s and 1s, return the number of elements in the largest
# square subgrid that has all 1s on its border, or 0 if such a subgrid doesn't
# exist in the grid.
# 
# Example 1:
# 
# Input: grid = [[1,1,1],[1,0,1],[1,1,1]]
# Output: 9
# 
# Example 2:
# 
# Input: grid = [[1,1,0,0]]
# Output: 1
# 
# 
# Constraints:
#         1 <= grid.length <= 100
#         1 <= grid[0].length <= 100
#         grid[i][j] is 0 or 1


# Solution: https://algo.monster/liteproblems/1139
# Credit: AlgoMonster
def largest_1_bordered_square(grid):
    # Get dimensions of the grid
    rows, cols = len(grid), len(grid[0])
    
    # Create DP tables to store consecutive 1s count
    # consecutive_ones_down[i][j] = number of consecutive 1s going down from (i,j)
    # consecutive_ones_right[i][j] = number of consecutive 1s going right from (i,j)
    consecutive_ones_down = [[0] * cols for _ in range(rows)]
    consecutive_ones_right = [[0] * cols for _ in range(rows)]
    
    # Build the DP tables by iterating from bottom-right to top-left
    for row in range(rows - 1, -1, -1):
        for col in range(cols - 1, -1, -1):
            if grid[row][col] == 1:
                # Count consecutive 1s going down from current position
                if row + 1 < rows:
                    consecutive_ones_down[row][col] = consecutive_ones_down[row + 1][col] + 1
                else:
                    consecutive_ones_down[row][col] = 1
                
                # Count consecutive 1s going right from current position
                if col + 1 < cols:
                    consecutive_ones_right[row][col] = consecutive_ones_right[row][col + 1] + 1
                else:
                    consecutive_ones_right[row][col] = 1
    
    # Try to find the largest square, starting from maximum possible size
    max_possible_size = min(rows, cols)
    
    for square_size in range(max_possible_size, 0, -1):
        # Check all possible top-left corners for current square size
        for top_row in range(rows - square_size + 1):
            for left_col in range(cols - square_size + 1):
                # Calculate positions of the four corners
                bottom_row = top_row + square_size - 1
                right_col = left_col + square_size - 1
                
                # Check if all four borders have enough consecutive 1s
                has_top_border = consecutive_ones_right[top_row][left_col] >= square_size
                has_left_border = consecutive_ones_down[top_row][left_col] >= square_size
                has_bottom_border = consecutive_ones_right[bottom_row][left_col] >= square_size
                has_right_border = consecutive_ones_down[top_row][right_col] >= square_size
                
                if has_top_border and has_left_border and has_bottom_border and has_right_border:
                    # Found a valid square with all borders made of 1s
                    return square_size * square_size
    
    # No valid square found
    return 0
    # Time: O(m * n * min(m, n))
    # Space: O(m * n)


def main():
    result = largest_1_bordered_square(grid = [[1,1,1],[1,0,1],[1,1,1]])
    print(result) # 9

    result = largest_1_bordered_square(grid = [[1,1,0,0]])
    print(result) # 1

if __name__ == "__main__":
    main()
