# ---------------------
# 1037. Valid Boomerang
# ---------------------

# Problem: https://leetcode.com/problems/valid-boomerang
#
# Given an array points where points[i] = [xᵢ, yᵢ] represents a point on the X-Y
# plane, return true if these points are a boomerang.
# 
# A boomerang is a set of three points that are all distinct and not in a straight
# line.
# 
# Example 1:
# 
# Input: points = [[1,1],[2,3],[3,2]]
# Output: true
# 
# Example 2:
# 
# Input: points = [[1,1],[2,2],[3,3]]
# Output: false
# 
# 
# Constraints:
#         points.length == 3
#         points[i].length == 2
#         0 <= xᵢ, yᵢ <= 100


# Solution: https://algo.monster/liteproblems/1037
# Credit: AlgoMonster
def is_boomerang(points):
    # Unpack the three points
    (x1, y1), (x2, y2), (x3, y3) = points
    
    # Check if the three points are collinear using cross multiplication
    # If points are collinear: (y2 - y1) / (x2 - x1) == (y3 - y2) / (x3 - x2)
    # To avoid division by zero, we cross multiply:
    # (y2 - y1) * (x3 - x2) == (y3 - y2) * (x2 - x1)
    # Points form a boomerang if they are NOT collinear (inequality)
    return (y2 - y1) * (x3 - x2) != (y3 - y2) * (x2 - x1)
    # Time: O(1)
    # Space: O(1)


def main():
    result = is_boomerang(points = [[1,1],[2,3],[3,2]])
    print(result) # True

    result = is_boomerang(points = [[1,1],[2,2],[3,3]])
    print(result) # False

if __name__ == "__main__":
    main()
