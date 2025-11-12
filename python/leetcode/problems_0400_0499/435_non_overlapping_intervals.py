# ------------------------------
# 435. Non Overlapping Intervals
# ------------------------------

# Problem: https://leetcode.com/problems/non-overlapping-intervals/
# 
# Given an array of intervals intervals where intervals[i] = [starti, endi], 
# return the minimum number of intervals you need to remove to make the rest 
# of the intervals non-overlapping.
# 
# Note that intervals which only touch at a point are non-overlapping. For 
# example, [1, 2] and [2, 3] are non-overlapping.
# 
#  
# Example 1:
# 
# Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
# Output: 1
# Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.
# 
# 
# Example 2:
# 
# Input: intervals = [[1,2],[1,2],[1,2]]
# Output: 2
# Explanation: You need to remove two [1,2] to make the rest of the intervals non-overlapping.
# 
# 
# Example 3:
# 
# Input: intervals = [[1,2],[2,3]]
# Output: 0
# Explanation: You don't need to remove any of the intervals since they're already non-overlapping.
# 
#   
# Constraints:
# 
# 	1 <= intervals.length <= 10^5
# 	intervals[i].length == 2
# 	-5 * 10^4 <= starti < endi <= 5 * 10^4


# Solution: https://youtu.be/nONCGxWoUfM
# Credit: Navdeep Singh founder of NeetCode
def erase_overlap_intervals(intervals):
    intervals.sort()
    res = 0
    prevEnd = intervals[0][1]
    for start, end in intervals[1:]:
        if start >= prevEnd:
            prevEnd = end
        else:
            res += 1
            prevEnd = min(end, prevEnd)
    return res


def main():
    result = erase_overlap_intervals([[1,2],[2,3],[3,4],[1,3]])
    print(result) # 1

    result = erase_overlap_intervals([[1,2],[1,2],[1,2]])
    print(result) # 2

    result = erase_overlap_intervals([[1,2],[2,3]])
    print(result) # 0

if __name__ == "__main__":
    main()
