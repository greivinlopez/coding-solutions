# -----------------------------------
# 1184. Distance Between Bus Stops 🚌
# -----------------------------------

# Problem: https://leetcode.com/problems/distance-between-bus-stops
#
# A bus has n stops numbered from 0 to n - 1 that form a circle. We know the
# distance between all pairs of neighboring stops where distance[i] is the
# distance between the stops number i and (i + 1) % n.
# 
# The bus goes along both directions i.e. clockwise and counterclockwise.
# 
# Return the shortest distance between the given start and destination stops.
# 
# Example 1:
# 
# Input: distance = [1,2,3,4], start = 0, destination = 1
# Output: 1
# 
# Explanation: Distance between 0 and 1 is 1 or 9, minimum is 1.
# 
# Example 2:
# 
# Input: distance = [1,2,3,4], start = 0, destination = 2
# Output: 3
# 
# Explanation: Distance between 0 and 2 is 3 or 7, minimum is 3.
# 
# Example 3:
# 
# Input: distance = [1,2,3,4], start = 0, destination = 3
# Output: 4
# 
# Explanation: Distance between 0 and 3 is 6 or 4, minimum is 4.
# 
# 
# Constraints:
#         1 <= n <= 10⁴
#         distance.length == n
#         0 <= start, destination < n
#         0 <= distance[i] <= 10⁴


# Credit: Jaweria Batool -> https://github.com/Jaweria-B
def distance_between_bus_stops(distance, start, destination):
    clockwise_distance = 0
    n = len(distance)
    i = start
    
    while i != destination:
        clockwise_distance += distance[i]
        start += 1
        i = start % n
    
    anticlockwise_distance = sum(distance) - clockwise_distance
    
    return min(clockwise_distance, anticlockwise_distance)
    # Time: O(n)
    # Space: O(1)


def main():
    result = distance_between_bus_stops(distance = [1,2,3,4], start = 0, destination = 1)
    print(result) # 1

    result = distance_between_bus_stops(distance = [1,2,3,4], start = 0, destination = 2)
    print(result) # 3

    result = distance_between_bus_stops(distance = [1,2,3,4], start = 0, destination = 3)
    print(result) # 4

if __name__ == "__main__":
    main()
