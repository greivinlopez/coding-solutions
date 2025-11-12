# ----------------------------------------
# 329. Longest Increasing Path In A Matrix
# ----------------------------------------

# Problem: https://leetcode.com/problems/longest-increasing-path-in-a-matrix/
# 
# Given an m x n integers matrix, return the length of the longest increasing 
# path in matrix.
# 
# From each cell, you can either move in four directions: left, right, up, or 
# down. You may not move diagonally or move outside the boundary 
# (i.e., wrap-around is not allowed).
# 
#  
# Example 1:
# 
# Input: matrix = [[9,9,4],[6,6,8],[2,1,1]]
# Output: 4
# Explanation: The longest increasing path is [1, 2, 6, 9].
# 
# 
# Example 2:
# 
# Input: matrix = [[3,4,5],[3,2,6],[2,2,1]]
# Output: 4
# Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.
# 
# 
# Example 3:
# 
# Input: matrix = [[1]]
# Output: 1
# 
# 
# Constraints:
# 
# 	m == matrix.length
# 	n == matrix[i].length
# 	1 <= m, n <= 200
# 	0 <= matrix[i][j] <= 231 - 1


# Solution: https://youtu.be/wCc_nd-GiEc
# Credit: Navdeep Singh founder of NeetCode
def longest_increasing_path(matrix):
    ROWS, COLS = len(matrix), len(matrix[0])
    dp = {}  # (r, c) -> LIP

    def dfs(r, c, prevVal):
        if r < 0 or r == ROWS or c < 0 or c == COLS or matrix[r][c] <= prevVal:
            return 0
        if (r, c) in dp:
            return dp[(r, c)]

        res = 1
        res = max(res, 1 + dfs(r + 1, c, matrix[r][c]))
        res = max(res, 1 + dfs(r - 1, c, matrix[r][c]))
        res = max(res, 1 + dfs(r, c + 1, matrix[r][c]))
        res = max(res, 1 + dfs(r, c - 1, matrix[r][c]))
        dp[(r, c)] = res
        return res

    for r in range(ROWS):
        for c in range(COLS):
            dfs(r, c, -1)
    return max(dp.values())


def main():
    result = longest_increasing_path([[9,9,4],[6,6,8],[2,1,1]])
    print(result) # 4

    result = longest_increasing_path([[3,4,5],[3,2,6],[2,2,1]])
    print(result) # 4

    result = longest_increasing_path([[1]])
    print(result) # 1

if __name__ == "__main__":
    main()
