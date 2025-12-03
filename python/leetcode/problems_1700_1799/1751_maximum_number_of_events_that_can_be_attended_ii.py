# ------------------------------------------------------
# 1751. Maximum Number of Events That Can Be Attended II
# ------------------------------------------------------

# Problem: https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended-ii
#
# You are given an array of events where events[i] = [startDayi, endDayi, valuei].
# The ith event starts at startDayi and ends at endDayi, and if you attend this
# event, you will receive a value of valuei. You are also given an integer k which
# represents the maximum number of events you can attend.
# 
# You can only attend one event at a time. If you choose to attend an event, you
# must attend the entire event. Note that the end day is inclusive: that is, you
# cannot attend two events where one of them starts and the other ends on the same
# day.
# 
# Return the maximum sum of values that you can receive by attending events.
# 
# Example 1:
# 
# https://assets.leetcode.com/uploads/2021/01/10/screenshot-2021-01-11-at-60048-pm.png
# 
# Input: events = [[1,2,4],[3,4,3],[2,3,1]], k = 2
# Output: 7
# 
# Explanation: Choose the green events, 0 and 1 (0-indexed) for a total value of 4
# + 3 = 7.
# 
# Example 2:
# 
# https://assets.leetcode.com/uploads/2021/01/10/screenshot-2021-01-11-at-60150-pm.png
# 
# Input: events = [[1,2,4],[3,4,3],[2,3,10]], k = 2
# Output: 10
# 
# Explanation: Choose event 2 for a total value of 10.
# Notice that you cannot attend any other event as they overlap, and that you do
# not have to attend k events.
# 
# Example 3:
# 
# https://assets.leetcode.com/uploads/2021/01/10/screenshot-2021-01-11-at-60703-pm.png
# 
# Input: events = [[1,1,1],[2,2,2],[3,3,3],[4,4,4]], k = 3
# Output: 9
# 
# Explanation: Although the events do not overlap, you can only attend 3 events.
# Pick the highest valued three.
# 
# 
# Constraints:
#         1 <= k <= events.length
#         1 <= k * events.length <= 10⁶
#         1 <= startDayi <= endDayi <= 10⁹
#         1 <= valuei <= 10⁶


# Solution: https://algo.monster/liteproblems/1751
# Credit: AlgoMonster
def max_value(events, k):
    from functools import cache
    import bisect

    @cache
    def dp(index, remaining_events):
        # Base case: no more events to consider
        if index >= len(events):
            return 0

        # Extract current event details
        start_day, end_day, value = events[index]

        # Option 1: Skip current event
        max_value = dp(index + 1, remaining_events)

        # Option 2: Take current event (if we have remaining capacity)
        if remaining_events > 0:
            # Find next non-overlapping event using binary search
            # We need to find first event that starts after current event ends
            next_valid_index = bisect.bisect_right(
                events,
                end_day,
                lo=index + 1,
                key=lambda event: event[0]  # Compare by start day
            )

            # Take current event and continue from next valid index
            max_value = max(
                max_value,
                dp(next_valid_index, remaining_events - 1) + value
            )

        return max_value

    # Sort events by start day for binary search to work correctly
    events.sort()

    # Start recursion from first event with k available selections
    return dp(0, k)
    # Time: O(n * log n + n * k)
    # Space: O(n * k)


def main():
    result = max_value(events = [[1,2,4],[3,4,3],[2,3,1]], k = 2)
    print(result) # 7

    result = max_value(events = [[1,2,4],[3,4,3],[2,3,10]], k = 2)
    print(result) # 10

    result = max_value(events = [[1,1,1],[2,2,2],[3,3,3],[4,4,4]], k = 3)
    print(result) # 9

if __name__ == "__main__":
    main()
