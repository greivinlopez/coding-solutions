# --------------------------
# 240. Search a 2D Matrix II
# --------------------------

# Problem: https://leetcode.com/problems/search-a-2d-matrix-ii
#
# Write an efficient algorithm that searches for a value target in an m x n
# integer matrix matrix. This matrix has the following properties:
#   * Integers in each row are sorted in ascending from left to right.
#   * Integers in each column are sorted in ascending from top to bottom.
# 
# Example 1:
# 
# https://assets.leetcode.com/uploads/2020/11/24/searchgrid2.jpg
# 
# Input: matrix =
# [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]],
# target = 5
# Output: true
# 
# Example 2:
# 
# https://assets.leetcode.com/uploads/2020/11/24/searchgrid.jpg
# 
# Input: matrix =
# [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]],
# target = 20
# Output: false
# 
# Constraints:
#         m == matrix.length
#         n == matrix[i].length
#         1 <= n, m <= 300
#         -10⁹ <= matrix[i][j] <= 10⁹
#         All the integers in each row are sorted in ascending order.
#         All the integers in each column are sorted in ascending order.
#         -10⁹ <= target <= 10⁹


# Solution: https://leetcode.com/problems/search-a-2d-matrix-ii/solutions/2324351/python-explained
def search_matrix(matrix, target):
    m=len(matrix)
    n=len(matrix[0])
    
    i=m-1
    j=0
    
    while i>=0 and j<n:
        if matrix[i][j]==target:
            return True
        elif matrix[i][j]<target:
            j+=1
        else:
            i-=1
            
    return False
    # O(m + n)
    # O(1)
    # m = the number of rows in the matrix
    # n = the number of columns in the matrix


def main():
    matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
    result = search_matrix(matrix, 5)
    print(result) # True

    matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
    result = search_matrix(matrix, 20)
    print(result) # False

if __name__ == "__main__":
    main()
