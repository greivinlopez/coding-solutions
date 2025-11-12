# --------------
# 542. 01 Matrix
# --------------

# Problem: https://leetcode.com/problems/01-matrix
#
# Given an m x n binary matrix mat, return the distance of the nearest 0 for each
# cell.
# The distance between two cells sharing a common edge is 1.
# 
# Example 1:
# 
# https://assets.leetcode.com/uploads/2021/04/24/01-1-grid.jpg
# 
# Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
# Output: [[0,0,0],[0,1,0],[0,0,0]]
# 
# Example 2:
# 
# https://assets.leetcode.com/uploads/2021/04/24/01-2-grid.jpg
# 
# Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
# Output: [[0,0,0],[0,1,0],[1,2,1]]
# 
# 
# Constraints:
#         m == mat.length
#         n == mat[i].length
#         1 <= m, n <= 10⁴
#         1 <= m * n <= 10⁴
#         mat[i][j] is either 0 or 1.
#         There is at least one 0 in mat.
# 
# Note: This question is the same as 1765: https://leetcode.com/problems/map-of-highest-peak/

# Credit: Jaweria Batool -> https://github.com/Jaweria-B
def update_matrix(mat):
    n = len(mat)
    m = len(mat[0])
    
    if mat[0][0] != 0:
        mat[0][0] = m + n
    
    # Travel top down
    for j in range(1, m):
        if mat[0][j] != 0:
            mat[0][j] = mat[0][j - 1] + 1
    
    for i in range(1, n):
        if mat[i][0] != 0:
            mat[i][0] = mat[i - 1][0] + 1
    
    for i in range(1, n):
        for j in range(1, m):
            if mat[i][j] != 0:
                mat[i][j] = min(mat[i - 1][j], mat[i][j - 1]) + 1
    
    # Travel up
    for j in range(m - 2, -1, -1):
        if mat[n - 1][j] != 0:
            mat[n - 1][j] = min(mat[n - 1][j], mat[n - 1][j + 1] + 1)
    
    for i in range(n - 2, -1, -1):
        if mat[i][m - 1] != 0:
            mat[i][m - 1] = min(mat[i][m - 1], mat[i + 1][m - 1] + 1)
    
    for i in range(n - 2, -1, -1):
        for j in range(m - 2, -1, -1):
            if mat[i][j] != 0:
                mat[i][j] = min(mat[i][j], min(mat[i + 1][j], mat[i][j + 1]) + 1)
    
    return mat
    # Time: O(n * m)
    # Space: (1)
    # n = the number of rows
    # m = the number of columns


def main():
    result = update_matrix(mat = [[0,0,0],[0,1,0],[0,0,0]])
    print(result) # [[0,0,0],[0,1,0],[0,0,0]]

    result = update_matrix(mat = [[0,0,0],[0,1,0],[1,1,1]])
    print(result) # [[0,0,0],[0,1,0],[1,2,1]]

if __name__ == "__main__":
    main()
