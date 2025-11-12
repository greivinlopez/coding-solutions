# --------------------------------
# 986. Interval List Intersections
# --------------------------------

# Problem: https://leetcode.com/problems/interval-list-intersections
#
# You are given two lists of closed intervals, firstList and secondList, where
# firstList[i] = [startᵢ, endᵢ] and secondList[j] = [startⱼ, endⱼ]. Each list of
# intervals is pairwise disjoint and in sorted order.
# 
# Return the intersection of these two interval lists.
# 
# A closed interval [a, b] (with a <= b) denotes the set of real numbers x with 
# a <= x <= b.
# 
# The intersection of two closed intervals is a set of real numbers that are
# either empty or represented as a closed interval. For example, the intersection
# of [1, 3] and [2, 4] is [2, 3].
# 
# Example 1:
# 
# https://assets.leetcode.com/uploads/2019/01/30/interval1.png
# 
# Input: firstList = [[0,2],[5,10],[13,23],[24,25]], secondList =
# [[1,5],[8,12],[15,24],[25,26]]
# Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
# 
# Example 2:
# 
# Input: firstList = [[1,3],[5,9]], secondList = []
# Output: []
# 
# 
# Constraints:
#         0 <= firstList.length, secondList.length <= 1000
#         firstList.length + secondList.length >= 1
#         0 <= startᵢ < endᵢ <= 109
#         endᵢ < startᵢ₊₁
#         0 <= startⱼ < endⱼ <= 109
#         endⱼ < startⱼ₊₁


# Solution: https://algo.monster/liteproblems/986
# Credit: AlgoMonster
def interval_intersection(firstList, secondList):
    # Initialize two pointers for traversing both lists
    i = 0  # Pointer for firstList
    j = 0  # Pointer for secondList
    result = []  # Store the intersection intervals
    
    # Process intervals while both lists have remaining elements
    while i < len(firstList) and j < len(secondList):
        # Extract start and end points of current intervals
        start1, end1 = firstList[i]
        start2, end2 = secondList[j]
        
        # Calculate the intersection boundaries
        # The intersection starts at the maximum of both start points
        intersection_start = max(start1, start2)
        # The intersection ends at the minimum of both end points
        intersection_end = min(end1, end2)
        
        # Check if there's a valid intersection
        # Valid when start is less than or equal to end
        if intersection_start <= intersection_end:
            result.append([intersection_start, intersection_end])
        
        # Move the pointer of the interval that ends first
        # This ensures we don't miss any potential intersections
        if end1 < end2:
            i += 1  # Move to next interval in firstList
        else:
            j += 1  # Move to next interval in secondList
    
    return result
    # Time: O(m + n)
    # Space: O(1)


def main():
    result = interval_intersection(firstList = [[0,2],[5,10],[13,23],[24,25]], 
                                   secondList = [[1,5],[8,12],[15,24],[25,26]])
    print(result) # [[1, 2], [5, 5], [8, 10], [15, 23], [24, 24], [25, 25]]

    result = interval_intersection(firstList = [[1,3],[5,9]], secondList = [])
    print(result) # []

if __name__ == "__main__":
    main()
