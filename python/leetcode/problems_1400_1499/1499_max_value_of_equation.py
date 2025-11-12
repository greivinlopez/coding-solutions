# ---------------------------
# 1499. Max Value of Equation
# ---------------------------

# Problem: https://leetcode.com/problems/max-value-of-equation
#
# You are given an array points containing the coordinates of points on a 2D
# plane, sorted by the x-values, where points[i] = [xᵢ, yᵢ] such that xᵢ < xⱼ for
# all 1 <= i < j <= points.length. You are also given an integer k.
# 
# Return the maximum value of the equation yᵢ + yⱼ + |xᵢ - xⱼ| where |xᵢ - xⱼ| <=
# k and 1 <= i < j <= points.length.
# 
# It is guaranteed that there exists at least one pair of points that satisfy the
# constraint |xᵢ - xⱼ| <= k.
# 
# Example 1:
# 
# Input: points = [[1,3],[2,0],[5,10],[6,-10]], k = 1
# Output: 4
# 
# Explanation: The first two points satisfy the condition |xi - xj| <= 1 and if we
# calculate the equation we get 3 + 0 + |1 - 2| = 4. Third and fourth points also
# satisfy the condition and give a value of 10 + -10 + |5 - 6| = 1.
# No other pairs satisfy the condition, so we return the max of 4 and 1.
# 
# Example 2:
# 
# Input: points = [[0,0],[3,0],[9,2]], k = 3
# Output: 3
# 
# Explanation: Only the first two points have an absolute difference of 3 or less
# in the x-values, and give the value of 0 + 0 + |0 - 3| = 3.
# 
# 
# Constraints:
#         2 <= points.length <= 10⁵
#         points[i].length == 2
#         -10⁸ <= xᵢ, yᵢ <= 10⁸
#         0 <= k <= 2 * 10⁸
#         xᵢ < xⱼ for all 1 <= i < j <= points.length
#         xᵢ form a strictly increasing sequence.

import heapq
from math import inf

# Solution: https://algo.monster/liteproblems/1499
# Credit: AlgoMonster
def find_max_value_of_equation(points, k):
    # Initialize the maximum result as negative infinity
    max_value = -inf
    
    # Min-heap to store tuples of (x - y, x)
    # We want to maximize (y - x) + (current_y + current_x)
    # Since heapq is a min-heap, we store (x - y) to get the minimum (x - y),
    # which corresponds to maximum (y - x)
    min_heap = []
    
    # Iterate through each point
    for current_x, current_y in points:
        # Remove points from heap that are too far away (distance > k)
        while min_heap and current_x - min_heap[0][1] > k:
            heapq.heappop(min_heap)
        
        # If heap is not empty, calculate the value of the equation
        # with the best previous point
        if min_heap:
            # The equation value is: current_x + current_y - (x_i - y_i)
            # which equals: current_x + current_y + y_i - x_i
            max_value = max(max_value, current_x + current_y - min_heap[0][0])
        
        # Add current point to the heap for future comparisons
        # Store (x - y, x) tuple
        heapq.heappush(min_heap, (current_x - current_y, current_x))
    
    return max_value
    # Time: O(n * log n)
    # Space: O(n)


def main():
    result = find_max_value_of_equation(points = [[1,3],[2,0],[5,10],[6,-10]], k = 1)
    print(result) # 4

    result = find_max_value_of_equation(points = [[0,0],[3,0],[9,2]], k = 3)
    print(result) # 3

if __name__ == "__main__":
    main()
