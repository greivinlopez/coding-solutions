# ---------------------
# 980. Unique Paths III
# ---------------------

# Problem: https://leetcode.com/problems/unique-paths-iii
#
# You are given an m x n integer array grid where grid[i][j] could be:
# 
#   * 1 representing the starting square. There is exactly one starting square.
#   * 2 representing the ending square. There is exactly one ending square.
#   * 0 representing empty squares we can walk over.
#   * -1 representing obstacles that we cannot walk over.
# 
# Return the number of 4-directional walks from the starting square to the ending
# square, that walk over every non-obstacle square exactly once.
# 
# Example 1:
# 
# https://assets.leetcode.com/uploads/2021/08/02/lc-unique1.jpg
# 
# Input: grid = [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
# Output: 2
# Explanation: We have the following two paths:
# 1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2)
# 2. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2)
# 
# Example 2:
# 
# https://assets.leetcode.com/uploads/2021/08/02/lc-unique2.jpg
# 
# Input: grid = [[1,0,0,0],[0,0,0,0],[0,0,0,2]]
# Output: 4
# Explanation: We have the following four paths:
# 1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2),(2,3)
# 2. (0,0),(0,1),(1,1),(1,0),(2,0),(2,1),(2,2),(1,2),(0,2),(0,3),(1,3),(2,3)
# 3. (0,0),(1,0),(2,0),(2,1),(2,2),(1,2),(1,1),(0,1),(0,2),(0,3),(1,3),(2,3)
# 4. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2),(2,3)
# 
# Example 3:
# 
# https://assets.leetcode.com/uploads/2021/08/02/lc-unique3-.jpg
# 
# Input: grid = [[0,1],[2,0]]
# Output: 0
# 
# Explanation: There is no path that walks over every empty square exactly once.
# Note that the starting and ending square can be anywhere in the grid.
# 
# 
# Constraints:
#         m == grid.length
#         n == grid[i].length
#         1 <= m, n <= 20
#         1 <= m * n <= 20
#         -1 <= grid[i][j] <= 2
#         There is exactly one starting cell and one ending cell.


# Solution: https://algo.monster/liteproblems/980
# Credit: AlgoMonster
def unique_paths_iii(grid):
    def dfs(row, col, steps):
        # Check if we reached the destination
        if grid[row][col] == 2:
            # Valid path only if we visited all empty cells plus start
            return 1 if steps == empty_cells + 1 else 0
        
        path_count = 0
        
        # Try all four directions: up, right, down, left
        for i in range(4):
            next_row = row + directions[i]
            next_col = col + directions[i + 1]
            
            # Check if next cell is valid and unvisited
            if (0 <= next_row < rows and 
                0 <= next_col < cols and 
                (next_row, next_col) not in visited and 
                grid[next_row][next_col] != -1):
                
                # Mark cell as visited
                visited.add((next_row, next_col))
                
                # Recursively explore from next cell
                path_count += dfs(next_row, next_col, steps + 1)
                
                # Backtrack: unmark cell as visited
                visited.remove((next_row, next_col))
        
        return path_count
    
    # Initialize grid dimensions
    rows, cols = len(grid), len(grid[0])
    
    # Find starting position (cell with value 1)
    start_row, start_col = 0, 0
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                start_row, start_col = i, j
                break
    
    # Direction vectors for moving up, right, down, left
    directions = [-1, 0, 1, 0, -1]
    
    # Count empty cells (cells with value 0)
    empty_cells = sum(row.count(0) for row in grid)
    
    # Initialize visited set with starting position
    visited = {(start_row, start_col)}
    
    # Start DFS from starting position with 0 steps taken
    return dfs(start_row, start_col, 0)
    # Time: O(3^(m * n))
    # Space: O(m * n)


def main():
    result = unique_paths_iii(grid = [[1,0,0,0],[0,0,0,0],[0,0,2,-1]])
    print(result) # 2

    result = unique_paths_iii(grid = [[1,0,0,0],[0,0,0,0],[0,0,0,2]])
    print(result) # 4

    result = unique_paths_iii(grid = [[0,1],[2,0]])
    print(result) # 0

if __name__ == "__main__":
    main()
