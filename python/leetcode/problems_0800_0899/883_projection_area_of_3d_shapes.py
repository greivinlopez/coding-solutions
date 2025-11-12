# ---------------------------------
# 883. Projection Area of 3D Shapes
# ---------------------------------

# Problem: https://leetcode.com/problems/projection-area-of-3d-shapes
#
# You are given an n x n grid where we place some 1 x 1 x 1 cubes that are axis-
# aligned with the x, y, and z axes.
# 
# Each value v = grid[i][j] represents a tower of v cubes placed on top of the
# cell (i, j).
# 
# We view the projection of these cubes onto the xy, yz, and zx planes.
# 
# A projection is like a shadow, that maps our 3-dimensional figure to a
# 2-dimensional plane. We are viewing the "shadow" when looking at the cubes from
# the top, the front, and the side.
# 
# Return the total area of all three projections.
# 
# Example 1:
# 
# https://s3-lc-upload.s3.amazonaws.com/uploads/2018/08/02/shadow.png
# 
# Input: grid = [[1,2],[3,4]]
# Output: 17
# 
# Explanation: Here are the three projections ("shadows") of the shape made with
# each axis-aligned plane.
# 
# Example 2:
# 
# Input: grid = [[2]]
# Output: 5
# 
# Example 3:
# 
# Input: grid = [[1,0],[0,2]]
# Output: 8
# 
# 
# Constraints:
#         n == grid.length == grid[i].length
#         1 <= n <= 50
#         0 <= grid[i][j] <= 50


# Solution: 
# Credit: Navdeep Singh founder of NeetCode
def projection_area(grid):
    # Calculate the projection area on XY plane (top view)
    # Count all non-zero cells (each non-zero value creates a shadow of area 1)
    xy_projection = sum(value > 0 for row in grid for value in row)
    
    # Calculate the projection area on YZ plane (front view)
    # For each row, take the maximum height (looking from the side)
    yz_projection = sum(max(row) for row in grid)
    
    # Calculate the projection area on ZX plane (side view)
    # For each column, take the maximum height (looking from the front)
    # zip(*grid) transposes the grid to iterate through columns
    zx_projection = sum(max(column) for column in zip(*grid))
    
    # Return the total projection area (sum of all three projections)
    return xy_projection + yz_projection + zx_projection
    # Time: O(n²)
    # Space: O(n)


def main():
    result = projection_area(grid = [[1,2],[3,4]])
    print(result) # 17

    result = projection_area(grid = [[2]])
    print(result) # 5

    result = projection_area(grid = [[1,0],[0,2]])
    print(result) # 8

if __name__ == "__main__":
    main()
