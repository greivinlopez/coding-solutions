# -----------------------------------
# 417. Pacific Atlantic Water Flow 🌊
# -----------------------------------

# Problem: https://leetcode.com/problems/pacific-atlantic-water-flow/
# 
# There is an m x n rectangular island that borders both the Pacific Ocean and 
# Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, 
# and the Atlantic Ocean touches the island's right and bottom edges.
# 
# The island is partitioned into a grid of square cells. You are given an m x n 
# integer matrix heights where heights[r][c] represents the height above sea 
# level of the cell at coordinate (r, c).
# 
# The island receives a lot of rain, and the rain water can flow to neighboring 
# cells directly north, south, east, and west if the neighboring cell's height 
# is less than or equal to the current cell's height. Water can flow from any 
# cell adjacent to an ocean into the ocean.
# 
# Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes 
# that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic 
# oceans.
# 
#  
# Example 1:
# 
# Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
# Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
# Explanation: The following cells can flow to the Pacific and Atlantic oceans, as shown below:
# [0,4]: [0,4] -> Pacific Ocean 
#        [0,4] -> Atlantic Ocean
# [1,3]: [1,3] -> [0,3] -> Pacific Ocean 
#        [1,3] -> [1,4] -> Atlantic Ocean
# [1,4]: [1,4] -> [1,3] -> [0,3] -> Pacific Ocean 
#        [1,4] -> Atlantic Ocean
# [2,2]: [2,2] -> [1,2] -> [0,2] -> Pacific Ocean 
#        [2,2] -> [2,3] -> [2,4] -> Atlantic Ocean
# [3,0]: [3,0] -> Pacific Ocean 
#        [3,0] -> [4,0] -> Atlantic Ocean
# [3,1]: [3,1] -> [3,0] -> Pacific Ocean 
#        [3,1] -> [4,1] -> Atlantic Ocean
# [4,0]: [4,0] -> Pacific Ocean 
#        [4,0] -> Atlantic Ocean
# Note that there are other possible paths for these cells to flow to the Pacific and Atlantic oceans.
# 
# 
# Example 2:
# 
# Input: heights = [[1]]
# Output: [[0,0]]
# Explanation: The water can flow from the only cell to the Pacific and Atlantic oceans.
# 
# 
# Constraints:
# 
# 	m == heights.length
# 	n == heights[r].length
# 	1 <= m, n <= 200
# 	0 <= heights[r][c] <= 10^5


# Solution: https://youtu.be/s-VkcjHqkGI
# Credit: Navdeep Singh founder of NeetCode
def pacific_atlantic(heights):
    ROWS, COLS = len(heights), len(heights[0])
    pac, atl = set(), set()

    def dfs(r, c, visit, prevHeight):
        if (
            (r, c) in visit
            or r < 0
            or c < 0
            or r == ROWS
            or c == COLS
            or heights[r][c] < prevHeight
        ):
            return
        visit.add((r, c))
        dfs(r + 1, c, visit, heights[r][c])
        dfs(r - 1, c, visit, heights[r][c])
        dfs(r, c + 1, visit, heights[r][c])
        dfs(r, c - 1, visit, heights[r][c])

    for c in range(COLS):
        dfs(0, c, pac, heights[0][c])
        dfs(ROWS - 1, c, atl, heights[ROWS - 1][c])

    for r in range(ROWS):
        dfs(r, 0, pac, heights[r][0])
        dfs(r, COLS - 1, atl, heights[r][COLS - 1])

    res = []
    for r in range(ROWS):
        for c in range(COLS):
            if (r, c) in pac and (r, c) in atl:
                res.append([r, c])
    return res

# Solution: https://youtu.be/pDvvDvgHUKE
# Credit: Greg Hogg
def pacific_atlantic_alt(heights):
    p_que = deque()
    p_seen = set()
    
    a_que = deque()
    a_seen = set()
    
    m, n = len(heights), len(heights[0])

    for j in range(n):
        p_que.append((0, j))
        p_seen.add((0, j))
        
    for i in range(1, m):
        p_que.append((i, 0))
        p_seen.add((i, 0))
        
    for i in range(m):
        a_que.append((i, n - 1))
        a_seen.add((i, n - 1))
        
    for j in range(n - 1):
        a_que.append((m - 1, j))
        a_seen.add((m - 1, j))

    def get_coords(que, seen):
        coords = set()
        while que:
            i, j = que.popleft()
            for i_off, j_off in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                r, c = i + i_off, j + j_off
                if 0 <= r < m and 0 <= c < n and heights[r][c] >= heights[i][j] and (r, c) not in seen:
                    seen.add((r, c))
                    que.append((r, c))
        
    get_coords(p_que, p_seen)
    get_coords(a_que, a_seen)
    return list(p_seen.intersection(a_seen))
    # Time: O(m*n)
    # Space: O(m*n)

def main():
    heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
    result = pacific_atlantic(heights)
    print(result) # [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]

    result = pacific_atlantic([[1]])
    print(result) # [[0,0]]

if __name__ == "__main__":
    main()
