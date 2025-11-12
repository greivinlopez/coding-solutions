# -----------------------------
# 840. Magic Squares In Grid 🪄
# -----------------------------

# Problem: https://leetcode.com/problems/magic-squares-in-grid
#
# A 3 x 3 magic square is a 3 x 3 grid filled with distinct numbers from 1 to 9
# such that each row, column, and both diagonals all have the same sum.
# 
# Given a row x col grid of integers, how many 3 x 3 magic square subgrids are
# there?
# 
# Note: while a magic square can only contain numbers from 1 to 9, grid may
# contain numbers up to 15.
# 
# Example 1:
# 
# https://assets.leetcode.com/uploads/2020/09/11/magic_main.jpg
# 
# Input: grid = [[4,3,8,4],[9,5,1,9],[2,7,6,2]]
# Output: 1
# 
# Explanation:
# 
# The following subgrid is a 3 x 3 magic square:
# 
# https://assets.leetcode.com/uploads/2020/09/11/magic_valid.jpg
# 
# while this one is not:
# 
# https://assets.leetcode.com/uploads/2020/09/11/magic_invalid.jpg
# 
# In total, there is only one magic square inside the given grid.
# 
# Example 2:
# 
# Input: grid = [[8]]
# Output: 0
# 
# 
# Constraints:
#         row == grid.length
#         col == grid[i].length
#         1 <= row, col <= 10
#         0 <= grid[i][j] <= 15


# Solution: https://youtu.be/FV52wWrivNc
# Credit: Navdeep Singh founder of NeetCode
def num_magic_squares_inside_rec(grid):
    # Recursive solution
    ROWS, COLS = len(grid), len(grid[0])

    def magic(r, c):
        # Ensure 1 - 9
        values = set()
        for i in range(r, r + 3):
            for j in range(c, c + 3):
                if grid[i][j] in values or not (1 <= grid[i][j] <= 9):
                    return 0
                values.add(grid[i][j])

        # Rows
        for i in range(r, r + 3):
            if sum(grid[i][c:c + 3]) != 15:
                return 0

        # Cols
        for i in range(c, c + 3):
            if (grid[r][i] + grid[r + 1][i] + grid[r + 2][i]) != 15:
                return 0

        # Diagonals
        if (
            grid[r][c] + grid[r + 1][c + 1] + grid[r + 2][c + 2] != 15 or
            grid[r][c + 2] + grid[r + 1][c + 1] + grid[r + 2][c] != 15
        ):
            return 0

        return 1

    res = 0
    for r in range(ROWS - 2):
        for c in range(COLS - 2):
            if magic(r, c):
                res += 1

    return res
    # Time: O(r * c)
    # Space: O(1)

def num_magic_squares_inside(grid):
    # Iterative Solution
    ROWS, COLS = len(grid), len(grid[0])
    res = 0
    pattern1 = "438167294381672"
    pattern2 = "927618349276183"

    def magic(r, c):
        if grid[r][c] != 5:
            return 0

        neighbors = [
            [r - 1, c], [r - 1, c + 1],
            [r, c + 1], [r + 1, c + 1],
            [r + 1, c], [r + 1, c - 1],
            [r, c - 1], [r - 1, c - 1]
        ]
        
        seq = ""
        for nr, nc in neighbors:
            seq += str(grid[nr][nc])
        
        if seq in pattern1 or seq in pattern2:
            return 1
        
        return 0

    for r in range(1, ROWS - 1):
        for c in range(1, COLS - 1):
            res += magic(r, c)
    
    return res
    # Time: O(r * c)
    # Space: O(1)


def main():
    result = num_magic_squares_inside(grid = [[4,3,8,4],[9,5,1,9],[2,7,6,2]])
    print(result) # 1

    result = num_magic_squares_inside(grid = [[8]])
    print(result) # 0

if __name__ == "__main__":
    main()
