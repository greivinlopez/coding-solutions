# ------------------------------------------
# 1582. Special Positions In A Binary Matrix
# ------------------------------------------

# Problem: https://leetcode.com/problems/special-positions-in-a-binary-matrix
#
# Given an m x n binary matrix mat, return the number of special positions in mat.
# 
# A position (i, j) is called special if mat[i][j] == 1 and all other elements in
# row i and column j are 0 (rows and columns are 0-indexed).
# 
# 
# Example 1:
# 
# Input: mat = [[1,0,0],[0,0,1],[1,0,0]]
# Output: 1
# Explanation: (1, 2) is a special position because mat[1][2] == 1 and all other
# elements in row 1 and column 2 are 0.
# 
# Example 2:
# 
# Input: mat = [[1,0,0],[0,1,0],[0,0,1]]
# Output: 3
# Explanation: (0, 0), (1, 1) and (2, 2) are special positions.
# 
# 
# Constraints:
#         m == mat.length
#         n == mat[i].length
#         1 <= m, n <= 100
#         mat[i][j] is either 0 or 1.


# Solution: No video found
# Credit: Navdeep Singh founder of NeetCode
def num_special(mat):
    m = len(mat)
    n = len(mat[0])
    rowCount = [0] * m
    colCount = [0] * n
    res = 0
    for r in range(m):
        for c in range(n):
            if mat[r][c] == 1:
                rowCount[r] += 1
                colCount[c] += 1
    for r in range(m):
        for c in range(n):
            if mat[r][c] == 1 and rowCount[r] == 1 and colCount[c] == 1:
                res += 1
    return res


def main():
    result = num_special([[1,0,0],[0,0,1],[1,0,0]])
    print(result) # 1

    result = num_special([[1,0,0],[0,1,0],[0,0,1]])
    print(result) # 3

if __name__ == "__main__":
    main()
