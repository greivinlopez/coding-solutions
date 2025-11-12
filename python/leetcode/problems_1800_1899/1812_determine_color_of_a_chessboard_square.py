# -----------------------------------------------
# 1812. Determine Color of a Chessboard Square ♟️
# -----------------------------------------------

# Problem: https://leetcode.com/problems/determine-color-of-a-chessboard-square
#
# You are given coordinates, a string that represents the coordinates of a square
# of the chessboard. Below is a chessboard for your reference.
# 
# https://assets.leetcode.com/uploads/2021/02/19/screenshot-2021-02-20-at-22159-pm.png
# 
# Return true if the square is white, and false if the square is black.
# 
# The coordinate will always represent a valid chessboard square. The coordinate
# will always have the letter first, and the number second.
# 
# Example 1:
# 
# Input: coordinates = "a1"
# Output: false
# 
# Explanation: From the chessboard above, the square with coordinates "a1" is
# black, so return false.
# 
# Example 2:
# 
# Input: coordinates = "h3"
# Output: true
# 
# Explanation: From the chessboard above, the square with coordinates "h3" is
# white, so return true.
# 
# Example 3:
# 
# Input: coordinates = "c7"
# Output: false
# 
# 
# Constraints:
#         coordinates.length == 2
#         'a' <= coordinates[0] <= 'h'
#         '1' <= coordinates[1] <= '8'

# Credit: Jaweria Batool -> https://github.com/Jaweria-B
def square_is_white_l(coordinates):
    row = {
        'a': 0,
        'b': 1,
        'c': 2,
        'd': 3,
        'e': 4,
        'f': 5,
        'g': 6,
        'h': 7
    }
    
    x = row[coordinates[0]]
    y = int(coordinates[1])
    
    if y % 2 == 0:
        if x % 2 == 0:
            return True
        else:
            return False
    else:
        if x % 2 == 0:
            return False
        else:
            return True
    # Time: O(1)
    # Space: O(1)

# My Solution
def square_is_white(coordinates):
    l = coordinates[0]
    n = int(coordinates[1])
    return (((n - 1) * 8 + ord(l) - 96) % 2) == 0
    # Time: O(1)
    # Space: O(1)


def main():
    result = square_is_white("a1")
    print(result) # False

    result = square_is_white("h3")
    print(result) # True

    result = square_is_white("c7")
    print(result) # False

if __name__ == "__main__":
    main()
