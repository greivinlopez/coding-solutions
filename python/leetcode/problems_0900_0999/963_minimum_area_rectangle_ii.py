# ------------------------------
# 963. Minimum Area Rectangle II
# ------------------------------

# Problem: https://leetcode.com/problems/minimum-area-rectangle-ii
#
# You are given an array of points in the X-Y plane points where points[i] = [xᵢ, yᵢ].
# 
# Return the minimum area of any rectangle formed from these points, with sides
# not necessarily parallel to the X and Y axes. If there is not any such
# rectangle, return 0.
# 
# Answers within 10⁻⁵ of the actual answer will be accepted.
# 
# Example 1:
# 
# https://assets.leetcode.com/uploads/2018/12/21/1a.png
# 
# Input: points = [[1,2],[2,1],[1,0],[0,1]]
# Output: 2.00000
# 
# Explanation: The minimum area rectangle occurs at [1,2],[2,1],[1,0],[0,1], with
# an area of 2.
# 
# Example 2:
# 
# https://assets.leetcode.com/uploads/2018/12/22/2.png
# 
# Input: points = [[0,1],[2,1],[1,1],[1,0],[2,0]]
# Output: 1.00000
# 
# Explanation: The minimum area rectangle occurs at [1,0],[1,1],[2,1],[2,0], with
# an area of 1.
# 
# Example 3:
# 
# https://assets.leetcode.com/uploads/2018/12/22/3.png
# 
# Input: points = [[0,3],[1,2],[3,1],[1,3],[2,1]]
# Output: 0
# 
# Explanation: There is no possible rectangle to form from these points.
# 
# 
# Constraints:
#         1 <= points.length <= 50
#         points[i].length == 2
#         0 <= xᵢ, yᵢ <= 4 * 10⁴
#         All the given points are unique.


# Solution: https://algo.monster/liteproblems/963
# Credit: AlgoMonster
def min_area_free_rect(points):
    # Convert points list to a set for O(1) lookup
    point_set = {(x, y) for x, y in points}
    num_points = len(points)
    min_area = float('inf')
    
    # Try each point as a potential corner of the rectangle
    for i in range(num_points):
        x1, y1 = points[i]
        
        # Try second point to form one side of rectangle
        for j in range(num_points):
            if j == i:
                continue
                
            x2, y2 = points[j]
            
            # Try third point to form another side of rectangle
            for k in range(j + 1, num_points):
                if k == i:
                    continue
                    
                x3, y3 = points[k]
                
                # Calculate where the fourth point should be if these form a rectangle
                # Using vector addition: point4 = point2 - point1 + point3
                x4 = x2 - x1 + x3
                y4 = y2 - y1 + y3
                
                # Check if the fourth point exists in our point set
                if (x4, y4) in point_set:
                    # Create vectors from point1 to point2 and point1 to point3
                    vector_1_to_2 = (x2 - x1, y2 - y1)
                    vector_1_to_3 = (x3 - x1, y3 - y1)
                    
                    # Check if vectors are perpendicular (dot product equals 0)
                    dot_product = vector_1_to_2[0] * vector_1_to_3[0] + vector_1_to_2[1] * vector_1_to_3[1]
                    
                    if dot_product == 0:
                        # Calculate the lengths of the two sides
                        width = (vector_1_to_2[0] ** 2 + vector_1_to_2[1] ** 2) ** 0.5
                        height = (vector_1_to_3[0] ** 2 + vector_1_to_3[1] ** 2) ** 0.5
                        
                        # Update minimum area
                        area = width * height
                        min_area = min(min_area, area)
    
    # Return 0 if no rectangle was found, otherwise return the minimum area
    return 0.0 if min_area == float('inf') else min_area
    # Time: O(n³)
    # Space: O(n)


def main():
    result = min_area_free_rect(points = [[1,2],[2,1],[1,0],[0,1]])
    print(result) # 2.00

    result = min_area_free_rect(points = [[0,1],[2,1],[1,1],[1,0],[2,0]])
    print(result) # 1.0

    result = min_area_free_rect(points = [[0,3],[1,2],[3,1],[1,3],[2,1]])
    print(result) # 0.0

if __name__ == "__main__":
    main()
