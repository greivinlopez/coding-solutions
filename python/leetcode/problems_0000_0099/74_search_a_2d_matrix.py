# -----------------------
# 74. Search a 2D Matrix
# -----------------------

# Problem: https://leetcode.com/problems/search-a-2d-matrix/
# 
# You are given an m x n integer matrix matrix with the following two properties:
# 
# - Each row is sorted in non-decreasing order.
# - The first integer of each row is greater than the last integer of the previous row.
# 
# Given an integer target, return true if target is in matrix or false otherwise.
# 
# You must write a solution in O(log(m * n)) time complexity.

# Solution: https://youtu.be/Ber2pi2C0j0
# Credit: Navdeep Singh founder of NeetCode 
def search_matrix(matrix, target):
    ROWS, COLS = len(matrix), len(matrix[0])

    top, bot = 0, ROWS - 1
    while top <= bot:
        row = (top + bot) // 2
        if target > matrix[row][-1]:
            top = row + 1
        elif target < matrix[row][0]:
            bot = row - 1
        else:
            break

    if not (top <= bot):
        return False
    row = (top + bot) // 2
    l, r = 0, COLS - 1
    while l <= r:
        m = (l + r) // 2
        if target > matrix[row][m]:
            l = m + 1
        elif target < matrix[row][m]:
            r = m - 1
        else:
            return True
    return False

# Solution: https://youtu.be/x-dYOtIudzc
# Credit: Greg Hogg
def search_matrix_alt(matrix, target):
    # Time: O(log(m * n))
    # Space: O(1)
    m = len(matrix)
    n = len(matrix[0])
    t = m * n
    l = 0
    r = t - 1

    while l <= r:
        mid = (l + r) // 2
        mid_i = mid // n
        mid_j = mid % n
        mid_num = matrix[mid_i][mid_j]

        if target == mid_num:
            return True
        elif target < mid_num:
            r = mid - 1
        else:
            l = mid + 1

    return False

def main():
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    result = search_matrix(matrix, 3) 
    # Expected Output: True
    print(result)
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    result = search_matrix(matrix, 13)
    # Expected Output: False
    print(result)

if __name__ == "__main__":
    main()