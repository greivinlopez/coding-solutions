# -------------------------
# 200. Number Of Islands 🏝️
# -------------------------

# Problem: https://leetcode.com/problems/number-of-islands/
# 
# Given an m x n 2D binary grid grid which represents a map of '1's (land) 
# and '0's (water), return the number of islands.
# 
# An island is surrounded by water and is formed by connecting adjacent lands 
# horizontally or vertically. You may assume all four edges of the grid are 
# all surrounded by water.
# 
#  
# Example 1:
# 
# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1
# 
# 
# Example 2:
# 
# Input: grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# Output: 3
# 
# 
# Constraints:
# 
# 	m == grid.length
# 	n == grid[i].length
# 	1 <= m, n <= 300
# 	grid[i][j] is '0' or '1'.


# Solution: https://youtu.be/pV2kpPD66nE
# Credit: Navdeep Singh founder of NeetCode
def num_islands(grid):
    if not grid or not grid[0]:
        return 0

    islands = 0
    visit = set()
    rows, cols = len(grid), len(grid[0])

    def dfs(r, c):
        if (
            r not in range(rows)
            or c not in range(cols)
            or grid[r][c] == "0"
            or (r, c) in visit
        ):
            return

        visit.add((r, c))
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        for dr, dc in directions:
            dfs(r + dr, c + dc)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1" and (r, c) not in visit:
                islands += 1
                dfs(r, c)
    return islands

# DFS O(1) Space and much less code
def num_islands_dfs(grid):
    rows, cols = len(grid), len(grid[0])
    def dfs(r, c):
        if not 0 <= r < len(grid) or not 0 <= c < len(grid[0]) or grid[r][c] == '0':
            return 0
        grid[r][c] = '0'
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)
        return 1
    count = 0
    for r in range(rows):
        for c in range(cols):
            count += dfs(r, c)
    return count

# BFS Version From Video
def num_islands_bfs(grid):
    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    visited = set()
    islands = 0

    def bfs(r, c):
        q = deque()
        visited.add((r, c))
        q.append((r, c))
    
        while q:
            row, col = q.popleft()
            directions = [[1, 0],[-1, 0],[0, 1],[0, -1]]
        
            for dr, dc in directions:
                r, c = row + dr, col + dc
                if (r) in range(rows) and (c) in range(cols) and grid[r][c] == '1' and (r, c) not in visited:
                
                    q.append((r, c ))
                    visited.add((r, c ))

    for r in range(rows):
        for c in range(cols):
        
            if grid[r][c] == "1" and (r, c) not in visited:
                bfs(r, c)
                islands += 1 

    return islands

# Solution: https://youtu.be/gCswsDauXPc
# Credit: Greg Hogg
def num_islands_dfs_alt(grid):
    m, n = len(grid), len(grid[0])

    def dfs(i, j):
        if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] != "1":
            return
        else:
            grid[i][j] = "0"
            dfs(i, j + 1)
            dfs(i + 1, j)
            dfs(i, j - 1)
            dfs(i - 1, j)

    num_islands = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == "1":
                num_islands += 1
                dfs(i, j)

    return num_islands

def main():
    grid = [
            ["1","1","1","1","0"],
            ["1","1","0","1","0"],
            ["1","1","0","0","0"],
            ["0","0","0","0","0"]
            ]
    result = num_islands_dfs(grid)
    print(result) # 1

    grid = [
            ["1","1","0","0","0"],
            ["1","1","0","0","0"],
            ["0","0","1","0","0"],
            ["0","0","0","1","1"]
            ]
    result = num_islands_dfs(grid)
    print(result) # 3

if __name__ == "__main__":
    main()
