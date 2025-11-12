# ------------------------
# 1572. Matrix Diagonal Sum
# ------------------------

# Problem: https://leetcode.com/problems/matrix-diagonal-sum
#
# Given a square matrix mat, return the sum of the matrix diagonals.
# Only include the sum of all the elements on the primary diagonal and all the
# elements on the secondary diagonal that are not part of the primary diagonal.
# Example 1:
# Input: mat = [[1,2,3],
#               [4,5,6],
#               [7,8,9]]
# Output: 25
# Explanation: Diagonals sum: 1 + 5 + 9 + 3 + 7 = 25
# Notice that element mat[1][1] = 5 is counted only once.
# Example 2:
# Input: mat = [[1,1,1,1],
#               [1,1,1,1],
#               [1,1,1,1],
#               [1,1,1,1]]
# Output: 8
# Example 3:
# Input: mat = [[5]]
# Output: 5
# Constraints:
#         n == mat.length == mat[i].length
#         1 <= n <= 100
#         1 <= mat[i][j] <= 100


# Solution: https://youtu.be/WliTu6gIK7o
# Credit: Navdeep Singh founder of NeetCode
def prime_sum(mat):
    cnt = 0
    for i in range(len(mat)):
        cnt += mat[i][i]
    return cnt

def cross_sum(mat):
    cnt = 0
    for i in range(len(mat)):
        cnt += mat[i][len(mat) - i - 1]
    return cnt

def diagonal_sum(mat):
    prime = prime_sum(mat)
    cross = cross_sum(mat)

    if len(mat) % 2 == 0:
        return prime + cross
    else:
        mid = len(mat) // 2
        mid_ele = mat[mid][mid]
        return prime + cross - mid_ele


def main():
    mat = [[1,2,3],
           [4,5,6],
           [7,8,9]]
    result = diagonal_sum(mat)
    print(result) # 25

    mat = [[1,1,1,1],
           [1,1,1,1],
           [1,1,1,1],
           [1,1,1,1]]
    result = diagonal_sum(mat)
    print(result) # 8

    result = diagonal_sum(mat = [[5]])
    print(result) # 5

if __name__ == "__main__":
    main()
