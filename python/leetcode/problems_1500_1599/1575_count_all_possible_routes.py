# -------------------------------
# 1575. Count All Possible Routes
# -------------------------------

# Problem: https://leetcode.com/problems/count-all-possible-routes
#
# You are given an array of distinct positive integers locations where
# locations[i] represents the position of city i. You are also given integers
# start, finish and fuel representing the starting city, ending city, and the
# initial amount of fuel you have, respectively.
# 
# At each step, if you are at city i, you can pick any city j such that j != i and
# 0 <= j < locations.length and move to city j. Moving from city i to city j
# reduces the amount of fuel you have by |locations[i] - locations[j]|. Please
# notice that |x| denotes the absolute value of x.
# 
# Notice that fuel cannot become negative at any point in time, and that you are
# allowed to visit any city more than once (including start and finish).
# 
# Return the count of all possible routes from start to finish. Since the answer
# may be too large, return it modulo 10⁹ + 7.
# 
# Example 1:
# 
# Input: locations = [2,3,6,8,4], start = 1, finish = 3, fuel = 5
# Output: 4
# 
# Explanation: The following are all possible routes, each uses 5 units of fuel:
# 1 -> 3
# 1 -> 2 -> 3
# 1 -> 4 -> 3
# 1 -> 4 -> 2 -> 3
# 
# Example 2:
# 
# Input: locations = [4,3,1], start = 1, finish = 0, fuel = 6
# Output: 5
# 
# Explanation: The following are all possible routes:
# 1 -> 0, used fuel = 1
# 1 -> 2 -> 0, used fuel = 5
# 1 -> 2 -> 1 -> 0, used fuel = 5
# 1 -> 0 -> 1 -> 0, used fuel = 3
# 1 -> 0 -> 1 -> 0 -> 1 -> 0, used fuel = 5
# 
# Example 3:
# 
# Input: locations = [5,2,1], start = 0, finish = 2, fuel = 3
# Output: 0
# 
# Explanation: It is impossible to get from 0 to 2 using only 3 units of fuel
# since the shortest route needs 4 units of fuel.
# 
# 
# Constraints:
#         2 <= locations.length <= 100
#         1 <= locations[i] <= 10⁹
#         All integers in locations are distinct.
#         0 <= start, finish < locations.length
#         1 <= fuel <= 200

from functools import cache

# Solution: https://algo.monster/liteproblems/1575
# Credit: AlgoMonster
def count_routes(locations, start, finish, fuel):
    MOD = 10**9 + 7
    
    @cache
    def dfs(current_city, remaining_fuel):
        # If we don't have enough fuel to reach the finish city even directly,
        # there are no valid routes from here
        if remaining_fuel < abs(locations[current_city] - locations[finish]):
            return 0
        
        # Initialize route count - if we're at the finish, this counts as one route
        route_count = 1 if current_city == finish else 0
        
        # Try moving to every other city
        for next_city in range(len(locations)):
            if next_city != current_city:
                # Calculate fuel cost to move to next_city
                fuel_cost = abs(locations[current_city] - locations[next_city])
                
                # Recursively count routes from next_city with reduced fuel
                route_count = (route_count + dfs(next_city, remaining_fuel - fuel_cost)) % MOD
        
        return route_count
    
    # Start the DFS from the starting city with full fuel
    return dfs(start, fuel)
    # Time: O(n² * m)
    # Space: O(n * m)


def main():
    result = count_routes(locations = [2,3,6,8,4], start = 1, finish = 3, fuel = 5)
    print(result) # 4

    result = count_routes(locations = [4,3,1], start = 1, finish = 0, fuel = 6)
    print(result) # 5

    result = count_routes(locations = [5,2,1], start = 0, finish = 2, fuel = 3)
    print(result) # 0

if __name__ == "__main__":
    main()
