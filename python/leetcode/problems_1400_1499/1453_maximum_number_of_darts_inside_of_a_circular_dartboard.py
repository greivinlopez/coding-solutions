# ------------------------------------------------------------
# 1453. Maximum Number of Darts Inside of a Circular Dartboard
# ------------------------------------------------------------

# Problem: https://leetcode.com/problems/maximum-number-of-darts-inside-of-a-circular-dartboard
#
# Alice is throwing n darts on a very large wall. You are given an array darts
# where darts[i] = [xi, yi] is the position of the ith dart that Alice threw on
# the wall.
# 
# Bob knows the positions of the n darts on the wall. He wants to place a
# dartboard of radius r on the wall so that the maximum number of darts that Alice
# throws lie on the dartboard.
# 
# Given the integer r, return the maximum number of darts that can lie on the
# dartboard.
# 
# Example 1:
# 
# Input: darts = [[-2,0],[2,0],[0,2],[0,-2]], r = 2
# Output: 4
# 
# Explanation: Circle dartboard with center in (0,0) and radius = 2 contain all
# points.
# 
# Example 2:
# 
# Input: darts = [[-3,0],[3,0],[2,6],[5,4],[0,9],[7,8]], r = 5
# Output: 5
# 
# Explanation: Circle dartboard with center in (0,4) and radius = 5 contain all
# points except the point (7,8).
# 
# 
# Constraints:
#         1 <= darts.length <= 100
#         darts[i].length == 2
#         -10⁴ <= xᵢ, yᵢ <= 10⁴
#         All the darts are unique
#         1 <= r <= 5000


# Solution: https://algo.monster/liteproblems/1453
# Credit: AlgoMonster
def num_points(darts, r):
    from math import sqrt
    
    def count_darts_in_circle(center_x, center_y):
        count = 0
        for dart_x, dart_y in darts:
            # Calculate distance from dart to center
            distance = sqrt((center_x - dart_x) ** 2 + (center_y - dart_y) ** 2)
            # Check if dart is within circle (with small epsilon for floating point comparison)
            if distance <= r + 1e-7:
                count += 1
        return count
    
    def find_circle_centers(x1, y1, x2, y2):
        # Calculate distance between the two points
        dx = x2 - x1
        dy = y2 - y1
        distance_between_points = sqrt(dx * dx + dy * dy)
        
        # If points are too far apart, no circle of radius r can pass through both
        if distance_between_points > 2 * r:
            return []
        
        # Find midpoint between the two points
        mid_x = (x1 + x2) / 2
        mid_y = (y1 + y2) / 2
        
        # Calculate distance from midpoint to circle center
        # Using Pythagorean theorem: r^2 = (d/2)^2 + dist_to_center^2
        dist_to_center = sqrt(r * r - (distance_between_points / 2) * (distance_between_points / 2))
        
        # Calculate perpendicular offset from midpoint to circle centers
        # The perpendicular direction is obtained by rotating the vector (dx, dy) by 90 degrees
        offset_x = dist_to_center * dy / distance_between_points
        offset_y = dist_to_center * (-dx) / distance_between_points
        
        # Return both possible circle centers
        return [
            (mid_x + offset_x, mid_y + offset_y),
            (mid_x - offset_x, mid_y - offset_y),
        ]
    
    n = len(darts)
    max_darts_in_circle = 1  # At minimum, we can always enclose one dart
    
    # Try all pairs of darts to find circle centers
    for i in range(n):
        for j in range(i + 1, n):
            # Find possible circle centers that pass through darts[i] and darts[j]
            possible_centers = find_circle_centers(
                darts[i][0], darts[i][1], 
                darts[j][0], darts[j][1]
            )
            
            # For each possible center, count darts and update maximum
            for center_x, center_y in possible_centers:
                darts_count = count_darts_in_circle(center_x, center_y)
                max_darts_in_circle = max(max_darts_in_circle, darts_count)
    
    return max_darts_in_circle
    # Time: O(n³)
    # Space: O(1)


def main():
    result = num_points(darts = [[-2,0],[2,0],[0,2],[0,-2]], r = 2)
    print(result) # 4

    result = num_points(darts = [[-3,0],[3,0],[2,6],[5,4],[0,9],[7,8]], r = 5)
    print(result) # 5

if __name__ == "__main__":
    main()
