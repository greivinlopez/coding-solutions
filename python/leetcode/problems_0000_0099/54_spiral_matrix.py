# ---------------------
# 54. Spiral Matrix 🔄
# ---------------------

# Problem: https://leetcode.com/problems/spiral-matrix/
# Given an m x n matrix, return all elements of the matrix in spiral order.

# Solution: https://youtu.be/BJnMZNwUk1M
# Credit: Navdeep Singh founder of NeetCode 
def spiral_order(matrix):
    res = []
    left, right = 0, len(matrix[0])
    top, bottom = 0, len(matrix)

    while left < right and top < bottom:
        # get every i in the top row
        for i in range(left, right):
            res.append(matrix[top][i])
        top += 1
        # get every i in the right col
        for i in range(top, bottom):
            res.append(matrix[i][right - 1])
        right -= 1
        if not (left < right and top < bottom):
            break
        # get every i in the bottom row
        for i in range(right - 1, left - 1, -1):
            res.append(matrix[bottom - 1][i])
        bottom -= 1
        # get every i in the left col
        for i in range(bottom - 1, top - 1, -1):
            res.append(matrix[i][left])
        left += 1

    return res

# Solution: https://youtu.be/fcn8qkRcFVM
# Credit: Greg Hogg
def spiral_order_alt(matrix):
    # Time: O(m*n)
    # Space: O(1)
    m, n = len(matrix), len(matrix[0])
    ans = []
    i, j = 0, 0
    UP, RIGHT, DOWN, LEFT = 0, 1, 2, 3
    direction = RIGHT

    UP_WALL = 0
    RIGHT_WALL = n
    DOWN_WALL = m
    LEFT_WALL = -1

    while len(ans) != m*n:
        if direction == RIGHT:
            while j < RIGHT_WALL:
                ans.append(matrix[i][j])
                j += 1
            i, j = i+1, j-1
            RIGHT_WALL -= 1
            direction = DOWN
        elif direction == DOWN:
            while i < DOWN_WALL:
                ans.append(matrix[i][j])
                i += 1
            i, j = i-1, j-1
            DOWN_WALL -= 1
            direction = LEFT
        elif direction == LEFT:
            while j > LEFT_WALL:
                ans.append(matrix[i][j])
                j -= 1
            i, j = i-1, j+1
            LEFT_WALL += 1
            direction = UP
        else:
            while i > UP_WALL:
                ans.append(matrix[i][j])
                i -= 1
            i, j = i+1, j+1
            UP_WALL += 1
            direction = RIGHT
    
    return ans

def main():
    result = spiral_order([[1,2,3],[4,5,6],[7,8,9]])
    # Expected Output: [1,2,3,6,9,8,7,4,5]
    print(result)
    result = spiral_order([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
    # Expected Output: [1,2,3,4,8,12,11,10,9,5,6,7]
    print(result)

if __name__ == "__main__":
    main()