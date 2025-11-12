# ----------------------------------------------------
# 2406. Divide Intervals Into Minimum Number of Groups
# ----------------------------------------------------

# Problem: https://leetcode.com/problems/divide-intervals-into-minimum-number-of-groups
#
# You are given a 2D integer array intervals where intervals[i] = [leftᵢ, rightᵢ]
# represents the inclusive interval [leftᵢ, rightᵢ].
# 
# You have to divide the intervals into one or more groups such that each interval
# is in exactly one group, and no two intervals that are in the same group
# intersect each other.
# 
# Return the minimum number of groups you need to make.
# 
# Two intervals intersect if there is at least one common number between them. For
# example, the intervals [1, 5] and [5, 8] intersect.
# 
# Example 1:
# 
# Input: intervals = [[5,10],[6,8],[1,5],[2,3],[1,10]]
# Output: 3
# 
# Explanation: We can divide the intervals into the following groups:
# - Group 1: [1, 5], [6, 8].
# - Group 2: [2, 3], [5, 10].
# - Group 3: [1, 10].
# It can be proven that it is not possible to divide the intervals into fewer than
# 3 groups.
# 
# Example 2:
# 
# Input: intervals = [[1,3],[5,6],[8,10],[11,13]]
# Output: 1
# 
# Explanation: None of the intervals overlap, so we can put all of them in one
# group.
# 
# 
# Constraints:
#         1 <= intervals.length <= 10⁵
#         intervals[i].length == 2
#         1 <= leftᵢ <= rightᵢ <= 10⁶


# Solution: https://youtu.be/FVjKrhdMutc
# Credit: Navdeep Singh founder of NeetCode
def min_groups(intervals):
    start, end = [], []
    for l, r in intervals:
        start.append(l)
        end.append(r)
    start.sort()
    end.sort()
    i, j = 0, 0
    res = 0
    while i < len(intervals):
        if start[i] <= end[j]:
            i += 1
        else:
            j += 1
        res = max(res, i - j)
    return res
    # Time: O(n * log(n))
    # Space: O(n)


def main():
    result = min_groups(intervals = [[5,10],[6,8],[1,5],[2,3],[1,10]])
    print(result) # 3

    result = min_groups(intervals = [[1,3],[5,6],[8,10],[11,13]])
    print(result) # 1

if __name__ == "__main__":
    main()
