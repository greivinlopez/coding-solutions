# --------------------
# 934. Shortest Bridge
# --------------------

# Problem: https://leetcode.com/problems/shortest-bridge
#
# You are given an n x n binary matrix grid where 1 represents land and 0
# represents water.
# 
# An island is a 4-directionally connected group of 1's not connected to any other
# 1's. There are exactly two islands in grid.
# 
# You may change 0's to 1's to connect the two islands to form one island.
# 
# Return the smallest number of 0's you must flip to connect the two islands.
# 
# Example 1:
# 
# Input: grid = [[0,1],[1,0]]
# Output: 1
# 
# Example 2:
# 
# Input: grid = [[0,1,0],[0,0,0],[0,0,1]]
# Output: 2
# 
# Example 3:
# 
# Input: grid = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
# Output: 1
# 
# 
# Constraints:
#         n == grid.length == grid[i].length
#         2 <= n <= 100
#         grid[i][j] is either 0 or 1.
#         There are exactly two islands in grid.

from collections import deque

# Solution: https://youtu.be/gkINMhbbIbU
# Credit: Navdeep Singh founder of NeetCode
def shortest_bridge(grid):
    N = len(grid)
    direct = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    
    def invalid(r, c):
        return r < 0 or c < 0 or r == N or c == N
    
    visit = set()
    def dfs(r, c):
        if (invalid(r, c) or not grid[r][c] or (r, c) in visit):
            return
        visit.add((r, c))
        for dr, dc in direct:
            dfs(r + dr, c + dc)
    
    def bfs():
        res, q = 0, deque(visit)
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in direct:
                    currR, currC = r + dr, c + dc
                    if invalid(currR, currC) or (currR, currC) in visit:
                        continue
                    if grid[currR][currC]:
                        return res
                    q.append((currR, currC))
                    visit.add((currR, currC))
            res += 1
    
    for r in range(N):
        for c in range(N):
            if grid[r][c]:
                dfs(r, c)
                return bfs()
    # Time: O(n²)
    # Space: O(n²)


def main():
    result = shortest_bridge(grid = [[0,1],[1,0]])
    print(result) # 1

    result = shortest_bridge(grid = [[0,1,0],
                                     [0,0,0],
                                     [0,0,1]])
    print(result) # 2

    result = shortest_bridge(grid = [[1,1,1,1,1],
                                     [1,0,0,0,1],
                                     [1,0,1,0,1],
                                     [1,0,0,0,1],
                                     [1,1,1,1,1]])
    print(result) # 1

if __name__ == "__main__":
    main()
