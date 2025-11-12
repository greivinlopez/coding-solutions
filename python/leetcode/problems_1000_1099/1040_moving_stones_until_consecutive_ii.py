# ----------------------------------------
# 1040. Moving Stones Until Consecutive II
# ----------------------------------------

# Problem: https://leetcode.com/problems/moving-stones-until-consecutive-ii
#
# There are some stones in different positions on the X-axis. You are given an
# integer array stones, the positions of the stones.
# 
# Call a stone an endpoint stone if it has the smallest or largest position. In
# one move, you pick up an endpoint stone and move it to an unoccupied position so
# that it is no longer an endpoint stone.
#         
#   * In particular, if the stones are at say, stones = [1,2,5], you cannot
#     move the endpoint stone at position 5, since moving it to any position (such as
#     0, or 3) will still keep that stone as an endpoint stone.
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
# Input: stones = [7,4,9]
# Output: [1,2]
# 
# Explanation: We can move 4 -> 8 for one move to finish the game.
# Or, we can move 9 -> 5, 4 -> 6 for two moves to finish the game.
# 
# Example 2:
# 
# Input: stones = [6,5,4,3,10]
# Output: [2,3]
# 
# Explanation: We can move 3 -> 8 then 10 -> 7 to finish the game.
# Or, we can move 3 -> 7, 4 -> 8, 5 -> 9 to finish the game.
# Notice we cannot move 10 -> 2 to finish the game, because that would be an
# illegal move.
# 
# 
# Constraints:
#         3 <= stones.length <= 10⁴
#         1 <= stones[i] <= 10⁹
#         All the values of stones are unique.


# Solution: https://algo.monster/liteproblems/1040
# Credit: AlgoMonster
def num_moves_stones_ii(stones):
    # Sort stones positions in ascending order
    stones.sort()
    n = len(stones)
    
    # Calculate maximum moves
    # The maximum moves is the number of gaps we can create
    # We can move all stones except the endpoints to fill gaps
    # Choose the side that gives more gaps
    max_moves = max(stones[-1] - stones[1] + 1, stones[-2] - stones[0] + 1) - (n - 1)
    
    # Calculate minimum moves using sliding window
    min_moves = n
    left = 0
    
    # Iterate through each stone as the right boundary of window
    for right, stone_pos in enumerate(stones):
        # Shrink window from left if window size exceeds n positions
        while stone_pos - stones[left] + 1 > n:
            left += 1
        
        # Special case: when we have n-1 stones in consecutive positions
        # except for one gap (stones form pattern like [1,2,3,4,6])
        if right - left + 1 == n - 1 and stone_pos - stones[left] == n - 2:
            # Need at least 2 moves in this case
            min_moves = min(min_moves, 2)
        else:
            # General case: minimum moves = stones outside current window
            stones_in_window = right - left + 1
            min_moves = min(min_moves, n - stones_in_window)
    
    return [min_moves, max_moves]
    # Time: O(n * log(n))
    # Space: O(1) or O(n) depending on whether we count the sorting space.


def main():
    result = num_moves_stones_ii(stones = [7,4,9])
    print(result) # [1, 2]

    result = num_moves_stones_ii(stones = [6,5,4,3,10])
    print(result) # [2, 3]

if __name__ == "__main__":
    main()
