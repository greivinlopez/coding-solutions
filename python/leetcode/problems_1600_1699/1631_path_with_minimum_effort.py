# ------------------------------
# 1631. Path With Minimum Effort
# ------------------------------

# Problem: https://leetcode.com/problems/path-with-minimum-effort
#
# You are a hiker preparing for an upcoming hike. You are given heights, a 2D
# array of size rows x columns, where heights[row][col] represents the height of
# cell (row, col). You are situated in the top-left cell, (0, 0), and you hope to
# travel to the bottom-right cell, (rows-1, columns-1) (i.e., 0-indexed). You can
# move up, down, left, or right, and you wish to find a route that requires the
# minimum effort.
# 
# A route's effort is the maximum absolute difference in heights between two
# consecutive cells of the route.
# 
# Return the minimum effort required to travel from the top-left cell to the
# bottom-right cell.
# 
# Example 1:
# 
# Input: heights = [[1,2,2],[3,8,2],[5,3,5]]
# Output: 2
# Explanation: The route of [1,3,5,3,5] has a maximum absolute difference of 2 in
# consecutive cells.
# This is better than the route of [1,2,2,2,5], where the maximum absolute
# difference is 3.
# 
# Example 2:
# 
# Input: heights = [[1,2,3],[3,8,4],[5,3,5]]
# Output: 1
# Explanation: The route of [1,2,3,4,5] has a maximum absolute difference of 1 in
# consecutive cells, which is better than route [1,3,5,3,5].
# 
# Example 3:
# 
# Input: heights = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]
# Output: 0
# Explanation: This route does not require any effort.
# 
# 
# Constraints:
#         rows == heights.length
#         columns == heights[i].length
#         1 <= rows, columns <= 100
#         1 <= heights[i][j] <= 10^6

import heapq

# Solution: https://youtu.be/XQlxCCx2vI4
# Credit: Navdeep Singh founder of NeetCode
def minimum_effort_path(heights):
    m, n = len(heights), len(heights[0])
    
    efforts = [[float('inf')] * n for _ in range(m)]
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    efforts[0][0] = 0
    pq = [(0, 0, 0)]  # (effort, row, col)
    
    while pq:
        curEffort, i, j = heapq.heappop(pq)
        
        # reached the bottom-right corner => return the effort
        if i == m - 1 and j == n - 1:
            return curEffort
        
        for dx, dy in directions:
            x, y = i + dx, j + dy
            
            if 0 <= x < m and 0 <= y < n:
                newEffort = max(abs(heights[x][y] - heights[i][j]), curEffort)
                
                if newEffort < efforts[x][y]:
                    efforts[x][y] = newEffort
                    heapq.heappush(pq, (newEffort, x, y))
    
    return efforts[m - 1][n - 1]


def main():
    result = minimum_effort_path([[1,2,2],[3,8,2],[5,3,5]])
    print(result) # 2

    result = minimum_effort_path([[1,2,3],[3,8,4],[5,3,5]])
    print(result) # 1

    result = minimum_effort_path([[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]])
    print(result) # 0

if __name__ == "__main__":
    main()
