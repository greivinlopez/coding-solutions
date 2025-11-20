# ------------------------------
# 1559. Detect Cycles in 2D Grid
# ------------------------------

# Problem: https://leetcode.com/problems/detect-cycles-in-2d-grid
#
# Given a 2D array of characters grid of size m x n, you need to find if there
# exists any cycle consisting of the same value in grid.
# 
# A cycle is a path of length 4 or more in the grid that starts and ends at the
# same cell. From a given cell, you can move to one of the cells adjacent to it -
# in one of the four directions (up, down, left, or right), if it has the same
# value of the current cell.
# 
# Also, you cannot move to the cell that you visited in your last move. For
# example, the cycle (1, 1) -> (1, 2) -> (1, 1) is invalid because from (1, 2) we
# visited (1, 1) which was the last visited cell.
# 
# Return true if any cycle of the same value exists in grid, otherwise, return
# false.
# 
# Example 1:
# 
# https://assets.leetcode.com/uploads/2020/07/15/1.png
# 
# Input: grid =
# [["a","a","a","a"],["a","b","b","a"],["a","b","b","a"],["a","a","a","a"]]
# 
# Output: true
# 
# Explanation: There are two valid cycles shown in different colors in the image
# below:
# 
# https://assets.leetcode.com/uploads/2020/07/15/11.png
# 
# Example 2:
# 
# https://assets.leetcode.com/uploads/2020/07/15/22.png
# 
# Input: grid =
# [["c","c","c","a"],["c","d","c","c"],["c","c","e","c"],["f","c","c","c"]]
# Output: true
# 
# Explanation: There is only one valid cycle highlighted in the image below:
# 
# https://assets.leetcode.com/uploads/2020/07/15/2.png
# 
# Example 3:
# 
# https://assets.leetcode.com/uploads/2020/07/15/3.png
# 
# Input: grid = [["a","b","b"],["b","z","b"],["b","b","a"]]
# Output: false
# 
# 
# Constraints:
#         m == grid.length
#         n == grid[i].length
#         1 <= m, n <= 500
#         grid consists only of lowercase English letters.


# Solution: https://algo.monster/liteproblems/1559
# Credit: AlgoMonster
def contains_cycle(grid):
    # Get grid dimensions
    rows, cols = len(grid), len(grid[0])
    
    # Track visited cells
    visited = [[False] * cols for _ in range(rows)]
    
    # Direction vectors for moving up, right, down, left
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    
    # Check each cell as a potential starting point
    for start_row in range(rows):
        for start_col in range(cols):
            # Skip if already visited
            if visited[start_row][start_col]:
                continue
            
            # Mark starting cell as visited
            visited[start_row][start_col] = True
            
            # Initialize stack for DFS: (current_row, current_col, parent_row, parent_col)
            # Parent is used to avoid going back to the cell we came from
            stack = [(start_row, start_col, -1, -1)]
            
            # Perform DFS to find cycle
            while stack:
                curr_row, curr_col, parent_row, parent_col = stack.pop()
                
                # Check all four adjacent cells
                for delta_row, delta_col in directions:
                    next_row = curr_row + delta_row
                    next_col = curr_col + delta_col
                    
                    # Check if next cell is within bounds
                    if 0 <= next_row < rows and 0 <= next_col < cols:
                        # Skip if different value or if it's the parent cell
                        if (grid[next_row][next_col] != grid[start_row][start_col] or 
                            (next_row == parent_row and next_col == parent_col)):
                            continue
                        
                        # If we've visited this cell before in current component, we found a cycle
                        if visited[next_row][next_col]:
                            return True
                        
                        # Mark as visited and add to stack
                        visited[next_row][next_col] = True
                        stack.append((next_row, next_col, curr_row, curr_col))
    
    # No cycle found
    return False
    # Time: O(m × n)
    # Space: O(m × n)


def main():
    grid = [["a","a","a","a"],
            ["a","b","b","a"],
            ["a","b","b","a"],
            ["a","a","a","a"]]
    result = contains_cycle(grid)
    print(result) # True

    grid = [["c","c","c","a"],
            ["c","d","c","c"],
            ["c","c","e","c"],
            ["f","c","c","c"]]
    result = contains_cycle(grid)
    print(result) # True

    grid = [["a","b","b"],
            ["b","z","b"],
            ["b","b","a"]]
    result = contains_cycle(grid)
    print(result) # False

if __name__ == "__main__":
    main()
