# ---------------------------
# 933. Number of Recent Calls
# ---------------------------

# Problem: https://leetcode.com/problems/number-of-recent-calls
#
# You have a RecentCounter class which counts the number of recent requests within
# a certain time frame.
# 
# Implement the RecentCounter class:
#         
#   * RecentCounter() Initializes the counter with zero recent requests.
#   * int ping(int t) Adds a new request at time t, where t represents some time 
#     in milliseconds, and returns the number of requests that has happened in
#     the past 3000 milliseconds (including the new request). Specifically, return the
#     number of requests that have happened in the inclusive range [t - 3000, t].
# 
# It is guaranteed that every call to ping uses a strictly larger value of t than
# the previous call.
# 
# Example 1:
# 
# Input
# ["RecentCounter", "ping", "ping", "ping", "ping"]
# [[], [1], [100], [3001], [3002]]
# Output
# [null, 1, 2, 3, 3]
# 
# Explanation
# RecentCounter recentCounter = new RecentCounter();
# recentCounter.ping(1);     // requests = [1], range is [-2999,1], return 1
# recentCounter.ping(100);   // requests = [1, 100], range is [-2900,100], return
# 2
# recentCounter.ping(3001);  // requests = [1, 100, 3001], range is [1,3001],
# return 3
# recentCounter.ping(3002);  // requests = [1, 100, 3001, 3002], range is
# [2,3002], return 3
# 
# 
# Constraints:
#         1 <= t <= 10⁹
#         Each test case will call ping with strictly increasing values of t.
#         At most 10⁴ calls will be made to ping.

from collections import deque

# Solution: https://algo.monster/liteproblems/933
# Credit: AlgoMonster
class RecentCounter:
    """
    A class to count recent requests within a sliding time window of 3000ms.
    Each ping represents a request at time t (in milliseconds).
    """
  
    def __init__(self) -> None:
        """
        Initialize the RecentCounter with an empty queue to store timestamps.
        """
        self.request_queue = deque()
  
    def ping(self, t: int) -> int:
        """
        Record a request at time t and return the number of requests 
        that have happened in the past 3000 milliseconds (including current request).
      
        Args:
            t: The timestamp of the current request in milliseconds.
               It's guaranteed that every call uses a larger t value than before.
      
        Returns:
            The number of requests in the time window [t-3000, t].
        """
        # Add the current timestamp to the queue
        self.request_queue.append(t)
      
        # Remove all timestamps that are outside the 3000ms window
        # Keep removing from the front while timestamp is older than t-3000
        while self.request_queue[0] < t - 3000:
            self.request_queue.popleft()
      
        # Return the count of requests within the valid time window
        return len(self.request_queue)


def main():
    print("TO DO")

if __name__ == "__main__":
    main()
