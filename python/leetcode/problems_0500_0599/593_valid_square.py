# -----------------
# 593. Valid Square
# -----------------

# Problem: https://leetcode.com/problems/valid-square
#
# Given the coordinates of four points in 2D space p1, p2, p3 and p4, return true
# if the four points construct a square.
# 
# The coordinate of a point pᵢ is represented as [xᵢ, yᵢ]. The input is not given
# in any order.
# 
# A valid square has four equal sides with positive length and four equal angles
# (90-degree angles).
# 
# Example 1:
# 
# Input: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1]
# Output: true
# 
# Example 2:
# 
# Input: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,12]
# Output: false
# 
# Example 3:
# 
# Input: p1 = [1,0], p2 = [-1,0], p3 = [0,1], p4 = [0,-1]
# Output: true
# 
# 
# Constraints:
#         p1.length == p2.length == p3.length == p4.length == 2
#         -10⁴ <= xᵢ, yᵢ <= 10⁴


# Solution: https://algo.monster/liteproblems/593
# Credit: AlgoMonster
def valid_square(p1, p2, p3, p4): 
    def is_right_isosceles_triangle(point_a, point_b, point_c):
        # Extract coordinates for readability
        x1, y1 = point_a[0], point_a[1]
        x2, y2 = point_b[0], point_b[1]
        x3, y3 = point_c[0], point_c[1]
        
        # Calculate squared distances between each pair of points
        # Using squared distances to avoid floating point operations
        dist_squared_ab = (x1 - x2) ** 2 + (y1 - y2) ** 2
        dist_squared_ac = (x1 - x3) ** 2 + (y1 - y3) ** 2
        dist_squared_bc = (x2 - x3) ** 2 + (y2 - y3) ** 2
        
        # Check if any configuration forms a right isosceles triangle:
        # Two sides must be equal (isosceles) and satisfy Pythagorean theorem (right angle)
        # Also ensure sides have non-zero length (last condition in each case)
        return any([
            # Case 1: AB == AC, and AB² + AC² == BC² (right angle at A)
            dist_squared_ab == dist_squared_ac and 
            dist_squared_ab + dist_squared_ac == dist_squared_bc and 
            dist_squared_ab > 0,
            
            # Case 2: AC == BC, and AC² + BC² == AB² (right angle at C)
            dist_squared_ac == dist_squared_bc and 
            dist_squared_ac + dist_squared_bc == dist_squared_ab and 
            dist_squared_ac > 0,
            
            # Case 3: AB == BC, and AB² + BC² == AC² (right angle at B)
            dist_squared_ab == dist_squared_bc and 
            dist_squared_ab + dist_squared_bc == dist_squared_ac and 
            dist_squared_ab > 0,
        ])
    
    # For four points to form a square, every combination of three points
    # must form a right isosceles triangle (the fourth point being the opposite corner)
    return (
        is_right_isosceles_triangle(p1, p2, p3) and
        is_right_isosceles_triangle(p2, p3, p4) and
        is_right_isosceles_triangle(p1, p3, p4) and
        is_right_isosceles_triangle(p1, p2, p4)
    )


def main():
    result = valid_square(p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1])
    print(result) # True

    result = valid_square(p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,12])
    print(result) # False

    result = valid_square(p1 = [1,0], p2 = [-1,0], p3 = [0,1], p4 = [0,-1])
    print(result) # True

if __name__ == "__main__":
    main()
