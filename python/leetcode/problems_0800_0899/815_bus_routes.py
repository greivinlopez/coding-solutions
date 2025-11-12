# ------------------
# 815. Bus Routes 🚌
# ------------------

# Problem: https://leetcode.com/problems/bus-routes
#
# You are given an array routes representing bus routes where routes[i] is a bus
# route that the iᵗʰ bus repeats forever.
#         
#   * For example, if routes[0] = [1, 5, 7], this means that the 0ᵗʰ bus
#     travels in the sequence 1 -> 5 -> 7 -> 1 -> 5 -> 7 -> 1 -> ... forever.
# 
# You will start at the bus stop source (You are not on any bus initially), and
# you want to go to the bus stop target. You can travel between bus stops by buses
# only.
# 
# Return the least number of buses you must take to travel from source to target.
# Return -1 if it is not possible.
# 
# Example 1:
# 
# Input: routes = [[1,2,7],[3,6,7]], source = 1, target = 6
# Output: 2
# 
# Explanation: The best strategy is take the first bus to the bus stop 7, then
# take the second bus to the bus stop 6.
# 
# Example 2:
# 
# Input: routes = [[7,12],[4,5,15],[6],[15,19],[9,12,13]], source = 15, target = 12
# Output: -1
# 
# 
# Constraints:
#         1 <= routes.length <= 500.
#         1 <= routes[i].length <= 10⁵
#         All the values of routes[i] are unique.
#         sum(routes[i].length) <= 10⁵
#         0 <= routes[i][j] < 10⁶
#         0 <= source, target < 10⁶

from collections import defaultdict, deque

# Credit: Jeel Gajera -> https://github.com/JeelGajera
def num_buses_to_destination(routes, source, target):
    stops_map = defaultdict(set)
    if source == target:
        return 0

    for i, route in enumerate(routes):
        for stop in route:
            stops_map[stop].add(i)

    queue = deque([(source, 0)])
    visited = set([source])

    while queue:
        cur_stop, bus_count = queue.popleft()
        if cur_stop == target:
            return bus_count

        for bus in stops_map[cur_stop]:
            for next_stop in routes[bus]:
                if next_stop not in visited:
                    queue.append((next_stop, bus_count + 1))
                    visited.add(next_stop)
            routes[bus] = []

    return -1
    # Time: O(k)
    # Space: O(k)
    # k = the total number of stops across all given routes.


def main():
    result = num_buses_to_destination(routes = [[1,2,7],[3,6,7]], source = 1, target = 6)
    print(result) # 2

    result = num_buses_to_destination(routes = [[7,12],[4,5,15],[6],[15,19],[9,12,13]], source = 15, target = 12)
    print(result) # -1

if __name__ == "__main__":
    main()
