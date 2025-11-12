# --------------------
# 994. Rotting Oranges
# --------------------

# Problem: https://leetcode.com/problems/rotting-oranges
#
# You are given an m x n grid where each cell can have one of three values:
#         0 representing an empty cell,
#         1 representing a fresh orange, or
#         2 representing a rotten orange.
# 
# Every minute, any fresh orange that is 4-directionally adjacent to a rotten
# orange becomes rotten.
# 
# Return the minimum number of minutes that must elapse until no cell has a fresh
# orange. If this is impossible, return -1.
# 
# Example 1:
# 
# Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
# Output: 4
# 
# Example 2:
# 
# Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
# Output: -1
# Explanation: The orange in the bottom left corner (row 2, column 0) is never
# rotten, because rotting only happens 4-directionally.
# 
# Example 3:
# 
# Input: grid = [[0,2]]
# Output: 0
# Explanation: Since there are already no fresh oranges at minute 0, the answer is
# just 0.
# 
# 
# Constraints:
# 
#         m == grid.length
#         n == grid[i].length
#         1 <= m, n <= 10
#         grid[i][j] is 0, 1, or 2.

import collections

# Solution: https://youtu.be/y704fEOx0s0
# Credit: Navdeep Singh founder of NeetCode
def oranges_rotting(grid):
    q = collections.deque()
    fresh = 0
    time = 0

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == 1:
                fresh += 1
            if grid[r][c] == 2:
                q.append((r, c))

    directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    while fresh > 0 and q:
        length = len(q)
        for i in range(length):
            r, c = q.popleft()

            for dr, dc in directions:
                row, col = r + dr, c + dc
                # if in bounds and nonrotten, make rotten
                # and add to q
                if (
                    row in range(len(grid))
                    and col in range(len(grid[0]))
                    and grid[row][col] == 1
                ):
                    grid[row][col] = 2
                    q.append((row, col))
                    fresh -= 1
        time += 1
    return time if fresh == 0 else -1

# Solution: https://youtu.be/nAVKrpJ8LUI
# Credit: Greg Hogg
def oranges_rotting_alt(grid):
    EMPTY, FRESH, ROTTEN = 0, 1, 2
    m, n = len(grid), len(grid[0])
    num_fresh = 0
    q = collections.deque()

    for i in range(m):
        for j in range(n):
            if grid[i][j] == ROTTEN:
                q.append((i, j))
            elif grid[i][j] == FRESH:
                num_fresh += 1

    if num_fresh == 0:
        return 0

    num_minutes = -1
    while q:
        q_size = len(q)
        num_minutes += 1
    
        for _ in range(q_size):
            i, j = q.popleft()
            for r, c in [(i, j + 1), (i + 1, j), (i, j - 1), (i - 1, j)]:
                if 0 <= r < m and 0 <= c < n and grid[r][c] == FRESH:
                    grid[r][c] = ROTTEN
                    num_fresh -= 1
                    q.append((r, c))

    if num_fresh == 0:
        return num_minutes
    else:
        return -1
    # Time: O(m*n)
    # Space: O(m*n)

def oranges_rotting_bootcamp(grid):
    # Initialize variables
    Minute = 0
    Q = collections.deque()
    FreshCount = 0
    M, N = len(grid), len(grid[0])
    
    # Populate queue with initial rotten oranges and count fresh oranges
    for i in range(M):
        for j in range(N):
            if grid[i][j] == 2:
                Q.append((i, j))
            elif grid[i][j] == 1:
                FreshCount += 1

    # Perform BFS
    while Q and FreshCount > 0:
        NumRotting = len(Q)
        for _ in range(NumRotting):
            i, j = Q.popleft()
            for r, c in [(i, j + 1), (i + 1, j), (i, j - 1), (i - 1, j)]:
                if 0 <= r < M and 0 <= c < N and grid[r][c] == 1:
                    grid[r][c] = 2
                    FreshCount -= 1
                    Q.append((r, c))
        Minute += 1  # Increment minute after processing all rotten oranges in this round
    
    # Return the time taken or -1 if fresh oranges remain
    return Minute if FreshCount == 0 else -1

def main():
    result = oranges_rotting([[2,1,1],[1,1,0],[0,1,1]])
    print(result) # 4

    result = oranges_rotting([[2,1,1],[0,1,1],[1,0,1]])
    print(result) # -1

    result = oranges_rotting([[0,2]])
    print(result) # 0

if __name__ == "__main__":
    main()
