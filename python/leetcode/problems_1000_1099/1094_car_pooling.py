# --------------------
# 1094. Car Pooling 🚗
# --------------------

# Problem: https://leetcode.com/problems/car-pooling
#
# There is a car with capacity empty seats. The vehicle only drives east (i.e., it
# cannot turn around and drive west).
# 
# You are given the integer capacity and an array trips where trips[i] =
# [numPassengersᵢ, fromᵢ, toᵢ] indicates that the i^th trip has numPassengersᵢ
# passengers and the locations to pick them up and drop them off are fromᵢ and toᵢ
# respectively. The locations are given as the number of kilometers due east from
# the car's initial location.
# 
# Return true if it is possible to pick up and drop off all passengers for all the
# given trips, or false otherwise.
# 
# Example 1:
# 
# Input: trips = [[2,1,5],[3,3,7]], capacity = 4
# Output: false
# 
# Example 2:
# 
# Input: trips = [[2,1,5],[3,3,7]], capacity = 5
# Output: true
# 
# 
# Constraints:
#         1 <= trips.length <= 1000
#         trips[i].length == 3
#         1 <= numPassengersᵢ <= 100
#         0 <= fromᵢ < toᵢ <= 1000
#         1 <= capacity <= 10⁵

import heapq

# Solution: https://youtu.be/08sn_w4LWEE
# Credit: Navdeep Singh founder of NeetCode
def car_pooling(trips, capacity):
    trips.sort(key=lambda t: t[1])
    
    min_heap = []
    cur_pass = 0
    
    for t in trips:
        num_pass, start, end = t
        
        while min_heap and min_heap[0][0] <= start:
            cur_pass -= min_heap[0][1]
            heapq.heappop(min_heap)
            
        cur_pass += num_pass
        if cur_pass > capacity:
            return False
            
        heapq.heappush(min_heap, [end, num_pass])
        
    return True
    # Time: O(n * log(n))
    # Space: O(n)


def main():
    result = car_pooling(trips = [[2,1,5],[3,3,7]], capacity = 4)
    print(result) # False

    result = car_pooling(trips = [[2,1,5],[3,3,7]], capacity = 5)
    print(result) # True

if __name__ == "__main__":
    main()
