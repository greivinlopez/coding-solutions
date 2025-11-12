# ----------------------
# 63. Unique Paths II 🤖
# ----------------------

# Problem: https://leetcode.com/problems/unique-paths-ii/
# 
# You are given an m x n integer array grid. There is a robot initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.
# 
# An obstacle and space are marked as 1 or 0 respectively in grid. A path that the robot takes cannot include any square that is an obstacle.
# 
# Return the number of possible unique paths that the robot can take to reach the bottom-right corner.
# 
# The testcases are generated so that the answer will be less than or equal to 2 * 10^9.

# Solution: https://youtu.be/d3UOz7zdE4I
# Credit: Navdeep Singh founder of NeetCode 
def unique_paths_with_obstacles(grid):
    # Time: O(m * n)
    # Space: O(m * n)
    M, N = len(grid), len(grid[0])
    dp = {(M - 1, N - 1): 1}

    def dfs(r, c):
        if r == M or c == N or grid[r][c]:
            return 0
        if (r, c) in dp:
            return dp[(r, c)]
        dp[(r, c)] = dfs(r + 1, c) + dfs(r, c + 1)
        return dp[(r, c)]
    return dfs(0, 0)

# Solution: https://youtu.be/d3UOz7zdE4I
# Credit: Navdeep Singh founder of NeetCode 
def unique_paths_with_obstacles_alt(grid):
    # Time: O(m * n)
    # Space: O(n)
    M, N = len(grid), len(grid[0])
    dp = [0] * N
    dp[N-1] = 1

    for r in reversed(range(M)):
        for c in reversed(range(N)):
            if grid[r][c]:
                dp[c] = 0
            elif c + 1 < N:
                dp[c] = dp[c] + dp[c + 1]
    return dp[0]


def main():
    result = unique_paths_with_obstacles([[0,0,0],[0,1,0],[0,0,0]]) # 2
    print(result)
    result = unique_paths_with_obstacles([[0,1],[0,0]]) # 1
    print(result)

if __name__ == "__main__":
    main()