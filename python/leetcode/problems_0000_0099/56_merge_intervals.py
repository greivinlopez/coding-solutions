# --------------------
# 56. Merge Intervals
# --------------------

# Problem: https://leetcode.com/problems/merge-intervals/
# Given an array of intervals where intervals[i] = [starti, endi], 
# merge all overlapping intervals, and return an array of the non-overlapping
# intervals that cover all the intervals in the input.

# Solution: https://youtu.be/44H3cEC2fFM
# Credit: Navdeep Singh founder of NeetCode 
def merge(intervals):
    intervals.sort(key=lambda pair: pair[0])
    output = [intervals[0]]

    for start, end in intervals:
        lastEnd = output[-1][1]

        if start <= lastEnd:
            # merge
            output[-1][1] = max(lastEnd, end)
        else:
            output.append([start, end])
    return output

# Solution: https://youtu.be/HCbKvBOlMVI
# Credit: Greg Hogg
def merge_alt(intervals):
    # Time: O(n log n)
    # Space: O(n)
    intervals.sort(key=lambda interval: interval[0])
    merged = []

    for interval in intervals:
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            merged[-1] = [merged[-1][0], max(merged[-1][1], interval[1])]
    
    return merged

def main():
    result = merge([[1,3],[2,6],[8,10],[15,18]])
    # Expected Output: [[1,6],[8,10],[15,18]]
    print(result)
    result = merge([[1,4],[4,5]])
    # Expected Output: [[1,5]]
    print(result)

if __name__ == "__main__":
    main()