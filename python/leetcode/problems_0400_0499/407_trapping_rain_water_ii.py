# ------------------------------
# 407. Trapping Rain Water II 🌧️
# ------------------------------

# Problem: https://leetcode.com/problems/trapping-rain-water-ii
#
# Given an m x n integer matrix heightMap representing the height of each unit
# cell in a 2D elevation map, return the volume of water it can trap after
# raining.
# 
# Example 1:
# 
# Input: heightMap = [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]
# Output: 4
# 
# Explanation: After the rain, water is trapped between the blocks.
# We have two small ponds 1 and 3 units trapped.
# The total volume of water trapped is 4.
# 
# Example 2:
# 
# Input: heightMap = [[3,3,3,3,3],[3,2,2,2,3],[3,2,1,2,3],[3,2,2,2,3],[3,3,3,3,3]]
# Output: 10
# 
# 
# Constraints:
#         m == heightMap.length
#         n == heightMap[i].length
#         1 <= m, n <= 200
#         0 <= heightMap[i][j] <= 2 * 10^4

from heapq import heappop, heappush

# Solution: https://youtu.be/onA7_MaPGkM
# Credit: Navdeep Singh founder of NeetCode
def trap_rain_water(heightMap):
    ROWS, COLS = len(heightMap), len(heightMap[0])
    
    # 1. Add border to min heap, mark as visited.
    min_heap = []
    for r in range(ROWS):
        for c in range(COLS):
            if r in [0, ROWS - 1] or c in [0, COLS - 1]:
                heappush(min_heap, (heightMap[r][c], r, c))
                heightMap[r][c] = -1

    # 2. Prioritize smallest heights.
    # Maintain max height to calculate
    # water stored in each inner position.
    res = 0
    max_h = -1
    # O(n * m *)
    while min_heap:
        h, r, c = heappop(min_heap)
        max_h = max(max_h, h)
        res += max_h - h

        neighbors = [[r + 1, c], [r - 1, c], [r, c + 1], [r, c - 1]]
        for nr, nc in neighbors:
            if (
                nr < 0 or nc < 0 or
                nr == ROWS or nc == COLS or
                heightMap[nr][nc] == -1
            ):
                continue
            heappush(min_heap, (heightMap[nr][nc], nr, nc))
            heightMap[nr][nc] = -1 # visited

    return res
    # Time: O(m * n * log(m * n)) m = ROWS (len of heightMap), n = COLS (len of heightMap[0])
    # Space: O(n)


def main():
    heightMap = [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]
    result = trap_rain_water(heightMap)
    print(result) # 4

    heightMap = [[3,3,3,3,3],[3,2,2,2,3],[3,2,1,2,3],[3,2,2,2,3],[3,3,3,3,3]]
    result = trap_rain_water(heightMap)
    print(result) # 10

if __name__ == "__main__":
    main()
