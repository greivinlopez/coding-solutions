# ----------------------
# 391. Perfect Rectangle
# ----------------------

# Problem: https://leetcode.com/problems/perfect-rectangle
#
# Given an array rectangles where rectangles[i] = [xᵢ, yᵢ, aᵢ, bᵢ] represents an
# axis-aligned rectangle. The bottom-left point of the rectangle is (xᵢ, yᵢ) and
# the top-right point of it is (aᵢ, bᵢ).
# 
# Return true if all the rectangles together form an exact cover of a rectangular
# region.
#
# Example 1:
# 
# https://assets.leetcode.com/uploads/2021/03/27/perectrec1-plane.jpg
# 
# Input: rectangles = [[1,1,3,3],[3,1,4,2],[3,2,4,4],[1,3,2,4],[2,3,3,4]]
# Output: true
# 
# Explanation: All 5 rectangles together form an exact cover of a rectangular
# region.
# 
# Example 2:
# 
# https://assets.leetcode.com/uploads/2021/03/27/perfectrec2-plane.jpg
# 
# Input: rectangles = [[1,1,2,3],[1,3,2,4],[3,1,4,2],[3,2,4,4]]
# Output: false
# 
# Explanation: Because there is a gap between the two rectangular regions.
# 
# Example 3:
# 
# https://assets.leetcode.com/uploads/2021/03/27/perfecrrec4-plane.jpg
# 
# Input: rectangles = [[1,1,3,3],[3,1,4,2],[1,3,2,4],[2,2,4,4]]
# Output: false
# 
# Explanation: Because two of the rectangles overlap with each other.
# 
# 
# Constraints:
#         1 <= rectangles.length <= 2 * 10⁴
#         rectangles[i].length == 4
#         -10⁵ <= xᵢ < aᵢ <= 10⁵
#         -10⁵ <= yᵢ < bᵢ <= 10⁵


# Solution: https://leetcode.com/problems/perfect-rectangle/solutions/968076/python-fast-and-clear-solution-with-explanation
# Credit: https://leetcode.com/u/modusv/
def is_rectangle_cover(rectangles):
    area = 0
    corners = set()
    a = lambda: (Y-y) * (X-x)
    
    for x, y, X, Y in rectangles:
        area += a()
        corners ^= {(x,y), (x,Y), (X,y), (X,Y)}

    if len(corners) != 4: return False
    x, y = min(corners, key=lambda x: x[0] + x[1])
    X, Y = max(corners, key=lambda x: x[0] + x[1])
    return a() == area
    # Time: O(n)
    # Space: O(n)
    # n = the number of rectangles


def main():
    result = is_rectangle_cover([[1,1,3,3],[3,1,4,2],[3,2,4,4],[1,3,2,4],[2,3,3,4]])
    print(result) # True

    result = is_rectangle_cover([[1,1,2,3],[1,3,2,4],[3,1,4,2],[3,2,4,4]])
    print(result) # False

    result = is_rectangle_cover([[1,1,3,3],[3,1,4,2],[1,3,2,4],[2,2,4,4]])
    print(result) # False

if __name__ == "__main__":
    main()
