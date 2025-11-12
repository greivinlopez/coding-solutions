# -------------------------------------
# 1033. Moving Stones Until Consecutive
# -------------------------------------

# Problem: https://leetcode.com/problems/moving-stones-until-consecutive
#
# There are three stones in different positions on the X-axis. You are given three
# integers a, b, and c, the positions of the stones.
# 
# In one move, you pick up a stone at an endpoint (i.e., either the lowest or
# highest position stone), and move it to an unoccupied position between those
# endpoints. Formally, let's say the stones are currently at positions x, y, and z
# with x < y < z. You pick up the stone at either position x or position z, and
# move that stone to an integer position k, with x < k < z and k != y.
# 
# The game ends when you cannot make any more moves (i.e., the stones are in three
# consecutive positions).
# 
# Return an integer array answer of length 2 where:
#         
#   * answer[0] is the minimum number of moves you can play, and
#   * answer[1] is the maximum number of moves you can play.
# 
# Example 1:
# 
# Input: a = 1, b = 2, c = 5
# Output: [1,2]
# 
# Explanation: Move the stone from 5 to 3, or move the stone from 5 to 4 to 3.
# 
# Example 2:
# 
# Input: a = 4, b = 3, c = 2
# Output: [0,0]
# 
# Explanation: We cannot make any moves.
# 
# Example 3:
# 
# Input: a = 3, b = 5, c = 1
# Output: [1,2]
# 
# Explanation: Move the stone from 1 to 4; or move the stone from 1 to 2 to 4.
# 
# 
# Constraints:
#         1 <= a, b, c <= 100
#         a, b, and c have different values.


# Solution: https://algo.monster/liteproblems/1033
# Credit: AlgoMonster
def num_moves_stones(a, b, c):
    # Sort the three positions to get left, middle, and right stones
    left = min(a, b, c)
    right = max(a, b, c)
    middle = a + b + c - left - right  # Calculate middle value without sorting
    
    # Initialize minimum and maximum moves
    min_moves = 0
    max_moves = 0
    
    # Check if stones are not already consecutive
    if right - left > 2:
        # For minimum moves:
        # If either gap (middle-left or right-middle) is <= 2, we can do it in 1 move
        # Otherwise, we need 2 moves
        if middle - left <= 2 or right - middle <= 2:
            min_moves = 1
        else:
            min_moves = 2
        
        # For maximum moves:
        # We can move stones one position at a time
        # Total empty spaces between leftmost and rightmost stones
        max_moves = right - left - 2
    
    return [min_moves, max_moves]
    # Time: O(1)
    # Space: O(1)


def main():
    result = num_moves_stones(a = 1, b = 2, c = 5)
    print(result) # [1, 2]

    result = num_moves_stones(a = 4, b = 3, c = 2)
    print(result) # [0, 0]

    result = num_moves_stones(a = 3, b = 5, c = 1)
    print(result) # [1, 2]

if __name__ == "__main__":
    main()
