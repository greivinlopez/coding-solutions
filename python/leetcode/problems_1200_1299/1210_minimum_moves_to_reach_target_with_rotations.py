# -----------------------------------------------------
# 1210. Minimum Moves to Reach Target with Rotations 🐍
# -----------------------------------------------------

# Problem: https://leetcode.com/problems/minimum-moves-to-reach-target-with-rotations
#
# In an n*n grid, there is a snake that spans 2 cells and starts moving from the
# top left corner at (0, 0) and (0, 1). The grid has empty cells represented by
# zeros and blocked cells represented by ones. The snake wants to reach the lower
# right corner at (n-1, n-2) and (n-1, n-1).
# 
# In one move the snake can:
#         
#   * Move one cell to the right if there are no blocked cells there. This
#     move keeps the horizontal/vertical position of the snake as it is.
#   * Move down one cell if there are no blocked cells there. This move keeps
#     the horizontal/vertical position of the snake as it is.
#   * Rotate clockwise if it's in a horizontal position and the two cells
#     under it are both empty. In that case the snake moves from (r, c) and (r,
#     c+1) to (r, c) and (r+1, c).
# 
#     https://assets.leetcode.com/uploads/2019/09/24/image-2.png  
# 
#   * Rotate counterclockwise if it's in a vertical position and the two cells
#     to its right are both empty. In that case the snake moves from (r, c) and (r+1,
#     c) to (r, c) and (r, c+1).
# 
#     https://assets.leetcode.com/uploads/2019/09/24/image-1.png
# 
# Return the minimum number of moves to reach the target.
# 
# If there is no way to reach the target, return -1.
# 
# Example 1:
# 
# https://assets.leetcode.com/uploads/2019/09/24/image.png
# 
# Input: grid = [[0,0,0,0,0,1],
#                [1,1,0,0,1,0],
#                [0,0,0,0,1,1],
#                [0,0,1,0,1,0],
#                [0,1,1,0,0,0],
#                [0,1,1,0,0,0]]
# Output: 11
# 
# Explanation:
# One possible solution is [right, right, rotate clockwise, right, down, down,
# down, down, rotate counterclockwise, right, down].
# 
# Example 2:
# 
# Input: grid = [[0,0,1,1,1,1],
#                [0,0,0,0,1,1],
#                [1,1,0,0,0,1],
#                [1,1,1,0,0,1],
#                [1,1,1,0,0,1],
#                [1,1,1,0,0,0]]
# Output: 9
# 
# 
# Constraints:
#         2 <= n <= 100
#         0 <= grid[i][j] <= 1
#         It is guaranteed that the snake starts at empty cells.

from collections import deque

# Solution: https://algo.monster/liteproblems/1210
# Credit: AlgoMonster
def minimum_moves(grid):

    def try_move(head_row, head_col, tail_row, tail_col):
        # Check if both positions are within bounds
        if (0 <= head_row < grid_size and 0 <= head_col < grid_size and 
            0 <= tail_row < grid_size and 0 <= tail_col < grid_size):
            
            # Convert 2D coordinates to 1D indices
            head_index = head_row * grid_size + head_col
            tail_index = tail_row * grid_size + tail_col
            
            # Determine orientation: 0 for horizontal, 1 for vertical
            orientation = 0 if head_row == tail_row else 1
            
            # Check if this state hasn't been visited and both cells are empty
            if ((head_index, orientation) not in visited and 
                grid[head_row][head_col] == 0 and grid[tail_row][tail_col] == 0):
                
                queue.append((head_index, tail_index))
                visited.add((head_index, orientation))
    
    grid_size = len(grid)
    # Target position: snake at bottom-right corner, horizontal orientation
    target_position = (grid_size * grid_size - 2, grid_size * grid_size - 1)
    
    # BFS initialization: start with snake at top-left, horizontal
    queue = deque([(0, 1)])  # Head at (0,0), tail at (0,1)
    visited = {(0, 0)}  # (head_index, orientation)
    moves_count = 0
    
    # BFS to find shortest path
    while queue:
        # Process all positions at current distance
        for _ in range(len(queue)):
            head_index, tail_index = queue.popleft()
            
            # Check if we reached the target
            if (head_index, tail_index) == target_position:
                return moves_count
            
            # Convert 1D indices back to 2D coordinates
            head_row, head_col = head_index // grid_size, head_index % grid_size
            tail_row, tail_col = tail_index // grid_size, tail_index % grid_size
            
            # Try moving right (maintaining current orientation)
            try_move(head_row, head_col + 1, tail_row, tail_col + 1)
            
            # Try moving down (maintaining current orientation)
            try_move(head_row + 1, head_col, tail_row + 1, tail_col)
            
            # If horizontal, try clockwise rotation (pivot on head)
            if head_row == tail_row and head_row + 1 < grid_size and grid[head_row + 1][tail_col] == 0:
                try_move(head_row, head_col, head_row + 1, head_col)
            
            # If vertical, try counter-clockwise rotation (pivot on head)
            if head_col == tail_col and head_col + 1 < grid_size and grid[tail_row][head_col + 1] == 0:
                try_move(head_row, head_col, head_row, head_col + 1)
        
        moves_count += 1
    
    # Target unreachable
    return -1
    # Time: O(n²)
    # Space: O(n²)


def main():
    grid = [[0,0,0,0,0,1],
            [1,1,0,0,1,0],
            [0,0,0,0,1,1],
            [0,0,1,0,1,0],
            [0,1,1,0,0,0],
            [0,1,1,0,0,0]]
    result = minimum_moves(grid)
    print(result) # 11

    grid = [[0,0,1,1,1,1],
            [0,0,0,0,1,1],
            [1,1,0,0,0,1],
            [1,1,1,0,0,1],
            [1,1,1,0,0,1],
            [1,1,1,0,0,0]]
    result = minimum_moves(grid)
    print(result) # 9

if __name__ == "__main__":
    main()
