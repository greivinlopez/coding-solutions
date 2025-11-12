# -------------------------------------
# 1349. Maximum Students Taking Exam 🧑🏻‍🎓
# -------------------------------------

# Problem: https://leetcode.com/problems/maximum-students-taking-exam
#
# Given a m * n matrix seats  that represent seats distributions in a
# classroom. If a seat is broken, it is denoted by '#' character otherwise it is
# denoted by a '.' character.
# 
# Students can see the answers of those sitting next to the left, right, upper
# left and upper right, but he cannot see the answers of the student
# sitting directly in front or behind him. Return the maximum number of students
# that can take the exam together without any cheating being possible.
# 
# Students must be placed in seats in good condition.
# 
# Example 1:
# 
# https://assets.leetcode.com/uploads/2020/01/29/image.png
# 
# Input: seats = [["#",".","#","#",".","#"],
#                 [".","#","#","#","#","."],
#                 ["#",".","#","#",".","#"]]
# Output: 4
# 
# Explanation: Teacher can place 4 students in available seats so they don't cheat
# on the exam.
# 
# Example 2:
# 
# Input: seats = [[".","#"],
#                 ["#","#"],
#                 ["#","."],
#                 ["#","#"],
#                 [".","#"]]
# Output: 3
# 
# Explanation: Place all students in available seats.
# 
# Example 3:
# 
# Input: seats = [["#",".",".",".","#"],
#                 [".","#",".","#","."],
#                 [".",".","#",".","."],
#                 [".","#",".","#","."],
#                 ["#",".",".",".","#"]]
# Output: 10
# 
# Explanation: Place students in available seats in column 1, 3 and 5.
# 
# 
# Constraints:
#         seats contains only characters '.' and'#'.
#         m == seats.length
#         n == seats[i].length
#         1 <= m <= 8
#         1 <= n <= 8


# Solution: https://algo.monster/liteproblems/1349
# Credit: AlgoMonster
def max_students(seats):
    from functools import cache

    def get_available_mask(row):
        mask = 0
        for position, seat in enumerate(row):
            if seat == '.':
                mask |= 1 << position
        return mask

    @cache
    def dp(available_seats, row_index):
        max_students = 0
        
        # Try all possible seating arrangements for current row
        for seating_mask in range(1 << num_cols):
            # Check if seating arrangement is valid:
            # 1. Students only sit in available seats (seating_mask is subset of available_seats)
            # 2. No two students sit adjacent to each other (no consecutive 1s in mask)
            if (available_seats | seating_mask) != available_seats or (seating_mask & (seating_mask << 1)):
                continue
            
            # For Python 3.10+ use:
            # students_in_row = seating_mask.bit_count()
            students_in_row = bin(seating_mask).count('1')
            
            # Base case: last row
            if row_index == len(seat_masks) - 1:
                max_students = max(max_students, students_in_row)
            else:
                # Calculate available seats for next row considering current seating
                # Students in current row block diagonal seats in next row
                next_available = seat_masks[row_index + 1]
                next_available &= ~(seating_mask << 1)  # Block left diagonal
                next_available &= ~(seating_mask >> 1)  # Block right diagonal
                
                # Recursively solve for next row
                max_students = max(max_students, students_in_row + dp(next_available, row_index + 1))
        
        return max_students

    num_cols = len(seats[0])
    # Convert each row to a bitmask representation
    seat_masks = [get_available_mask(row) for row in seats]
    
    # Start dynamic programming from first row
    return dp(seat_masks[0], 0)
    # Time: O(4ⁿ * n * m)
    # Space: O(2ⁿ * m)


def main():
    seats = [["#",".","#","#",".","#"],
             [".","#","#","#","#","."],
             ["#",".","#","#",".","#"]]
    result = max_students(seats)
    print(result) # 4

    seats = [[".","#"],
             ["#","#"],
             ["#","."],
             ["#","#"],
             [".","#"]]
    result = max_students(seats)
    print(result) # 3

    seats = [["#",".",".",".","#"],
             [".","#",".","#","."],
             [".",".","#",".","."],
             [".","#",".","#","."],
             ["#",".",".",".","#"]]
    result = max_students(seats)
    print(result) # 10

if __name__ == "__main__":
    main()
