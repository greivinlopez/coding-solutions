# -----------------------------------------
# 871. Minimum Number of Refueling Stops ⛽
# -----------------------------------------

# Problem: https://leetcode.com/problems/minimum-number-of-refueling-stops
#
# A car travels from a starting position to a destination which is target miles
# east of the starting position.
# 
# There are gas stations along the way. The gas stations are represented as an
# array stations where stations[i] = [positionᵢ, fuelᵢ] indicates that the iᵗʰ gas
# station is positionᵢ miles east of the starting position and has fuelᵢ liters of
# gas.
# 
# The car starts with an infinite tank of gas, which initially has startFuel
# liters of fuel in it. It uses one liter of gas per one mile that it drives. When
# the car reaches a gas station, it may stop and refuel, transferring all the gas
# from the station into the car.
# 
# Return the minimum number of refueling stops the car must make in order to reach
# its destination. If it cannot reach the destination, return -1.
# 
# Note that if the car reaches a gas station with 0 fuel left, the car can still
# refuel there. If the car reaches the destination with 0 fuel left, it is still
# considered to have arrived.
# 
# Example 1:
# 
# Input: target = 1, startFuel = 1, stations = []
# Output: 0
# 
# Explanation: We can reach the target without refueling.
# 
# Example 2:
# 
# Input: target = 100, startFuel = 1, stations = [[10,100]]
# Output: -1
# 
# Explanation: We can not reach the target (or even the first gas station).
# 
# Example 3:
# 
# Input: target = 100, startFuel = 10, stations =
# [[10,60],[20,30],[30,30],[60,40]]
# Output: 2
# 
# Explanation: We start with 10 liters of fuel.
# We drive to position 10, expending 10 liters of fuel.  We refuel from 0 liters
# to 60 liters of gas.
# Then, we drive from position 10 to position 60 (expending 50 liters of fuel),
# and refuel from 10 liters to 50 liters of gas.  We then drive to and reach the
# target.
# We made 2 refueling stops along the way, so we return 2.
# 
# 
# Constraints:
#         1 <= target, startFuel <= 10⁹
#         0 <= stations.length <= 500
#         1 <= positioni < positioni+1 < target
#         1 <= fueli < 10⁹

from heapq import heappop, heappush

# Solution: https://algo.monster/liteproblems/871
# Credit: AlgoMonster
def min_refuel_stops(target, startFuel, stations):
    # Max heap to store available fuel amounts (negative values for max heap)
    max_heap = []
    
    # Initialize counters
    refuel_count = 0
    previous_position = 0
    
    # Add the target as a final station with 0 fuel to simplify logic
    stations.append([target, 0])
    
    # Process each station (including the target)
    for position, fuel_available in stations:
        # Calculate distance from previous position
        distance = position - previous_position
        
        # Consume fuel for the distance traveled
        startFuel -= distance
        
        # If we don't have enough fuel, refuel from the largest available stations
        while startFuel < 0 and max_heap:
            # Pop the maximum fuel amount (negative value, so negate it back)
            startFuel -= heappop(max_heap)
            refuel_count += 1
        
        # If still not enough fuel after using all available stations, impossible
        if startFuel < 0:
            return -1
        
        # Add current station's fuel to available options (negative for max heap)
        heappush(max_heap, -fuel_available)
        
        # Update previous position for next iteration
        previous_position = position
    
    return refuel_count
    # Time: O(n * log(n))
    # Space: O(n)


def main():
    result = min_refuel_stops(target = 1, startFuel = 1, stations = [])
    print(result) # 0

    result = min_refuel_stops(target = 100, startFuel = 1, stations = [[10,100]])
    print(result) # -1

    result = min_refuel_stops(target = 100, startFuel = 10, stations = [[10,60],[20,30],[30,30],[60,40]])
    print(result) # 2

if __name__ == "__main__":
    main()
