# ---------------------------------------------------
# 1072. Flip Columns For Maximum Number of Equal Rows
# ---------------------------------------------------

# Problem: https://leetcode.com/problems/flip-columns-for-maximum-number-of-equal-rows
#
# You are given an m x n binary matrix matrix.
# 
# You can choose any number of columns in the matrix and flip every cell in that
# column (i.e., Change the value of the cell from 0 to 1 or vice versa).
# 
# Return the maximum number of rows that have all values equal after some number
# of flips.
# 
# Example 1:
# 
# Input: matrix = [[0,1],[1,1]]
# Output: 1
# 
# Explanation: After flipping no values, 1 row has all values equal.
# 
# Example 2:
# 
# Input: matrix = [[0,1],[1,0]]
# Output: 2
# 
# Explanation: After flipping values in the first column, both rows have equal
# values.
# 
# Example 3:
# 
# Input: matrix = [[0,0,0],[0,0,1],[1,1,0]]
# Output: 2
# 
# Explanation: After flipping values in the first two columns, the last two rows
# have equal values.
# 
# 
# Constraints:
#         m == matrix.length
#         n == matrix[i].length
#         1 <= m, n <= 300
#         matrix[i][j] is either 0 or 1.

from collections import defaultdict

# Solution: https://youtu.be/MsdLjL87BEo
# Credit: Navdeep Singh founder of NeetCode
def max_equal_rows_after_flips(matrix):
    count = defaultdict(int)

    for row in matrix:
        row_key = str(row)
        if row[0]:
            row_key = str([0 if n else 1 for n in row])

        count[row_key] += 1

    return max(count.values())
    # Time: O(rows * cols)
    # Space: O(rows * cols)


def main():
    result = max_equal_rows_after_flips(matrix = [[0,1],[1,1]])
    print(result) # 1

    result = max_equal_rows_after_flips(matrix = [[0,1],[1,0]])
    print(result) # 2

    result = max_equal_rows_after_flips(matrix = [[0,0,0],[0,0,1],[1,1,0]])
    print(result) # 2

if __name__ == "__main__":
    main()
