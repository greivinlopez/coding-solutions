# --------------------------------------------------------
# 1293. Shortest Path in a Grid with Obstacles Elimination
# --------------------------------------------------------

# Problem: https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination
#
# You are given an m x n integer matrix grid where each cell is either 0 (empty)
# or 1 (obstacle). You can move up, down, left, or right from and to an empty cell
# in one step.
# 
# Return the minimum number of steps to walk from the upper left corner (0, 0) to
# the lower right corner (m - 1, n - 1) given that you can eliminate at most k
# obstacles. If it is not possible to find such walk return -1.
# 
# Example 1:
# 
# https://assets.leetcode.com/uploads/2021/09/30/short1-grid.jpg
# 
# Input: grid = [[0,0,0],[1,1,0],[0,0,0],[0,1,1],[0,0,0]], k = 1
# Output: 6
# 
# Explanation:
# The shortest path without eliminating any obstacle is 10.
# The shortest path with one obstacle elimination at position (3,2) is 6. Such
# path is (0,0) -> (0,1) -> (0,2) -> (1,2) -> (2,2) -> (3,2) -> (4,2).
# 
# Example 2:
# 
# https://assets.leetcode.com/uploads/2021/09/30/short2-grid.jpg
# 
# Input: grid = [[0,1,1],[1,1,1],[1,0,0]], k = 1
# Output: -1
# 
# Explanation: We need to eliminate at least two obstacles to find such a walk.
# 
# 
# Constraints:
#         m == grid.length
#         n == grid[i].length
#         1 <= m, n <= 40
#         1 <= k <= m * n
#         grid[i][j] is either 0 or 1.
#         grid[0][0] == grid[m - 1][n - 1] == 0

from collections import deque

# Solution: https://algo.monster/liteproblems/1293
# Credit: AlgoMonster
def shortest_path(grid, k):
    # Get grid dimensions
    rows, cols = len(grid), len(grid[0])
    
    # Early optimization: if we have enough eliminations to go straight through
    # The maximum obstacles we'd need to eliminate is (rows - 1) + (cols - 1) - 1
    if k >= rows + cols - 3:
        return rows + cols - 2
    
    # BFS queue: stores (row, col, remaining_eliminations)
    queue = deque([(0, 0, k)])
    
    # Visited set: tracks (row, col, remaining_eliminations) states
    visited = {(0, 0, k)}
    
    # Track current distance/steps
    steps = 0
    
    # BFS to find shortest path
    while queue:
        steps += 1
        
        # Process all nodes at current distance level
        for _ in range(len(queue)):
            current_row, current_col, remaining_k = queue.popleft()
            
            # Check all 4 directions: up, down, right, left
            directions = [[0, -1], [0, 1], [1, 0], [-1, 0]]
            for delta_row, delta_col in directions:
                next_row = current_row + delta_row
                next_col = current_col + delta_col
                
                # Check if next position is within grid bounds
                if 0 <= next_row < rows and 0 <= next_col < cols:
                    # Check if we reached the destination
                    if next_row == rows - 1 and next_col == cols - 1:
                        return steps
                    
                    # If next cell is empty (0), move without using elimination
                    if grid[next_row][next_col] == 0:
                        state = (next_row, next_col, remaining_k)
                        if state not in visited:
                            queue.append(state)
                            visited.add(state)
                    
                    # If next cell is obstacle (1), use elimination if available
                    elif grid[next_row][next_col] == 1 and remaining_k > 0:
                        state = (next_row, next_col, remaining_k - 1)
                        if state not in visited:
                            queue.append(state)
                            visited.add(state)
    
    # No path found
    return -1
    # Time: O(m * n * k)
    # Space: O(m * n * k)


def main():
    result = shortest_path(grid = [[0,0,0],[1,1,0],[0,0,0],[0,1,1],[0,0,0]], k = 1)
    print(result) # 6

    result = shortest_path(grid = [[0,1,1],[1,1,1],[1,0,0]], k = 1)
    print(result) # -1

if __name__ == "__main__":
    main()
