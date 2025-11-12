# -------------------------------
# 803. Bricks Falling When Hit 🧱
# -------------------------------

# Problem: https://leetcode.com/problems/bricks-falling-when-hit
#
# You are given an m x n binary grid, where each 1 represents a brick and 0
# represents an empty space. A brick is stable if:
# 
#   * It is directly connected to the top of the grid, or
#   * At least one other brick in its four adjacent cells is stable.
# 
# You are also given an array hits, which is a sequence of erasures we want to
# apply. Each time we want to erase the brick at the location hits[i] = (rowi,
# coli). The brick on that location (if it exists) will disappear. Some other
# bricks may no longer be stable because of that erasure and will fall. Once a
# brick falls, it is immediately erased from the grid (i.e., it does not land on
# other stable bricks).
# 
# Return an array result, where each result[i] is the number of bricks that will
# fall after the iᵗʰ erasure is applied.
# 
# Note that an erasure may refer to a location with no brick, and if it does, no
# bricks drop.
# 
# Example 1:
# 
# Input: grid = [[1,0,0,0],[1,1,1,0]], hits = [[1,0]]
# Output: [2]
# 
# Explanation: Starting with the grid:
# [[1,0,0,0],
#  [1,1,1,0]]
# We erase the underlined brick at (1,0), resulting in the grid:
# [[1,0,0,0],
#  [0,1,1,0]]
# The two underlined bricks are no longer stable as they are no longer connected
# to the top nor adjacent to another stable brick, so they will fall. The
# resulting grid is:
# [[1,0,0,0],
#  [0,0,0,0]]
# Hence the result is [2].
# 
# Example 2:
# 
# Input: grid = [[1,0,0,0],[1,1,0,0]], hits = [[1,1],[1,0]]
# Output: [0,0]
# 
# Explanation: Starting with the grid:
# [[1,0,0,0],
#  [1,1,0,0]]
# We erase the underlined brick at (1,1), resulting in the grid:
# [[1,0,0,0],
#  [1,0,0,0]]
# All remaining bricks are still stable, so no bricks fall. The grid remains the
# same:
# [[1,0,0,0],
#  [1,0,0,0]]
# Next, we erase the underlined brick at (1,0), resulting in the grid:
# [[1,0,0,0],
#  [0,0,0,0]]
# Once again, all remaining bricks are still stable, so no bricks fall.
# Hence the result is [0,0].
# 
# 
# Constraints:
#         m == grid.length
#         n == grid[i].length
#         1 <= m, n <= 200
#         grid[i][j] is 0 or 1.
#         1 <= hits.length <= 4 * 10⁴
#         hits[i].length == 2
#         0 <= xᵢ <= m - 1
#         0 <= yᵢ <= n - 1
#         All (xᵢ, yᵢ) are unique.


# Solution: https://algo.monster/liteproblems/803
# Credit: AlgoMonster
def hit_bricks(grid, hits):
    def find(node: int) -> int:
        if parent[node] != node:
            parent[node] = find(parent[node])
        return parent[node]
    
    def union(node_a: int, node_b: int) -> None:
        root_a, root_b = find(node_a), find(node_b)
        if root_a != root_b:
            # Merge smaller component into larger one
            component_size[root_b] += component_size[root_a]
            parent[root_a] = root_b
    
    rows, cols = len(grid), len(grid[0])
    
    # Initialize Union-Find structure
    # Index rows * cols represents the virtual "ceiling" node
    ceiling_node = rows * cols
    parent = list(range(rows * cols + 1))
    component_size = [1] * (rows * cols + 1)
    
    # Create grid state after all hits are applied
    grid_after_hits = [row[:] for row in grid]  # Deep copy
    for row_idx, col_idx in hits:
        grid_after_hits[row_idx][col_idx] = 0
    
    # Connect all bricks in top row to ceiling
    for col_idx in range(cols):
        if grid_after_hits[0][col_idx] == 1:
            union(col_idx, ceiling_node)
    
    # Connect all remaining bricks to their neighbors
    for row_idx in range(1, rows):
        for col_idx in range(cols):
            if grid_after_hits[row_idx][col_idx] == 0:
                continue
                
            current_node = row_idx * cols + col_idx
            
            # Connect to brick above if exists
            if grid_after_hits[row_idx - 1][col_idx] == 1:
                above_node = (row_idx - 1) * cols + col_idx
                union(current_node, above_node)
            
            # Connect to brick on left if exists
            if col_idx > 0 and grid_after_hits[row_idx][col_idx - 1] == 1:
                left_node = row_idx * cols + col_idx - 1
                union(current_node, left_node)
    
    result = []
    
    # Process hits in reverse order (adding bricks back)
    for row_idx, col_idx in reversed(hits):
        # If original grid had no brick here, no bricks can fall
        if grid[row_idx][col_idx] == 0:
            result.append(0)
            continue
        
        # Add brick back
        grid_after_hits[row_idx][col_idx] = 1
        current_node = row_idx * cols + col_idx
        
        # Count stable bricks before adding this brick
        stable_bricks_before = component_size[find(ceiling_node)]
        
        # If brick is in top row, connect to ceiling
        if row_idx == 0:
            union(col_idx, ceiling_node)
        
        # Connect to all adjacent bricks
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]  # up, down, right, left
        for delta_row, delta_col in directions:
            adjacent_row = row_idx + delta_row
            adjacent_col = col_idx + delta_col
            
            # Check if adjacent position is valid and has a brick
            if (0 <= adjacent_row < rows and 
                0 <= adjacent_col < cols and 
                grid_after_hits[adjacent_row][adjacent_col] == 1):
                adjacent_node = adjacent_row * cols + adjacent_col
                union(current_node, adjacent_node)
        
        # Count stable bricks after adding this brick
        stable_bricks_after = component_size[find(ceiling_node)]
        
        # Calculate fallen bricks (exclude the added brick itself)
        fallen_bricks = max(0, stable_bricks_after - stable_bricks_before - 1)
        result.append(fallen_bricks)
    
    # Reverse result to match original hit order
    return result[::-1]
    # Time: O(k * m * n * α(m * n))
    # Space: O(m * n)
    # m, n = the dimensions of the grid
    # k = the number of hits
    # α = the inverse Ackermann function


def main():
    result = hit_bricks(grid = [[1,0,0,0],[1,1,1,0]], hits = [[1,0]])
    print(result) # [2]

    result = hit_bricks(grid = [[1,0,0,0],[1,1,0,0]], hits = [[1,1],[1,0]])
    print(result) # [0,0]

if __name__ == "__main__":
    main()
