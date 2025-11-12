# ---------------------------------------
# 757. Set Intersection Size At Least Two
# ---------------------------------------

# Problem: https://leetcode.com/problems/set-intersection-size-at-least-two
#
# You are given a 2D integer array intervals where intervals[i] = [starti, endi]
# represents all the integers from starti to endi inclusively.
# 
# A containing set is an array nums where each interval from intervals has at
# least two integers in nums.
#         
#   * For example, if intervals = [[1,3], [3,7], [8,9]], then [1,2,4,7,8,9]
#     and [2,3,4,8,9] are containing sets.
# 
# Return the minimum possible size of a containing set.
# 
# Example 1:
# 
# Input: intervals = [[1,3],[3,7],[8,9]]
# Output: 5
# 
# Explanation: let nums = [2, 3, 4, 8, 9].
# It can be shown that there cannot be any containing array of size 4.
# 
# Example 2:
# 
# Input: intervals = [[1,3],[1,4],[2,5],[3,5]]
# Output: 3
# 
# Explanation: let nums = [2, 3, 4].
# It can be shown that there cannot be any containing array of size 2.
# 
# Example 3:
# 
# Input: intervals = [[1,2],[2,3],[2,4],[4,5]]
# Output: 5
# 
# Explanation: let nums = [1, 2, 3, 4, 5].
# It can be shown that there cannot be any containing array of size 4.
# 
# 
# Constraints:
#         1 <= intervals.length <= 3000
#         intervals[i].length == 2
#         0 <= starti < endi <= 10⁸


# Solution: https://algo.monster/liteproblems/757
# Credit: AlgoMonster
def intersection_size_two(intervals):
    # Sort intervals by end point (ascending), then by start point (descending)
    # This ensures we process intervals with earlier endpoints first
    # For same endpoints, we prefer intervals with larger start points
    intervals.sort(key=lambda interval: (interval[1], -interval[0]))
    
    # Initialize two points that will be in our result set
    # second_last: the second-to-last point we've chosen
    # last: the last (most recent) point we've chosen
    second_last = -1
    last = -1
    result_size = 0
    
    for start, end in intervals:
        # Case 1: Current interval already contains both tracked points
        # No new points needed
        if start <= second_last:
            continue
        
        # Case 2: Current interval doesn't contain any tracked points
        # We need to add 2 new points (choose the two largest in the interval)
        if start > last:
            result_size += 2
            second_last = end - 1
            last = end
        
        # Case 3: Current interval contains only the last point
        # We need to add 1 new point (choose the largest in the interval)
        else:
            result_size += 1
            second_last = last
            last = end
    
    return result_size
    # Time: O(n * log(n))
    # Space: O(1) or O(n) in the worst case scenario.


def main():
    result = intersection_size_two(intervals = [[1,3],[3,7],[8,9]])
    print(result) # 5

    result = intersection_size_two(intervals = [[1,3],[1,4],[2,5],[3,5]])
    print(result) # 3

    result = intersection_size_two(intervals = [[1,2],[2,3],[2,4],[4,5]])
    print(result) # 5

if __name__ == "__main__":
    main()
