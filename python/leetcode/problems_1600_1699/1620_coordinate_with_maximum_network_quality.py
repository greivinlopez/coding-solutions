# ---------------------------------------------
# 1620. Coordinate With Maximum Network Quality
# ---------------------------------------------

# Problem: https://leetcode.com/problems/coordinate-with-maximum-network-quality
#
# You are given an array of network towers towers, where towers[i] = [xᵢ, yᵢ, qᵢ]
# denotes the iᵗʰ network tower with location (xᵢ, yᵢ) and quality factor qᵢ. All
# the coordinates are integral coordinates on the X-Y plane, and the distance
# between the two coordinates is the Euclidean distance.
# 
# You are also given an integer radius where a tower is reachable if the distance
# is less than or equal to radius. Outside that distance, the signal becomes
# garbled, and the tower is not reachable.
# 
# The signal quality of the iᵗʰ tower at a coordinate (x, y) is calculated with
# the formula ⌊qᵢ / (1 + d)⌋, where d is the distance between the tower and the
# coordinate. The network quality at a coordinate is the sum of the signal
# qualities from all the reachable towers.
# 
# Return the array [cₓ, cᵧ] representing the integral coordinate (cₓ, cᵧ) where
# the network quality is maximum. If there are multiple coordinates with the same
# network quality, return the lexicographically minimum non-negative coordinate.
# 
# Note:
#         
#   * A coordinate (x1, y1) is lexicographically smaller than (x2, y2) if either:
#                 x1 < x2, or
#                 x1 == x2 and y1 < y2.
#   * ⌊val⌋ is the greatest integer less than or equal to val (the floor function).
# 
# Example 1:
# 
# https://assets.leetcode.com/uploads/2020/09/22/untitled-diagram.png
# 
# Input: towers = [[1,2,5],[2,1,7],[3,1,9]], radius = 2
# Output: [2,1]
# 
# Explanation: At coordinate (2, 1) the total quality is 13.
# - Quality of 7 from (2, 1) results in ⌊7 / (1 + sqrt(0)⌋ = ⌊7⌋ = 7
# - Quality of 5 from (1, 2) results in ⌊5 / (1 + sqrt(2)⌋ = ⌊2.07⌋ = 2
# - Quality of 9 from (3, 1) results in ⌊9 / (1 + sqrt(1)⌋ = ⌊4.5⌋ = 4
# No other coordinate has a higher network quality.
# 
# Example 2:
# 
# Input: towers = [[23,11,21]], radius = 9
# Output: [23,11]
# 
# Explanation: Since there is only one tower, the network quality is highest right
# at the tower's location.
# 
# Example 3:
# 
# Input: towers = [[1,2,13],[2,1,7],[0,1,9]], radius = 2
# Output: [1,2]
# 
# Explanation: Coordinate (1, 2) has the highest network quality.
# 
# 
# Constraints:
#         1 <= towers.length <= 50
#         towers[i].length == 3
#         0 <= xᵢ, yᵢ, qi <= 50
#         1 <= radius <= 50


# Solution: https://algo.monster/liteproblems/1620
# Credit: AlgoMonster
def best_coordinate(towers, radius):
    max_quality = 0
    best_coordinate = [0, 0]
    
    # Check all possible coordinates in the grid (0 to 50 inclusive)
    for x_coord in range(51):
        for y_coord in range(51):
            total_quality = 0
            
            # Calculate total network quality at current coordinate
            for tower_x, tower_y, signal_quality in towers:
                # Calculate Euclidean distance from current point to tower
                distance = ((tower_x - x_coord) ** 2 + (tower_y - y_coord) ** 2) ** 0.5
                
                # Only consider towers within the effective radius
                if distance <= radius:
                    # Calculate signal contribution using the given formula
                    total_quality += int(signal_quality / (1 + distance))
            
            # Update best coordinate if current quality is higher
            if total_quality > max_quality:
                max_quality = total_quality
                best_coordinate = [x_coord, y_coord]
    
    return best_coordinate
    # Time: O(n)
    # Space: O(1)


def main():
    result = best_coordinate(towers = [[1,2,5],[2,1,7],[3,1,9]], radius = 2)
    print(result) # [2, 1]

    result = best_coordinate(towers = [[23,11,21]], radius = 9)
    print(result) # [23, 11]

    result = best_coordinate(towers = [[1,2,13],[2,1,7],[0,1,9]], radius = 2)
    print(result) # [1, 2]

if __name__ == "__main__":
    main()
