# -------------------------
# 1036. Escape a Large Maze
# -------------------------

# Problem: https://leetcode.com/problems/escape-a-large-maze
#
# There is a 1 million by 1 million grid on an XY-plane, and the coordinates of
# each grid square are (x, y).
# 
# We start at the source = [sₓ, sᵧ] square and want to reach the target = [tₓ, tᵧ]
# square. There is also an array of blocked squares, where each blocked[i] = [xᵢ, yᵢ] 
# represents a blocked square with coordinates (xᵢ, yᵢ).
# 
# Each move, we can walk one square north, east, south, or west if the square is
# not in the array of blocked squares. We are also not allowed to walk outside of
# the grid.
# 
# Return true if and only if it is possible to reach the target square from the
# source square through a sequence of valid moves.
# 
# Example 1:
# 
# Input: blocked = [[0,1],[1,0]], source = [0,0], target = [0,2]
# Output: false
# 
# Explanation: The target square is inaccessible starting from the source square
# because we cannot move.
# We cannot move north or east because those squares are blocked.
# We cannot move south or west because we cannot go outside of the grid.
# 
# Example 2:
# 
# Input: blocked = [], source = [0,0], target = [999999,999999]
# Output: true
# 
# Explanation: Because there are no blocked cells, it is possible to reach the
# target square.
# 
# 
# Constraints:
#         0 <= blocked.length <= 200
#         blocked[i].length == 2
#         0 <= xᵢ, yᵢ < 10⁶
#         source.length == target.length == 2
#         0 <= sₓ, sᵧ, tₓ, tᵧ < 10⁶
#         source != target
#         It is guaranteed that source and target are not blocked.


# Solution: 
# Credit: Navdeep Singh founder of NeetCode
def is_escape_possible(blocked, source, target):
    
    def can_escape_or_reach(start_pos, end_pos, visited):
        # Mark current position as visited
        visited.add(tuple(start_pos))
        
        # If we've explored more cells than the maximum possible enclosed area,
        # we've definitely escaped any enclosure
        if len(visited) > max_enclosed_area:
            return True
        
        # Explore all four directions (up, right, down, left)
        for i in range(4):
            # Calculate next position using direction vectors
            next_row = start_pos[0] + directions[i]
            next_col = start_pos[1] + directions[i + 1]
            
            # Check if next position is valid:
            # 1. Within grid boundaries
            # 2. Not blocked
            # 3. Not visited
            if (0 <= next_row < grid_size and 
                0 <= next_col < grid_size and 
                (next_row, next_col) not in blocked_set and 
                (next_row, next_col) not in visited):
                
                # Check if we've reached the target
                if [next_row, next_col] == end_pos:
                    return True
                
                # Continue DFS from the next position
                if can_escape_or_reach([next_row, next_col], end_pos, visited):
                    return True
        
        return False
    
    # Convert blocked list to set for O(1) lookup
    blocked_set = {(row, col) for row, col in blocked}
    
    # Direction vectors for moving up, right, down, left
    # Using the pattern: (row_delta, col_delta) pairs
    directions = [-1, 0, 1, 0, -1]  # Creates pairs: (-1,0), (0,1), (1,0), (0,-1)
    
    # Grid size (10^6 x 10^6)
    grid_size = 10**6
    
    # Maximum area that can be enclosed by blocked cells
    # This is approximately (number of blocked cells)^2 / 2
    # This represents the worst-case scenario where blocked cells form a diagonal
    max_enclosed_area = len(blocked) ** 2 // 2
    
    # Check both directions:
    # 1. Can we reach target from source?
    # 2. Can we reach source from target?
    # Both must be true for a valid path to exist
    return (can_escape_or_reach(source, target, set()) and 
            can_escape_or_reach(target, source, set()))
    # Time: O(m)
    # Space: O(m)
    # m = len(blocked)^2 / 2


def main():
    result = is_escape_possible(blocked = [[0,1],[1,0]], source = [0,0], target = [0,2])
    print(result) # False

    result = is_escape_possible(blocked = [], source = [0,0], target = [999999,999999])
    print(result) # True

if __name__ == "__main__":
    main()
