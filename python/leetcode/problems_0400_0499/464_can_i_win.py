# --------------
# 464. Can I Win
# --------------

# Problem: https://leetcode.com/problems/can-i-win
#
# In the "100 game" two players take turns adding, to a running total, any integer
# from 1 to 10. The player who first causes the running total to reach or exceed
# 100 wins.
# 
# What if we change the game so that players cannot re-use integers?
# 
# For example, two players might take turns drawing from a common pool of numbers
# from 1 to 15 without replacement until they reach a total >= 100.
# 
# Given two integers maxChoosableInteger and desiredTotal, return true if the
# first player to move can force a win, otherwise, return false. Assume both
# players play optimally.
# 
# Example 1:
# 
# Input: maxChoosableInteger = 10, desiredTotal = 11
# Output: false
# 
# Explanation:
# No matter which integer the first player choose, the first player will lose.
# The first player can choose an integer from 1 up to 10.
# If the first player choose 1, the second player can only choose integers from 2
# up to 10.
# The second player will win by choosing 10 and get a total = 11, which is >=
# desiredTotal.
# Same with other integers chosen by the first player, the second player will
# always win.
# 
# Example 2:
# 
# Input: maxChoosableInteger = 10, desiredTotal = 0
# Output: true
# 
# Example 3:
# 
# Input: maxChoosableInteger = 10, desiredTotal = 1
# Output: true
# 
# 
# Constraints:
#         1 <= maxChoosableInteger <= 20
#         0 <= desiredTotal <= 300

from functools import cache

# Solution: https://algo.monster/liteproblems/464
# Credit: AlgoMonster
def can_i_win(maxChoosableInteger, desiredTotal):   
    # Early termination: if the sum of all available numbers is less than
    # the desired total, nobody can win (first player loses)
    total_available_sum = (1 + maxChoosableInteger) * maxChoosableInteger // 2
    if total_available_sum < desiredTotal:
        return False

    @cache
    def can_win_from_state(used_numbers_mask, current_sum):
        # Try each possible number from 1 to maxChoosableInteger
        for number in range(1, maxChoosableInteger + 1):
            # Check if this number hasn't been used yet
            # (bit at position 'number' should be 0)
            if (used_numbers_mask >> number) & 1 == 0:
                # Calculate new sum after choosing this number
                new_sum = current_sum + number
                
                # Current player wins if either:
                # 1. This move reaches or exceeds the desired total
                # 2. The opponent cannot win from the resulting state
                if new_sum >= desiredTotal:
                    return True
                
                # Mark this number as used and check opponent's position
                new_mask = used_numbers_mask | (1 << number)
                if not can_win_from_state(new_mask, new_sum):
                    return True
        
        # If no winning move exists, current player loses
        return False
    
    # Start the game with no numbers used and sum of 0
    return can_win_from_state(0, 0)
    # Time: O(2ⁿ * n)
    # Space: O(2ⁿ)
    # n = maxChoosableInteger


def main():
    result = can_i_win(maxChoosableInteger = 10, desiredTotal = 11)
    print(result) # False

    result = can_i_win(maxChoosableInteger = 10, desiredTotal = 0)
    print(result) # True

    result = can_i_win(maxChoosableInteger = 10, desiredTotal = 1)
    print(result) # True

if __name__ == "__main__":
    main()
