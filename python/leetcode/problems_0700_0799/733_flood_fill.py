# ---------------
# 733. Flood Fill
# ---------------

# Problem: https://leetcode.com/problems/flood-fill
#
# You are given an image represented by an m x n grid of integers image, where
# image[i][j] represents the pixel value of the image. You are also given three
# integers sr, sc, and color. Your task is to perform a flood fill on the image
# starting from the pixel image[sr][sc].
# 
# To perform a flood fill:
#         
#   * Begin with the starting pixel and change its color to color.
#   * Perform the same process for each pixel that is directly adjacent
#     (pixels that share a side with the original pixel, either horizontally or
#      vertically) and shares the same color as the starting pixel.
#   * Keep repeating this process by checking neighboring pixels of the
#     updated pixels and modifying their color if it matches the original color of the
#     starting pixel.
#   * The process stops when there are no more adjacent pixels of the original
#     color to update.
# 
# Return the modified image after performing the flood fill.
# 
# Example 1:
# 
# Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2
# Output: [[2,2,2],[2,2,0],[2,0,1]]
# 
# Explanation:
# 
# https://assets.leetcode.com/uploads/2021/06/01/flood1-grid.jpg
# 
# From the center of the image with position (sr, sc) = (1, 1) (i.e., the red
# pixel), all pixels connected by a path of the same color as the starting pixel
# (i.e., the blue pixels) are colored with the new color.
# Note the bottom corner is not colored 2, because it is not horizontally or
# vertically connected to the starting pixel.
# 
# Example 2:
# 
# Input: image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, color = 0
# Output: [[0,0,0],[0,0,0]]
# 
# Explanation:
# The starting pixel is already colored with 0, which is the same as the target
# color. Therefore, no changes are made to the image.
# 
# 
# Constraints:
#         m == image.length
#         n == image[i].length
#         1 <= m, n <= 50
#         0 <= image[i][j], color < 2¹⁶
#         0 <= sr < m
#         0 <= sc < n


# Solution: https://algo.monster/liteproblems/733
# Credit: AlgoMonster
def flood_fill(image, sr, sc, color):
    # Store the original color at starting position
    original_color = image[sr][sc]
    
    # Only proceed if new color is different from original color
    # This prevents infinite recursion
    if original_color == color:
        return image
    
    # Get dimensions of the image
    rows = len(image)
    cols = len(image[0])
    
    def dfs(row, col):
        # Fill current pixel with new color
        image[row][col] = color
        
        # Define four directions: up, right, down, left
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        
        # Explore all four adjacent cells
        for delta_row, delta_col in directions:
            new_row = row + delta_row
            new_col = col + delta_col
            
            # Check if new position is valid and has the original color
            if (0 <= new_row < rows and 
                0 <= new_col < cols and 
                image[new_row][new_col] == original_color):
                # Recursively fill the adjacent cell
                dfs(new_row, new_col)
    
    # Start flood fill from the given starting position
    dfs(sr, sc)
    
    return image
    # Time: O(m * n)
    # Space: O(m * n)
    # n = the number of rows
    # m = the number of columns


def main():
    result = flood_fill(image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2)
    print(result) # [[2,2,2],[2,2,0],[2,0,1]]

    result = flood_fill(image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, color = 0)
    print(result) # [[0,0,0],[0,0,0]]

if __name__ == "__main__":
    main()
