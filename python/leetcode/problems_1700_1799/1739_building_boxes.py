# --------------------
# 1739. Building Boxes
# --------------------

# Problem: https://leetcode.com/problems/building-boxes
#
# You have a cubic storeroom where the width, length, and height of the room are
# all equal to n units. You are asked to place n boxes in this room where each box
# is a cube of unit side length. There are however some rules to placing the
# boxes:
#         
#   * You can place the boxes anywhere on the floor.
#   * If box x is placed on top of the box y, then each side of the four
#     vertical sides of the box y must either be adjacent to another box or to a wall.
# 
# Given an integer n, return the minimum possible number of boxes touching the
# floor.
# 
# Example 1:
# 
# https://assets.leetcode.com/uploads/2021/01/04/3-boxes.png
# 
# Input: n = 3
# Output: 3
# 
# Explanation: The figure above is for the placement of the three boxes.
# These boxes are placed in the corner of the room, where the corner is on the
# left side.
# 
# Example 2:
# 
# https://assets.leetcode.com/uploads/2021/01/04/4-boxes.png
# 
# Input: n = 4
# Output: 3
# 
# Explanation: The figure above is for the placement of the four boxes.
# These boxes are placed in the corner of the room, where the corner is on the
# left side.
# 
# Example 3:
# 
# https://assets.leetcode.com/uploads/2021/01/04/10-boxes.png
# 
# Input: n = 10
# Output: 6
# 
# Explanation: The figure above is for the placement of the ten boxes.
# These boxes are placed in the corner of the room, where the corner is on the
# back side.
# 
# 
# Constraints:
#         1 <= n <= 10⁹


# Solution: https://algo.monster/liteproblems/1739
# Credit: AlgoMonster
def minimum_boxes(n):
    # Find the maximum complete pyramid that can be built with n boxes
    # A complete pyramid of height h has h layers, where layer i has i*(i+1)/2 boxes on the ground

    # Step 1: Find the maximum height of complete pyramid we can build
    total_boxes = 0  # Total boxes used so far
    height = 1  # Current height being considered

    # Keep adding complete layers while we have enough boxes
    while total_boxes + height * (height + 1) // 2 <= n:
        total_boxes += height * (height + 1) // 2  # Add boxes from this layer
        height += 1

    # Backtrack since we went one layer too far
    height -= 1

    # Calculate the number of ground boxes for the complete pyramid
    ground_boxes = height * (height + 1) // 2

    # Step 2: Add remaining boxes one column at a time
    # Each additional ground box can support a column of increasing height
    column_height = 1  # Height of the next column we can add

    while total_boxes < n:
        ground_boxes += 1  # Add one more box to the ground
        total_boxes += column_height  # Add a column of this height
        column_height += 1  # Next column can be one box taller

    return ground_boxes
    # Time: O(√n)
    # Space: O(1)


def main():
    result = minimum_boxes(n = 3)
    print(result) # 3

    result = minimum_boxes(n = 4)
    print(result) # 3

    result = minimum_boxes(n = 10)
    print(result) # 6

if __name__ == "__main__":
    main()
