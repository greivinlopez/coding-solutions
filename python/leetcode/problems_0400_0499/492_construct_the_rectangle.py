# ----------------------------
# 492. Construct the Rectangle
# ----------------------------

# Problem: https://leetcode.com/problems/construct-the-rectangle
#
# A web developer needs to know how to design a web page's size. So, given a
# specific rectangular web page’s area, your job by now is to design a rectangular
# web page, whose length L and width W satisfy the following requirements:
#         
#   1. The area of the rectangular web page you designed must equal to the
#      given target area.
#   2. The width W should not be larger than the length L, which means L >= W.
#   3. The difference between length L and width W should be as small as possible.
# 
# Return an array [L, W] where L and W are the length and width of the web page
# you designed in sequence.
# 
# Example 1:
# 
# Input: area = 4
# Output: [2,2]
# 
# Explanation: The target area is 4, and all the possible ways to construct it are
# [1,4], [2,2], [4,1].
# But according to requirement 2, [1,4] is illegal; according to requirement 3,
# [4,1] is not optimal compared to [2,2]. So the length L is 2, and the width W is
# 2.
# 
# Example 2:
# 
# Input: area = 37
# Output: [37,1]
# 
# Example 3:
# 
# Input: area = 122122
# Output: [427,286]
# 
# 
# Constraints:
#         1 <= area <= 10⁷

from math import sqrt

# Solution: https://algo.monster/liteproblems/492
# Credit: AlgoMonster
def construct_rectangle_alt(area):
    # Start with width as the square root of area (rounded down)
    # This ensures we find the closest L and W values where L >= W
    width = int(sqrt(area))
    
    # Decrease width until we find a value that divides the area evenly
    # This guarantees width is a factor of area
    while area % width != 0:
        width -= 1
    
    # Calculate length using the found width
    # Return [L, W] where L >= W as required
    length = area // width
    return [length, width]
    # Time: O(√n)
    # Space: O(1)
    # n = area

# Solution: https://leetcode.com/problems/construct-the-rectangle/solutions/899176/python-a-simple-for-loop
def construct_rectangle(area):
    for l in range(int(area**0.5), 0, -1):            
        if area % l == 0: 
            return [area // l, l]
    # Time: O(√n)
    # Space: O(1)
    # n = area


def main():
    result = construct_rectangle(4)
    print(result) # [2, 2]

    result = construct_rectangle(37)
    print(result) # [37, 1]

    result = construct_rectangle(122122)
    print(result) # [427, 286]

if __name__ == "__main__":
    main()
