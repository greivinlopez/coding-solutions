# -------------------------
# 447. Number of Boomerangs
# -------------------------

# Problem: https://leetcode.com/problems/number-of-boomerangs
#
# You are given n points in the plane that are all distinct, where points[i] =
# [xᵢ, yᵢ]. A boomerang is a tuple of points (i, j, k) such that the distance
# between i and j equals the distance between i and k (the order of the tuple
# matters).
# 
# Return the number of boomerangs.
# 
# Example 1:
# 
# Input: points = [[0,0],[1,0],[2,0]]
# Output: 2
# 
# Explanation: The two boomerangs are [[1,0],[0,0],[2,0]] and [[1,0],[2,0],[0,0]].
# 
# Example 2:
# 
# Input: points = [[1,1],[2,2],[3,3]]
# Output: 2
# 
# Example 3:
# 
# Input: points = [[1,1]]
# Output: 0
# 
# 
# Constraints:
#         n == points.length
#         1 <= n <= 500
#         points[i].length == 2
#         -10⁴ <= xᵢ, yᵢ <= 10⁴
#         All the points are unique.

from collections import Counter

# Solution: https://algo.monster/liteproblems/447
# Credit: AlgoMonster
def number_of_boomerangs(points):
    total_boomerangs = 0
    
    # For each point as the center point (i in the tuple)
    for center_point in points:
        # Track count of points at each distance from the center
        distance_count = Counter()
        
        # Calculate distances from center to all other points
        for other_point in points:
            # Calculate squared Euclidean distance (avoid sqrt for efficiency)
            distance = (center_point[0] - other_point[0]) ** 2 + \
                        (center_point[1] - other_point[1]) ** 2
            
            # For each point at this distance, it can form boomerangs with
            # all previously seen points at the same distance
            total_boomerangs += distance_count[distance]
            
            # Increment count for this distance
            distance_count[distance] += 1
    
    # Multiply by 2 because each valid pair (j, k) can be ordered in 2 ways
    return total_boomerangs * 2
    # Time: O(n²)
    # Space: O(n)


def main():
    result = number_of_boomerangs([[0,0],[1,0],[2,0]])
    print(result) # 2

    result = number_of_boomerangs([[1,1],[2,2],[3,3]])
    print(result) # 2

    result = number_of_boomerangs([[1,1]])
    print(result) # 0

if __name__ == "__main__":
    main()
