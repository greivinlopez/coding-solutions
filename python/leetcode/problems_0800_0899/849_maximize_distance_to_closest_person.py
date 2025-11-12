# ----------------------------------------
# 849. Maximize Distance to Closest Person
# ----------------------------------------

# Problem: https://leetcode.com/problems/maximize-distance-to-closest-person
#
# You are given an array representing a row of seats where seats[i] = 1 represents
# a person sitting in the iᵗʰ seat, and seats[i] = 0 represents that the iᵗʰ seat
# is empty (0-indexed).
# 
# There is at least one empty seat, and at least one person sitting.
# 
# Alex wants to sit in the seat such that the distance between him and the closest
# person to him is maximized. 
# 
# Return that maximum distance to the closest person.
# 
# Example 1:
# 
# https://assets.leetcode.com/uploads/2020/09/10/distance.jpg
# 
# Input: seats = [1,0,0,0,1,0,1]
# Output: 2
# 
# Explanation:
# If Alex sits in the second open seat (i.e. seats[2]), then the closest person
# has distance 2.
# If Alex sits in any other open seat, the closest person has distance 1.
# Thus, the maximum distance to the closest person is 2.
# 
# Example 2:
# 
# Input: seats = [1,0,0,0]
# Output: 3
# 
# Explanation:
# If Alex sits in the last seat (i.e. seats[3]), the closest person is 3 seats
# away.
# This is the maximum distance possible, so the answer is 3.
# 
# Example 3:
# 
# Input: seats = [0,1]
# Output: 1
# 
# 
# Constraints:
#         2 <= seats.length <= 2 * 10⁴
#         seats[i] is 0 or 1.
#         At least one seat is empty.
#         At least one seat is occupied.


# Solution: https://algo.monster/liteproblems/849
# Credit: AlgoMonster
def max_dist_to_closest(seats):
    # Track the first and last occupied seat positions
    first_occupied = None
    last_occupied = None
    
    # Track the maximum distance between two consecutive occupied seats
    max_distance_between_occupied = 0
    
    # Iterate through all seats to find occupied ones
    for index, is_occupied in enumerate(seats):
        if is_occupied:
            # If we've seen an occupied seat before, calculate distance
            if last_occupied is not None:
                max_distance_between_occupied = max(
                    max_distance_between_occupied, 
                    index - last_occupied
                )
            
            # Record the first occupied seat we encounter
            if first_occupied is None:
                first_occupied = index
            
            # Update the most recent occupied seat position
            last_occupied = index
    
    # The maximum distance to the closest person can be:
    # 1. Distance from start to first occupied seat (edge case)
    # 2. Distance from last occupied seat to end (edge case)
    # 3. Half the distance between two occupied seats (middle case)
    return max(
        first_occupied,                              # Distance from start
        len(seats) - last_occupied - 1,             # Distance to end
        max_distance_between_occupied // 2          # Half of max gap between occupied seats
    )
    # Time: O(n)
    # Space: O(1)


def main():
    result = max_dist_to_closest(seats = [1,0,0,0,1,0,1])
    print(result) # 2

    result = max_dist_to_closest(seats = [1,0,0,0])
    print(result) # 3

    result = max_dist_to_closest(seats = [0,1])
    print(result) # 1

if __name__ == "__main__":
    main()
