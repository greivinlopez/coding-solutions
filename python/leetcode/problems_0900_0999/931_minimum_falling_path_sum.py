# -----------------------------
# 931. Minimum Falling Path Sum
# -----------------------------

# Problem: https://leetcode.com/problems/minimum-falling-path-sum/
# 
# Given an n x n array of integers matrix, return the minimum sum of any 
# falling path through matrix.
# 
# A falling path starts at any element in the first row and chooses the 
# element in the next row that is either directly below or diagonally 
# left/right. Specifically, the next element from position (row, col) will 
# be (row + 1, col - 1), (row + 1, col), or (row + 1, col + 1).
# 
#  
# Example 1:
# 
# Input: matrix = [[2,1,3],[6,5,4],[7,8,9]]
# Output: 13
# Explanation: There are two falling paths with a minimum sum as shown.
# 
# Example 2:
# 
# Input: matrix = [[-19,57],[-40,-5]]
# Output: -59
# Explanation: The falling path with a minimum sum is shown.
#  
# 
# Constraints:
# 
#   n == matrix.length == matrix[i].length
#   1 <= n <= 100
#   -100 <= matrix[i][j] <= 100

# Solution: https://youtu.be/b_F3mz9l-uQ
# Credit: Navdeep Singh founder of NeetCode
def min_falling_path_sum(matrix):
    Memo = {}

    def Path(i, k, n):
        if (i, k) in Memo:
            return Memo[(i, k)]
        if i == n - 1:
            return matrix[i][k]
        if k > 0 and k < n - 1:
            Psx = matrix[i][k] + Path(i + 1, k - 1, n)
            Pst = matrix[i][k] + Path(i + 1, k, n)
            Pdx = matrix[i][k] + Path(i + 1, k + 1, n)
            Memo[(i, k)] = min(min(Pdx, Pst), Psx)
            return Memo[(i, k)]
        else:
            if k == 0:
                Pst = matrix[i][k] + Path(i + 1, k, n)
                Pdx = matrix[i][k] + Path(i + 1, k + 1, n)
                Memo[(i, k)] = min(Pst, Pdx)
                return Memo[(i, k)]
            else:
                Psx = matrix[i][k] + Path(i + 1, k - 1, n)
                Pst = matrix[i][k] + Path(i + 1, k, n)
                Memo[(i, k)] = min(Pst, Psx)
                return Memo[(i, k)]

    Min = 10**7
    for k in range(0, len(matrix[0])):
        CP = Path(0, k, len(matrix[0]))
        if CP < Min:
            Min = CP
    return Min


def main():
    result = min_falling_path_sum(matrix = [[2,1,3],[6,5,4],[7,8,9]])
    print(result) # 13

    result = min_falling_path_sum(matrix = [[-19,57],[-40,-5]])
    print(result) # -59

if __name__ == "__main__":
    main()
