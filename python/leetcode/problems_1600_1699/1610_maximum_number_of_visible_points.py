# --------------------------------------
# 1610. Maximum Number of Visible Points
# --------------------------------------

# Problem: https://leetcode.com/problems/maximum-number-of-visible-points
#
# You are given an array points, an integer angle, and your location, where
# location = [posx, posy] and points[i] = [xi, yi] both denote integral
# coordinates on the X-Y plane.
# 
# Initially, you are facing directly east from your position. You cannot move from
# your position, but you can rotate. In other words, posx and posy cannot be
# changed. Your field of view in degrees is represented by angle, determining how
# wide you can see from any given view direction. Let d be the amount in degrees
# that you rotate counterclockwise. Then, your field of view is the inclusive
# range of angles [d - angle/2, d + angle/2].
# 
# https://assets.leetcode.com/uploads/2020/09/30/angle.mp4
# 
# You can see some set of points if, for each point, the angle formed by the
# point, your position, and the immediate east direction from your position is in
# your field of view.
# 
# There can be multiple points at one coordinate. There may be points at your
# location, and you can always see these points regardless of your rotation.
# Points do not obstruct your vision to other points.
# 
# Return the maximum number of points you can see.
# 
# Example 1:
# 
# https://assets.leetcode.com/uploads/2020/09/30/89a07e9b-00ab-4967-976a-c723b2aa8656.png
# 
# Input: points = [[2,1],[2,2],[3,3]], angle = 90, location = [1,1]
# Output: 3
# 
# Explanation: The shaded region represents your field of view. All points can be
# made visible in your field of view, including [3,3] even though [2,2] is in
# front and in the same line of sight.
# 
# Example 2:
# 
# Input: points = [[2,1],[2,2],[3,4],[1,1]], angle = 90, location = [1,1]
# Output: 4
# 
# Explanation: All points can be made visible in your field of view, including the
# one at your location.
# 
# Example 3:
# 
# https://assets.leetcode.com/uploads/2020/09/30/5010bfd3-86e6-465f-ac64-e9df941d2e49.png
# 
# Input: points = [[1,0],[2,1]], angle = 13, location = [1,1]
# Output: 1
# 
# Explanation: You can only see one of the two points, as shown above.
# 
# 
# Constraints:
#         1 <= points.length <= 10⁵
#         points[i].length == 2
#         location.length == 2
#         0 <= angle < 360
#         0 <= posx, posy, xi, yi <= 100


# Solution: https://algo.monster/liteproblems/1610
# Credit: AlgoMonster
def visible_points(points, angle, location):
    from math import atan2, pi
    from bisect import bisect_right
    
    # Extract observer's location coordinates
    observer_x, observer_y = location
    
    # Count points that are at the same location as the observer
    same_location_count = 0
    
    # Store angles of all points relative to the observer
    angles = []
    
    # Calculate angle for each point relative to the observer
    for point_x, point_y in points:
        if point_x == observer_x and point_y == observer_y:
            # Point is at the same location as observer
            same_location_count += 1
        else:
            # Calculate angle using atan2 (returns angle in radians)
            angle_rad = atan2(point_y - observer_y, point_x - observer_x)
            angles.append(angle_rad)
    
    # Sort angles in ascending order
    angles.sort()
    
    # Get number of unique angle points
    num_angles = len(angles)
    
    # Duplicate the angles array with 2π added to handle circular nature
    # This allows us to check angles that wrap around the circle
    angles += [angle_val + 2 * pi for angle_val in angles]
    
    # Convert viewing angle from degrees to radians
    viewing_angle_rad = angle * pi / 180
    
    # Find maximum number of points visible within the viewing angle
    # Use sliding window approach with binary search
    max_visible = max(
        (bisect_right(angles, angles[i] + viewing_angle_rad) - i 
            for i in range(num_angles)), 
        default=0
    )
    
    # Return total visible points (including those at observer's location)
    return max_visible + same_location_count
    # Time: O(n * log n)
    # Space: O(n)


def main():
    result = visible_points(points = [[2,1],[2,2],[3,3]], angle = 90, location = [1,1])
    print(result) # 3

    result = visible_points(points = [[2,1],[2,2],[3,4],[1,1]], angle = 90, location = [1,1])
    print(result) # 4

    result = visible_points(points = [[1,0],[2,1]], angle = 13, location = [1,1])
    print(result) # 1

if __name__ == "__main__":
    main()
