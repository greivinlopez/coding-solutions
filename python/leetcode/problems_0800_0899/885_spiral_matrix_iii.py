# ----------------------
# 885. Spiral Matrix III
# ----------------------

# Problem: https://leetcode.com/problems/spiral-matrix-iii
#
# You start at the cell (rStart, cStart) of an rows x cols grid facing east. The
# northwest corner is at the first row and column in the grid, and the southeast
# corner is at the last row and column.
# 
# You will walk in a clockwise spiral shape to visit every position in this grid.
# Whenever you move outside the grid's boundary, we continue our walk outside the
# grid (but may return to the grid boundary later.). 
# Eventually, we reach all rows * cols spaces of the grid.
# 
# Return an array of coordinates representing the positions of the grid in the
# order you visited them.
# 
# Example 1:
# 
# Input: rows = 1, cols = 4, rStart = 0, cStart = 0
# Output: [[0,0],[0,1],[0,2],[0,3]]
# 
# Example 2:
# 
# Input: rows = 5, cols = 6, rStart = 1, cStart = 4
# Output: [[1,4],[1,5],[2,5],[2,4],[2,3],[1,3],[0,3],[0,4],[0,5],[3,5],[3,4],[3,3]
# ,[3,2],[2,2],[1,2],[0,2],[4,5],[4,4],[4,3],[4,2],[4,1],[3,1],[2,1],[1,1],[0,1],[
# 4,0],[3,0],[2,0],[1,0],[0,0]]
# 
# 
# Constraints:
#         1 <= rows, cols <= 100
#         0 <= rStart < rows
#         0 <= cStart < cols


# Solution: https://youtu.be/Xf5Zm5Y8PKM
# Credit: Navdeep Singh founder of NeetCode
def spiral_matrix_iii(rows, cols, rStart, cStart):
    directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]  # r, c
    
    res = []
    r, c = rStart, cStart
    steps = 1
    i = 0
    while len(res) < rows * cols:
        for x in range(2):
            dr, dc = directions[i]
            for y in range(steps):
                if (0 <= r < rows and 0 <= c < cols):
                    res.append([r, c])
                r, c = r + dr, c + dc
            i = (i + 1) % 4
        steps += 1
    
    return res
    # Time: O(max(rows * cols, n²))  where n = max(rows, cols) 
    # Space: O(rows * cols)


def main():
    result = spiral_matrix_iii(rows = 1, cols = 4, rStart = 0, cStart = 0)
    print(result) # [[0, 0], [0, 1], [0, 2], [0, 3]]

    result = spiral_matrix_iii(rows = 5, cols = 6, rStart = 1, cStart = 4)
    print(result) # [[1,4],[1,5],[2,5],[2,4],
                  #  [2,3],[1,3],[0,3],[0,4],
                  #  [0,5],[3,5],[3,4],[3,3],
                  #  [3,2],[2,2],[1,2],[0,2],
                  #  [4,5],[4,4],[4,3],[4,2],
                  #  [4,1],[3,1],[2,1],[1,1],
                  #  [0,1],[4,0],[3,0],[2,0],
                  #  [1,0],[0,0]]

if __name__ == "__main__":
    main()
