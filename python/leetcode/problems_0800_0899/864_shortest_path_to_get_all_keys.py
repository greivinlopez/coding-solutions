# -------------------------------------
# 864. Shortest Path to Get All Keys 🔑
# -------------------------------------

# Problem: https://leetcode.com/problems/shortest-path-to-get-all-keys
#
# You are given an m x n grid grid where:
# 
#         '.' is an empty cell.
#         '#' is a wall.
#         '@' is the starting point.
#         Lowercase letters represent keys.
#         Uppercase letters represent locks.
# 
# You start at the starting point and one move consists of walking one space in
# one of the four cardinal directions. You cannot walk outside the grid, or walk
# into a wall.
# 
# If you walk over a key, you can pick it up and you cannot walk over a lock
# unless you have its corresponding key.
# 
# For some 1 <= k <= 6, there is exactly one lowercase and one uppercase letter of
# the first k letters of the English alphabet in the grid. This means that there
# is exactly one key for each lock, and one lock for each key; and also that the
# letters used to represent the keys and locks were chosen in the same order as
# the English alphabet.
# 
# Return the lowest number of moves to acquire all keys. If it is impossible,
# return -1.
# 
# Example 1:
# 
# https://assets.leetcode.com/uploads/2021/07/23/lc-keys2.jpg
# 
# Input: grid = ["@.a..","###.#","b.A.B"]
# Output: 8
# 
# Explanation: Note that the goal is to obtain all the keys not to open all the
# locks.
# 
# Example 2:
# 
# https://assets.leetcode.com/uploads/2021/07/23/lc-key2.jpg
# 
# Input: grid = ["@..aA","..B#.","....b"]
# Output: 6
# 
# Example 3:
# 
# https://assets.leetcode.com/uploads/2021/07/23/lc-keys3.jpg
# 
# Input: grid = ["@Aa"]
# Output: -1
# 
# 
# Constraints:
#         m == grid.length
#         n == grid[i].length
#         1 <= m, n <= 30
#         grid[i][j] is either an English letter, '.', '#', or '@'. 
#         There is exactly one '@' in the grid.
#         The number of keys in the grid is in the range [1, 6].
#         Each key in the grid is unique.
#         Each key in the grid has a matching lock.

from collections import deque

# Solution: https://algo.monster/liteproblems/864
# Credit: AlgoMonster
def shortest_path_all_keys(grid):
    rows, cols = len(grid), len(grid[0])
    
    # Find the starting position marked with '@'
    start_row, start_col = next(
        (i, j) for i in range(rows) for j in range(cols) 
        if grid[i][j] == '@'
    )
    
    # Count total number of keys (lowercase letters)
    total_keys = sum(cell.islower() for row in grid for cell in row)
    
    # Direction vectors for moving up, right, down, left
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    
    # BFS queue: (row, col, key_state)
    # key_state uses bits to represent which keys we have
    queue = deque([(start_row, start_col, 0)])
    
    # Set to track visited states: (row, col, key_state)
    visited = {(start_row, start_col, 0)}
    
    steps = 0
    
    # BFS to find shortest path
    while queue:
        # Process all nodes at current level
        for _ in range(len(queue)):
            current_row, current_col, key_state = queue.popleft()
            
            # Check if we have collected all keys
            if key_state == (1 << total_keys) - 1:
                return steps
            
            # Explore all four directions
            for delta_row, delta_col in directions:
                next_row = current_row + delta_row
                next_col = current_col + delta_col
                next_key_state = key_state
                
                # Check if next position is within grid bounds
                if 0 <= next_row < rows and 0 <= next_col < cols:
                    cell = grid[next_row][next_col]
                    
                    # Check if cell is a wall or a locked door without key
                    if cell == '#':
                        continue
                    if cell.isupper():
                        # Check if we have the key for this lock
                        key_bit = ord(cell) - ord('A')
                        if (key_state & (1 << key_bit)) == 0:
                            continue
                    
                    # If cell contains a key, add it to our key state
                    if cell.islower():
                        key_bit = ord(cell) - ord('a')
                        next_key_state |= (1 << key_bit)
                    
                    # Add unvisited state to queue
                    if (next_row, next_col, next_key_state) not in visited:
                        visited.add((next_row, next_col, next_key_state))
                        queue.append((next_row, next_col, next_key_state))
        
        # Increment step count after processing current level
        steps += 1
    
    # No path found that collects all keys
    return -1
    # Time: O(m * n * 2ᵏ)
    # Space: O(m * n * 2ᵏ)
    # k = is the number of keys


def main():
    result = shortest_path_all_keys(grid = ["@.a..","###.#","b.A.B"])
    print(result) # 8

    result = shortest_path_all_keys(grid = ["@..aA","..B#.","....b"])
    print(result) # 6

    result = shortest_path_all_keys(grid = ["@Aa"])
    print(result) # -1

if __name__ == "__main__":
    main()
