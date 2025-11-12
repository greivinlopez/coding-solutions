# ----------------------------------------
# 1937. Maximum Number of Points with Cost
# ----------------------------------------

# Problem: https://leetcode.com/problems/maximum-number-of-points-with-cost
#
# You are given an m x n integer matrix points (0-indexed). Starting with 0
# points, you want to maximize the number of points you can get from the matrix.
# 
# To gain points, you must pick one cell in each row. Picking the cell at
# coordinates (r, c) will add points[r][c] to your score.
# 
# However, you will lose points if you pick a cell too far from the cell that you
# picked in the previous row. For every two adjacent rows r and r + 1 (where 0 <=
# r < m - 1), picking cells at coordinates (r, c1) and (r + 1, c2) will subtract
# abs(c1 - c2) from your score.
# 
# Return the maximum number of points you can achieve.
# 
# abs(x) is defined as:
#         x for x >= 0.
#         -x for x < 0.
# 
# Example 1:
# 
# https://assets.leetcode.com/uploads/2021/07/12/screenshot-2021-07-12-at-13-40-26-diagram-drawio-diagrams-net.png
# 
# Input: points = [[1,2,3],[1,5,1],[3,1,1]]
# Output: 9
# 
# Explanation:
# The blue cells denote the optimal cells to pick, which have coordinates (0, 2),
# (1, 1), and (2, 0).
# You add 3 + 5 + 3 = 11 to your score.
# However, you must subtract abs(2 - 1) + abs(1 - 0) = 2 from your score.
# Your final score is 11 - 2 = 9.
# 
# Example 2:
# 
# https://assets.leetcode.com/uploads/2021/07/12/screenshot-2021-07-12-at-13-42-14-diagram-drawio-diagrams-net.png
# 
# Input: points = [[1,5],[2,3],[4,2]]
# Output: 11
# 
# Explanation:
# The blue cells denote the optimal cells to pick, which have coordinates (0, 1),
# (1, 1), and (2, 0).
# You add 5 + 3 + 4 = 12 to your score.
# However, you must subtract abs(1 - 1) + abs(1 - 0) = 1 from your score.
# Your final score is 12 - 1 = 11.
# 
# 
# Constraints:
#         m == points.length
#         n == points[r].length
#         1 <= m, n <= 10^5
#         1 <= m * n <= 10^5
#         0 <= points[r][c] <= 10^5


# Solution: https://youtu.be/ik1y7fz8AOc
# Credit: Navdeep Singh founder of NeetCode
def max_points(points):
    ROWS, COLS = len(points), len(points[0])
    row = points[0]

    for r in range(1, ROWS):
        next_row = points[r].copy()
        left, right = [0] * COLS, [0] * COLS

        left[0] = row[0]
        for c in range(1, COLS):
            left[c] = max(row[c], left[c - 1] - 1)

        right[COLS - 1] = row[COLS - 1]
        for c in range(COLS - 2, -1, -1):
            right[c] = max(row[c], right[c + 1] - 1)

        for c in range(COLS):
            next_row[c] += max(left[c], right[c])

        row = next_row
    
    return max(row)
    # Time: O(rows * cols)
    # Space: O(cols)


def main():
    result = max_points(points = [[1,2,3],[1,5,1],[3,1,1]])
    print(result) # 9

    result = max_points(points = [[1,5],[2,3],[4,2]])
    print(result) # 11

if __name__ == "__main__":
    main()
