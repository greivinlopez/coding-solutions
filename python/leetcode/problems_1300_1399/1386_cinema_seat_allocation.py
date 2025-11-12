# -------------------------------
# 1386. Cinema Seat Allocation 🍿
# -------------------------------

# Problem: https://leetcode.com/problems/cinema-seat-allocation
#
# https://assets.leetcode.com/uploads/2020/02/14/cinema_seats_1.png
# 
# A cinema has n rows of seats, numbered from 1 to n and there are ten seats in
# each row, labelled from 1 to 10 as shown in the figure above.
# 
# Given the array reservedSeats containing the numbers of seats already reserved,
# for example, reservedSeats[i] = [3,8] means the seat located in row 3 and
# labelled with 8 is already reserved.
# 
# Return the maximum number of four-person groups you can assign on the
# cinema seats. A four-person group occupies four adjacent seats in one single
# row. Seats across an aisle (such as [3,3] and [3,4]) are not considered to be
# adjacent, but there is an exceptional case on which an aisle split a four-person
# group, in that case, the aisle split a four-person group in the middle, which
# means to have two people on each side.
# 
# Example 1:
# 
# https://assets.leetcode.com/uploads/2020/02/14/cinema_seats_3.png
# 
# Input: n = 3, reservedSeats = [[1,2],[1,3],[1,8],[2,6],[3,1],[3,10]]
# Output: 4
# 
# Explanation: The figure above shows the optimal allocation for four groups,
# where seats mark with blue are already reserved and contiguous seats mark with
# orange are for one group.
# 
# Example 2:
# 
# Input: n = 2, reservedSeats = [[2,1],[1,8],[2,6]]
# Output: 2
# 
# Example 3:
# 
# Input: n = 4, reservedSeats = [[4,3],[1,4],[4,6],[1,7]]
# Output: 4
# 
# 
# Constraints:
#         1 <= n <= 10^9
#         1 <= reservedSeats.length <= min(10*n, 10^4)
#         reservedSeats[i].length == 2
#         1 <= reservedSeats[i][0] <= n
#         1 <= reservedSeats[i][1] <= 10
#         All reservedSeats[i] are distinct.

from collections import defaultdict

# Solution: https://algo.monster/liteproblems/1386
# Credit: AlgoMonster
def max_number_of_families(n, reservedSeats):
    # Dictionary to store reserved seats for each row using bit manipulation
    # Each row's reserved seats are represented as a bitmask
    reserved_by_row = defaultdict(int)
    
    # Convert reserved seats to bitmask representation
    # Seat j in row i becomes bit (10 - j) in the bitmask
    for row, seat in reservedSeats:
        reserved_by_row[row] |= 1 << (10 - seat)
    
    # Define masks for three possible 4-person family group positions:
    # - Left group: seats 2-5 (0b0111100000)
    # - Right group: seats 6-9 (0b0000011110)
    # - Middle group: seats 4-7 (0b0001111000)
    family_group_masks = (0b0111100000, 0b0000011110, 0b0001111000)
    
    # Start with maximum possible families in rows without any reservations
    # Each empty row can fit 2 families (left and right groups)
    total_families = (n - len(reserved_by_row)) * 2
    
    # Check each row with reservations
    for row_reservation in reserved_by_row.values():
        # Try to place family groups in this row
        for mask in family_group_masks:
            # Check if this group position has no conflicts with reserved seats
            if (row_reservation & mask) == 0:
                # Mark these seats as occupied and count the family
                row_reservation |= mask
                total_families += 1
    
    return total_families
    # Time: O(m)
    # Space: O(m)
    # m is the length of reservedSeats


def main():
    result = max_number_of_families(n = 3, reservedSeats = [[1,2],[1,3],[1,8],[2,6],[3,1],[3,10]])
    print(result) # 4

    result = max_number_of_families(n = 2, reservedSeats = [[2,1],[1,8],[2,6]])
    print(result) # 2

    result = max_number_of_families(n = 4, reservedSeats = [[4,3],[1,4],[4,6],[1,7]])
    print(result) # 4

if __name__ == "__main__":
    main()
