# --------------------------------------
# 352. Data Stream as Disjoint Intervals
# --------------------------------------

# Problem: https://leetcode.com/problems/data-stream-as-disjoint-intervals
#
# Given a data stream input of non-negative integers a₁, a₂, ..., aₙ, summarize
# the numbers seen so far as a list of disjoint intervals.
# 
# Implement the SummaryRanges class:
#         
#   * SummaryRanges() Initializes the object with an empty stream.
#   * void addNum(int value) Adds the integer value to the stream.
#   * int[][] getIntervals() Returns a summary of the integers in the stream
#     currently as a list of disjoint intervals [startₗ, endₗ]. The answer should 
#     be sorted by startₗ.
# 
# Example 1:
# 
# Input
# ["SummaryRanges", "addNum", "getIntervals", "addNum", "getIntervals", "addNum",
# "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals"]
# [[], [1], [], [3], [], [7], [], [2], [], [6], []]
# Output
# [null, null, [[1, 1]], null, [[1, 1], [3, 3]], null, [[1, 1], [3, 3], [7, 7]],
# null, [[1, 3], [7, 7]], null, [[1, 3], [6, 7]]]
# 
# Explanation
# SummaryRanges summaryRanges = new SummaryRanges();
# summaryRanges.addNum(1);      // arr = [1]
# summaryRanges.getIntervals(); // return [[1, 1]]
# summaryRanges.addNum(3);      // arr = [1, 3]
# summaryRanges.getIntervals(); // return [[1, 1], [3, 3]]
# summaryRanges.addNum(7);      // arr = [1, 3, 7]
# summaryRanges.getIntervals(); // return [[1, 1], [3, 3], [7, 7]]
# summaryRanges.addNum(2);      // arr = [1, 2, 3, 7]
# summaryRanges.getIntervals(); // return [[1, 3], [7, 7]]
# summaryRanges.addNum(6);      // arr = [1, 2, 3, 6, 7]
# summaryRanges.getIntervals(); // return [[1, 3], [6, 7]]
# 
# 
# Constraints:
#         0 <= value <= 10⁴
#         At most 3 * 10⁴ calls will be made to addNum and getIntervals.
#         At most 10² calls will be made to getIntervals.
# 
# Follow up: What if there are lots of merges and the number of disjoint intervals
# is small compared to the size of the data stream?

# You will need to install sortedcontainers library
# ----------------------------
# pip install sortedcontainers
# ----------------------------
from sortedcontainers import SortedDict

# Solution: https://youtu.be/FavoZjPIWpo
# Credit: Navdeep Singh founder of NeetCode
class SummaryRanges:
    def __init__(self):
        self.tree_map = SortedDict()

    def addNum(self, value):
        self.tree_map[value] = True

    def getIntervals(self):
        res = []
        for n in self.tree_map:
            if res and res[-1][1] + 1 == n:
                res[-1][1] = n
            else:
                res.append([n, n])
        return res


def main():
    summaryRanges = SummaryRanges()
    summaryRanges.addNum(1)
    print(summaryRanges.getIntervals()) # [[1, 1]]
    summaryRanges.addNum(3)
    print(summaryRanges.getIntervals()) # [[1, 1], [3, 3]]
    summaryRanges.addNum(7)
    print(summaryRanges.getIntervals()) # [[1, 1], [3, 3], [7, 7]]
    summaryRanges.addNum(2)
    print(summaryRanges.getIntervals()) # [[1, 3], [7, 7]]
    summaryRanges.addNum(6)
    print(summaryRanges.getIntervals()) # [[1, 3], [6, 7]]

if __name__ == "__main__":
    main()
