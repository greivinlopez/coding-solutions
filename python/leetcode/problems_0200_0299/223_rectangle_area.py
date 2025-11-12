# -------------------
# 223. Rectangle Area
# -------------------

# Problem: https://leetcode.com/problems/rectangle-area
#
# Given the coordinates of two rectilinear rectangles in a 2D plane, return the
# total area covered by the two rectangles.
# 
# The first rectangle is defined by its bottom-left corner (ax1, ay1) and its top-
# right corner (ax2, ay2).
# 
# The second rectangle is defined by its bottom-left corner (bx1, by1) and its
# top-right corner (bx2, by2).
# 
# Example 1:
# 
# Input: ax1 = -3, ay1 = 0, ax2 = 3, ay2 = 4, bx1 = 0, by1 = -1, bx2 = 9, by2 = 2
# Output: 45
# 
# Example 2:
# 
# Input: ax1 = -2, ay1 = -2, ax2 = 2, ay2 = 2, bx1 = -2, by1 = -2, bx2 = 2, by2 = 2
# Output: 16
# 
# 
# Constraints:
#         -10⁴ <= ax1 <= ax2 <= 10⁴
#         -10⁴ <= ay1 <= ay2 <= 10⁴
#         -10⁴ <= bx1 <= bx2 <= 10⁴
#         -10⁴ <= by1 <= by2 <= 10⁴


# Solution: https://leetcode.com/problems/rectangle-area/solutions/665532/python-js-java-c-sol-by-math-w-hint
# Credit: Brian Chiang -> https://leetcode.com/u/brianchiang_tw/
def compute_area(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2):
    left_boundary = max(ax1, bx1)
    right_boundary = min(ax2, bx2)
    
    top_boundary = min(ay2, by2)
    bottom_bondary = max(ay1, by1)
    
    area_1 = (ax2 - ax1)*(ay2 - ay1)
    area_2 = (bx2 - bx1)*(by2 - by1)
    
    if (left_boundary < right_boundary) and (bottom_bondary < top_boundary):
        # area_1 and area_2 has overlapped area
        intersection = ( right_boundary - left_boundary ) * ( top_boundary - bottom_bondary )       
    else:
        # area_1 and area_2 has no overlapped area
        intersection = 0
    
    return area_1 + area_2 - intersection
    # Time: O(1)
    # Space: O(1)


def main():
    result = compute_area(ax1 = -3, ay1 = 0, ax2 = 3, ay2 = 4, bx1 = 0, by1 = -1, bx2 = 9, by2 = 2)
    print(result) # 45

    result = compute_area(ax1 = -2, ay1 = -2, ax2 = 2, ay2 = 2, bx1 = -2, by1 = -2, bx2 = 2, by2 = 2)
    print(result) # 16

if __name__ == "__main__":
    main()
