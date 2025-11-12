# -------------------------
# 1861. Rotating the Box 📦
# -------------------------

# Problem: https://leetcode.com/problems/rotating-the-box
#
# You are given an m x n matrix of characters boxGrid representing a side-view of
# a box. Each cell of the box is one of the following:
#         A stone '#'
#         A stationary obstacle '*'
#         Empty '.'
# 
# The box is rotated 90 degrees clockwise, causing some of the stones to fall due
# to gravity. Each stone falls down until it lands on an obstacle, another stone,
# or the bottom of the box. Gravity does not affect the obstacles' positions, and
# the inertia from the box's rotation does not affect the stones' horizontal
# positions.
# 
# It is guaranteed that each stone in boxGrid rests on an obstacle, another stone,
# or the bottom of the box.
# 
# Return an n x m matrix representing the box after the rotation described above.
# 
# Example 1:
# 
# https://assets.leetcode.com/uploads/2021/04/08/rotatingtheboxleetcodewithstones.png
# 
# Input: boxGrid = [["#",".","#"]]
# Output: [["."],
#          ["#"],
#          ["#"]]
# 
# Example 2:
# 
# https://assets.leetcode.com/uploads/2021/04/08/rotatingtheboxleetcode2withstones.png
# 
# Input: boxGrid = [["#",".","*","."],
#               ["#","#","*","."]]
# Output: [["#","."],
#          ["#","#"],
#          ["*","*"],
#          [".","."]]
# 
# Example 3:
# 
# https://assets.leetcode.com/uploads/2021/04/08/rotatingtheboxleetcode3withstone.png
# 
# Input: boxGrid = [["#","#","*",".","*","."],
#               ["#","#","#","*",".","."],
#               ["#","#","#",".","#","."]]
# Output: [[".","#","#"],
#          [".","#","#"],
#          ["#","#","*"],
#          ["#","*","."],
#          ["#",".","*"],
#          ["#",".","."]]
# 
# 
# Constraints:
#         m == boxGrid.length
#         n == boxGrid[i].length
#         1 <= m, n <= 500
#         boxGrid[i][j] is either '#', '*', or '.'.


# Solution: https://youtu.be/LZr1w0LVzFw
# Credit: Navdeep Singh founder of NeetCode
def rotate_the_box(box):
    ROWS, COLS = len(box), len(box[0])
    for r in range(ROWS):
        i = COLS - 1
        for c in reversed(range(COLS)):
            if box[r][c] == "#":
                box[r][c], box[r][i] = box[r][i], box[r][c]
                i -= 1
            elif box[r][c] == "*":
                i = c - 1
    res = []
    for c in range(COLS):
        col = []
        for r in reversed(range(ROWS)):
            col.append(box[r][c])
        res.append(col)
    return res
    # Time: O(r * c)
    # Space: O(r * c)


def main():
    result = rotate_the_box([["#",".","#"]])
    print(result) # [['.'], ['#'], ['#']]

    result = rotate_the_box([["#",".","*","."], ["#","#","*","."]])
    print(result) # [['#', '.'], ['#', '#'], ['*', '*'], ['.', '.']]

    result = rotate_the_box([["#","#","*",".","*","."],
              ["#","#","#","*",".","."],
              ["#","#","#",".","#","."]])
    print(result) # [['.', '#', '#'], ['.', '#', '#'], ['#', '#', '*'], ['#', '*', '.'], ['#', '.', '*'], ['#', '.', '.']]

if __name__ == "__main__":
    main()
