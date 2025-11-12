# ---------------------
# 64. Minimum Path Sum
# ---------------------

# Problem: https://leetcode.com/problems/minimum-path-sum/
# 
# Given a m x n grid filled with non-negative numbers, find a path from top left
# to bottom right, which minimizes the sum of all numbers along its path.
# 
# Note: You can only move either down or right at any point in time.

# Solution: https://youtu.be/pGMsrvt0fpk
# Credit: Navdeep Singh founder of NeetCode 
def min_path_sum(grid):
    m, n = len(grid), len(grid[0])
    prev = [float("inf")] * n
    prev[-1] = 0

    for row in range(m - 1, -1, -1):
        dp = [float("inf")] * n
        for col in range(n - 1, -1, -1):
            if col < n - 1:
                dp[col] = min(dp[col], dp[col + 1])
            dp[col] = min(dp[col], prev[col]) + grid[row][col]
        prev = dp

    return prev[0]

def main():
    result = min_path_sum([[1,3,1],[1,5,1],[4,2,1]]) # 7
    print(result)
    result = min_path_sum([[1,2,3],[4,5,6]]) # 12
    print(result)

if __name__ == "__main__":
    main()