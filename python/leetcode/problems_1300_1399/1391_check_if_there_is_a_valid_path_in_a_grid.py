# -------------------------------------------------
# 1391. Check if There is a Valid Path in a Grid 🛣️
# -------------------------------------------------

# Problem: https://leetcode.com/problems/check-if-there-is-a-valid-path-in-a-grid
#
# You are given an m x n grid. Each cell of grid represents a street. The street
# of grid[i][j] can be:
# 
#         1 which means a street connecting the left cell and the right cell.
#         2 which means a street connecting the upper cell and the lower cell.
#         3 which means a street connecting the left cell and the lower cell.
#         4 which means a street connecting the right cell and the lower cell.
#         5 which means a street connecting the left cell and the upper cell.
#         6 which means a street connecting the right cell and the upper cell.
# 
# https://assets.leetcode.com/uploads/2020/03/05/main.png
# 
# You will initially start at the street of the upper-left cell (0, 0). A valid
# path in the grid is a path that starts from the upper left cell (0, 0) and ends
# at the bottom-right cell (m - 1, n - 1). The path should only follow the
# streets.
# 
# Notice that you are not allowed to change any street.
# 
# Return true if there is a valid path in the grid or false otherwise.
# 
# Example 1:
# 
# https://assets.leetcode.com/uploads/2020/03/05/e1.png
# 
# Input: grid = [[2,4,3],[6,5,2]]
# Output: true
# 
# Explanation: As shown you can start at cell (0, 0) and visit all the cells of
# the grid to reach (m - 1, n - 1).
# 
# Example 2:
# 
# https://assets.leetcode.com/uploads/2020/03/05/e2.png
# 
# Input: grid = [[1,2,1],[1,2,1]]
# Output: false
# 
# Explanation: As shown you the street at cell (0, 0) is not connected with any
# street of any other cell and you will get stuck at cell (0, 0)
# 
# Example 3:
# 
# Input: grid = [[1,1,2]]
# Output: false
# 
# Explanation: You will get stuck at cell (0, 1) and you cannot reach cell (0, 2).
# 
# 
# Constraints:
#         m == grid.length
#         n == grid[i].length
#         1 <= m, n <= 300
#         1 <= grid[i][j] <= 6


# Solution: https://algo.monster/liteproblems/1391
# Credit: AlgoMonster
def has_valid_path(grid):
    rows, cols = len(grid), len(grid[0])
    
    # Initialize parent array for Union-Find
    # Each cell is initially its own parent
    parent = list(range(rows * cols))
    
    def find(node):
        if parent[node] != node:
            parent[node] = find(parent[node])  # Path compression
        return parent[node]
    
    def connect_left(row, col):
        # Check if left neighbor exists and can connect from right
        # Streets 1, 4, 6 have right openings
        if col > 0 and grid[row][col - 1] in (1, 4, 6):
            current_root = find(row * cols + col)
            left_root = find(row * cols + col - 1)
            parent[current_root] = left_root
    
    def connect_right(row, col):
        # Check if right neighbor exists and can connect from left
        # Streets 1, 3, 5 have left openings
        if col < cols - 1 and grid[row][col + 1] in (1, 3, 5):
            current_root = find(row * cols + col)
            right_root = find(row * cols + col + 1)
            parent[current_root] = right_root
    
    def connect_up(row, col):
        # Check if upper neighbor exists and can connect from bottom
        # Streets 2, 3, 4 have bottom openings
        if row > 0 and grid[row - 1][col] in (2, 3, 4):
            current_root = find(row * cols + col)
            up_root = find((row - 1) * cols + col)
            parent[current_root] = up_root
    
    def connect_down(row, col):
        # Check if lower neighbor exists and can connect from top
        # Streets 2, 5, 6 have top openings
        if row < rows - 1 and grid[row + 1][col] in (2, 5, 6):
            current_root = find(row * cols + col)
            down_root = find((row + 1) * cols + col)
            parent[current_root] = down_root
    
    # Process each cell in the grid
    for row in range(rows):
        for col in range(cols):
            street_type = grid[row][col]
            
            # Connect neighbors based on street type
            if street_type == 1:  # Horizontal street
                connect_left(row, col)
                connect_right(row, col)
            elif street_type == 2:  # Vertical street
                connect_up(row, col)
                connect_down(row, col)
            elif street_type == 3:  # Left-down corner
                connect_left(row, col)
                connect_down(row, col)
            elif street_type == 4:  # Right-down corner
                connect_right(row, col)
                connect_down(row, col)
            elif street_type == 5:  # Left-up corner
                connect_left(row, col)
                connect_up(row, col)
            else:  # street_type == 6, Right-up corner
                connect_right(row, col)
                connect_up(row, col)
    
    # Check if start (0,0) and end (m-1,n-1) are connected
    start_root = find(0)
    end_root = find(rows * cols - 1)
    return start_root == end_root
    # Time: O(m * n * α(m * n))
    # Space: O(m * n)


def main():
    result = has_valid_path(grid = [[2,4,3],[6,5,2]])
    print(result) # True

    result = has_valid_path(grid = [[1,2,1],[1,2,1]])
    print(result) # False

    result = has_valid_path(grid = [[1,1,2]])
    print(result) # False

if __name__ == "__main__":
    main()
