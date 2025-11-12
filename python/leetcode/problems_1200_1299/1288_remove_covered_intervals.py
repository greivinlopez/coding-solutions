# ------------------------------
# 1288. Remove Covered Intervals
# ------------------------------

# Problem: https://leetcode.com/problems/remove-covered-intervals
#
# Given an array intervals where intervals[i] = [li, ri] represent the interval
# [li, ri), remove all intervals that are covered by another interval in the list.
# 
# The interval [a, b) is covered by the interval [c, d) if and only if c <= a and
# b <= d.
# 
# Return the number of remaining intervals.
# 
# Example 1:
# 
# Input: intervals = [[1,4],[3,6],[2,8]]
# Output: 2
# Explanation: Interval [3,6] is covered by [2,8], therefore it is removed.
# 
# Example 2:
# 
# Input: intervals = [[1,4],[2,3]]
# Output: 1
# 
# 
# Constraints:
#         1 <= intervals.length <= 1000
#         intervals[i].length == 2
#         0 <= li < ri <= 10^5
#         All the given intervals are unique.


# Solution: https://youtu.be/nhAsMabiVkM
# Credit: Navdeep Singh founder of NeetCode
def remove_covered_intervals(intervals):
    # sort on the basis of inc li first and then on the basis of dec length (=> -ri)
    intervals.sort(key=lambda x: (x[0], -x[1]))
    
    covered, maxri = 0, 0
    
    for _, ri in intervals:
        if ri > maxri:
            maxri = ri
        else:
            covered += 1
            
    return len(intervals) - covered


def main():
    result = remove_covered_intervals([[1,4],[3,6],[2,8]])
    print(result) # 2

    result = remove_covered_intervals([[1,4],[2,3]])
    print(result) # 1

if __name__ == "__main__":
    main()
