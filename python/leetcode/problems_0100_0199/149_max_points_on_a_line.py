# -------------------------
# 149. Max Points On A Line
# -------------------------

# Problem: https://leetcode.com/problems/max-points-on-a-line/
# 
# Given an array of points where points[i] = [xi, yi] represents a point on 
# the X-Y plane, return the maximum number of points that lie on the same 
# straight line.
# 
#  
# Example 1:
# 
# Input: points = [[1,1],[2,2],[3,3]]
# Output: 3
# 
# 
# Example 2:
# 
# Input: points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
# Output: 4
# 
# 
# Constraints:
# 
# 	1 <= points.length <= 300
# 	points[i].length == 2
# 	-104 <= xi, yi <= 104
# 	All the points are unique.

import collections

# Solution: https://youtu.be/Bb9lOXUOnFw
# Credit: Navdeep Singh founder of NeetCode
def max_points(points):
    # 1. For each pt determine if it lies on the longest line
    # 2. Count all pts with same slope
    # 3. Update result with max

    res = 1
    for i in range(len(points)):
        p1 = points[i]
        count = collections.defaultdict(int)
        for j in range(i + 1, len(points)):
            p2 = points[j]
            if p2[0] == p1[0]:
                slope = float("inf")
            else:
                slope = (p2[1] - p1[1]) / (p2[0] - p1[0])
            count[slope] += 1
            res = max(res, count[slope] + 1)
    return res


def main():
    result = max_points([[1,1],[2,2],[3,3]])
    print(result) # 3

    result = max_points([[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]])
    print(result) # 4

if __name__ == "__main__":
    main()
