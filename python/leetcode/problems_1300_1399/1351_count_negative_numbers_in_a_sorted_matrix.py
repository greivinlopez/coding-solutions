# -----------------------------------------------
# 1351. Count Negative Numbers in a Sorted Matrix
# -----------------------------------------------

# Problem: https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix
#
# Given a m x n matrix grid which is sorted in non-increasing order both row-wise
# and column-wise, return the number of negative numbers in grid.
# 
# Example 1:
# 
# Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
# Output: 8
# 
# Explanation: There are 8 negatives number in the matrix.
# 
# Example 2:
# 
# Input: grid = [[3,2],[1,0]]
# Output: 0
# 
# 
# Constraints:
#         m == grid.length
#         n == grid[i].length
#         1 <= m, n <= 100
#         -100 <= grid[i][j] <= 100
# 
# Follow up: Could you find an O(n + m) solution?


# Solution: https://algo.monster/liteproblems/1351
# Credit: AlgoMonster
def count_negatives(grid):
    # Get dimensions of the grid
    rows, cols = len(grid), len(grid[0])
    
    # Start from bottom-left corner of the grid
    row_idx, col_idx = rows - 1, 0
    
    # Initialize counter for negative numbers
    negative_count = 0
    
    # Traverse the grid using staircase pattern
    while row_idx >= 0 and col_idx < cols:
        # If current element is negative
        if grid[row_idx][col_idx] < 0:
            # All elements to the right in this row are also negative
            # (since rows are sorted in non-increasing order)
            negative_count += cols - col_idx
            # Move up to the previous row
            row_idx -= 1
        else:
            # Current element is non-negative, move right to find negatives
            col_idx += 1
            
    return negative_count
    # Time: O(m + n)
    # Space: O(m + n)


def main():
    result = count_negatives(grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]])
    print(result) # 8

    result = count_negatives(grid = [[3,2],[1,0]])
    print(result) # 0

if __name__ == "__main__":
    main()
