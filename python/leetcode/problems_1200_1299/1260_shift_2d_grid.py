# -------------------
# 1260. Shift 2D Grid
# -------------------

# Problem: https://leetcode.com/problems/shift-2d-grid
#
# Given a 2D grid of size m x n and an integer k. You need to shift the grid k
# times.
# 
# In one shift operation:
#         Element at grid[i][j] moves to grid[i][j + 1].
#         Element at grid[i][n - 1] moves to grid[i + 1][0].
#         Element at grid[m - 1][n - 1] moves to grid[0][0].
# 
# Return the 2D grid after applying shift operation k times.
# 
# Example 1:
# 
# Input: grid = [[1,2,3],[4,5,6],[7,8,9]], k = 1
# Output: [[9,1,2],[3,4,5],[6,7,8]]
# 
# Example 2:
# 
# Input: grid = [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]], k = 4
# Output: [[12,0,21,13],[3,8,1,9],[19,7,2,5],[4,6,11,10]]
# 
# Example 3:
# 
# Input: grid = [[1,2,3],[4,5,6],[7,8,9]], k = 9
# Output: [[1,2,3],[4,5,6],[7,8,9]]
# 
# 
# Constraints:
#         m == grid.length
#         n == grid[i].length
#         1 <= m <= 50
#         1 <= n <= 50
#         -1000 <= grid[i][j] <= 1000
#         0 <= k <= 100


# Solution: https://youtu.be/nJYFh4Dl-as
# Credit: Navdeep Singh founder of NeetCode
def shift_grid(grid, k):
    M, N = len(grid), len(grid[0])
    
    def posToVal(r, c):
        return r * N + c
    def valToPos(v):
        return [v // N, v % N] # r, c
    
    res = [[0] * N for i in range(M)]
    for r in range(M):
        for c in range(N):
            newVal = (posToVal(r, c) + k) % (M * N)
            newR, newC = valToPos(newVal)
            res[newR][newC] = grid[r][c]
    return res


def main():
    grid = [[1,2,3],[4,5,6],[7,8,9]]
    result = shift_grid(grid, 1)
    print(result) # [[9,1,2],[3,4,5],[6,7,8]]

    grid = [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]]
    result = shift_grid(grid, 4)
    print(result) # [[12, 0, 21, 13], [3, 8, 1, 9], [19, 7, 2, 5], [4, 6, 11, 10]]

    grid = [[1,2,3],[4,5,6],[7,8,9]]
    result = shift_grid(grid, 9)
    print(result) # [[1,2,3],[4,5,6],[7,8,9]]

if __name__ == "__main__":
    main()
