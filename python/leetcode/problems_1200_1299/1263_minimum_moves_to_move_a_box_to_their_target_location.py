# -------------------------------------------------------------
# 1263. Minimum Moves to Move a Box to Their Target Location 📦
# -------------------------------------------------------------

# Problem: https://leetcode.com/problems/minimum-moves-to-move-a-box-to-their-target-location
#
# A storekeeper is a game in which the player pushes boxes around in a warehouse
# trying to get them to target locations.
# 
# The game is represented by an m x n grid of characters grid where each element
# is a wall, floor, or box.
# 
# Your task is to move the box 'B' to the target position 'T' under the following
# rules:
#         
#   * The character 'S' represents the player. The player can move up, down,
#     left, right in grid if it is a floor (empty cell).
#   * The character '.' represents the floor which means a free cell to walk.
#   * The character '#' represents the wall which means an obstacle
#     (impossible to walk there).
#   * There is only one box 'B' and one target cell 'T' in the grid.
#   * The box can be moved to an adjacent free cell by standing next to the
#     box and then moving in the direction of the box. This is a push.
#   * The player cannot walk through the box.
# 
# Return the minimum number of pushes to move the box to the target. If there is
# no way to reach the target, return -1.
# 
# Example 1:
# 
# https://assets.leetcode.com/uploads/2019/11/06/sample_1_1620.png
# 
# Input: grid = [["#","#","#","#","#","#"],
#                ["#","T","#","#","#","#"],
#                ["#",".",".","B",".","#"],
#                ["#",".","#","#",".","#"],
#                ["#",".",".",".","S","#"],
#                ["#","#","#","#","#","#"]]
# Output: 3
# 
# Explanation: We return only the number of times the box is pushed.
# 
# Example 2:
# 
# Input: grid = [["#","#","#","#","#","#"],
#                ["#","T","#","#","#","#"],
#                ["#",".",".","B",".","#"],
#                ["#","#","#","#",".","#"],
#                ["#",".",".",".","S","#"],
#                ["#","#","#","#","#","#"]]
# Output: -1
# 
# Example 3:
# 
# Input: grid = [["#","#","#","#","#","#"],
#                ["#","T",".",".","#","#"],
#                ["#",".","#","B",".","#"],
#                ["#",".",".",".",".","#"],
#                ["#",".",".",".","S","#"],
#                ["#","#","#","#","#","#"]]
# Output: 5
# 
# Explanation: push the box down, left, left, up and up.
# Constraints:
#         m == grid.length
#         n == grid[i].length
#         1 <= m, n <= 20
#         grid contains only characters '.', '#', 'S', 'T', or 'B'.
#         There is only one character 'S', 'B', and 'T' in the grid.

from collections import deque

# Solution: https://algo.monster/liteproblems/1263
# Credit: AlgoMonster
def min_push_box(grid):

    def encode_position(row: int, col: int) -> int:
        """Encode 2D grid position to 1D integer for efficient storage."""
        return row * cols + col
    
    def is_valid_cell(row: int, col: int) -> bool:
        """Check if a cell is within bounds and not a wall."""
        return 0 <= row < rows and 0 <= col < cols and grid[row][col] != "#"
    
    # Find initial positions of person (S) and box (B)
    person_row, person_col = 0, 0
    box_row, box_col = 0, 0
    
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == "S":
                person_row, person_col = i, j
            elif cell == "B":
                box_row, box_col = i, j
    
    rows, cols = len(grid), len(grid[0])
    
    # Direction vectors: up, right, down, left
    directions = (-1, 0, 1, 0, -1)
    
    # BFS queue: (person_position, box_position, push_count)
    queue = deque([(encode_position(person_row, person_col), 
                    encode_position(box_row, box_col), 0)])
    
    # Visited states: visited[person_pos][box_pos] = True if visited
    visited = [[False] * (rows * cols) for _ in range(rows * cols)]
    visited[encode_position(person_row, person_col)][encode_position(box_row, box_col)] = True
    
    while queue:
        person_pos, box_pos, pushes = queue.popleft()
        
        # Decode box position
        current_box_row, current_box_col = box_pos // cols, box_pos % cols
        
        # Check if box reached target
        if grid[current_box_row][current_box_col] == "T":
            return pushes
        
        # Decode person position
        current_person_row, current_person_col = person_pos // cols, person_pos % cols
        
        # Try moving person in all four directions
        for i in range(4):
            next_person_row = current_person_row + directions[i]
            next_person_col = current_person_col + directions[i + 1]
            
            # Skip if next position is invalid
            if not is_valid_cell(next_person_row, next_person_col):
                continue
            
            # Check if person would move to box position (push the box)
            if next_person_row == current_box_row and next_person_col == current_box_col:
                # Calculate new box position after push
                next_box_row = current_box_row + directions[i]
                next_box_col = current_box_col + directions[i + 1]
                
                # Skip if box can't be pushed there or state already visited
                if not is_valid_cell(next_box_row, next_box_col):
                    continue
                if visited[encode_position(next_person_row, next_person_col)][encode_position(next_box_row, next_box_col)]:
                    continue
                
                # Mark as visited and add to queue (push action increases count)
                visited[encode_position(next_person_row, next_person_col)][encode_position(next_box_row, next_box_col)] = True
                queue.append((encode_position(next_person_row, next_person_col), 
                                encode_position(next_box_row, next_box_col), 
                                pushes + 1))
            else:
                # Person moves without pushing box
                if not visited[encode_position(next_person_row, next_person_col)][encode_position(current_box_row, current_box_col)]:
                    # Mark as visited and add to front of queue (no push, same distance)
                    visited[encode_position(next_person_row, next_person_col)][encode_position(current_box_row, current_box_col)] = True
                    queue.appendleft((encode_position(next_person_row, next_person_col), 
                                        encode_position(current_box_row, current_box_col), 
                                        pushes))
    
    # No solution found
    return -1
    # Time: O(m² * n²)
    # Space: O(m² * n²)


def main():
    grid = [["#","#","#","#","#","#"],
            ["#","T","#","#","#","#"],
            ["#",".",".","B",".","#"],
            ["#",".","#","#",".","#"],
            ["#",".",".",".","S","#"],
            ["#","#","#","#","#","#"]]
    result = min_push_box(grid)
    print(result) # 3

    grid = [["#","#","#","#","#","#"],
            ["#","T","#","#","#","#"],
            ["#",".",".","B",".","#"],
            ["#","#","#","#",".","#"],
            ["#",".",".",".","S","#"],
            ["#","#","#","#","#","#"]]
    result = min_push_box(grid)
    print(result) # -1

    grid = [["#","#","#","#","#","#"],
            ["#","T",".",".","#","#"],
            ["#",".","#","B",".","#"],
            ["#",".",".",".",".","#"],
            ["#",".",".",".","S","#"],
            ["#","#","#","#","#","#"]]
    result = min_push_box(grid)
    print(result) # 5

if __name__ == "__main__":
    main()
