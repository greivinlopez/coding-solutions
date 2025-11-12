# ---------------------------------------------------------------------
# 1284. Minimum Number of Flips to Convert Binary Matrix to Zero Matrix
# ---------------------------------------------------------------------

# Problem: https://leetcode.com/problems/minimum-number-of-flips-to-convert-binary-matrix-to-zero-matrix
#
# Given a m x n binary matrix mat. In one step, you can choose one cell and flip
# it and all the four neighbors of it if they exist (Flip is changing 1 to 0 and 0
# to 1). A pair of cells are called neighbors if they share one edge.
# 
# Return the minimum number of steps required to convert mat to a zero matrix or
# -1 if you cannot.
# 
# A binary matrix is a matrix with all cells equal to 0 or 1 only.
# 
# A zero matrix is a matrix with all cells equal to 0.
# 
# Example 1:
# 
# https://assets.leetcode.com/uploads/2019/11/28/matrix.png
# 
# Input: mat = [[0,0],[0,1]]
# Output: 3
# 
# Explanation: One possible solution is to flip (1, 0) then (0, 1) and finally (1,
# 1) as shown.
# 
# Example 2:
# 
# Input: mat = [[0]]
# Output: 0
# 
# Explanation: Given matrix is a zero matrix. We do not need to change it.
# 
# Example 3:
# 
# Input: mat = [[1,0,0],[1,0,0]]
# Output: -1
# 
# Explanation: Given matrix cannot be a zero matrix.
# 
# 
# Constraints:
#         m == mat.length
#         n == mat[i].length
#         1 <= m, n <= 3
#         mat[i][j] is either 0 or 1.

from collections import deque

# Solution: https://algo.monster/liteproblems/1284
# Credit: AlgoMonster
def min_flips(mat):
    # Get matrix dimensions
    rows, cols = len(mat), len(mat[0])
    
    # Convert initial matrix to a bit representation
    # Each cell (i, j) is represented by bit at position (i * cols + j)
    initial_state = sum(
        1 << (i * cols + j) 
        for i in range(rows) 
        for j in range(cols) 
        if mat[i][j] == 1
    )
    
    # BFS queue starting with initial state
    queue = deque([initial_state])
    # Set to track visited states to avoid cycles
    visited = {initial_state}
    # Number of flip operations performed
    flip_count = 0
    
    # Direction vectors: current position, up, down, left, right
    # Using a flat array to represent (0,0), (-1,0), (1,0), (0,-1), (0,1)
    directions = [0, -1, 0, 1, 0, 0]
    
    # BFS to find minimum flips to reach all-zeros state
    while queue:
        # Process all states at current level
        level_size = len(queue)
        for _ in range(level_size):
            current_state = queue.popleft()
            
            # Check if we've reached the target (all zeros)
            if current_state == 0:
                return flip_count
            
            # Try flipping each cell in the matrix
            for i in range(rows):
                for j in range(cols):
                    next_state = current_state
                    
                    # Flip current cell and its 4 adjacent cells
                    for k in range(5):
                        new_row = i + directions[k]
                        new_col = j + directions[k + 1]
                        
                        # Check if the cell is within bounds
                        if not (0 <= new_row < rows and 0 <= new_col < cols):
                            continue
                        
                        # Toggle the bit at position (new_row * cols + new_col)
                        bit_position = new_row * cols + new_col
                        if next_state & (1 << bit_position):
                            # If bit is 1, turn it to 0
                            next_state -= 1 << bit_position
                        else:
                            # If bit is 0, turn it to 1
                            next_state |= 1 << bit_position
                    
                    # Add new state to queue if not visited
                    if next_state not in visited:
                        visited.add(next_state)
                        queue.append(next_state)
        
        # Increment flip count after processing each level
        flip_count += 1
    
    # If no solution found, return -1
    return -1
    # Time: O(2ᵐ*ⁿ * m * n)
    # Space: O(2ᵐ*ⁿ)


def main():
    result = min_flips(mat = [[0,0],[0,1]])
    print(result) # 3

    result = min_flips(mat = [[0]])
    print(result) # 0

    result = min_flips(mat = [[1,0,0],[1,0,0]])
    print(result) # -1

if __name__ == "__main__":
    main()
