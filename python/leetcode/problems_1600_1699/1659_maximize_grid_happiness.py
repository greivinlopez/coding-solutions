# -----------------------------
# 1659. Maximize Grid Happiness
# -----------------------------

# Problem: https://leetcode.com/problems/maximize-grid-happiness
#
# You are given four integers, m, n, introvertsCount, and extrovertsCount. You
# have an m x n grid, and there are two types of people: introverts and
# extroverts. There are introvertsCount introverts and extrovertsCount extroverts.
# 
# You should decide how many people you want to live in the grid and assign each
# of them one grid cell. Note that you do not have to have all the people living
# in the grid.
# 
# The happiness of each person is calculated as follows:
#         
#   * Introverts start with 120 happiness and lose 30 happiness for each
#     neighbor (introvert or extrovert).
#   * Extroverts start with 40 happiness and gain 20 happiness for each
#     neighbor (introvert or extrovert).
# 
# Neighbors live in the directly adjacent cells north, east, south, and west of a
# person's cell.
# 
# The grid happiness is the sum of each person's happiness. Return the maximum
# possible grid happiness.
# 
# Example 1:
# 
# Input: m = 2, n = 3, introvertsCount = 1, extrovertsCount = 2
# Output: 240
# 
# Explanation: Assume the grid is 1-indexed with coordinates (row, column).
# We can put the introvert in cell (1,1) and put the extroverts in cells (1,3) and
# (2,3).
# - Introvert at (1,1) happiness: 120 (starting happiness) - (0 * 30) (0
# neighbors) = 120
# - Extrovert at (1,3) happiness: 40 (starting happiness) + (1 * 20) (1 neighbor)
# = 60
# - Extrovert at (2,3) happiness: 40 (starting happiness) + (1 * 20) (1 neighbor)
# = 60
# The grid happiness is 120 + 60 + 60 = 240.
# The above figure shows the grid in this example with each person's happiness.
# The introvert stays in the light green cell while the extroverts live on the
# light purple cells.
# 
# Example 2:
# 
# Input: m = 3, n = 1, introvertsCount = 2, extrovertsCount = 1
# Output: 260
# 
# Explanation: Place the two introverts in (1,1) and (3,1) and the extrovert at
# (2,1).
# - Introvert at (1,1) happiness: 120 (starting happiness) - (1 * 30) (1 neighbor)
# = 90
# - Extrovert at (2,1) happiness: 40 (starting happiness) + (2 * 20) (2 neighbors)
# = 80
# - Introvert at (3,1) happiness: 120 (starting happiness) - (1 * 30) (1 neighbor)
# = 90
# The grid happiness is 90 + 80 + 90 = 260.
# 
# Example 3:
# 
# Input: m = 2, n = 2, introvertsCount = 4, extrovertsCount = 0
# Output: 240
# 
# 
# Constraints:
#         1 <= m, n <= 5
#         0 <= introvertsCount, extrovertsCount <= min(m * n, 6)


# Solution: https://algo.monster/liteproblems/1659
# Credit: AlgoMonster
def get_max_grid_happiness(m, n, introvertsCount, extrovertsCount):
    from functools import cache

    @cache
    def dfs(row, prev_state, introverts_left, extroverts_left):
        # Base cases: reached end of grid or no people left to place
        if row == m or (introverts_left == 0 and extroverts_left == 0):
            return 0
        
        max_happiness = 0
        # Try all possible states for current row
        for curr_state in range(max_states):
            # Check if we have enough people for this state
            if introverts_in_state[curr_state] <= introverts_left and \
                extroverts_in_state[curr_state] <= extroverts_left:
                # Calculate happiness for current row + interaction with previous row
                current_happiness = base_happiness[curr_state] + interaction_happiness[prev_state][curr_state]
                # Recursively calculate happiness for remaining rows
                future_happiness = dfs(
                    row + 1, 
                    curr_state, 
                    introverts_left - introverts_in_state[curr_state], 
                    extroverts_left - extroverts_in_state[curr_state]
                )
                max_happiness = max(max_happiness, current_happiness + future_happiness)
        
        return max_happiness
    
    # Maximum possible states for a row (3^n: empty, introvert, extrovert)
    max_states = 3 ** n
    
    # Precomputed values for efficiency
    base_happiness = [0] * max_states  # Base happiness for each row state
    interaction_happiness = [[0] * max_states for _ in range(max_states)]  # Interaction between adjacent rows
    
    # Happiness matrix for adjacent cells
    # happiness_matrix[i][j] = happiness change when cell type i is adjacent to cell type j
    # 0: empty, 1: introvert, 2: extrovert
    happiness_matrix = [
        [0, 0, 0],      # Empty cell adjacent to anything
        [0, -60, -10],  # Introvert adjacent to [empty, introvert, extrovert]
        [0, -10, 40]    # Extrovert adjacent to [empty, introvert, extrovert]
    ]
    
    # Decode each state into cell configurations
    state_cells = [[0] * n for _ in range(max_states)]
    introverts_in_state = [0] * max_states
    extroverts_in_state = [0] * max_states
    
    # Precompute state information
    for state in range(max_states):
        temp_state = state
        for col in range(n):
            # Extract cell type using ternary representation
            temp_state, cell_type = divmod(temp_state, 3)
            state_cells[state][col] = cell_type
            
            # Count people and calculate base happiness
            if cell_type == 1:  # Introvert
                introverts_in_state[state] += 1
                base_happiness[state] += 120
            elif cell_type == 2:  # Extrovert
                extroverts_in_state[state] += 1
                base_happiness[state] += 40
            
            # Add horizontal interaction happiness (within same row)
            if col > 0:
                base_happiness[state] += happiness_matrix[cell_type][state_cells[state][col - 1]]
    
    # Precompute vertical interaction happiness between adjacent rows
    for prev_state in range(max_states):
        for curr_state in range(max_states):
            for col in range(n):
                interaction_happiness[prev_state][curr_state] += \
                    happiness_matrix[state_cells[prev_state][col]][state_cells[curr_state][col]]
    
    # Start DFS from first row with no previous state
    return dfs(0, 0, introvertsCount, extrovertsCount)
    # Time: O(m * 9ⁿ * i * e)
    # Space: O(m * 3ⁿ * i * e)
    # Where m and n are grid dimensions
    # i = introvertsCount
    # e = extrovertsCount


def main():
    result = get_max_grid_happiness(m = 2, n = 3, introvertsCount = 1, extrovertsCount = 2)
    print(result) # 240

    result = get_max_grid_happiness(m = 3, n = 1, introvertsCount = 2, extrovertsCount = 1)
    print(result) # 260

    result = get_max_grid_happiness(m = 2, n = 2, introvertsCount = 4, extrovertsCount = 0)
    print(result) # 240

if __name__ == "__main__":
    main()
