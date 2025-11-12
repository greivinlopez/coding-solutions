# ---------------------------
# 939. Minimum Area Rectangle
# ---------------------------

# Problem: https://leetcode.com/problems/minimum-area-rectangle
#
# You are given an array of points in the X-Y plane points where points[i] = [xᵢ, yᵢ].
# 
# Return the minimum area of a rectangle formed from these points, with sides
# parallel to the X and Y axes. If there is not any such rectangle, return 0.
# 
# Example 1:
# 
# https://assets.leetcode.com/uploads/2021/08/03/rec1.JPG
# 
# Input: points = [[1,1],[1,3],[3,1],[3,3],[2,2]]
# Output: 4
# 
# Example 2:
# 
# https://assets.leetcode.com/uploads/2021/08/03/rec2.JPG
# 
# Input: points = [[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]
# Output: 2
# 
# 
# Constraints:
#         1 <= points.length <= 500
#         points[i].length == 2
#         0 <= xᵢ, yᵢ <= 4 * 10⁴
#         All the given points are unique.

from collections import defaultdict
import math

# Solution: https://algo.monster/liteproblems/939
# Credit: AlgoMonster
def min_area_rect(points):
    # Group points by their x-coordinate
    x_to_y_coords = defaultdict(list)
    for x, y in points:
        x_to_y_coords[x].append(y)
    
    # Dictionary to store the last x-coordinate where a pair of y-values was seen
    y_pair_to_last_x = {}
    min_area = math.inf
    
    # Process x-coordinates in sorted order
    for current_x in sorted(x_to_y_coords):
        # Get all y-coordinates for this x and sort them
        y_coords = x_to_y_coords[current_x]
        y_coords.sort()
        num_y_coords = len(y_coords)
        
        # Check all pairs of y-coordinates at this x
        for i, y1 in enumerate(y_coords):
            for y2 in y_coords[i + 1:]:
                # If we've seen this y-pair before, we can form a rectangle
                if (y1, y2) in y_pair_to_last_x:
                    previous_x = y_pair_to_last_x[(y1, y2)]
                    # Calculate area: width * height
                    area = (current_x - previous_x) * (y2 - y1)
                    min_area = min(min_area, area)
                
                # Update the last x-coordinate where this y-pair was seen
                y_pair_to_last_x[(y1, y2)] = current_x
    
    # Return 0 if no rectangle was found, otherwise return minimum area
    return 0 if min_area == math.inf else min_area
    # Time: O(n²)
    # Space: O(n)


def main():
    result = min_area_rect(points = [[1,1],[1,3],[3,1],[3,3],[2,2]])
    print(result) # 4

    result = min_area_rect(points = [[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]])
    print(result) # 2

if __name__ == "__main__":
    main()
