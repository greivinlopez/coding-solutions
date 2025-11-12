# ----------------------
# 1001. Grid Illumination
# ----------------------

# Problem: https://leetcode.com/problems/grid-illumination
#
# There is a 2D grid of size n x n where each cell of this grid has a lamp that is
# initially turned off.
# 
# You are given a 2D array of lamp positions lamps, where lamps[i] = [rowᵢ, colᵢ]
# indicates that the lamp at grid[rowᵢ][colᵢ] is turned on. Even if the same lamp
# is listed more than once, it is turned on.
# 
# When a lamp is turned on, it illuminates its cell and all other cells in the
# same row, column, or diagonal.
# 
# You are also given another 2D array queries, where queries[j] = [rowⱼ, colⱼ].
# For the jth query, determine whether grid[rowⱼ][colⱼ] is illuminated or not.
# After answering the jth query, turn off the lamp at grid[rowⱼ][colⱼ] and its 8
# adjacent lamps if they exist. A lamp is adjacent if its cell shares either a
# side or corner with grid[rowⱼ][colⱼ].
# 
# Return an array of integers ans, where ans[j] should be 1 if the cell in the jᵗʰ
# query was illuminated, or 0 if the lamp was not.
# 
# Example 1:
# 
# https://assets.leetcode.com/uploads/2020/08/19/illu_1.jpg
# 
# Input: n = 5, lamps = [[0,0],[4,4]], queries = [[1,1],[1,0]]
# Output: [1,0]
# 
# Explanation: We have the initial grid with all lamps turned off. In the above
# picture we see the grid after turning on the lamp at grid[0][0] then turning on
# the lamp at grid[4][4].
# The 0th query asks if the lamp at grid[1][1] is illuminated or not (the blue
# square). It is illuminated, so set ans[0] = 1. Then, we turn off all lamps in
# the red square.
# 
# https://assets.leetcode.com/uploads/2020/08/19/illu_step1.jpg
# 
# The 1st query asks if the lamp at grid[1][0] is illuminated or not (the blue
# square). It is not illuminated, so set ans[1] = 0. Then, we turn off all lamps
# in the red rectangle.
# 
# https://assets.leetcode.com/uploads/2020/08/19/illu_step2.jpg
# 
# Example 2:
# 
# Input: n = 5, lamps = [[0,0],[4,4]], queries = [[1,1],[1,1]]
# Output: [1,1]
# 
# Example 3:
# 
# Input: n = 5, lamps = [[0,0],[0,4]], queries = [[0,4],[0,1],[1,4]]
# Output: [1,1,0]
# 
# 
# Constraints:
#         1 <= n <= 10⁹
#         0 <= lamps.length <= 20000
#         0 <= queries.length <= 20000
#         lamps[i].length == 2
#         0 <= rowᵢ, colᵢ < n
#         queries[j].length == 2
#         0 <= rowⱼ, colⱼ < n

from collections import Counter

# Solution: https://algo.monster/liteproblems/1001
# Credit: AlgoMonster
def grid_illumination(n, lamps, queries):
    # Convert lamp positions to a set for O(1) lookup and to remove duplicates
    lamp_positions = {(row, col) for row, col in lamps}
    
    # Initialize counters to track illuminated rows, columns, and diagonals
    # Each counter tracks how many lamps illuminate that particular line
    illuminated_rows = Counter()
    illuminated_cols = Counter()
    illuminated_main_diag = Counter()  # Main diagonal (top-left to bottom-right)
    illuminated_anti_diag = Counter()  # Anti-diagonal (top-right to bottom-left)
    
    # Count illumination for each lamp
    for row, col in lamp_positions:
        illuminated_rows[row] += 1
        illuminated_cols[col] += 1
        illuminated_main_diag[row - col] += 1  # Main diagonal has constant row - col
        illuminated_anti_diag[row + col] += 1  # Anti-diagonal has constant row + col
    
    # Initialize result array
    result = [0] * len(queries)
    
    # Process each query
    for query_idx, (query_row, query_col) in enumerate(queries):
        # Check if the queried cell is illuminated
        # A cell is illuminated if its row, column, or either diagonal has any lamp
        if (illuminated_rows[query_row] or 
            illuminated_cols[query_col] or 
            illuminated_main_diag[query_row - query_col] or 
            illuminated_anti_diag[query_row + query_col]):
            result[query_idx] = 1
        
        # Turn off all lamps in the 3x3 grid centered at the query position
        for neighbor_row in range(query_row - 1, query_row + 2):
            for neighbor_col in range(query_col - 1, query_col + 2):
                if (neighbor_row, neighbor_col) in lamp_positions:
                    # Remove the lamp from the set
                    lamp_positions.remove((neighbor_row, neighbor_col))
                    
                    # Update illumination counters
                    illuminated_rows[neighbor_row] -= 1
                    illuminated_cols[neighbor_col] -= 1
                    illuminated_main_diag[neighbor_row - neighbor_col] -= 1
                    illuminated_anti_diag[neighbor_row + neighbor_col] -= 1
    
    return result
    # Time: O(m + q)
    # Space: O(m)
    # m = the number of lamps
    # q = the number of queries


def main():
    result = grid_illumination(n = 5, lamps = [[0,0],[4,4]], queries = [[1,1],[1,0]])
    print(result) # [1,0]

    result = grid_illumination(n = 5, lamps = [[0,0],[4,4]], queries = [[1,1],[1,1]])
    print(result) # [1,1]

    result = grid_illumination(n = 5, lamps = [[0,0],[0,4]], queries = [[0,4],[0,1],[1,4]])
    print(result) # [1,1,0]

if __name__ == "__main__":
    main()
