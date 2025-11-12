# ------------------------------------------------
# 1240. Tiling a Rectangle with the Fewest Squares
# ------------------------------------------------

# Problem: https://leetcode.com/problems/tiling-a-rectangle-with-the-fewest-squares
#
# Given a rectangle of size n x m, return the minimum number of integer-sided
# squares that tile the rectangle.
# 
# Example 1:
# 
# https://assets.leetcode.com/uploads/2019/10/17/sample_11_1592.png
# 
# Input: n = 2, m = 3
# Output: 3
# 
# Explanation: 3 squares are necessary to cover the rectangle.
# 2 (squares of 1x1)
# 1 (square of 2x2)
# 
# Example 2:
# 
# https://assets.leetcode.com/uploads/2019/10/17/sample_22_1592.png
# 
# Input: n = 5, m = 8
# Output: 5
# 
# Example 3:
# 
# https://assets.leetcode.com/uploads/2019/10/17/sample_33_1592.png
# 
# Input: n = 11, m = 13
# Output: 6
# 
# 
# Constraints:
#         1 <= n, m <= 13


# Solution: https://algo.monster/liteproblems/1240
# Credit: AlgoMonster
def tiling_rectangle(n, m):
    def backtrack(row, col, num_squares):
        """
        Recursively try to fill the rectangle with squares using backtracking.
        
        Args:
            row: Current row position
            col: Current column position  
            num_squares: Number of squares used so far
        """
        nonlocal min_squares
        
        # Move to next row if we've reached the end of current row
        if col == m:
            row += 1
            col = 0
        
        # If we've filled all rows, update the minimum answer
        if row == n:
            min_squares = num_squares
            return
        
        # If current cell is already filled, move to next cell
        if filled_cells[row] >> col & 1:
            backtrack(row, col + 1, num_squares)
        # Only continue if we can potentially get a better solution
        elif num_squares + 1 < min_squares:
            # Find maximum possible square size from current position
            max_rows = 0
            max_cols = 0
            
            # Count empty rows from current position
            for k in range(row, n):
                if filled_cells[k] >> col & 1:
                    break
                max_rows += 1
            
            # Count empty columns from current position
            for k in range(col, m):
                if filled_cells[row] >> k & 1:
                    break
                max_cols += 1
            
            # Maximum square size is limited by available rows and columns
            max_square_size = min(max_rows, max_cols)
            
            # Try all possible square sizes from 1 to max_square_size
            for square_size in range(1, max_square_size + 1):
                # Mark cells as filled for current square
                for k in range(square_size):
                    # Fill bottom row of the square
                    filled_cells[row + square_size - 1] |= 1 << (col + k)
                    # Fill rightmost column of the square
                    filled_cells[row + k] |= 1 << (col + square_size - 1)
                
                # Recursively try to fill remaining cells
                backtrack(row, col + square_size, num_squares + 1)
            
            # Backtrack: unmark all cells that were filled
            for x in range(row, row + max_square_size):
                for y in range(col, col + max_square_size):
                    filled_cells[x] ^= 1 << y
    
    # Initialize minimum squares to worst case (all 1x1 squares)
    min_squares = n * m
    
    # Track filled cells using bit manipulation (each row is a bitmask)
    filled_cells = [0] * n
    
    # Start backtracking from top-left corner
    backtrack(0, 0, 0)
    
    return min_squares
    # Time: O((n*m)^(n*m))
    # Space: O(n + n*m)


def main():
    result = tiling_rectangle(n = 2, m = 3)
    print(result) # 3

    result = tiling_rectangle(n = 5, m = 8)
    print(result) # 5

    result = tiling_rectangle(n = 11, m = 13)
    print(result) # 6

if __name__ == "__main__":
    main()
