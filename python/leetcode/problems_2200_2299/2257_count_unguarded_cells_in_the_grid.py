# ---------------------------------------
# 2257. Count Unguarded Cells in the Grid
# ---------------------------------------

# Problem: https://leetcode.com/problems/count-unguarded-cells-in-the-grid
#
# You are given two integers m and n representing a 0-indexed m x n grid. You are
# also given two 2D integer arrays guards and walls where guards[i] = [rowi, coli]
# and walls[j] = [rowj, colj] represent the positions of the ith guard and jth
# wall respectively.
# 
# A guard can see every cell in the four cardinal directions (north, east, south,
# or west) starting from their position unless obstructed by a wall or another
# guard. A cell is guarded if there is at least one guard that can see it.
# 
# Return the number of unoccupied cells that are not guarded.
# 
# Example 1:
# 
# Input: m = 4, n = 6, guards = [[0,0],[1,1],[2,3]], walls = [[0,1],[2,2],[1,4]]
# Output: 7
# 
# Explanation: The guarded and unguarded cells are shown in red and green
# respectively in the above diagram.
# There are a total of 7 unguarded cells, so we return 7.
# 
# Example 2:
# 
# Input: m = 3, n = 3, guards = [[1,1]], walls = [[0,1],[1,0],[2,1],[1,2]]
# Output: 4
# 
# Explanation: The unguarded cells are shown in green in the above diagram.
# There are a total of 4 unguarded cells, so we return 4.
# 
# 
# Constraints:
#         1 <= m, n <= 10^5
#         2 <= m * n <= 10^5
#         1 <= guards.length, walls.length <= 5 * 10^4
#         2 <= guards.length + walls.length <= m * n
#         guards[i].length == walls[j].length == 2
#         0 <= rowi, rowj < m
#         0 <= coli, colj < n
#         All the positions in guards and walls are unique.


# Solution: https://youtu.be/3WVHdSWHxxQ
# Credit: Navdeep Singh founder of NeetCode
def count_unguarded(m, n, guards, walls):
    mat = [[0] * n for _ in range(m)]

    # 0 = empty
    # 1 = guard
    # 2 = wall
    # 3 = guardable

    for r, c in guards:
        mat[r][c] = 1

    for r, c in walls:
        mat[r][c] = 2

    for r in range(m):
        guard = False
        for c in range(n):
            if mat[r][c] == 1:
                guard = True
            elif mat[r][c] == 2:
                guard = False
            if not mat[r][c] and guard:
                mat[r][c] = 3

        guard = False
        for c in reversed(range(n)):
            if mat[r][c] == 1:
                guard = True
            elif mat[r][c] == 2:
                guard = False
            if not mat[r][c] and guard:
                mat[r][c] = 3

    for c in range(n):
        guard = False
        for r in range(m):
            if mat[r][c] == 1:
                guard = True
            elif mat[r][c] == 2:
                guard = False
            if not mat[r][c] and guard:
                mat[r][c] = 3

        guard = False
        for r in reversed(range(m)):
            if mat[r][c] == 1:
                guard = True
            elif mat[r][c] == 2:
                guard = False
            if not mat[r][c] and guard:
                mat[r][c] = 3
    
    res = 0
    for row in mat:
        for n in row:
            if n == 0:
                res += 1
    return res


def main():
    result = count_unguarded(m = 4, n = 6, guards = [[0,0],[1,1],[2,3]], walls = [[0,1],[2,2],[1,4]])
    print(result) # 7

    result = count_unguarded(m = 3, n = 3, guards = [[1,1]], walls = [[0,1],[1,0],[2,1],[1,2]])
    print(result) # 4

if __name__ == "__main__":
    main()
