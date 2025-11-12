# -----------------------------
# 827. Making A Large Island 🏝️
# -----------------------------

# Problem: https://leetcode.com/problems/making-a-large-island
#
# You are given an n x n binary matrix grid. You are allowed to change at most one
# 0 to be 1.
# 
# Return the size of the largest island in grid after applying this operation.
# 
# An island is a 4-directionally connected group of 1s.
# 
# Example 1:
# 
# Input: grid = [[1,0],[0,1]]
# Output: 3
# 
# Explanation: Change one 0 to 1 and connect two 1s, then we get an island with
# area = 3.
# 
# Example 2:
# 
# Input: grid = [[1,1],[1,0]]
# Output: 4
# 
# Explanation: Change the 0 to 1 and make the island bigger, only one island with
# area = 4.
# 
# Example 3:
# 
# Input: grid = [[1,1],[1,1]]
# Output: 4
# 
# Explanation: Can't change any 0 to 1, only one island with area = 4.
# 
# 
# Constraints:
#         n == grid.length
#         n == grid[i].length
#         1 <= n <= 500
#         grid[i][j] is either 0 or 1.

from collections import defaultdict

# Solution: https://youtu.be/pq61VNqXGvA
# Credit: Navdeep Singh founder of NeetCode
def largest_island(grid):
    N = len(grid)

    def out_of_bounds(r, c):
        return (
            r < 0 and c < 0 or
            r == N or c == N
        )
    
    def dfs(r, c, label):
        if (out_of_bounds(r, c) or
            grid[r][c] != 1
        ):
            return 0
        grid[r][c] = label
        size = 1
        nei = [[r+1,c],[r-1,c],[r,c+1],[r,c-1]]
        for nr, nc in nei:
            size += dfs(nr, nc, label)
        return size    

    # 1. Precompute areas
    size = defaultdict(int)  # island label -> size
    label = 2
    for r in range(N):
        for c in range(N):
            if grid[r][c] == 1:
                size[label] = dfs(r, c, label)
                label += 1

    def connect(r, c):
        nei = [[r+1,c],[r-1,c],[r,c+1],[r,c-1]]
        visit = set()
        res = 1
        for nr, nc in nei:
            if not out_of_bounds(nr, nc) and grid[nr][nc] not in visit:
                res += size[grid[nr][nc]]
                visit.add(grid[nr][nc])
        return res

    # 2. Try flipping water
    res = 0 if not size else max(size.values())
    for r in range(N):
        for c in range(N):
            if grid[r][c] == 0:
                res = max(res, connect(r, c))
    return res
    # Time: O(n²)
    # Space: O(n²)


def main():
    result = largest_island(grid = [[1,0],[0,1]])
    print(result) # 3

    result = largest_island(grid = [[1,1],[1,0]])
    print(result) # 4

    result = largest_island(grid = [[1,1],[1,1]])
    print(result) # 4

if __name__ == "__main__":
    main()
