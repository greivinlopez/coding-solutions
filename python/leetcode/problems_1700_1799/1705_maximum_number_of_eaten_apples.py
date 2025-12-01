# ---------------------------------------
# 1705. Maximum Number of Eaten Apples 🍎
# ---------------------------------------

# Problem: https://leetcode.com/problems/maximum-number-of-eaten-apples
#
# There is a special kind of apple tree that grows apples every day for n days. On
# the iᵗʰ day, the tree grows apples[i] apples that will rot after days[i] days,
# that is on day i + days[i] the apples will be rotten and cannot be eaten. On
# some days, the apple tree does not grow any apples, which are denoted by
# apples[i] == 0 and days[i] == 0.
# 
# You decided to eat at most one apple a day (to keep the doctors away). Note that
# you can keep eating after the first n days.
# 
# Given two integer arrays days and apples of length n, return the maximum number
# of apples you can eat.
# 
# Example 1:
# 
# Input: apples = [1,2,3,5,2], days = [3,2,1,4,2]
# Output: 7
# 
# Explanation: You can eat 7 apples:
# - On the first day, you eat an apple that grew on the first day.
# - On the second day, you eat an apple that grew on the second day.
# - On the third day, you eat an apple that grew on the second day. After this
# day, the apples that grew on the third day rot.
# - On the fourth to the seventh days, you eat apples that grew on the fourth day.
# 
# Example 2:
# 
# Input: apples = [3,0,0,0,0,2], days = [3,0,0,0,0,2]
# Output: 5
# 
# Explanation: You can eat 5 apples:
# - On the first to the third day you eat apples that grew on the first day.
# - Do nothing on the fouth and fifth days.
# - On the sixth and seventh days you eat apples that grew on the sixth day.
# 
# 
# Constraints:
#         n == apples.length == days.length
#         1 <= n <= 2 * 10⁴
#         0 <= apples[i], days[i] <= 2 * 10⁴
#         days[i] = 0 if and only if apples[i] = 0.


# Solution: https://algo.monster/liteproblems/1705
# Credit: AlgoMonster
def eaten_apples(apples, days):
    from heapq import heappop, heappush

    n = len(days)
    current_day = 0
    total_eaten = 0
    
    # Min heap storing (expiration_day, apple_count) tuples
    # Priority queue ordered by expiration date
    heap = []
    
    # Continue while there are days to process or apples to eat
    while current_day < n or heap:
        # Add new apples produced on current day to the heap
        if current_day < n and apples[current_day] > 0:
            expiration_day = current_day + days[current_day] - 1
            heappush(heap, (expiration_day, apples[current_day]))
        
        # Remove all expired apples from the heap
        while heap and heap[0][0] < current_day:
            heappop(heap)
        
        # Eat one apple if available
        if heap:
            expiration_day, apple_count = heappop(heap)
            apple_count -= 1
            total_eaten += 1
            
            # Put remaining apples back if they haven't expired
            if apple_count > 0 and expiration_day > current_day:
                heappush(heap, (expiration_day, apple_count))
        
        current_day += 1
    
    return total_eaten
    # Time: O(n * log n + M)
    # Space: O(n)
    # n = the length of the arrays apples and days
    # m = the maximum value in the days array.


def main():
    result = eaten_apples(apples = [1,2,3,5,2], days = [3,2,1,4,2])
    print(result) # 7

    result = eaten_apples(apples = [3,0,0,0,0,2], days = [3,0,0,0,0,2])
    print(result) # 5

if __name__ == "__main__":
    main()
