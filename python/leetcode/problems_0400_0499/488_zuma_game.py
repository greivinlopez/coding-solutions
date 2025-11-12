# --------------
# 488. Zuma Game
# --------------

# Problem: https://leetcode.com/problems/zuma-game
#
# You are playing a variation of the game Zuma.
# 
# In this variation of Zuma, there is a single row of colored balls on a board,
# where each ball can be colored red 'R', yellow 'Y', blue 'B', green 'G', or
# white 'W'. You also have several colored balls in your hand.
# 
# Your goal is to clear all of the balls from the board. On each turn:
#         
#   * Pick any ball from your hand and insert it in between two balls in the
#     row or on either end of the row.
#   * If there is a group of three or more consecutive balls of the same color, 
#     remove the group of balls from the board.
#       * If this removal causes more groups of three or more of the same color to 
#         form, then continue removing each group until there are none left.
#   * If there are no more balls on the board, then you win the game.
#   * Repeat this process until you either win or do not have any more balls
#     in your hand.
# 
# Given a string board, representing the row of balls on the board, and a string
# hand, representing the balls in your hand, return the minimum number of balls
# you have to insert to clear all the balls from the board. If you cannot clear
# all the balls from the board using the balls in your hand, return -1.
# 
# Example 1:
# 
# Input: board = "WRRBBW", hand = "RB"
# Output: -1
# 
# Explanation: It is impossible to clear all the balls. The best you can do is:
# - Insert 'R' so the board becomes WRRRBBW. WRRRBBW -> WBBW.
# - Insert 'B' so the board becomes WBBBW. WBBBW -> WW.
# There are still balls remaining on the board, and you are out of balls to
# insert.
# 
# Example 2:
# 
# Input: board = "WWRRBBWW", hand = "WRBRW"
# Output: 2
# 
# Explanation: To make the board empty:
# - Insert 'R' so the board becomes WWRRRBBWW. WWRRRBBWW -> WWBBWW.
# - Insert 'B' so the board becomes WWBBBWW. WWBBBWW -> WWWW -> empty.
# 2 balls from your hand were needed to clear the board.
# 
# Example 3:
# 
# Input: board = "G", hand = "GGGGG"
# Output: 2
# 
# Explanation: To make the board empty:
# - Insert 'G' so the board becomes GG.
# - Insert 'G' so the board becomes GGG. GGG -> empty.
# 2 balls from your hand were needed to clear the board.
# 
# 
# Constraints:
#       1 <= board.length <= 16
#       1 <= hand.length <= 5
#       board and hand consist of the characters 'R', 'Y', 'B', 'G', and 'W'.
#       The initial row of balls on the board will not have any groups of three
#       or more consecutive balls of the same color.

import re
from collections import deque

# Solution: https://algo.monster/liteproblems/488
# Credit: AlgoMonster
def find_min_step(board, hand):
    def remove_consecutive_balls(board_state):
        while board_state:
            # Remove any sequence of 3 or more consecutive same-colored balls
            new_board = re.sub(r'B{3,}|G{3,}|R{3,}|W{3,}|Y{3,}', '', board_state)
            
            # If nothing was removed, we're done
            if len(new_board) == len(board_state):
                break
                
            board_state = new_board
        
        return board_state
    
    # Track visited board states to avoid revisiting
    visited_states = set()
    
    # BFS queue: each element is (current_board_state, remaining_balls_in_hand)
    queue = deque([(board, hand)])
    
    while queue:
        current_board, remaining_balls = queue.popleft()
        
        # If board is empty, we've won - return number of balls used
        if not current_board:
            return len(hand) - len(remaining_balls)
        
        # Try each unique ball color in our hand
        for ball_color in set(remaining_balls):
            # Remove one ball of this color from hand
            new_hand = remaining_balls.replace(ball_color, '', 1)
            
            # Try inserting the ball at each position in the board (including after last position)
            for insert_position in range(len(current_board) + 1):
                # Insert ball at current position
                new_board = current_board[:insert_position] + ball_color + current_board[insert_position:]
                
                # Remove any groups of 3+ consecutive balls
                new_board = remove_consecutive_balls(new_board)
                
                # If we haven't seen this board state before, explore it
                if new_board not in visited_states:
                    visited_states.add(new_board)
                    queue.append((new_board, new_hand))
    
    # If we exhausted all possibilities without clearing the board, return -1
    return -1
    # Time: O(n * m! * n² * k)
    # Space: O(n * m! * n)
    # n = the length of the board string
    # m = the length of the hand string (number of balls in hand)
    # k = the average number of iterations needed for the remove function to stabilize


def main():
    result = find_min_step(board = "WRRBBW", hand = "RB")
    print(result) # -1

    result = find_min_step(board = "WWRRBBWW", hand = "WRBRW")
    print(result) # 2

    result = find_min_step(board = "G", hand = "GGGGG")
    print(result) # 2

if __name__ == "__main__":
    main()
