# --------------------------------------
# 478. Generate Random Point in a Circle
# --------------------------------------

# Problem: https://leetcode.com/problems/generate-random-point-in-a-circle
#
# Given the radius and the position of the center of a circle, implement the
# function randPoint which generates a uniform random point inside the circle.
# 
# Implement the Solution class:
#         
#   * Solution(double radius, double x_center, double y_center) initializes
#     the object with the radius of the circle radius and the position of the center
#     (x_center, y_center).
#   * randPoint() returns a random point inside the circle. A point on the
#     circumference of the circle is considered to be in the circle. The answer is
#     returned as an array [x, y].
# 
# Example 1:
# 
# Input
# ["Solution", "randPoint", "randPoint", "randPoint"]
# [[1.0, 0.0, 0.0], [], [], []]
# Output
# [null, [-0.02493, -0.38077], [0.82314, 0.38945], [0.36572, 0.17248]]
# 
# Explanation
# Solution solution = new Solution(1.0, 0.0, 0.0);
# solution.randPoint(); // return [-0.02493, -0.38077]
# solution.randPoint(); // return [0.82314, 0.38945]
# solution.randPoint(); // return [0.36572, 0.17248]
# 
# 
# Constraints:
#         0 < radius <= 10⁸
#         -10⁷ <= x_center, y_center <= 10⁷
#         At most 3 * 10⁴ calls will be made to randPoint.

import math
import random
from typing import List

# Solution: https://algo.monster/liteproblems/478
# Credit: AlgoMonster
class Solution:
    def __init__(self, radius: float, x_center: float, y_center: float):
        self.radius = radius
        self.x_center = x_center
        self.y_center = y_center

    def randPoint(self) -> List[float]:
        # Generate random radius using square root for uniform distribution
        # sqrt is used to ensure uniform distribution across the circle area
        # Without sqrt, points would be more concentrated near the center
        random_radius = math.sqrt(random.uniform(0, self.radius ** 2))
      
        # Generate random angle in radians (0 to 2π)
        random_angle = random.uniform(0, 1) * 2 * math.pi
      
        # Convert polar coordinates to Cartesian coordinates
        # x = center_x + r * cos(θ)
        x = self.x_center + random_radius * math.cos(random_angle)
        # y = center_y + r * sin(θ)
        y = self.y_center + random_radius * math.sin(random_angle)
      
        return [x, y]

def main():
    print("TO DO")

if __name__ == "__main__":
    main()
