# ------------------------------
# 892. Surface Area of 3D Shapes
# ------------------------------

# Problem: https://leetcode.com/problems/surface-area-of-3d-shapes
#
# You are given an n x n grid where you have placed some 1 x 1 x 1 cubes. Each
# value v = grid[i][j] represents a tower of v cubes placed on top of cell (i, j).
# After placing these cubes, you have decided to glue any directly adjacent cubes
# to each other, forming several irregular 3D shapes.
# Return the total surface area of the resulting shapes.
# Note: The bottom face of each shape counts toward its surface area.
# 
# Example 1:
# 
# https://assets.leetcode.com/uploads/2021/01/08/tmp-grid2.jpg
# 
# Input: grid = [[1,2],[3,4]]
# Output: 34
# 
# Example 2:
# 
# https://assets.leetcode.com/uploads/2021/01/08/tmp-grid4.jpg
# 
# Input: grid = [[1,1,1],[1,0,1],[1,1,1]]
# Output: 32
# 
# Example 3:
# 
# https://assets.leetcode.com/uploads/2021/01/08/tmp-grid5.jpg
# 
# Input: grid = [[2,2,2],[2,1,2],[2,2,2]]
# Output: 46
# 
# 
# Constraints:
#         n == grid.length == grid[i].length
#         1 <= n <= 50
#         0 <= grid[i][j] <= 50


# Solution: 
# Credit: Navdeep Singh founder of NeetCode
def surface_area(grid):
    total_surface_area = 0
    
    # Iterate through each cell in the grid
    for row_idx, row in enumerate(grid):
        for col_idx, height in enumerate(row):
            # If there are cubes at this position
            if height > 0:
                # Add surface area for this stack of cubes:
                # - Top and bottom faces: 2
                # - Side faces: height * 4 (4 sides, each with area = height)
                total_surface_area += 2 + height * 4
                
                # Subtract overlapping area with the stack above (previous row)
                if row_idx > 0:
                    # The overlapping area is 2 times the minimum height between adjacent stacks
                    # (counted twice: once from each stack's perspective)
                    overlap_above = min(height, grid[row_idx - 1][col_idx])
                    total_surface_area -= overlap_above * 2
                
                # Subtract overlapping area with the stack to the left (previous column)
                if col_idx > 0:
                    # The overlapping area is 2 times the minimum height between adjacent stacks
                    overlap_left = min(height, grid[row_idx][col_idx - 1])
                    total_surface_area -= overlap_left * 2
    
    return total_surface_area
    # Time: O(n²)
    # Space: O(1)


def main():
    result = surface_area(grid = [[1,2],[3,4]])
    print(result) # 34

    result = surface_area(grid = [[1,1,1],[1,0,1],[1,1,1]])
    print(result) # 32

    result = surface_area(grid = [[2,2,2],[2,1,2],[2,2,2]])
    print(result) # 46

if __name__ == "__main__":
    main()
