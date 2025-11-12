# ----------------------
# 836. Rectangle Overlap
# ----------------------

# Problem: https://leetcode.com/problems/rectangle-overlap
#
# An axis-aligned rectangle is represented as a list [x1, y1, x2, y2], where (x1,
# y1) is the coordinate of its bottom-left corner, and (x2, y2) is the coordinate
# of its top-right corner. Its top and bottom edges are parallel to the X-axis,
# and its left and right edges are parallel to the Y-axis.
# 
# Two rectangles overlap if the area of their intersection is positive. To be
# clear, two rectangles that only touch at the corner or edges do not overlap.
# 
# Given two axis-aligned rectangles rec1 and rec2, return true if they overlap,
# otherwise return false.
# 
# Example 1:
# 
# Input: rec1 = [0,0,2,2], rec2 = [1,1,3,3]
# Output: true
# 
# Example 2:
# 
# Input: rec1 = [0,0,1,1], rec2 = [1,0,2,1]
# Output: false
# 
# Example 3:
# 
# Input: rec1 = [0,0,1,1], rec2 = [2,2,3,3]
# Output: false
# 
# 
# Constraints:
#         rec1.length == 4
#         rec2.length == 4
#         -10⁹ <= rec1[i], rec2[i] <= 10⁹
#         rec1 and rec2 represent a valid rectangle with a non-zero area.


# Solution: 
# Credit: Navdeep Singh founder of NeetCode
def is_rectangle_overlap(rec1, rec2):
    # Extract coordinates for first rectangle
    x1, y1, x2, y2 = rec1
    
    # Extract coordinates for second rectangle  
    x3, y3, x4, y4 = rec2
    
    # Check if rectangles do NOT overlap:
    # - rec2 is completely above rec1 (y3 >= y2)
    # - rec2 is completely below rec1 (y4 <= y1)
    # - rec2 is completely to the right of rec1 (x3 >= x2)
    # - rec2 is completely to the left of rec1 (x4 <= x1)
    # If none of these conditions are true, rectangles must overlap
    return not (y3 >= y2 or y4 <= y1 or x3 >= x2 or x4 <= x1)
    # Time: O(1)
    # Space: O(1)


def main():
    result = is_rectangle_overlap(rec1 = [0,0,2,2], rec2 = [1,1,3,3])
    print(result) # True

    result = is_rectangle_overlap(rec1 = [0,0,1,1], rec2 = [1,0,2,1])
    print(result) # False

    result = is_rectangle_overlap(rec1 = [0,0,1,1], rec2 = [2,2,3,3])
    print(result) # False

if __name__ == "__main__":
    main()
