# ------------------------
# 1975. Maximum Matrix Sum
# ------------------------

# Problem: https://leetcode.com/problems/maximum-matrix-sum
#
# You are given an n x n integer matrix. You can do the following operation any
# number of times:
# 
#   * Choose any two adjacent elements of matrix and multiply each of them by -1.
# 
# Two elements are considered adjacent if and only if they share a border.
# 
# Your goal is to maximize the summation of the matrix's elements. Return the
# maximum sum of the matrix's elements using the operation mentioned above.
# 
# Example 1:
# 
# Input: matrix = [[1,-1],[-1,1]]
# Output: 4
# 
# Explanation: We can follow the following steps to reach sum equals 4:
# - Multiply the 2 elements in the first row by -1.
# - Multiply the 2 elements in the first column by -1.
# 
# Example 2:
# 
# Input: matrix = [[1,2,3],[-1,-2,-3],[1,2,3]]
# Output: 16
# 
# Explanation: We can follow the following step to reach sum equals 16:
# - Multiply the 2 last elements in the second row by -1.
# 
# 
# Constraints:
#         n == matrix.length == matrix[i].length
#         2 <= n <= 250
#         -10^5 <= matrix[i][j] <= 10^5


# Solution: https://youtu.be/XonYlqE049I
# Credit: Navdeep Singh founder of NeetCode
def max_matrix_sum(matrix):
    res = 0
    neg_cnt = 0
    mat_min = float("inf")
    for row in matrix:
        for n in row:
            res += abs(n)
            mat_min = min(mat_min, abs(n))
            if n < 0:
                neg_cnt += 1

    if neg_cnt & 1:
        res -= 2 * mat_min

    return res
    # Time: O(m * n) 
    # Space: O(1)


def main():
    result = max_matrix_sum([[1,-1],[-1,1]])
    print(result) # 4

    result = max_matrix_sum([[1,2,3],[-1,-2,-3],[1,2,3]])
    print(result) # 16

if __name__ == "__main__":
    main()
