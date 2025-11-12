# --------------------
# 48. Rotate Image 🔄
# --------------------

# Problem: https://leetcode.com/problems/rotate-image/
# You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
# 
# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. 
# DO NOT allocate another 2D matrix and do the rotation.

# Solution: https://youtu.be/fMSJSS7eO1w
# Credit: Navdeep Singh founder of NeetCode 
def rotate(matrix):
    # Time: O(n^2)
    # Space: O(1)
    """
    Do not return anything, modify matrix in-place instead.
    """
    l, r = 0, len(matrix) - 1
    while l < r:
        for i in range(r - l):
            top, bottom = l, r

            # save the topleft
            topLeft = matrix[top][l + i]

            # move bottom left into top left
            matrix[top][l + i] = matrix[bottom - i][l]

            # move bottom right into bottom left
            matrix[bottom - i][l] = matrix[bottom][r - i]

            # move top right into bottom right
            matrix[bottom][r - i] = matrix[top + i][r]

            # move top left into top right
            matrix[top + i][r] = topLeft
        r -= 1
        l += 1

# Solution: https://youtu.be/-jhbxNJijyE
# Credit: Greg Hogg
def rotate(matrix):
    # Time: O(n^2)
    # Space: O(1)
    n = len(matrix)
    
    # Tranpose
    for i in range(n):
        for j in range(i+1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    # Reflection
    for i in range(n):
        for j in range(n // 2):
            matrix[i][j], matrix[i][n-j-1] = matrix[i][n-j-1], matrix[i][j]

def main():
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    rotate(matrix) # [[7,4,1],[8,5,2],[9,6,3]]
    print(matrix)
    matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    rotate(matrix) # [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
    print(matrix)

if __name__ == "__main__":
    main()