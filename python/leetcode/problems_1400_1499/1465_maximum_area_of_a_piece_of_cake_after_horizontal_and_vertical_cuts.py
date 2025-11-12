# ------------------------------------------------------------------------
# 1465. Maximum Area of a Piece of Cake After Horizontal and Vertical Cuts
# ------------------------------------------------------------------------

# Problem: https://leetcode.com/problems/maximum-area-of-a-piece-of-cake-after-horizontal-and-vertical-cuts
#
# You are given a rectangular cake of size h x w and two arrays of integers
# horizontalCuts and verticalCuts where:
#         
#   * horizontalCuts[i] is the distance from the top of the rectangular cake to 
#     the iᵗʰ horizontal cut and similarly, and
#   * verticalCuts[j] is the distance from the left of the rectangular cake to
#     the jᵗʰ vertical cut.
# 
# Return the maximum area of a piece of cake after you cut at each horizontal and
# vertical position provided in the arrays horizontalCuts and verticalCuts. Since
# the answer can be a large number, return this modulo 10⁹ + 7.
# 
# Example 1:
# 
# https://assets.leetcode.com/uploads/2020/05/14/leetcode_max_area_2.png
# 
# Input: h = 5, w = 4, horizontalCuts = [1,2,4], verticalCuts = [1,3]
# Output: 4
# 
# Explanation: The figure above represents the given rectangular cake. Red lines
# are the horizontal and vertical cuts. After you cut the cake, the green piece of
# cake has the maximum area.
# 
# Example 2:
# 
# https://assets.leetcode.com/uploads/2020/05/14/leetcode_max_area_3.png
# 
# Input: h = 5, w = 4, horizontalCuts = [3,1], verticalCuts = [1]
# Output: 6
# 
# Explanation: The figure above represents the given rectangular cake. Red lines
# are the horizontal and vertical cuts. After you cut the cake, the green and
# yellow pieces of cake have the maximum area.
# 
# Example 3:
# 
# Input: h = 5, w = 4, horizontalCuts = [3], verticalCuts = [3]
# Output: 9
# 
# 
# Constraints:
#         2 <= h, w <= 10⁹
#         1 <= horizontalCuts.length <= min(h - 1, 10⁵)
#         1 <= verticalCuts.length <= min(w - 1, 10⁵)
#         1 <= horizontalCuts[i] < h
#         1 <= verticalCuts[i] < w
#         All the elements in horizontalCuts are distinct.
#         All the elements in verticalCuts are distinct.


# Solution: https://algo.monster/liteproblems/1465
# Credit: AlgoMonster
def max_area(h, w, horizontalCuts, verticalCuts):
    # Add boundaries (0 and max values) to both cut lists
    horizontalCuts.extend([0, h])
    verticalCuts.extend([0, w])
    
    # Sort both lists to process consecutive cuts
    horizontalCuts.sort()
    verticalCuts.sort()
    
    # Find maximum gap between consecutive horizontal cuts
    max_height = 0
    for i in range(1, len(horizontalCuts)):
        max_height = max(max_height, horizontalCuts[i] - horizontalCuts[i - 1])
    
    # Find maximum gap between consecutive vertical cuts
    max_width = 0
    for i in range(1, len(verticalCuts)):
        max_width = max(max_width, verticalCuts[i] - verticalCuts[i - 1])
    
    # Return the area of the largest piece modulo 10^9 + 7
    MOD = 10**9 + 7
    return (max_height * max_width) % MOD
    # Time: O(m log m + n log n)
    # Space: O(log m + log n)


def main():
    result = max_area(h = 5, w = 4, horizontalCuts = [1,2,4], verticalCuts = [1,3])
    print(result) # 4

    result = max_area(h = 5, w = 4, horizontalCuts = [3,1], verticalCuts = [1])
    print(result) # 6

    result = max_area(h = 5, w = 4, horizontalCuts = [3], verticalCuts = [3])
    print(result) # 9

if __name__ == "__main__":
    main()
