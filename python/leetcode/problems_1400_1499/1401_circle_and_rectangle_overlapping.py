# --------------------------------------------
# 1401. Circle and Rectangle Overlapping 🟡 🟦
# --------------------------------------------

# Problem: https://leetcode.com/problems/circle-and-rectangle-overlapping
#
# You are given a circle represented as (radius, xCenter, yCenter) and an axis-
# aligned rectangle represented as (x1, y1, x2, y2), where (x1, y1) are the
# coordinates of the bottom-left corner, and (x2, y2) are the coordinates of the
# top-right corner of the rectangle.
# 
# Return true if the circle and rectangle are overlapped otherwise return false.
# In other words, check if there is any point (xi, yi) that belongs to the circle
# and the rectangle at the same time.
# 
# Example 1:
# 
# Input: radius = 1, xCenter = 0, yCenter = 0, x1 = 1, y1 = -1, x2 = 3, y2 = 1
# Output: true
# 
# Explanation: Circle and rectangle share the point (1,0).
# 
# Example 2:
# 
# Input: radius = 1, xCenter = 1, yCenter = 1, x1 = 1, y1 = -3, x2 = 2, y2 = -1
# Output: false
# 
# Example 3:
# 
# Input: radius = 1, xCenter = 0, yCenter = 0, x1 = -1, y1 = 0, x2 = 0, y2 = 1
# Output: true
# 
# 
# Constraints:
#         1 <= radius <= 2000
#         -10⁴ <= xCenter, yCenter <= 10⁴
#         -10⁴ <= x1 < x2 <= 10⁴
#         -10⁴ <= y1 < y2 <= 10⁴


# Solution: https://algo.monster/liteproblems/1401
# Credit: AlgoMonster
def check_overlap(radius, xCenter, yCenter, x1, y1, x2, y2):

    def get_closest_distance_to_range(range_start, range_end, point):
        if range_start <= point <= range_end:
            # Point is within the range
            return 0
        
        if point < range_start:
            # Point is to the left/below the range
            return range_start - point
        else:
            # Point is to the right/above the range
            return point - range_end
    
    # Calculate the closest horizontal distance from circle center to rectangle
    horizontal_distance = get_closest_distance_to_range(x1, x2, xCenter)
    
    # Calculate the closest vertical distance from circle center to rectangle
    vertical_distance = get_closest_distance_to_range(y1, y2, yCenter)
    
    # Check if the squared distance is within the squared radius
    # Using squared values to avoid floating point operations
    squared_distance = horizontal_distance ** 2 + vertical_distance ** 2
    squared_radius = radius ** 2
    
    return squared_distance <= squared_radius
    # Time: O(n)
    # Space: O(n)


def main():
    result = check_overlap(radius = 1, xCenter = 0, yCenter = 0, x1 = 1, y1 = -1, x2 = 3, y2 = 1)
    print(result) # True

    result = check_overlap(radius = 1, xCenter = 1, yCenter = 1, x1 = 1, y1 = -3, x2 = 2, y2 = -1)
    print(result) # False

    result = check_overlap(radius = 1, xCenter = 0, yCenter = 0, x1 = -1, y1 = 0, x2 = 0, y2 = 1)
    print(result) # True

if __name__ == "__main__":
    main()
