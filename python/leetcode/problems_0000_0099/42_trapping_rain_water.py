# --------------------------
# 42. Trapping Rain Water 🌧️
# --------------------------

# Problem: https://leetcode.com/problems/trapping-rain-water/
# Given n non-negative integers representing an elevation map where 
# the width of each bar is 1, compute how much water it can trap 
# after raining.

# Solution: https://youtu.be/ZI2z5pq0TqA
# Credit: Navdeep Singh founder of NeetCode 
def trap(height):
    if not height:
        return 0

    l, r = 0, len(height) - 1
    leftMax, rightMax = height[l], height[r]
    res = 0
    while l < r:
        if leftMax < rightMax:
            l += 1
            leftMax = max(leftMax, height[l])
            res += leftMax - height[l]
        else:
            r -= 1
            rightMax = max(rightMax, height[r])
            res += rightMax - height[r]
    return res

# Solution: https://youtu.be/KFdHpOlz8hs
# Credit: Greg Hogg
def trap_alt(height):
    # Time: O(n)
    # Space: O(n)
    l_wall = r_wall = 0
    n = len(height)
    max_left = [0] * n
    max_right = [0] * n

    for i in range(n):
        j = -i - 1
        max_left[i] = l_wall
        max_right[j] = r_wall
        l_wall = max(l_wall, height[i])
        r_wall = max(r_wall, height[j])

    summ = 0
    for i in range(n):
        pot = min(max_left[i], max_right[i])
        summ += max(0, pot - height[i])

    return summ

def main():
    result = trap([0,1,0,2,1,0,1,3,2,1,2,1]) # 6
    print(result)
    result = trap([4,2,0,3,2,5]) # 9
    print(result)

if __name__ == "__main__":
    main()