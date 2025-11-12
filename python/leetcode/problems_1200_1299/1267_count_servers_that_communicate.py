# ------------------------------------
# 1267. Count Servers that Communicate
# ------------------------------------

# Problem: https://leetcode.com/problems/count-servers-that-communicate
#
# You are given a map of a server center, represented as a m * n integer matrix 
# grid, where 1 means that on that cell there is a server and 0 means that
# it is no server. Two servers are said to communicate if they are on the same row
# or on the same column.
# 
# Return the number of servers that communicate with any other server.
# 
# Example 1:
# 
# Input: grid = [[1,0],[0,1]]
# Output: 0
# 
# Explanation: No servers can communicate with others.
# 
# Example 2:
# 
# Input: grid = [[1,0],[1,1]]
# Output: 3
# 
# Explanation: All three servers can communicate with at least one other server.
# 
# Example 3:
# 
# Input: grid = [[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]
# Output: 4
# 
# Explanation: The two servers in the first row can communicate with each other.
# The two servers in the third column can communicate with each other. The server
# at right bottom corner can't communicate with any other server.
# 
# 
# Constraints:
#         m == grid.length
#         n == grid[i].length
#         1 <= m <= 250
#         1 <= n <= 250
#         grid[i][j] == 0 or 1


# Solution: https://youtu.be/meTbkgqNNYM
# Credit: Navdeep Singh founder of NeetCode
def count_servers(grid):
    ROWS, COLS = len(grid), len(grid[0])
    row_cnt = [0] * ROWS
    col_cnt = [0] * COLS

    # Preprocessing
    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] == 1:
                row_cnt[r] += 1
                col_cnt[c] += 1
    
    res = 0
    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] and max(row_cnt[r], col_cnt[c]) > 1:
                res += 1
    
    return res
    # Time: O(r * c)
    # Space: O(r + c)


def main():
    result = count_servers(grid = [[1,0],[0,1]])
    print(result) # 0

    result = count_servers(grid = [[1,0],[1,1]])
    print(result) # 3

    result = count_servers(grid = [[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]])
    print(result) # 4

if __name__ == "__main__":
    main()
