# --------------------
# 59. Spiral Matrix II
# --------------------

# Problem: https://leetcode.com/problems/spiral-matrix-ii
#
# Given a positive integer n, generate an n x n matrix filled with elements from 1
# to n^2 in spiral order.
# 
# Example 1:
# 
# https://assets.leetcode.com/uploads/2020/11/13/spiraln.jpg
# 
# Input: n = 3
# Output: [[1,2,3],[8,9,4],[7,6,5]]
# 
# Example 2:
# 
# Input: n = 1
# Output: [[1]]
# 
# 
# Constraints:
#         1 <= n <= 20


# Solution: https://youtu.be/RvLrWFBJ9fM
# Credit: Navdeep Singh founder of NeetCode
def generate_matrix(n):
    mat = [[0] * n for _ in range(n)]

    left, right = 0, n - 1
    top, bottom = 0, n - 1
    val = 1

    while left <= right:
        # fill every val in top row
        for c in range(left, right + 1):
            mat[top][c] = val
            val += 1
        top += 1

        # fill every val in right col
        for r in range(top, bottom + 1):
            mat[r][right] = val
            val += 1
        right -= 1

        # fill every val in bottom row (reverse order)
        for c in range(right, left - 1, -1):
            mat[bottom][c] = val
            val += 1
        bottom -= 1

        # fill every val in the left col (reverse order)
        for r in range(bottom, top - 1, -1):
            mat[r][left] = val
            val += 1
        left += 1

    return mat
    # Time: O(n²) 
    # Space: O(n²)


def main():
    result = generate_matrix(3)
    print(result) # [[1, 2, 3], [8, 9, 4], [7, 6, 5]]

    result = generate_matrix(1)
    print(result) # [[1]]

if __name__ == "__main__":
    main()
