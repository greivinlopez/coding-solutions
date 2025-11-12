# -----------------------
# 1034. Coloring A Border
# -----------------------

# Problem: https://leetcode.com/problems/coloring-a-border
#
# You are given an m x n integer matrix grid, and three integers row, col, and
# color. Each value in the grid represents the color of the grid square at that
# location.
# 
# Two squares are called adjacent if they are next to each other in any of the 4
# directions.
# 
# Two squares belong to the same connected component if they have the same color
# and they are adjacent.
# 
# The border of a connected component is all the squares in the connected
# component that are either adjacent to (at least) a square not in the component,
# or on the boundary of the grid (the first or last row or column).
# 
# You should color the border of the connected component that contains the square
# grid[row][col] with color.
# 
# Return the final grid.
# 
# Example 1:
# 
# Input: grid = [[1,1],[1,2]], row = 0, col = 0, color = 3
# Output: [[3,3],[3,2]]
# 
# Example 2:
# 
# Input: grid = [[1,2,2],[2,3,2]], row = 0, col = 1, color = 3
# Output: [[1,3,3],[2,3,3]]
# 
# Example 3:
# 
# Input: grid = [[1,1,1],[1,1,1],[1,1,1]], row = 1, col = 1, color = 2
# Output: [[2,2,2],[2,1,2],[2,2,2]]
# 
# 
# Constraints:
#         m == grid.length
#         n == grid[i].length
#         1 <= m, n <= 50
#         1 <= grid[i][j], color <= 1000
#         0 <= row < m
#         0 <= col < n


# Solution: https://algo.monster/liteproblems/1034
# Credit: AlgoMonster
def color_border(grid, row, col, color):
    
    def dfs(curr_row, curr_col, original_color):
        # Mark current cell as visited
        visited[curr_row][curr_col] = True
        
        # Check all 4 adjacent cells (up, right, down, left)
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        for dx, dy in directions:
            next_row = curr_row + dx
            next_col = curr_col + dy
            
            # Check if the adjacent cell is within grid bounds
            if 0 <= next_row < rows and 0 <= next_col < cols:
                if not visited[next_row][next_col]:
                    if grid[next_row][next_col] == original_color:
                        # Continue DFS for cells with same color
                        dfs(next_row, next_col, original_color)
                    else:
                        # Current cell is on border (adjacent to different color)
                        grid[curr_row][curr_col] = color
            else:
                # Current cell is on border (edge of grid)
                grid[curr_row][curr_col] = color
    
    # Initialize grid dimensions
    rows = len(grid)
    cols = len(grid[0])
    
    # Initialize visited matrix to track processed cells
    visited = [[False] * cols for _ in range(rows)]
    
    # Start DFS from the given starting position
    original_color = grid[row][col]
    dfs(row, col, original_color)
    
    return grid
    # Time: O(m * n)
    # Space: O(m * n)
    # m = the number of rows
    # n = the number of columns


def main():
    result = color_border(grid = [[1,1],[1,2]], row = 0, col = 0, color = 3)
    print(result) # [[3, 3], [3, 2]]

    result = color_border(grid = [[1,2,2],[2,3,2]], row = 0, col = 1, color = 3)
    print(result) # [[1, 3, 3], [2, 3, 3]]

    result = color_border(grid = [[1,1,1],[1,1,1],[1,1,1]], row = 1, col = 1, color = 2)
    print(result) # [[2, 2, 2], [2, 1, 2], [2, 2, 2]]

if __name__ == "__main__":
    main()
