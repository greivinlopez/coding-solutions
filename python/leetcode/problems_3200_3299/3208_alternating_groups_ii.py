# ---------------------------
# 3208. Alternating Groups II
# ---------------------------

# Problem: https://leetcode.com/problems/alternating-groups-ii
#
# There is a circle of red and blue tiles. You are given an array of integers
# colors and an integer k. The color of tile i is represented by colors[i]:
#         
#   colors[i] == 0 means that tile i is red.
#   colors[i] == 1 means that tile i is blue.
# 
# An alternating group is every k contiguous tiles in the circle with alternating
# colors (each tile in the group except the first and last one has a different
# color from its left and right tiles).
# 
# Return the number of alternating groups.
# 
# Note that since colors represents a circle, the first and the last tiles are
# considered to be next to each other.
# 
# Example 1:
# Input: colors = [0,1,0,1,0], k = 3
# Output: 3
# 
# Explanation:
# 
# https://assets.leetcode.com/uploads/2024/06/19/screenshot-2024-05-28-183519.png
# 
# Alternating groups:
# 
# https://assets.leetcode.com/uploads/2024/05/28/screenshot-2024-05-28-182448.png
# 
# Example 2:
# 
# Input: colors = [0,1,0,0,1,0,1], k = 6
# Output: 2
# 
# Explanation:
# 
# https://assets.leetcode.com/uploads/2024/06/19/screenshot-2024-05-28-183907.png
# 
# Alternating groups:
# 
# https://assets.leetcode.com/uploads/2024/06/19/screenshot-2024-05-28-184128.png
# 
# Example 3:
# 
# Input: colors = [1,1,0,1], k = 4
# Output: 0
# 
# Explanation:
# 
# https://assets.leetcode.com/uploads/2024/06/19/screenshot-2024-05-28-184516.png
# 
# 
# Constraints:
#         3 <= colors.length <= 10⁵
#         0 <= colors[i] <= 1
#         3 <= k <= colors.length


# Solution: https://youtu.be/Zexx16dNPX8
# Credit: Navdeep Singh founder of NeetCode
def number_of_alternating_groups( colors, k):
    N = len(colors)
    l = 0
    res = 0
    
    for r in range(1, N + k - 1):
        if colors[r % N] == colors[(r - 1) % N]:
            l = r
        if r - l + 1 > k:
            l += 1
        if r - l + 1 == k:
            res += 1
    return res
    # Time: O(n + k)
    # Space: O(1)


def main():
    result = number_of_alternating_groups(colors = [0,1,0,1,0], k = 3)
    print(result) # 3

    result = number_of_alternating_groups(colors = [0,1,0,0,1,0,1], k = 6)
    print(result) # 2

    result = number_of_alternating_groups(colors = [1,1,0,1], k = 4)
    print(result) # 0

if __name__ == "__main__":
    main()
