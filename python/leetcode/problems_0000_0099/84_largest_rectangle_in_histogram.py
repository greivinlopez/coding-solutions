# --------------------------------------
# 84. Largest Rectangle in Histogram 📊
# --------------------------------------

# Problem: https://leetcode.com/problems/largest-rectangle-in-histogram/
# 
# Given an array of integers heights representing the histogram's bar height 
# where the width of each bar is 1, return the area of the largest rectangle 
# in the histogram.

# Solution: https://youtu.be/zx5Sw9130L0
# Credit: Navdeep Singh founder of NeetCode
def largest_rectangle_area(heights):
    max_area = 0
    stack = [] # pair: (index, height)

    for i, h in enumerate(heights):
        start = i
        while stack and stack[-1][1] > h:
            index, height = stack.pop()
            max_area = max(max_area, height * (i - index))
            start = index
        stack.append((start, h))

    for i, h in stack:
        max_area = max(max_area, h * (len(heights) - i))
    return max_area

# Solution: https://youtu.be/ZGMw8Bvpwd4
# Credit: Greg Hogg
def largest_rectangle_area_alt(heights):
    n = len(heights)
    stk = []
    max_area = 0

    for i, height in enumerate(heights):
        start = i
        while stk and height < stk[-1][0]:
            h, j = stk.pop()
            w = i - j
            a = h*w
            max_area = max(max_area, a)
            start = j
        stk.append((height, start))
    
    while stk:
        h, j = stk.pop()
        w = n - j
        max_area = max(max_area, h*w)
    
    return max_area
    

def main():
    heights = [2,1,5,6,2,3]
    result = largest_rectangle_area(heights)
    print(result) # 10

    heights = [2,4]
    result = largest_rectangle_area(heights)
    print(result) # 4

if __name__ == "__main__":
    main()