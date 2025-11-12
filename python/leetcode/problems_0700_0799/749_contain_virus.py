# ---------------------
# 749. Contain Virus 🦠
# ---------------------

# Problem: https://leetcode.com/problems/contain-virus
#
# A virus is spreading rapidly, and your task is to quarantine the infected area
# by installing walls.
# 
# The world is modeled as an m x n binary grid isInfected, where isInfected[i][j]
# == 0 represents uninfected cells, and isInfected[i][j] == 1 represents cells
# contaminated with the virus. A wall (and only one wall) can be installed between
# any two 4-directionally adjacent cells, on the shared boundary.
# 
# Every night, the virus spreads to all neighboring cells in all four directions
# unless blocked by a wall. Resources are limited. Each day, you can install walls
# around only one region (i.e., the affected area (continuous block of infected
# cells) that threatens the most uninfected cells the following night). There will
# never be a tie.
# 
# Return the number of walls used to quarantine all the infected regions. If the
# world will become fully infected, return the number of walls used.
# 
# Example 1:
# 
# https://assets.leetcode.com/uploads/2021/06/01/virus11-grid.jpg
# 
# Input: isInfected =
# [[0,1,0,0,0,0,0,1],[0,1,0,0,0,0,0,1],[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0]]
# Output: 10
# 
# Explanation: There are 2 contaminated regions.
# On the first day, add 5 walls to quarantine the viral region on the left. The
# board after the virus spreads is:
# 
# https://assets.leetcode.com/uploads/2021/06/01/virus12edited-grid.jpg
# 
# On the second day, add 5 walls to quarantine the viral region on the right. The
# virus is fully contained.
# 
# https://assets.leetcode.com/uploads/2021/06/01/virus13edited-grid.jpg
# 
# Example 2:
# 
# https://assets.leetcode.com/uploads/2021/06/01/virus2-grid.jpg
# 
# Input: isInfected = [[1,1,1],[1,0,1],[1,1,1]]
# Output: 4
# 
# Explanation: Even though there is only one cell saved, there are 4 walls built.
# Notice that walls are only built on the shared boundary of two different cells.
# 
# Example 3:
# 
# Input: isInfected =
# [[1,1,1,0,0,0,0,0,0],[1,0,1,0,1,1,1,1,1],[1,1,1,0,0,0,0,0,0]]
# Output: 13
# 
# Explanation: The region on the left only builds two new walls.
# 
# 
# Constraints:
#         m == isInfected.length
#         n == isInfected[i].length
#         1 <= m, n <= 50
#         isInfected[i][j] is either 0 or 1.
#         There is always a contiguous viral region throughout the described
# process that will infect strictly more uncontaminated squares in the next round.


# Solution: https://algo.monster/liteproblems/749
# Credit: AlgoMonster
def contain_virus(isInfected):
    def dfs(row, col):
        visited[row][col] = True
        current_region.append((row, col))
        
        # Check all 4 adjacent cells
        for delta_row, delta_col in [[0, -1], [0, 1], [-1, 0], [1, 0]]:
            new_row, new_col = row + delta_row, col + delta_col
            
            if 0 <= new_row < rows and 0 <= new_col < cols:
                if isInfected[new_row][new_col] == 1 and not visited[new_row][new_col]:
                    # Continue exploring infected cells
                    dfs(new_row, new_col)
                elif isInfected[new_row][new_col] == 0:
                    # Count walls needed and track threatened cells
                    walls_needed[-1] += 1
                    threatened_cells[-1].add((new_row, new_col))
    
    rows, cols = len(isInfected), len(isInfected[0])
    total_walls = 0
    
    while True:
        # Initialize tracking structures for this iteration
        visited = [[False] * cols for _ in range(rows)]
        infected_regions = []  # List of infected cell coordinates for each region
        walls_needed = []      # Number of walls needed for each region
        threatened_cells = []  # Set of uninfected cells threatened by each region
        
        # Find all distinct infected regions
        for i in range(rows):
            for j in range(cols):
                if isInfected[i][j] == 1 and not visited[i][j]:
                    # Start new region exploration
                    current_region = []
                    infected_regions.append(current_region)
                    threatened_cells.append(set())
                    walls_needed.append(0)
                    dfs(i, j)
        
        # If no infected regions remain, we're done
        if not infected_regions:
            break
        
        # Find the region that threatens the most cells
        most_dangerous_idx = threatened_cells.index(max(threatened_cells, key=len))
        
        # Add walls needed for the most dangerous region
        total_walls += walls_needed[most_dangerous_idx]
        
        # Process each region
        for region_idx, region in enumerate(infected_regions):
            if region_idx == most_dangerous_idx:
                # Quarantine the most dangerous region (mark as contained with -1)
                for i, j in region:
                    isInfected[i][j] = -1
            else:
                # Spread virus from other regions to adjacent uninfected cells
                for i, j in region:
                    for delta_row, delta_col in [[0, -1], [0, 1], [-1, 0], [1, 0]]:
                        new_row, new_col = i + delta_row, j + delta_col
                        if (0 <= new_row < rows and 0 <= new_col < cols 
                            and isInfected[new_row][new_col] == 0):
                            isInfected[new_row][new_col] = 1
    
    return total_walls
    # Time: O(m * n)
    # Space: O(m * n)


def main():
    result = contain_virus([[0,1,0,0,0,0,0,1],[0,1,0,0,0,0,0,1],[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0]])
    print(result) # 10

    result = contain_virus([[1,1,1],[1,0,1],[1,1,1]])
    print(result) # 4

    result = contain_virus([[1,1,1,0,0,0,0,0,0],[1,0,1,0,1,1,1,1,1],[1,1,1,0,0,0,0,0,0]])
    print(result) # 13

if __name__ == "__main__":
    main()
