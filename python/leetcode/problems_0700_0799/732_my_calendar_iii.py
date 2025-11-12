# --------------------
# 732. My Calendar III
# --------------------

# Problem: https://leetcode.com/problems/my-calendar-iii
#
# A k-booking happens when k events have some non-empty intersection (i.e., there
# is some time that is common to all k events.)
# 
# You are given some events [startTime, endTime), after each given event, return
# an integer k representing the maximum k-booking between all the previous events.
# 
# Implement the MyCalendarThree class:
#         
#   * MyCalendarThree() Initializes the object.
#   * int book(int startTime, int endTime) Returns an integer k representing
#     the largest integer such that there exists a k-booking in the calendar.
# 
# Example 1:
# 
# Input
# ["MyCalendarThree", "book", "book", "book", "book", "book", "book"]
# [[], [10, 20], [50, 60], [10, 40], [5, 15], [5, 10], [25, 55]]
# Output
# [null, 1, 1, 2, 3, 3, 3]
# 
# Explanation
# MyCalendarThree myCalendarThree = new MyCalendarThree();
# myCalendarThree.book(10, 20); // return 1
# myCalendarThree.book(50, 60); // return 1
# myCalendarThree.book(10, 40); // return 2
# myCalendarThree.book(5, 15); // return 3
# myCalendarThree.book(5, 10); // return 3
# myCalendarThree.book(25, 55); // return 3
# 
# 
# Constraints:
#         0 <= startTime < endTime <= 10⁹
#         At most 400 calls will be made to book.

from sortedcontainers import SortedDict
from itertools import accumulate

# Solution: https://leetcodethehardway.com/solutions/0700-0799/my-calendar-iii-hard
# Credit: LeetCode The Hard Way -> https://leetcodethehardway.com/
class MyCalendarThree:
    def __init__(self):
        # in line sweeping, we need to ensure the keys are sorted
        # in python, we can use SortedDict which fulfils the above requirement
        # lines[i] = j means we have j overlapping elements at time point i
        self.lines = SortedDict()


    # finding number of overlapping elements at time points -> line sweeping
    def book(self, start: int, end: int) -> int:
        # new event starts here -> increase by 1
        self.lines[start] = self.lines.get(start, 0) + 1
        # the event ends here -> decrease by 1
        # p.s. sometimes you may see `lines.get(end + 1, 0) - 1;`. e.g. 2406. Divide Intervals Into Minimum Number of Groups
        #      you may search `leetcode-the-hard-way` on Discussion to see my solution explanation on that problem
        #      this is because the interval is inclusive, i.e [start, end]
        #      however, the interval in this problem is [start, end), so we don't need to add 1 here.
        self.lines[end] = self.lines.get(end, 0) - 1
        # here we calculate the prefix sum using `accumulate`
        # and get the maximum overlapping intervals using `max`
        return max(accumulate(self.lines.values()))
    # Time: O(n²)
    # Space: O(n)


def main():
    print("TO DO")

if __name__ == "__main__":
    main()
