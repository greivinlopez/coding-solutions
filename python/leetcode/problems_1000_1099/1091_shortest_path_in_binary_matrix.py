# -----------------------------------
# 1091. Shortest Path In Binary Matrix
# -----------------------------------

# Problem: https://leetcode.com/problems/shortest-path-in-binary-matrix
#
# 
# Given an n x n binary matrix grid, return the length of the shortest clear path
# in the matrix. If there is no clear path, return -1.
# 
# A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0))
# to the bottom-right cell (i.e., (n - 1, n - 1)) such that:
# 
#         - All the visited cells of the path are 0.
#         - All the adjacent cells of the path are 8-directionally connected (i.e.,
#           they are different and they share an edge or a corner).
# 
# The length of a clear path is the number of visited cells of this path.
# 
# Example 1:
# 
# Input: grid = [[0,1],[1,0]]
# Output: 2
# 
# Example 2:
# Input: grid = [[0,0,0],[1,1,0],[1,1,0]]
# Output: 4
# 
# Example 3:
# 
# Input: grid = [[1,0,0],[1,1,0],[1,1,0]]
# Output: -1
# 
# 
# Constraints:
#         n == grid.length
#         n == grid[i].length
#         1 <= n <= 100
#         grid[i][j] is 0 or 1

from collections import deque

# Solution: https://youtu.be/YnxUdAO7TAo
# Credit: Navdeep Singh founder of NeetCode
def shortest_path_binary_matrix(grid):
    N = len(grid)
    q = deque([(0, 0, 1)]) # r, c, length
    visit = set((0, 0))
    direct = [[0, 1], [1, 0], [0, -1], [-1, 0],
                [1, 1], [-1, -1], [1, -1], [-1, 1]]
    while q:
        r, c, length = q.popleft()
        if (min(r, c) < 0 or max(r, c) >= N or
            grid[r][c]):
            continue
        if r == N - 1 and c == N - 1:
            return length
        for dr, dc in direct:
            if (r + dr, c + dc) not in visit:
                q.append((r + dr, c + dc, length + 1))
                visit.add((r + dr, c + dc))
    return -1


def main():
    result = shortest_path_binary_matrix([[0,1],[1,0]])
    print(result) # 2

    result = shortest_path_binary_matrix([[0,0,0],[1,1,0],[1,1,0]])
    print(result) # 4

    result = shortest_path_binary_matrix([[1,0,0],[1,1,0],[1,1,0]])
    print(result) # -1

if __name__ == "__main__":
    main()
