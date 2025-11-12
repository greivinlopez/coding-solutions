# ------------------------------
# 1254. Number Of Closed Islands
# ------------------------------

# Problem: https://leetcode.com/problems/number-of-closed-islands
#
# Given a 2D grid consists of 0s (land) and 1s (water).  An island is a maximal
# 4-directionally connected group of 0s and a closed island is an island
# totally (all left, top, right, bottom) surrounded by 1s.
# 
# Return the number of closed islands.
# 
# Example 1:
# 
# Input: grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,
# 1,0,1],[1,1,1,1,1,1,1,0]]
# Output: 2
# Explanation:
# Islands in gray are closed because they are completely surrounded by water
# (group of 1s).
# 
# Example 2:
# 
# Input: grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]
# Output: 1
# 
# Example 3:
# Input: grid = [[1,1,1,1,1,1,1],
#                [1,0,0,0,0,0,1],
#                [1,0,1,1,1,0,1],
#                [1,0,1,0,1,0,1],
#                [1,0,1,1,1,0,1],
#                [1,0,0,0,0,0,1],
#                [1,1,1,1,1,1,1]]
# Output: 2
# 
# Constraints:
#         1 <= grid.length, grid[0].length <= 100
#         0 <= grid[i][j] <=1


# Solution: https://youtu.be/X8k48xek8g8
# Credit: Navdeep Singh founder of NeetCode
def closed_island(grid):
    r = len(grid)
    c = len(grid[0])
    seen = set()

    def dfs(x, y):
        if x < 0 or x >= r or y < 0 or y >= c or (x, y) in seen or grid[x][y] == 1:
            return
        seen.add((x, y))
        grid[x][y] = 1
        dfs(x+1, y)
        dfs(x, y+1)
        dfs(x-1, y)
        dfs(x, y-1)
    
    for i in range(r):
        for j in range(c):
            if i == 0 or j == 0 or i == r-1 or j == c-1:
                dfs(i, j)
    ans = 0
    for i in range(r):
        for j in range(c):
            if grid[i][j] == 0:
                dfs(i, j)
                ans += 1
    return ans 

def main():
    grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
    result = closed_island(grid)
    print(result) # 2

    grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]
    result = closed_island(grid)
    print(result) # 1

    grid = [[1,1,1,1,1,1,1],
            [1,0,0,0,0,0,1],
            [1,0,1,1,1,0,1],
            [1,0,1,0,1,0,1],
            [1,0,1,1,1,0,1],
            [1,0,0,0,0,0,1],
            [1,1,1,1,1,1,1]]
    result = closed_island(grid)
    print(result) # 2

if __name__ == "__main__":
    main()
