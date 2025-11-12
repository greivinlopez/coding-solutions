# --------------------
# 57. Insert Interval
# --------------------

# Problem: https://leetcode.com/problems/insert-interval/
# 
# You are given an array of non-overlapping intervals intervals where 
# intervals[i] = [starti, endi] represent the start and the end of the
# ith interval and intervals is sorted in ascending order by starti.
# You are also given an interval newInterval = [start, end] that represents 
# the start and end of another interval.
# 
# Insert newInterval into intervals such that intervals is still sorted in 
# ascending order by starti and intervals still does not have any overlapping 
# intervals (merge overlapping intervals if necessary).
# 
# Return intervals after the insertion.
# 
# Note that you don't need to modify intervals in-place. You can make a new array and return it.

# Solution: https://youtu.be/A8NUOmlwOlM
# Credit: Navdeep Singh founder of NeetCode 
def insert(intervals, newInterval):
    # Time: O(n)
    res = []

    for i in range(len(intervals)):
        if newInterval[1] < intervals[i][0]:
            res.append(newInterval)
            return res + intervals[i:]
        elif newInterval[0] > intervals[i][1]:
            res.append(intervals[i])
        else:
            newInterval = [
                min(newInterval[0], intervals[i][0]),
                max(newInterval[1], intervals[i][1]),
            ]
    res.append(newInterval)
    return res

def main():
    result = insert(intervals = [[1,3],[6,9]], newInterval = [2,5])
    # Expected Output: [[1,5],[6,9]]
    print(result)
    result = insert(intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8])
    # Expected Output: [[1,2],[3,10],[12,16]]
    print(result)

if __name__ == "__main__":
    main()