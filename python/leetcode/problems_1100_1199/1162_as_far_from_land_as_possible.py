# ----------------------------------
# 1162. As Far from Land as Possible
# ----------------------------------

# Problem: https://leetcode.com/problems/as-far-from-land-as-possible
#
# Given an n x n grid containing only values 0 and 1, where 0 represents water and
# 1 represents land, find a water cell such that its distance to the nearest land
# cell is maximized, and return the distance. If no land or water exists in the
# grid, return -1.
# 
# The distance used in this problem is the Manhattan distance: the distance
# between two cells (x0, y0) and (x1, y1) is |x0 - x1| + |y0 - y1|.
# 
# Example 1:
# 
# Input: grid = [[1,0,1],[0,0,0],[1,0,1]]
# Output: 2
# 
# Explanation: The cell (1, 1) is as far as possible from all the land with
# distance 2.
# 
# Example 2:
# 
# Input: grid = [[1,0,0],[0,0,0],[0,0,0]]
# Output: 4
# 
# Explanation: The cell (2, 2) is as far as possible from all the land with
# distance 4.
# 
# Constraints:
#         n == grid.length
#         n == grid[i].length
#         1 <= n <= 100
#         grid[i][j] is 0 or 1

from collections import deque

# Solution: https://youtu.be/fjxb1hQfrZk
# Credit: Navdeep Singh founder of NeetCode
def max_distance(grid):
    N = len(grid)
    q = deque()
    for r in range(N):
        for c in range(N):
            if grid[r][c]:
                q.append((r, c))

    res = -1
    direct = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    while q:
        r, c = q.popleft()

        res = grid[r][c]
        for dr, dc in direct:
            new_r, new_c = r + dr, c + dc
            if (min(new_r, new_c) >= 0 and
                    max(new_r, new_c) < N and
                    grid[new_r][new_c] == 0):
                q.append((new_r, new_c))
                grid[new_r][new_c] = grid[r][c] + 1

    return res - 1 if res > 1 else -1
    # Time: O(n ^ 2) 
    # Space: O(n ^ 2)


def main():
    result = max_distance(grid = [[1,0,1],[0,0,0],[1,0,1]])
    print(result) # 2

    result = max_distance(grid = [[1,0,0],[0,0,0],[0,0,0]])
    print(result) # 4

if __name__ == "__main__":
    main()
