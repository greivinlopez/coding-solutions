# --------------------
# 62. Unique Paths 🤖
# --------------------

# Problem: https://leetcode.com/problems/unique-paths/
# 
# There is a robot on an m x n grid. The robot is initially located at the 
# top-left corner (i.e., grid[0][0]). The robot tries to move to the 
# bottom-right corner (i.e., grid[m - 1][n - 1]). 
# The robot can only move either down or right at any point in time.
# 
# Given the two integers m and n, return the number of possible unique paths 
# that the robot can take to reach the bottom-right corner.
# 
# The test cases are generated so that the answer will be less than or equal to 2 * 10^9.

# Solution: https://youtu.be/IlEsdxuD4lY
# Credit: Navdeep Singh founder of NeetCode 
def unique_paths(m, n):
    # Time: O(m * n)
    # Space: O(n)
    row = [1] * n

    for i in range(m - 1):
        newRow = [1] * n
        for j in range(n - 2, -1, -1):
            newRow[j] = newRow[j + 1] + row[j]
        row = newRow
    return row[0]

# Solution: https://youtu.be/3ZFvBlynmls
# Credit: Greg Hogg
def unique_paths_alt(m, n):
    # Bottom Up DP (Tabulation)
    # Time: O(m * n)
    # Space: O(m * n)
    dp = []
    for _ in range(m):
        dp.append([0] * n)
    
    dp[0][0] = 1
    
    for i in range(m):
        for j in range(n):
            if i == j == 0:
                continue
                
            val = 0
            if i > 0:
                val += dp[i-1][j]
            if j > 0:
                val += dp[i][j-1]
            
            dp[i][j] = val
    
    return dp[m-1][n-1]

# Credit: Greg Hogg
def unique_paths_memo(m, n):
    # Top Down DP (Memoization)
    # Time: O(m*n)
    # Space: O(m*n)

    memo = {(0,0): 1}
    def paths(i, j):
        if (i,j) in memo:
            return memo[(i,j)]
        elif i < 0 or j < 0 or i == m or j == n:
            return 0
        else:
            val = paths(i, j-1) + paths(i-1, j)
            memo[(i,j)] = val
            return val
    
    return paths(m-1, n-1)

# Credit: Greg Hogg
def unique_paths_recursive(m, n):
    # Recursive Solution
    # Time: O(2^(m*n))
    # Space: O(m*n)
    
    def paths(i, j):
        if i == j == 0:
            return 1
        elif i < 0 or j < 0 or i == m or j == n:
            return 0
        else:
            return paths(i-1, j) + paths(i, j-1)
    
    return paths(m-1, n-1)

def main():
    result = unique_paths(m = 3, n = 7) # 28
    print(result)
    result = unique_paths(m = 3, n = 2) # 3
    print(result)

if __name__ == "__main__":
    main()