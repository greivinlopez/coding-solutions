# ------------------------------------
# 1030. Matrix Cells in Distance Order
# ------------------------------------

# Problem: https://leetcode.com/problems/matrix-cells-in-distance-order
#
# You are given four integers row, cols, rCenter, and cCenter. There is a rows x
# cols matrix and you are on the cell with the coordinates (rCenter, cCenter).
# 
# Return the coordinates of all cells in the matrix, sorted by their distance from
# (rCenter, cCenter) from the smallest distance to the largest distance. You may
# return the answer in any order that satisfies this condition.
# 
# The distance between two cells (r₁, c₁) and (r₂, c₂) is |r₁ - r₂| + |c₁ - c₂|.
# 
# Example 1:
# 
# Input: rows = 1, cols = 2, rCenter = 0, cCenter = 0
# Output: [[0,0],[0,1]]
# 
# Explanation: The distances from (0, 0) to other cells are: [0,1]
# 
# Example 2:
# 
# Input: rows = 2, cols = 2, rCenter = 0, cCenter = 1
# Output: [[0,1],[0,0],[1,1],[1,0]]
# 
# Explanation: The distances from (0, 1) to other cells are: [0,1,1,2]
# The answer [[0,1],[1,1],[0,0],[1,0]] would also be accepted as correct.
# 
# Example 3:
# 
# Input: rows = 2, cols = 3, rCenter = 1, cCenter = 2
# Output: [[1,2],[0,2],[1,1],[0,1],[1,0],[0,0]]
# 
# Explanation: The distances from (1, 2) to other cells are: [0,1,1,2,2,3]
# There are other answers that would also be accepted as correct, such as
# [[1,2],[1,1],[0,2],[1,0],[0,1],[0,0]].
# 
# 
# Constraints:
#         1 <= rows, cols <= 100
#         0 <= rCenter < rows
#         0 <= cCenter < cols

from collections import deque

# Solution: https://algo.monster/liteproblems/1030
# Credit: AlgoMonster
def all_cells_dist_order(rows, cols, rCenter, cCenter):
    # Initialize queue with the center cell
    queue = deque([[rCenter, cCenter]])
    
    # Create visited matrix to track processed cells
    visited = [[False] * cols for _ in range(rows)]
    visited[rCenter][cCenter] = True
    
    # Result list to store cells in order of distance
    result = []
    
    # BFS traversal
    while queue:
        # Process all cells at current distance level
        level_size = len(queue)
        for _ in range(level_size):
            current_cell = queue.popleft()
            result.append(current_cell)
            
            # Check all 4 adjacent cells (up, right, down, left)
            # Using pairwise to create direction pairs: (-1,0), (0,1), (1,0), (0,-1)
            for delta_row, delta_col in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                new_row = current_cell[0] + delta_row
                new_col = current_cell[1] + delta_col
                
                # Check if the new cell is within bounds and not visited
                if (0 <= new_row < rows and 
                    0 <= new_col < cols and 
                    not visited[new_row][new_col]):
                    visited[new_row][new_col] = True
                    queue.append([new_row, new_col])
    
    return result
    # Time: O(rows * cols)
    # Space: O(rows * cols)


def main():
    result = all_cells_dist_order(rows = 1, cols = 2, rCenter = 0, cCenter = 0)
    print(result) # [[0,0],[0,1]]

    result = all_cells_dist_order(rows = 2, cols = 2, rCenter = 0, cCenter = 1)
    print(result) # [[0,1],[0,0],[1,1],[1,0]]

    result = all_cells_dist_order(rows = 2, cols = 3, rCenter = 1, cCenter = 2)
    print(result) # [[1,2],[0,2],[1,1],[0,1],[1,0],[0,0]]

if __name__ == "__main__":
    main()
