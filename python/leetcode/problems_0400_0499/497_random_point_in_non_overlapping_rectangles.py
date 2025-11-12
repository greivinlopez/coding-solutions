# -----------------------------------------------
# 497. Random Point in Non-overlapping Rectangles
# -----------------------------------------------

# Problem: https://leetcode.com/problems/random-point-in-non-overlapping-rectangles
#
# You are given an array of non-overlapping axis-aligned rectangles rects where
# rects[i] = [aᵢ, bᵢ, xᵢ, yᵢ] indicates that (aᵢ, bᵢ) is the bottom-left corner
# point of the iᵗʰ rectangle and (xᵢ, yᵢ) is the top-right corner point of the ith
# rectangle. Design an algorithm to pick a random integer point inside the space
# covered by one of the given rectangles. A point on the perimeter of a rectangle
# is included in the space covered by the rectangle.
# 
# Any integer point inside the space covered by one of the given rectangles should
# be equally likely to be returned.
# 
# Note that an integer point is a point that has integer coordinates.
# 
# Implement the Solution class:
#         
#   * Solution(int[][] rects) Initializes the object with the given rectangles
#     rects.
#   * int[] pick() Returns a random integer point [u, v] inside the space
#     covered by one of the given rectangles.
# 
# Example 1:
# 
# https://assets.leetcode.com/uploads/2021/07/24/lc-pickrandomrec.jpg
# 
# Input
# ["Solution", "pick", "pick", "pick", "pick", "pick"]
# [[[[-2, -2, 1, 1], [2, 2, 4, 6]]], [], [], [], [], []]
# Output
# [null, [1, -2], [1, -1], [-1, -2], [-2, -2], [0, 0]]
# Explanation
# Solution solution = new Solution([[-2, -2, 1, 1], [2, 2, 4, 6]]);
# solution.pick(); // return [1, -2]
# solution.pick(); // return [1, -1]
# solution.pick(); // return [-1, -2]
# solution.pick(); // return [-2, -2]
# solution.pick(); // return [0, 0]
# 
# 
# Constraints:
#         1 <= rects.length <= 100
#         rects[i].length == 4
#         -10⁹ <= aᵢ < xᵢ <= 10⁹
#         -10⁹ <= bᵢ < yᵢ <= 10⁹
#         xᵢ - aᵢ <= 2000
#         yᵢ - bᵢ <= 2000
#         All the rectangles do not overlap.
#         At most 10⁴ calls will be made to pick.

import random
from bisect import bisect_left

# Solution: https://algo.monster/liteproblems/497
# Credit: AlgoMonster
class Solution:
    def __init__(self, rects):
        """
        Initialize with a list of non-overlapping rectangles.
        Each rectangle is represented as [x1, y1, x2, y2] where
        (x1, y1) is bottom-left corner and (x2, y2) is top-right corner.
        """
        self.rects = rects
        # Create prefix sum array to store cumulative count of points
        self.prefix_sums = [0] * len(rects)
      
        for i, (x1, y1, x2, y2) in enumerate(rects):
            # Calculate number of integer points in current rectangle
            points_count = (x2 - x1 + 1) * (y2 - y1 + 1)
          
            # Build prefix sum: add current rectangle's points to previous sum
            if i == 0:
                self.prefix_sums[i] = points_count
            else:
                self.prefix_sums[i] = self.prefix_sums[i - 1] + points_count

    def pick(self):
        """
        Pick a random integer point from one of the rectangles.
        Returns [x, y] coordinates of the selected point.
        """
        # Pick a random point index from 1 to total number of points
        random_point_index = random.randint(1, self.prefix_sums[-1])
      
        # Find which rectangle contains this point using binary search
        rectangle_index = bisect_left(self.prefix_sums, random_point_index)
      
        # Handle edge case where bisect_left returns exact match
        if rectangle_index < len(self.prefix_sums) and self.prefix_sums[rectangle_index] < random_point_index:
            rectangle_index += 1
          
        # Get the selected rectangle's coordinates
        x1, y1, x2, y2 = self.rects[rectangle_index]
      
        # Pick a random point within the selected rectangle
        random_x = random.randint(x1, x2)
        random_y = random.randint(y1, y2)
      
        return [random_x, random_y]


def main():
    print("TO DO")

if __name__ == "__main__":
    main()
