# ----------------------
# 850. Rectangle Area II
# ----------------------

# Problem: https://leetcode.com/problems/rectangle-area-ii
#
# You are given a 2D array of axis-aligned rectangles. Each rectangle[i] = [xᵢ₁,
# yᵢ₁, xᵢ₂, yᵢ₂] denotes the iᵗʰ rectangle where (xᵢ₁, yᵢ₁) are the coordinates of
# the bottom-left corner, and (xᵢ₂, yᵢ₂) are the coordinates of the top-right
# corner.
# 
# Calculate the total area covered by all rectangles in the plane. Any area
# covered by two or more rectangles should only be counted once.
# 
# Return the total area. Since the answer may be too large, return it modulo 10⁹ +
# 7.
# 
# Example 1:
# 
# https://s3-lc-upload.s3.amazonaws.com/uploads/2018/06/06/rectangle_area_ii_pic.png
# 
# Input: rectangles = [[0,0,2,2],[1,0,2,3],[1,0,3,1]]
# Output: 6
# 
# Explanation: A total area of 6 is covered by all three rectangles, as
# illustrated in the picture.
# From (1,1) to (2,2), the green and red rectangles overlap.
# From (1,0) to (2,3), all three rectangles overlap.
# 
# Example 2:
# 
# Input: rectangles = [[0,0,1000000000,1000000000]]
# Output: 49
# 
# Explanation: The answer is 10¹⁸ modulo (10⁹ + 7), which is 49.
# 
# 
# Constraints:
#         1 <= rectangles.length <= 200
#         rectanges[i].length == 4
#         0 <= xᵢ₁, yᵢ₁, xᵢ₂, yᵢ₂ <= 10⁹
#         xᵢ₁ <= xᵢ₂
#         yᵢ₁ <= yᵢ₂
#         All rectangles have non zero area.

from collections import defaultdict

# Solution: https://leetcode.com/problems/rectangle-area-ii/solutions/7257694/2d-line-sweep-difference-array-o-n-2-log-n
# Credit: gsvamsi -> https://leetcode.com/u/gsvamsi/
def rectangle_area(rectangles):
    MOD = 1_000_000_007
    rows = defaultdict(lambda: defaultdict(int))  # y -> diff map of x positions
    area = 0

    # Build difference maps for each horizontal boundary (y1 starts, y2 ends)
    for x1, y1, x2, y2 in rectangles:
        start_row = rows[y1] 
        end_row = rows[y2] 

        start_row[x1] += 1 
        start_row[x2] -= 1 
        end_row[x1] -= 1 
        end_row[x2] += 1

    sorted_rows = sorted(rows)
    active_x = defaultdict(int)  # ongoing x coverage counts

    for i, y in enumerate(sorted_rows):
        height = 0
        if i != 0:
            height = sorted_rows[i] - sorted_rows[i - 1]

        running_count = 0
        positions = sorted(active_x)

        # print(y, ":", end=" ")
        for pos in positions:
            if running_count == 0:
                start = pos
            running_count += active_x[pos]
            if running_count == 0:
                end = pos
                width = end - start
                area = (area + height * width) % MOD

        row = rows[y]  # this is the diff map for current y
        # Update active_x with current row’s diff map
        for pos in row:
            active_x[pos] += row[pos]
            if active_x[pos] == 0:
                active_x.pop(pos)

    return area 
    # Time: O(n² * log(n))
    # Space: O(n)


def main():
    result = rectangle_area(rectangles = [[0,0,2,2],[1,0,2,3],[1,0,3,1]])
    print(result) # 6

    result = rectangle_area(rectangles = [[0,0,1000000000,1000000000]])
    print(result) # 49

if __name__ == "__main__":
    main()
