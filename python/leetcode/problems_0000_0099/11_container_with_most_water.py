# ---------------------------------
# 11. Container With Most Water 🚰
# ---------------------------------

# Problem: https://leetcode.com/problems/container-with-most-water
#
# You are given an integer array height of length n. There are n vertical lines
# drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
# 
# Find two lines that together with the x-axis form a container, such that the
# container contains the most water.
# 
# Return the maximum amount of water a container can store.
# 
# Notice that you may not slant the container.
# 
# Example 1:
# 
# https://s3-lc-upload.s3.amazonaws.com/uploads/2018/07/17/question_11.jpg
# 
# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# 
# Explanation: The above vertical lines are represented by array
# [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the
# container can contain is 49.
# 
# Example 2:
# 
# Input: height = [1,1]
# Output: 1
# 
# 
# Constraints:
#         n == height.length
#         2 <= n <= 10⁵
#         0 <= height[i] <= 10⁴

# Solution: https://youtu.be/UuiTKBwPgAo
# Credit: Navdeep Singh founder of NeetCode 
def max_area(height):
    l, r = 0, len(height) - 1
    res = 0

    while l < r:
        res = max(res, min(height[l], height[r]) * (r - l))
        if height[l] < height[r]:
            l += 1
        elif height[r] <= height[l]:
            r -= 1
        
    return res
    # Time: O(n)
    # Space: O(1)

# Solution: https://youtu.be/Y_4_or0Sc7I
# Credit: Greg Hogg
def max_area_alt(height):
    n = len(height)
    l = 0
    r = n - 1
    max_area = 0

    while l < r:
        w = r - l
        h = min(height[l], height[r])
        a = w * h
        max_area = max(max_area, a)
        
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1

    return max_area
    # Time: O(n)
    # Space: O(1)


def main():
    result = max_area([1,8,6,2,5,4,8,3,7]) # 49
    print(result)
    result = max_area([1,1]) # 1
    print(result)

if __name__ == "__main__":
    main()