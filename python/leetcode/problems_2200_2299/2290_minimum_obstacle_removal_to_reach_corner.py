# ----------------------------------------------
# 2290. Minimum Obstacle Removal to Reach Corner
# ----------------------------------------------

# Problem: https://leetcode.com/problems/minimum-obstacle-removal-to-reach-corner
#
# You are given a 0-indexed 2D integer array grid of size m x n. Each cell has one
# of two values:
#         
#   0 represents an empty cell,
#   1 represents an obstacle that may be removed.
# 
# You can move up, down, left, or right from and to an empty cell.
# 
# Return the minimum number of obstacles to remove so you can move from the upper
# left corner (0, 0) to the lower right corner (m - 1, n - 1).
# 
# Example 1:
# 
# Input: grid = [[0,1,1],[1,1,0],[1,1,0]]
# Output: 2
# 
# Explanation: We can remove the obstacles at (0, 1) and (0, 2) to create a path
# from (0, 0) to (2, 2).
# It can be shown that we need to remove at least 2 obstacles, so we return 2.
# Note that there may be other ways to remove 2 obstacles to create a path.
# 
# Example 2:
# 
# Input: grid = [[0,1,0,0,0],[0,1,0,1,0],[0,0,0,1,0]]
# Output: 0
# 
# Explanation: We can move from (0, 0) to (2, 4) without removing any obstacles,
# so we return 0.
# 
# 
# Constraints:
#         m == grid.length
#         n == grid[i].length
#         1 <= m, n <= 10^5
#         2 <= m * n <= 10^5
#         grid[i][j] is either 0 or 1.
#         grid[0][0] == grid[m - 1][n - 1] == 0

from collections import deque

# Solution: https://youtu.be/VxeH7_QL-28
# Credit: Navdeep Singh founder of NeetCode
def minimum_obstacles(grid):
    ROWS, COLS = len(grid), len(grid[0])
    q = deque([(0, 0, 0)])  # (obstacles, r, c)
    visit = set([(0, 0)])

    while q:
        obstacles, r, c = q.popleft()

        if (r, c) == (ROWS - 1, COLS - 1):
            return obstacles

        nei = [[r + 1, c], [r - 1, c], [r, c + 1], [r, c - 1]]
        for nr, nc in nei:
            if (nr, nc) in visit or nr < 0 or nc < 0 or nc == COLS or nr == ROWS:
                continue

            if grid[nr][nc]:
                q.append((obstacles + 1, nr, nc))
            else:
                q.appendleft((obstacles, nr, nc))
            visit.add((nr, nc))
    # Time: O(rows * cols)
    # Space: O(rows * cols)

def main():
    result = minimum_obstacles(grid = [[0,1,1],[1,1,0],[1,1,0]])
    print(result) # 2

    result = minimum_obstacles(grid = [[0,1,0,0,0],[0,1,0,1,0],[0,0,0,1,0]])
    print(result) # 0

if __name__ == "__main__":
    main()
