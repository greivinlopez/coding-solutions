# ----------------------------
# 794. Valid Tic-Tac-Toe State
# ----------------------------

# Problem: https://leetcode.com/problems/valid-tic-tac-toe-state
#
# Given a Tic-Tac-Toe board as a string array board, return true if and only if it
# is possible to reach this board position during the course of a valid tic-tac-
# toe game.
# 
# The board is a 3 x 3 array that consists of characters ' ', 'X', and 'O'. The '
# ' character represents an empty square.
# 
# Here are the rules of Tic-Tac-Toe:
#         
#   * Players take turns placing characters into empty squares ' '.
#   * The first player always places 'X' characters, while the second player
#     always places 'O' characters.
#   * 'X' and 'O' characters are always placed into empty squares, never filled ones.
#   * The game ends when there are three of the same (non-empty) character filling 
#     any row, column, or diagonal.
#   * The game also ends if all squares are non-empty.
#   * No more moves can be played if the game is over.
# 
# Example 1:
# 
# https://assets.leetcode.com/uploads/2021/05/15/tictactoe1-grid.jpg
# 
# Input: board = ["O  ","   ","   "]
# Output: false
# 
# Explanation: The first player always plays "X".
# 
# Example 2:
# 
# https://assets.leetcode.com/uploads/2021/05/15/tictactoe2-grid.jpg
# 
# Input: board = ["XOX"," X ","   "]
# Output: false
# 
# Explanation: Players take turns making moves.
# 
# Example 3:
# 
# https://assets.leetcode.com/uploads/2021/05/15/tictactoe4-grid.jpg
# 
# Input: board = ["XOX","O O","XOX"]
# Output: true
# 
# 
# Constraints:
#         board.length == 3
#         board[i].length == 3
#         board[i][j] is either 'X', 'O', or ' '.


# Solution: 
# Credit: Navdeep Singh founder of NeetCode
def valid_tic_tac_toe(board):
    def check_winner(player):
        # Check horizontal wins (all cells in a row)
        for row in range(3):
            if all(board[row][col] == player for col in range(3)):
                return True
        
        # Check vertical wins (all cells in a column)
        for col in range(3):
            if all(board[row][col] == player for row in range(3)):
                return True
        
        # Check main diagonal (top-left to bottom-right)
        if all(board[i][i] == player for i in range(3)):
            return True
        
        # Check anti-diagonal (top-right to bottom-left)
        return all(board[i][2 - i] == player for i in range(3))
    
    # Count the number of X's and O's on the board
    x_count = sum(board[row][col] == 'X' for row in range(3) for col in range(3))
    o_count = sum(board[row][col] == 'O' for row in range(3) for col in range(3))
    
    # Valid game states: X plays first, so X count should equal O count or be one more
    if x_count != o_count and x_count - 1 != o_count:
        return False
    
    # If X won, the game should have ended with X's turn (X count = O count + 1)
    if check_winner('X') and x_count - 1 != o_count:
        return False
    
    # If O won, the game should have ended with O's turn (X count = O count)
    return not (check_winner('O') and x_count != o_count)
    # Time: O(1)
    # Space: O(1)


def main():
    result = valid_tic_tac_toe(board = ["O  ","   ","   "])
    print(result) # False

    result = valid_tic_tac_toe(board = ["XOX"," X ","   "])
    print(result) # False

    result = valid_tic_tac_toe(board = ["XOX","O O","XOX"])
    print(result) # True

if __name__ == "__main__":
    main()
