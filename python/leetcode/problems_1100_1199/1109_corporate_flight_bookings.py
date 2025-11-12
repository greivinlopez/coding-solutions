# ------------------------------
# 1109. Corporate Flight Bookings
# ------------------------------

# Problem: https://leetcode.com/problems/corporate-flight-bookings
#
# There are n flights that are labeled from 1 to n.
# 
# You are given an array of flight bookings bookings, where bookings[i] = [firstᵢ,
# lastᵢ, seatsᵢ] represents a booking for flights firstᵢ through lastᵢ (inclusive)
# with seatsᵢ seats reserved for each flight in the range.
# 
# Return an array answer of length n, where answer[i] is the total number of seats
# reserved for flight i.
# 
# Example 1:
# 
# Input: bookings = [[1,2,10],[2,3,20],[2,5,25]], n = 5
# Output: [10,55,45,25,25]
# 
# Explanation:
# Flight labels:        1   2   3   4   5
# Booking 1 reserved:  10  10
# Booking 2 reserved:      20  20
# Booking 3 reserved:      25  25  25  25
# Total seats:         10  55  45  25  25
# Hence, answer = [10,55,45,25,25]
# 
# Example 2:
# 
# Input: bookings = [[1,2,10],[2,2,15]], n = 2
# Output: [10,25]
# 
# Explanation:
# Flight labels:        1   2
# Booking 1 reserved:  10  10
# Booking 2 reserved:      15
# Total seats:         10  25
# Hence, answer = [10,25]
# 
# 
# Constraints:
#         1 <= n <= 2 * 10⁴
#         1 <= bookings.length <= 2 * 10⁴
#         bookings[i].length == 3
#         1 <= firstᵢ <= lastᵢ <= n
#         1 <= seatsᵢ <= 10⁴

from itertools import accumulate

# Solution: https://algo.monster/liteproblems/1109
# Credit: AlgoMonster
def corp_flight_bookings(bookings, n):
    # Initialize difference array with n elements, all set to 0
    # This will store the seat changes at each flight position
    difference_array = [0] * n
    
    # Process each booking
    for first_flight, last_flight, seats_to_add in bookings:
        # Add seats at the start of the booking range (convert to 0-indexed)
        difference_array[first_flight - 1] += seats_to_add
        
        # Subtract seats after the end of the booking range
        # This marks where the booking effect ends
        if last_flight < n:
            difference_array[last_flight] -= seats_to_add
    
    # Calculate prefix sum to get the actual seat counts for each flight
    # accumulate() computes running totals from the difference array
    return list(accumulate(difference_array))
    # Time: O(m + n)
    # Space: O(1)


def main():
    result = corp_flight_bookings(bookings = [[1,2,10],[2,3,20],[2,5,25]], n = 5)
    print(result) # [10, 55, 45, 25, 25]

    result = corp_flight_bookings(bookings = [[1,2,10],[2,2,15]], n = 2)
    print(result) # [10, 25]

if __name__ == "__main__":
    main()
