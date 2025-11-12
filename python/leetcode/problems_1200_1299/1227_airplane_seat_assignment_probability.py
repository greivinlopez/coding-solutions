# ---------------------------------------------
# 1227. Airplane Seat Assignment Probability ✈️
# ---------------------------------------------

# Problem: https://leetcode.com/problems/airplane-seat-assignment-probability
#
# n passengers board an airplane with exactly n seats. The first passenger has
# lost the ticket and picks a seat randomly. But after that, the rest of the
# passengers will:
#         
#   * Take their own seat if it is still available, and
#   * Pick other seats randomly when they find their seat occupied
# 
# Return the probability that the nth person gets his own seat.
# 
# Example 1:
# 
# Input: n = 1
# Output: 1.00000
# 
# Explanation: The first person can only get the first seat.
# 
# Example 2:
# 
# Input: n = 2
# Output: 0.50000
# 
# Explanation: The second person has a probability of 0.5 to get the second seat
# (when first person gets the first seat).
# 
# 
# Constraints:
#         1 <= n <= 10⁵


# Solution: https://algo.monster/liteproblems/1227
# Credit: AlgoMonster
def nth_person_gets_nth_seat(n):
    # Base case: single passenger always gets their seat
    if n == 1:
        return 1.0
    
    # For any n > 1, the probability is always 0.5
    return 0.5
    # Time: O(1)
    # Space: O(1)

# Similar Solution with more formal math explanation
# Solution: https://leetcode.com/problems/airplane-seat-assignment-probability/solutions/3179809/05-if-n-1-else-1-math-proof-by-moaz064-bf3g
# Credit: Moaz Mahmud -> https://leetcode.com/u/moaz064/
def nth_person_gets_nth_seat_alt(n):
    return 0.5 if n > 1 else 1

def main():
    result = nth_person_gets_nth_seat(1)
    print(result) # 1.0

    result = nth_person_gets_nth_seat(2)
    print(result) # 0.5

if __name__ == "__main__":
    main()
