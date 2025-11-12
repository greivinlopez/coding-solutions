# ---------------------------------------------------
# 1353. Maximum Number of Events That Can Be Attended
# ---------------------------------------------------

# Problem: https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended
#
# You are given an array of events where events[i] = [startDayᵢ, endDayᵢ]. Every
# event i starts at startDayᵢ and ends at endDayᵢ.
# 
# You can attend an event i at any day d where startDayᵢ <= d <= endDayᵢ. You can
# only attend one event at any time d.
# 
# Return the maximum number of events you can attend.
# 
# Example 1:
# 
# https://assets.leetcode.com/uploads/2020/02/05/e1.png
# 
# Input: events = [[1,2],[2,3],[3,4]]
# Output: 3
# 
# Explanation: You can attend all the three events.
# One way to attend them all is as shown.
# Attend the first event on day 1.
# Attend the second event on day 2.
# Attend the third event on day 3.
# 
# Example 2:
# 
# Input: events= [[1,2],[2,3],[3,4],[1,2]]
# Output: 4
# 
# 
# Constraints:
#         1 <= events.length <= 10⁵
#         events[i].length == 2
#         1 <= startDayᵢ <= endDayᵢ <= 10⁵

from collections import defaultdict
from heapq import heappush, heappop

# Solution: https://algo.monster/liteproblems/1353
# Credit: AlgoMonster
def max_events(events):
    # Group events by their start day
    events_by_start_day = defaultdict(list)
    
    # Find the range of days we need to consider
    min_start_day = float('inf')
    max_end_day = 0
    
    for start_day, end_day in events:
        events_by_start_day[start_day].append(end_day)
        min_start_day = min(min_start_day, start_day)
        max_end_day = max(max_end_day, end_day)
    
    # Min heap to store end days of available events
    available_events = []
    attended_events = 0
    
    # Process each day in the range
    for current_day in range(min_start_day, max_end_day + 1):
        # Remove events that have already ended (end day < current day)
        while available_events and available_events[0] < current_day:
            heappop(available_events)
        
        # Add all events starting on the current day to the heap
        # Store their end days in the heap
        for end_day in events_by_start_day[current_day]:
            heappush(available_events, end_day)
        
        # Attend the event that ends earliest (greedy approach)
        if available_events:
            heappop(available_events)
            attended_events += 1
    
    return attended_events
    # Time: O(M × log n)
    # Space: O(n)
    # M = the range of days from the minimum start day to the maximum end day of all events


def main():
    result = max_events(events = [[1,2],[2,3],[3,4]])
    print(result) # 3

    result = max_events(events= [[1,2],[2,3],[3,4],[1,2]])
    print(result) # 4

if __name__ == "__main__":
    main()
