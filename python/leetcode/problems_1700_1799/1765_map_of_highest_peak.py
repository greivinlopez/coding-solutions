# ----------------------------
# 1765. Map of Highest Peak 🗻
# ----------------------------

# Problem: https://leetcode.com/problems/map-of-highest-peak
#
# You are given an integer matrix isWater of size m x n that represents a map of
# land and water cells.
#         
#   If isWater[i][j] == 0, cell (i, j) is a land cell.       
#   If isWater[i][j] == 1, cell (i, j) is a water cell.
# 
# You must assign each cell a height in a way that follows these rules:
#         
#   The height of each cell must be non-negative.
#   If the cell is a water cell, its height must be 0.
#   Any two adjacent cells must have an absolute height difference of at
#   most 1. A cell is adjacent to another cell if the former is directly north,
#   east, south, or west of the latter (i.e., their sides are touching).
# 
# Find an assignment of heights such that the maximum height in the matrix is
# maximized.
# 
# Return an integer matrix height of size m x n where height[i][j] is cell (i,j)'s height. 
# If there are multiple solutions, return any of them.
# 
# Example 1:
# 
# Input: isWater = [[0,1],[0,0]]
# Output: [[1,0],[2,1]]
# 
# Explanation: The image shows the assigned heights of each cell.
# The blue cell is the water cell, and the green cells are the land cells.
# 
# Example 2:
# 
# Input: isWater = [[0,0,1],[1,0,0],[0,0,0]]
# Output: [[1,1,0],[0,1,1],[1,2,2]]
# 
# Explanation: A height of 2 is the maximum possible height of any assignment.
# Any height assignment that has a maximum height of 2 while still meeting the
# rules will also be accepted.
# 
# 
# Constraints:
#         m == isWater.length
#         n == isWater[i].length
#         1 <= m, n <= 1000
#         isWater[i][j] is 0 or 1.
#         There is at least one water cell.
# 
# Note: This question is the same as 542: https://leetcode.com/problems/01-matrix/

from collections import deque

# Solution: https://youtu.be/cQRZ202j-kA
# Credit: Navdeep Singh founder of NeetCode
def highest_peak(is_water):
    ROWS, COLS = len(is_water), len(is_water[0])
    q = deque()
    res = [[-1] * COLS for _ in range(ROWS)]

    # Enqueue all water cells
    for r in range(ROWS):
        for c in range(COLS):
            if is_water[r][c]:
                q.append((r, c))
                res[r][c] = 0

    # BFS
    while q:
        r, c = q.popleft()
        h = res[r][c]
        neighbors = [[r + 1, c], [r, c + 1], [r - 1, c], [r, c - 1]]
        for nr, nc in neighbors:
            if (nr < 0 or nc < 0 or
                    nr == ROWS or nc == COLS or
                    res[nr][nc] != -1):
                continue
            q.append((nr, nc))
            res[nr][nc] = h + 1

    return res
    # Time: O(r * c)
    # Space: O(r * c)
    # r = number of rows
    # c = number of columns


def main():
    result = highest_peak([[0,1],[0,0]])
    print(result) # [[1,0],[2,1]]

    result = highest_peak([[0,0,1],[1,0,0],[0,0,0]])
    print(result) # [[1,1,0],[0,1,1],[1,2,2]]

if __name__ == "__main__":
    main()
